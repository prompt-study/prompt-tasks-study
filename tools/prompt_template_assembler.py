import sqlite3
import os
import json
from tools.database import Database
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
import ast
import pandas as pd
import re
import traceback
from string import Template
from tqdm import tqdm
from datetime import datetime
from tools.get_dataset_paths import get_dataset_paths
import random
from fuzzywuzzy import fuzz, process
from langchain.docstore.document import Document
import hashlib
import asyncio
import shutil
import sys
from transformers import AutoTokenizer, AutoModel
from langchain.embeddings.base import Embeddings
import torch
from typing import List
from huggingface_hub import InferenceClient


import torch
from typing import List
from transformers import AutoTokenizer, AutoModel
from langchain.embeddings.base import Embeddings

def mean_pooling(model_output, attention_mask):
    # model_output[0] is last_hidden_state: (batch, seq_len, hidden_size)
    token_embeddings = model_output[0]
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

class JinaEmbeddings(Embeddings):
    def __init__(
        self,
        model_name: str = "jinaai/jina-embeddings-v2-base-code",
        device: str = "cpu",
    ):
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name, trust_remote_code=True, force_download=False
        )
        self.model = AutoModel.from_pretrained(
            model_name, trust_remote_code=True, force_download=False
        ).to(device)
        self.device = device

    def embed_documents(self, texts: List[str], batch_size: int = 8) -> List[List[float]]:
        embeddings = []
        for i in range(0, len(texts), batch_size):
            batch_texts = texts[i:i + batch_size]
            inputs = self.tokenizer(
                batch_texts,
                padding=True,
                truncation=True,
                return_tensors="pt"
            ).to(self.device)

            with torch.no_grad():
                model_output = self.model(**inputs)
                pooled = mean_pooling(model_output, inputs['attention_mask'])
            embeddings.extend(pooled.cpu().tolist())
        return embeddings

    def embed_query(self, text: str) -> List[float]:
        return self.embed_documents([text])[0]



class PromptTemplateAssembler:
    def __init__(self):
        self.pieces_table_name = '_prompt_pieces'
        self.source_table_name = '_source'
        self.prompts_ready_table_name = '_prompts_ready'
        self.tasks = {
            "defect": 'defect_detection',
            "clone": 'clone_detection',
            "exception": 'exception_type',
            "cosqa": 'code_question_answering',
            "search": 'code_search',
            "retrieval": 'code_to_code_retrieval',
            "translation": 'code_translation',
            "fixing": 'bug_fixing',
            "mutant": 'mutant_generation',
            "assert": 'assert_generation',
            "summarization": 'code_summarization',
            "generation": 'code_generation',
            # 'completion': 'code_completion,'
        }
        
        self.llms_used = {
            'defect_detection': ['deepseek-ai/DeepSeek-V3', 'o3-mini', 'Qwen/Qwen2.5-Coder-32B-Instruct', 'meta-llama/Llama-3.3-70B-Instruct-Turbo'],
            'clone_detection': ['deepseek-ai/DeepSeek-V3', 'o3-mini', 'Qwen/Qwen2.5-Coder-32B-Instruct', 'meta-llama/Llama-3.3-70B-Instruct-Turbo'],
            'exception_type': ['deepseek-ai/DeepSeek-V3', 'o3-mini', 'Qwen/Qwen2.5-Coder-32B-Instruct', 'meta-llama/Llama-3.3-70B-Instruct-Turbo'],
            'code_question_answering': ['deepseek-ai/DeepSeek-V3', 'o3-mini', 'Qwen/Qwen2.5-Coder-32B-Instruct', 'meta-llama/Llama-3.3-70B-Instruct-Turbo'],
            'code_search': ['deepseek-ai/DeepSeek-V3', 'o3-mini', 'Qwen/Qwen2.5-Coder-32B-Instruct', 'meta-llama/Llama-3.3-70B-Instruct-Turbo'],
            'code_to_code_retrieval': ['deepseek-ai/DeepSeek-V3', 'o3-mini', 'Qwen/Qwen2.5-Coder-32B-Instruct', 'meta-llama/Llama-3.3-70B-Instruct-Turbo'],
            'code_translation': ['deepseek-ai/DeepSeek-V3', 'o3-mini', 'Qwen/Qwen2.5-Coder-32B-Instruct', 'meta-llama/Llama-3.3-70B-Instruct-Turbo'],
            'bug_fixing': ['deepseek-ai/DeepSeek-V3', 'o3-mini', 'Qwen/Qwen2.5-Coder-32B-Instruct', 'meta-llama/Llama-3.3-70B-Instruct-Turbo'],
            'mutant_generation': ['deepseek-ai/DeepSeek-V3', 'o3-mini', 'Qwen/Qwen2.5-Coder-32B-Instruct', 'meta-llama/Llama-3.3-70B-Instruct-Turbo'],
            'assert_generation': ['deepseek-ai/DeepSeek-V3', 'o3-mini', 'Qwen/Qwen2.5-Coder-32B-Instruct', 'meta-llama/Llama-3.3-70B-Instruct-Turbo'],
            'code_summarization': ['deepseek-ai/DeepSeek-V3', 'o3-mini', 'Qwen/Qwen2.5-Coder-32B-Instruct', 'meta-llama/Llama-3.3-70B-Instruct-Turbo'],
            'code_generation': ['deepseek-ai/DeepSeek-V3', 'o3-mini', 'Qwen/Qwen2.5-Coder-32B-Instruct', 'meta-llama/Llama-3.3-70B-Instruct-Turbo'],
        }   
        
        self.templates_to_select = {
            'assert_generation': {
                # 'control_0': (1,),
                # 'winner_0': (1,),
                'exemplar_selection_knn': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'few_shot_contrastive_cot': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'tree_of_thought': (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15),
                # 'self_ask': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'universal_self_consistency': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'self_refine': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15), #
                # 'sg_in_context_learning': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15), #
                # 'thread_of_thought': (1, 3, 4, 8, 9, 11, 12, 13, 15, 16), #
                # 'step_back_prompting': (3, 4, 5, 7, 8, 11, 15, 16, 17, 18), #
                # 'analogical_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15), #
                # 'emotional_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20), #
                # 'style_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15), #
                # 'rephrase_and_respond': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15), #
                # 'role_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 14, 15), #
                },
            'bug_fixing': {
                # 'control_0': (1,),
                # 'winner_0': (1,),
                'exemplar_selection_knn': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'few_shot_contrastive_cot': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'tree_of_thought': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'self_ask': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'universal_self_consistency': (1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 13, 14, 15),
                # 'self_refine': (1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'sg_in_context_learning': (1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'thread_of_thought': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'step_back_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'analogical_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'emotional_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20),
                # 'style_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'rephrase_and_respond': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'role_prompting': (1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 14, 15),
                },
            'clone_detection': {
                # 'control_0': (1,),
                # 'winner_0': (1,),
                'exemplar_selection_knn': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'few_shot_contrastive_cot': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'tree_of_thought': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'self_ask': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'universal_self_consistency': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'self_refine': (1, 2, 4, 5, 7, 10, 11, 12, 13, 14),
                # 'sg_in_context_learning': (1, 2, 4, 7, 10, 11, 12, 13, 14, 16),
                # 'thread_of_thought': (1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'step_back_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'analogical_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'emotional_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1, 16, 17, 18, 19, 20),
                # 'style_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15),
                # 'rephrase_and_respond': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'role_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 14, 15),
                },
            'code_generation': {
                # 'control_0': (1,),
                # 'winner_0': (1,),
                'exemplar_selection_knn': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'few_shot_contrastive_cot': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'tree_of_thought': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'self_ask': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'universal_self_consistency': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'self_refine': (1, 2, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15),
                # 'sg_in_context_learning': (1, 2, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15),
                # 'thread_of_thought': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'step_back_prompting': (1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'analogical_prompting': (1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'emotional_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20),
                # 'style_prompting': (1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14),
                # 'rephrase_and_respond': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'role_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 14, 15),
                },
            'code_question_answering': {
                # 'control_0': (1,),
                # 'winner_0': (1,),
                'exemplar_selection_knn': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'few_shot_contrastive_cot': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'tree_of_thought': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'self_ask': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'universal_self_consistency': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'self_refine': (1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 14, 15),
                # 'sg_in_context_learning': (1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 14, 15),
                # 'thread_of_thought': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'step_back_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'analogical_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'emotional_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20),
                # 'style_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'rephrase_and_respond': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'role_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 14, 15),
                },
            'code_summarization': {
                # 'control_0': (1,),
                # 'winner_0': (1,),
                'exemplar_selection_knn': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'few_shot_contrastive_cot': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'tree_of_thought': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'self_ask': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'universal_self_consistency': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'self_refine': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'sg_in_context_learning': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'thread_of_thought': (1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15),
                # 'step_back_prompting': (1, 4, 5, 6, 7, 9, 10, 11, 13, 14, 15),
                # 'analogical_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 14, 15),
                # 'emotional_prompting': (1, 2, 3, 4, 5, 6, 16, 17, 18, 19, 20),
                # 'style_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15),
                # 'rephrase_and_respond': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'role_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 14, 15),
                },
            'code_translation': {
                # 'control_0': (1,),
                # 'winner_0': (1,),
                'exemplar_selection_knn': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'few_shot_contrastive_cot': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'tree_of_thought': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'self_ask': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'universal_self_consistency': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'self_refine': (1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14),
                # 'sg_in_context_learning': (1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14),
                # 'thread_of_thought': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'step_back_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'analogical_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'emotional_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20),
                # 'style_prompting': (1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'rephrase_and_respond': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'role_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 14, 15),
                },
            'defect_detection': {
                # 'control_0': (1,),
                # 'winner_0': (1,),
                'exemplar_selection_knn': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'few_shot_contrastive_cot': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'tree_of_thought': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'self_ask': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'universal_self_consistency': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'self_refine': (1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 13, 14, 15),
                # 'sg_in_context_learning': (1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 13, 14, 15),
                # 'thread_of_thought': (1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'step_back_prompting': (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'analogical_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'emotional_prompting': (1, 2, 3, 4, 5, 6, 7, 16, 17, 18, 19, 20),
                # 'style_prompting': (1, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15),
                # 'rephrase_and_respond': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'role_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 14, 15),
                },
            'exception_type': {
                # 'control_0': (1,),
                # 'winner_0': (1,),
                'exemplar_selection_knn': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'few_shot_contrastive_cot': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'tree_of_thought': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'self_ask': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'universal_self_consistency': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'self_refine': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'sg_in_context_learning': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'thread_of_thought': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'step_back_prompting': (1, 2, 4, 5, 6, 7, 9, 11, 12, 13, 14, 15),
                # 'analogical_prompting': (1, 2, 4, 5, 6, 7, 9, 11, 12, 13, 14, 15),
                # 'emotional_prompting': (1, 2, 3, 4, 5, 6, 7, 16, 17, 18, 19, 20),
                # 'style_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
                # 'rephrase_and_respond': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'role_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 14, 15),
                },
            'mutant_generation': {
                # 'control_0': (1,),
                # 'winner_0': (1,),
                'exemplar_selection_knn': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'few_shot_contrastive_cot': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'tree_of_thought': (1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'self_ask': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'universal_self_consistency': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15),
                # 'self_refine': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'sg_in_context_learning': (1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15),
                # 'thread_of_thought': (1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15),
                # 'step_back_prompting': (1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15),
                # 'analogical_prompting': (1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15),
                # 'emotional_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20),
                # 'style_prompting': (1, 2, 3, 4, 5, 7, 10, 12, 13, 14),
                # 'rephrase_and_respond': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                # 'role_prompting': (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 14, 15),
                },
        }   
       
    def is_valid_prompt_template(self, prompt_tempĺate):
        if prompt_tempĺate['task_name'] in self.templates_to_select:
            if prompt_tempĺate['technique_name'] in self.templates_to_select[prompt_tempĺate['task_name']]:
                if int(prompt_tempĺate['technique_variation_id']) in self.templates_to_select[prompt_tempĺate['task_name']][prompt_tempĺate['technique_name']]:
                    return True
        return False
        
    def extract_template_data(self, target_path, source_db):
        files = []
        if 'consenso' in target_path.lower():
            technique_dirs = [
                os.path.join(target_path, technique_dir)
                for technique_dir in os.listdir(target_path)
                if os.path.isdir(os.path.join(target_path, technique_dir)) and 'consenso' in target_path.lower()
            ]
            
            for technique_dir in technique_dirs:
                task_files = [
                    os.path.join(technique_dir, task_file)
                    for task_file in os.listdir(technique_dir) if 'xlsx' not in task_file]
            import_tag = 'consenso'  
            
            files = task_files  
            
        elif 'reference' in target_path.lower():  
            task_dirs = [
                os.path.join(target_path, technique_dir)
                for technique_dir in os.listdir(target_path)
                if os.path.isdir(os.path.join(target_path, technique_dir)) and 'backup' not in technique_dir.lower()
            ]
            
            for task_dir in task_dirs:
                technique_files = [
                    os.path.join(task_dir, technique_file)
                    for technique_file in os.listdir(task_dir) if technique_file.endswith('.md')
                ]
                files.extend(technique_files)
                
            import_tag = 'reference' 
            
        pt_exceptions = ['winner_0', 'control_0']
            
        file_parsers = []    
        for file in tqdm(files):
            print(f'file: {file} import_tag: {import_tag}')
            file_parser = FileParser(file, import_tag)
            prompt_templates = file_parser._extract_variations()
            index = 0
            for key, prompt_template_variations in prompt_templates.items():
                # print(f'here is one prompt template variations: {key}\n {prompt_template_variations}')
                for prompt_template in prompt_template_variations:
                    
                    if prompt_template['piece_id'] == 0:
                        index += 1
                        
                    if self.is_valid_prompt_template(prompt_template):
                        prompt_template['technique_variation_id_idx'] = index
                        source_db.cache(prompt_template, '_prompt_pieces')

                        
        source_db.save()
        variation_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        df_prompt_pieces = source_db.to_df('_prompt_pieces')
        
        
        for pt_exception in pt_exceptions:
            df_prompt_pieces_c = df_prompt_pieces[df_prompt_pieces['technique_name'] == pt_exception]
            for id in variation_ids:
                df_prompt_pieces_c['technique_variation_id'] = id
                df_prompt_pieces_c['technique_variation_id_idx'] = id
                dict_list = df_prompt_pieces_c.to_dict(orient='records')
                for row in dict_list:
                    source_db.cache(row, '_prompt_pieces')
        source_db.save()    
        
        return source_db
    
                        #     if prompt_template['technique_name'] in pt_exceptions:
                        #     for id in range(9):
                        #         prompt_template['technique_variation_id'] = id +1
                        #         source_db.cache(prompt_template, '_prompt_pieces')
                        # else  
                    #     parsed_item.update({
                    #     'technique_variation_id': index,
                    #     'technique_variation_id_idx': None,
                    #     'technique_name': self.technique,
                    #     'task_name': current_task_name,
                    #     'obs':  None,
                    # })

    def get_dataset_metadata(self, target_path, source_db):
        """
        Extracts source data, creates metadata table, and stores dataset paths.

        Args:
            target_path (str): Path to the target directory for os.walk.
            source_db (Database): Database connection object.

        Returns:
            Database: Updated database with the metadata table.
        """
        # Create the metadata table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS _dataset_metadata (
            source_path TEXT NOT NULL,
            target_path TEXT,
            task TEXT,
            timestamp TEXT,
            obs TEXT,
            status TEXT,
            PRIMARY KEY (source_path)  
        
        );
        """
        source_db.execute_sql(create_table_query)   
        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS _results_metadata (
            task TEXT,
            technique TEXT,
            prompted INTEGER,
            not_prompted INTEGER,
            task_success INTEGER,
            task_failure INTEGER,
            obs TEXT,
            status TEXT,
            timestamp TEXT,
            PRIMARY KEY (task)  
        
        );
        """
        source_db.execute_sql(create_table_query)

        # Populate dataset metadata table
        dataset_metadata = get_dataset_paths(self.tasks, target_path)
        for metadata in dataset_metadata:
            source_db.cache(metadata, "_dataset_metadata")
        source_db.save()
        return source_db
    
    def extract_source_data(self, target_path, source_db, restart=True):
        if restart:
            source_db = self.get_dataset_metadata(target_path, source_db)
        df_dataset_metadata = source_db.to_df('_dataset_metadata')
        # Traverse and handle the source databases
        DEX = DatasetExtractor()
        for index, row in df_dataset_metadata.iterrows():
            target_path = row['target_path']
            source_path = row['source_path']
            task = row['task']

            try:
                # Parse the dataset using DatasetExtractor
                parsed_data_ = DEX.run(source_path, target_path, task)

                # Create table for parsed data
                table_name = f"source_{task}"
                columns = ", ".join([f'"{key}" TEXT' for key in parsed_data_[0].keys()])
                create_table_query = f"""
                CREATE TABLE IF NOT EXISTS "{table_name}" (
                    {columns}
                );
                """
                count = 0
                source_db.execute_sql(create_table_query)
                random.shuffle(parsed_data_)
                source_db.cache(parsed_data_, table_name)
                # Update metadata status
                dataset_metadata_status = ({
                        "source_path": source_path,
                        "target_path": target_path,
                        "task": task,
                        "timestamp": datetime.now().isoformat(),
                        "obs": None,
                        "status": 'success'
                    })
                
                source_db.cache(dataset_metadata_status, '_dataset_metadata')
   
                
            except Exception as e:
                # Handle errors and update metadata
                traceback.print_exc()
                error_msg = f"Failed to process {source_path}: {str(e)}"
                dataset_metadata_status = ({
                        "source_path": source_path,
                        "target_path": target_path,
                        "task": task,
                        "timestamp": datetime.now().isoformat(),
                        "obs": error_msg,
                        "status": 'fail'
                    })
                
                source_db.cache(dataset_metadata_status, '_dataset_metadata')
        source_db.save()
        return source_db

    def get_sample_size(self, population_size, margin_of_error=5, confidence_level=95):
        import math
        from scipy.stats import norm
        """
        Calculate the required sample size for a survey.

        Parameters:
        - population_size: Total number of individuals in the population.
        - margin_of_error: Desired margin of error (as a percentage, e.g., 5 for 5%).
        - confidence_level: Desired confidence level (as a percentage, e.g., 95 for 95%).

        Returns:
        - The required sample size (rounded up to the next whole number).
        """
        # Worst-case scenario for the proportion (maximum variability)
        p = 0.5

        # Convert margin of error from percentage to decimal
        E = margin_of_error / 100.0

        # Calculate the z-score for the given confidence level.
        # For a two-tailed test, we need the quantile for (1 - alpha/2)
        alpha = 1 - confidence_level / 100.0
        z = norm.ppf(1 - alpha / 2)

        # Calculate initial sample size (n0) for an infinite population
        n0 = (z**2 * p * (1 - p)) / (E**2)

        # Apply finite population correction
        n = n0 / (1 + ((n0 - 1) / population_size))

        return math.ceil(n)
    
    def replicate_prompts(self, db, source_db):# -> Any:
        db, source_db = self._replicate_prompt_pieces(db, source_db)
        return db, source_db
    
    def assemble_prompts(self, db, source_db, backup_db):# -> Any:
        print('STARTED assembling source')
        db, source_db = self._assemble_source(db, source_db)
        print('finished assembling source')
        db, source_db, backup_db = self._ready_prompts(db, source_db, backup_db)
        return db, source_db, backup_db
    
    def create_vectorstores(self, source_db):
        table_names = [table_name for table_name in source_db.list_tables() if 'source_' in table_name]
        
        for table_name in table_names:
            collection_name = table_name.replace("source", "example") + '_chromadb'
            # os.path.isdir(os.path.join(os.getcwd(), f'{collection_name}')) or 
            if 'code_search' in table_name or 'code_to_code_retrieval' in table_name:
                print(f'skipping chroma_db already created {exit}')
                continue
            self.create_vectorstore(table_name, source_db)
            # print(f'table_name: {table_name}, it has len {len_dataset}, after sampling: {sample_size}')
        return source_db  
            
    
    def get_len_table(self, table_name, source_db):
        from sqlalchemy.engine.row import Row
        filter_language = "('python', 'java', '.java --> .cs', '.cs --> .java')"
        filter_dataset = 'train'
        query = f'''
        SELECT COUNT(*) AS table_length 
        FROM "{table_name}" AS tn
        WHERE tn.language IN {filter_language}
            AND tn.dataset_id LIKE '%{filter_dataset}%';
        '''
        results = source_db.execute_sql(query)
        
        if not results:
            raise ValueError("No rows returned from execute_sql")
        
        row = results[0]
        table_length = row[0]
        
        return int(table_length)

    def create_vectorstore(self, table_name, source_db):
        filter_language = "('python', 'java', '.java --> .cs', '.cs --> .java')"
        filter_dataset_test = 'test'
        filter_dataset_valid = 'valid'
        filter_dataset_dev = 'dev'
        filter_dataset_eval = 'eval'
        
        query_len = f'''
        SELECT COUNT(*) AS table_length 
        FROM (
            SELECT DISTINCT tn.source_1, tn.source_2, tn.nl, tn.target
            FROM "{table_name}" AS tn
            WHERE tn.language IN {filter_language}
            AND (tn.dataset_id LIKE '%{filter_dataset_test}%' OR tn.dataset_id LIKE '%{filter_dataset_valid}%' OR tn.dataset_id LIKE '%{filter_dataset_dev}%' OR tn.dataset_id LIKE '%{filter_dataset_eval}%')
        ) sub;
        '''
        results = source_db.execute_sql(query_len)
        
        if not results:
            raise ValueError("No rows returned from execute_sql")
        
        row = results[0]
        table_length = row[0]
        
        sample_size = self.get_sample_size(table_length, margin_of_error=1, confidence_level=99)
        
        # print(f'For a DF with len {table_length}, we sampled and used: {sample_size}')
        query = f"""
        SELECT DISTINCT tn.source_1, tn.source_2, tn.nl, tn.target
        FROM "{table_name}" AS tn 
        WHERE tn.language IN {filter_language}
        AND (tn.dataset_id LIKE '%{filter_dataset_test}%' OR tn.dataset_id LIKE '%{filter_dataset_valid}%' OR tn.dataset_id LIKE '%{filter_dataset_dev}%' OR tn.dataset_id LIKE '%{filter_dataset_eval}%')
        LIMIT {sample_size};
        """
        rows = source_db.execute_sql(query)
        
        df = pd.DataFrame(rows).drop_duplicates()
        dict_rows = df.to_dict(orient="records")
        # print(f'ROWS: {dict_rows}')
        # if len(dict_rows) == 0:
        #     print(f'rows len == 0')
        #     return
                
        separator = "-"
        if "defect_detection" in table_name:
            documents = [
                Document(
                    page_content=example["source_1"],
                    metadata={"output": example["target"]},
                    id=f"{example['source_1'] + separator + example['target']}"
                )
                for example in dict_rows
            ]

        elif "clone_detection" in table_name:
            documents = [
                Document(
                    page_content=f"{example['source_1']}_--_{example['source_2']}",
                    metadata={"output": example["target"]},
                    id=f"{example['source_1'] + separator + example['source_2'] + separator + example['target']}"
                )
                for example in dict_rows
            ]

        elif "exception_type" in table_name:
            documents = [
                Document(
                    page_content=example["source_1"],
                    metadata={"output": example["target"]},
                    id=f"{example['source_1'] + separator + example['target']}"
                )
                for example in dict_rows
            ]

        elif "code_question_answering" in table_name:
            documents = [
                Document(
                    page_content=f"{example['nl']}_--_{example['source_1']}",
                    metadata={"output": example["target"]},
                    id=f"{example['nl'] + separator + example['source_1'] + separator + example['target']}"
                )
                for example in dict_rows
            ]

        elif "code_translation" in table_name:
            documents = [
                Document(
                    page_content=example["source_1"],
                    metadata={"output": example["target"]},
                    id=f"{example['source_1'] + separator + example['target']}"
                )
                for example in dict_rows
            ]

        elif "bug_fixing" in table_name:
            documents = [
                Document(
                    page_content=example["source_1"],
                    metadata={"output": example["target"]},
                    id=f"{example['source_1'] + separator + example['target']}"
                )
                for example in dict_rows
            ]

        elif "mutant_generation" in table_name:
            documents = [
                Document(
                    page_content=example["source_1"],
                    metadata={"output": example["target"]},
                    id=f"{example['source_1'] + separator + example['target']}"
                )
                for example in dict_rows
            ]

        elif "assert_generation" in table_name:
            documents = [
                Document(
                    page_content=example["source_1"],
                    metadata={"output": example["target"]},
                    id=f"{example['source_1'] + separator + example['target']}"
                )
                for example in dict_rows
            ]

        elif "code_summarization" in table_name:
            documents = [
                Document(
                    page_content=example["source_1"],
                    metadata={"output": example["target"]},
                    id=f"{example['source_1'] + separator + example['target']}"
                )
                for example in dict_rows
            ]

        elif "code_generation" in table_name:
            documents = [
                Document(
                    page_content=example["nl"],
                    metadata={"output": example["target"]},
                    id=f"{example['nl'] + separator + example['target']}"
                )
                for example in dict_rows
            ]

        elif "code_completion" in table_name:
            documents = [
                Document(
                    page_content=example["source_1"],
                    metadata={"output": example["target"]},
                    id=f"{example['source_1'] + separator + example['target']}"
                )
                for example in dict_rows
            ]
            
        else:
            pass        
        
        collection_name = table_name.replace("source", "example")
        # embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
        # embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
        embeddings = JinaEmbeddings(model_name="jinaai/jina-embeddings-v2-base-code")  # or "cuda" if using GPU

        vector_store = Chroma(
            collection_name=collection_name,
            embedding_function=embeddings,  
            persist_directory=f"./{collection_name}_chromadb"
        )
        for document in tqdm(documents):
            vector_store.add_documents([document])
    
    def query_data(self, table_name, sample_size, source_db):
        filter_language = "('python', 'java', '.java --> .cs', '.cs --> .java')"
        filter_dataset = 'train'
        
        if 'code_translation' not in table_name:
            query = f"""
                SELECT * 
                FROM "{table_name}" AS tn 
                WHERE tn.language IN {filter_language}
                    AND tn.dataset_id LIKE '%{filter_dataset}%'
                LIMIT {sample_size};
                """
            
            rows = source_db.execute_sql(query)    
            df = pd.DataFrame(rows)
            
        else:
            filter_language = "('.java --> .cs')"
            query = f"""
                SELECT * 
                FROM "{table_name}" AS tn 
                WHERE tn.language IN {filter_language}
                    AND tn.dataset_id LIKE '%{filter_dataset}%'
                LIMIT {sample_size/2};
                """
            
            rows = source_db.execute_sql(query)    
            df_java_c = pd.DataFrame(rows)
            
            filter_language = "('.cs --> .java')"
            query = f"""
                SELECT * 
                FROM "{table_name}" AS tn 
                WHERE tn.language IN {filter_language}
                    AND tn.dataset_id LIKE '%{filter_dataset}%'
                LIMIT {sample_size/2};
                """
            
            rows_2 = source_db.execute_sql(query)    
            df_c_java = pd.DataFrame(rows_2)
            df = pd.concat([df_java_c, df_c_java], ignore_index=True)
            
        return df
    
    def map_group(self, sub_df):
        sub_df['technique_variation_id'] = sub_df['technique_variation_id'].astype(int)
        unique_vals = sorted(sub_df['technique_variation_id'].unique())
        # unique_vals = sorted(sub_df['technique_variation_id'].astype(int).unique())
        mapping = {val: i + 1 for i, val in enumerate(unique_vals)}
        sub_df['technique_variation_id_idx'] = sub_df['technique_variation_id'].map(mapping)

        return sub_df

    
    def _assemble_source(self, db, source_db):
        table_names = [table_name for table_name in source_db.list_tables() if 'source_' in table_name]
        
        for table_name in table_names:
            if 'code_search' in table_name or 'code_to_code_retrieval' in table_name:
                continue
            len_dataset = self.get_len_table(table_name, source_db)
            sample_size = self.get_sample_size(len_dataset)
            if sample_size % 10 != 0:
                sample_size = ((sample_size // 10) + 1) * 10# Round up to the next multiple of 10

            df = self.query_data(table_name, sample_size, source_db)

            if 'idx' in df.columns:
                try:
                    table = Table(table_name, df)
                    dict_list = table.export_relevant_source_data()
                    for dict in dict_list:
                        source_db.cache(dict, '_source')
                        
                    source_db.save()
                except Exception as e:
                    print(f"exception~ {e}, for table: {table_name}")
                    traceback.print_exc()
                    continue
        
        df_prompt_pieces = source_db.to_df('_prompt_pieces')
        
        df_prompt_pieces_mapped = df_prompt_pieces.groupby(['task_name', 'technique_name'], group_keys=False).apply(self.map_group)
        
        source_db.cache(df_prompt_pieces_mapped.to_dict(orient='records'), '_prompt_pieces')
        
        return db, source_db

    def _ready_prompts(self, db, source_db, backup_db):
        dictlist_existing = backup_db.to_df('_prompts_ready').to_dict(orient='records')
        
        df_source = source_db.to_df('_source')
        
        filter_prompt_pieces = {
            'status': 'ready',
            'technique_name': [
                'exemplar_selection_knn', 
                # 'few_shot_contrastive_cot', 
                # 'tree_of_thought', 
                # 'self_ask', 
                # 'universal_self_consistency', 
                # 'self_refine', 
                # 'sg_in_context_learning', 
                # 'thread_of_thought', 
                # 'step_back_prompting', 
                # 'analogical_prompting', 
                # 'prompt_paraphrasing', 
                # 'emotional_prompting', 
                # 'style_prompting', 
                # 'rephrase_and_respond', 
                # 'role_prompting', 
                # 'reverse_cot',
                # 'winner_0',
                # 'control_0',
                ],
            'task_name': [
                'defect_detection',
                'clone_detection',
                'exception_type',
                'code_question_answering',
                'code_translation',
                'bug_fixing',
                'mutant_generation',
                'assert_generation',
                'code_summarization',
                'code_generation',
                ] 
            }
        
        df_prompt_pieces = source_db.to_df('_prompt_pieces', filter_dict=filter_prompt_pieces)
        df_prompt_pieces['technique_variation_id'] = df_prompt_pieces['technique_variation_id'].astype(int)
        df_prompt_pieces['technique_variation_id_idx'] = df_prompt_pieces['technique_variation_id_idx'].astype(int)

        if len(df_prompt_pieces) == 0:
            raise Exception('no prompt templates_ready')
        
        tqdm.pandas()
        try:
            df = pd.merge(
                df_source,            
                df_prompt_pieces,     
                how="inner", 
                left_on=["task_name", "group_id"],
                right_on=["task_name", "technique_variation_id_idx"]
            )
            # print(f'After merging, here is the len of the df: {len(df)}')
            
            df_grouped = df.groupby(["task_name", "technique_name", "language", "task_instance_id", "technique_variation_id_idx"])
            
            embeddings = JinaEmbeddings(model_name="jinaai/jina-embeddings-v2-base-code")
            for group_key, group_df in tqdm(df_grouped, total=len(df_grouped), desc="Processing Groups"):
                dict_list, embeddings = self._craft_prompt(group_df, embeddings)
                db.cache(dict_list, '_prompts_ready')
            db.save()
            
            for existing_record in dictlist_existing:
                db.cache(existing_record, '_prompts_ready')
            db.save()
            return db, source_db, backup_db

        except Exception as e:
            print(f'exception: {e}')
            traceback.print_exc()
            return db, source_db, backup_db

    def select_examples(self, df_variables, vector_store, task_name):
        # print('and here')
        
        if task_name == 'defect_detection':
            text_input = df_variables.loc[df_variables['variable_name'] == 'source_1', 'variable_value'].iloc[0]
            examples = {
                r'{input_1}': None, r'{output_1}': None,
                r'{input_2}': None, r'{output_2}': None,
                r'{input_3}': None, r'{output_3}': None,
                r'{input_4}': None, r'{output_4}': None,
                r'{input_5}': None, r'{output_5}': None,
            }
            input_number = 1
            

        elif task_name == 'clone_detection':
            snippet_1 = df_variables.loc[df_variables['variable_name'] == 'source_1', 'variable_value'].iloc[0]
            snippet_2 = df_variables.loc[df_variables['variable_name'] == 'source_2', 'variable_value'].iloc[0]
            text_input = f'{snippet_1}_--_{snippet_2}'
            examples = {
                r'{input1_1}': None, r'{input2_1}': None, r'{output_1}': None,
                r'{input1_2}': None, r'{input2_2}': None, r'{output_2}': None,
                r'{input1_3}': None, r'{input2_3}': None, r'{output_3}': None,
                r'{input1_4}': None, r'{input2_4}': None, r'{output_4}': None,
                r'{input1_5}': None, r'{input2_5}': None, r'{output_5}': None,
            }
            input_number = 2

            

        elif task_name == 'exception_type':
            text_input = df_variables.loc[df_variables['variable_name'] == 'source_1', 'variable_value'].iloc[0]
            examples = {
                r'{input_1}': None, r'{output_1}': None,
                r'{input_2}': None, r'{output_2}': None,
                r'{input_3}': None, r'{output_3}': None,
                r'{input_4}': None, r'{output_4}': None,
                r'{input_5}': None, r'{output_5}': None,
            }
            input_number = 1
            
        elif task_name == 'code_question_answering':
            question = df_variables.loc[df_variables['variable_name'] == 'nl', 'variable_value'].iloc[0]
            code_snippet = df_variables.loc[df_variables['variable_name'] == 'source_1', 'variable_value'].iloc[0]
            text_input = f'{question}_--_{code_snippet}'
            examples = {
                r'{input1_1}': None, r'{input2_1}': None, r'{output_1}': None,
                r'{input1_2}': None, r'{input2_2}': None, r'{output_2}': None,
                r'{input1_3}': None, r'{input2_3}': None, r'{output_3}': None,
                r'{input1_4}': None, r'{input2_4}': None, r'{output_4}': None,
                r'{input1_5}': None, r'{input2_5}': None, r'{output_5}': None,
            }#input 1 is question, input 2 is code
            input_number = 2
            
            
        elif task_name == 'code_translation':
            text_input = df_variables.loc[df_variables['variable_name'] == 'source_1', 'variable_value'].iloc[0]
            examples = {
                r'{input_1}': None, r'{output_1}': None,
                r'{input_2}': None, r'{output_2}': None,
                r'{input_3}': None, r'{output_3}': None,
                r'{input_4}': None, r'{output_4}': None,
                r'{input_5}': None, r'{output_5}': None,
            }
            input_number = 1
            
        elif task_name == 'bug_fixing':
            text_input = df_variables.loc[df_variables['variable_name'] == 'source_1', 'variable_value'].iloc[0]
            examples = {
                r'{input_1}': None, r'{output_1}': None,
                r'{input_2}': None, r'{output_2}': None,
                r'{input_3}': None, r'{output_3}': None,
                r'{input_4}': None, r'{output_4}': None,
                r'{input_5}': None, r'{output_5}': None,
            }
            input_number = 1
            
        elif task_name == 'mutant_generation':
            text_input = df_variables.loc[df_variables['variable_name'] == 'source_1', 'variable_value'].iloc[0]
            examples = {
                r'{input_1}': None, r'{output_1}': None,
                r'{input_2}': None, r'{output_2}': None,
                r'{input_3}': None, r'{output_3}': None,
                r'{input_4}': None, r'{output_4}': None,
                r'{input_5}': None, r'{output_5}': None,
            }
            input_number = 1
            

        elif task_name == 'assert_generation':
            text_input = df_variables.loc[df_variables['variable_name'] == 'source_1', 'variable_value'].iloc[0]
            examples = {
                r'{input_1}': None, r'{output_1}': None,
                r'{input_2}': None, r'{output_2}': None,
                r'{input_3}': None, r'{output_3}': None,
                r'{input_4}': None, r'{output_4}': None,
                r'{input_5}': None, r'{output_5}': None,
            }
            input_number = 1

        elif task_name == 'code_summarization':
            text_input = df_variables.loc[df_variables['variable_name'] == 'source_1', 'variable_value'].iloc[0]
            examples = {
                r'{input_1}': None, r'{output_1}': None,
                r'{input_2}': None, r'{output_2}': None,
                r'{input_3}': None, r'{output_3}': None,
                r'{input_4}': None, r'{output_4}': None,
                r'{input_5}': None, r'{output_5}': None,
            }
            input_number = 1

        elif task_name == 'code_generation':
            text_input = df_variables.loc[df_variables['variable_name'] == 'nl', 'variable_value'].iloc[0]
            examples = {
                r'{input_1}': None, r'{output_1}': None,
                r'{input_2}': None, r'{output_2}': None,
                r'{input_3}': None, r'{output_3}': None,
                r'{input_4}': None, r'{output_4}': None,
                r'{input_5}': None, r'{output_5}': None,
            }
            input_number = 1

        elif task_name == 'code_completion':
            text_input = df_variables.loc[df_variables['variable_name'] == 'source_1', 'variable_value'].iloc[0]
            examples = {
                r'{input_1}': None, r'{output_1}': None,
                r'{input_2}': None, r'{output_2}': None,
                r'{input_3}': None, r'{output_3}': None,
                r'{input_4}': None, r'{output_4}': None,
                r'{input_5}': None, r'{output_5}': None,
            }
            input_number = 1
                    
        else:

            
            return {}   
        
        results = vector_store.similarity_search(query=text_input, k=5)
        if len(results) > 0 and input_number == 1:
            for index, doc in enumerate(results):
                examples[r'{input_'+str(index+1)+r'}'] = doc.page_content
                examples[r'{output_'+str(index+1)+r'}'] = doc.metadata['output']
                
            return examples 
        
        elif len(results) > 0 and input_number == 2:
            for index, doc in enumerate(results):
                examples[r'{input1_'+str(index+1)+r'}'] = doc.page_content.split('_--_')[0]
                examples[r'{input2_'+str(index+1)+r'}'] = doc.page_content.split('_--_')[1]
                examples[r'{output_'+str(index+1)+r'}'] = doc.metadata['output']
            
            return examples    

        else:
            return {}   

    def incorporate_examples(self, message, examples):
        for key, value in examples.items():
            message = message.replace(key, value)
        
        return message
    
    def _craft_prompt(self, group, embeddings):
        if group.empty:
            return
        
        first_row = group.iloc[0]
        task_name = first_row['task_name']
        technique_variation_id_idx = first_row['technique_variation_id_idx']
        technique_name = str(first_row['technique_name'])
        task_instance_id = str(first_row['task_instance_id'])
        technique_variation_id = str(first_row['technique_variation_id'])
        language = str(first_row['language'])
        df_pieces = group.filter(items=['piece_id', 'message_template_type', 'piece_content']).drop_duplicates().sort_values(by='piece_id', ascending=True)
        df_variables = group.filter(items=['variable_name', 'variable_value']).drop_duplicates()
        
        try:
            target = df_variables.loc[df_variables['variable_name'] == 'target', 'variable_value'].iloc[0]
        except:
            print(f'target not found in group inside _craft_prompt. {technique_name}, {task_name}')
            return
        
        substitutions = df_variables[df_variables['variable_name'] != 'target'].drop_duplicates()
        prompt = Prompt(task_name=task_name, substitutions=substitutions, language=language)
        
        if technique_name == 'exemplar_selection_knn' or technique_name == 'winner_0':
            collection_name = f'example_{task_name}'
            
            vector_store = Chroma(
                collection_name=collection_name,
                embedding_function=embeddings,  
                persist_directory=f"./{collection_name}_chromadb"   
            )
            # print('arrived here')
            examples = self.select_examples(df_variables, vector_store, task_name)

        for row in df_pieces.itertuples(index=False):
            messager = row.message_template_type
            message = row.piece_content
            if technique_name == 'exemplar_selection_knn' or technique_name == 'winner_0':
                message = self.incorporate_examples(message, examples)
            prompt.input_text_line(messager, message)

        prompt_to_send = prompt.text_form
        
        if self.llms_used[task_name] == []:
            llms = ['gpt-4o']
            print(f'WARNING, no LLM for task: {task_name}, defaulting for gpt-4o')
        else:
            llms = self.llms_used[task_name]
            
        output = []
        for llm in llms:
            prompt_assembled = {
                'llm': llm,
                "task_name": str(task_name), 
                "task_instance_id": task_instance_id,  
                "technique_name": technique_name,  
                'technique_variation_id_idx': str(technique_variation_id_idx),
                "technique_variation_id": technique_variation_id, 
                'prompt_to_send': prompt_to_send,  
                "language": language, 
                'response': None,
                'time_prompt_sent': None,
                'time_prompt_received': None,
                'target': target,
                'tokens_sent': 0,
                'tokens_received': 0,
                'tokens_reasoning': 0,
            }
            output.append(prompt_assembled)
        return output, embeddings

class Prompt:
    def __init__(self, task_name=None, substitutions=None, language=None):
        self.text_form = ''
        self.template_form = None
        self.language = language
        self.replace_interface = self.get_replace_interface(task_name, substitutions)

    def input_text_line(self, messager, prompt_line):
        for key, value in self.replace_interface.items():
            prompt_line = prompt_line.replace(key, value)
        prompt_line_to_add = f'{messager}_--_{prompt_line}_-_'
        self.text_form += prompt_line_to_add
        self.craft_template_form()

    def craft_template_form(self):
        """
        Keywords available to control the message flow when the list contains an instance of 'assistant' messager:
            - 'prompt' - simply prompt the current conversation and proceed the conversation after the response
            - 'prompt_and_reset_conversation' - do the same, but reset the conversation after the output
            - divide_N [_not_keep_history] - divive the current conversaiton thread into two at this node. Optional to reset the conversation history
            - unify - merge the conversation threads into one again
        
        When a messager named 'finish' is found, what was left is discarded and the output is registered as output of the technique
        """
        try:
            messages = []
            raw_messages = self.text_form.split('_-_')
            for raw_message in raw_messages:
                
                if raw_message == '':
                    continue
                
                # print(f'THIS IS THE RAW MESSAGEE {raw_message} where {type(raw_message)}')
                splitted = raw_message.split('_--_')
                messager = splitted[0]
                message = splitted[1]
                # print(f'messager: {messager}')
                if 'system' in messager.lower():
                    messages.append(SystemMessage(content=message))
                elif 'human' in messager.lower():
                    messages.append(HumanMessage(content=message))
                elif 'assistant' in messager.lower() or 'aimessage' in messager.lower():
                    messages.append(message)
            self.template_form = messages
        except Exception as e:
            self.template_form = False
            print(f'Exception: {e}')
            traceback.print_exc()

    def input_text(self, prompt_string):
        self.text_form = prompt_string
        self.craft_template_form()

    def get_replace_interface(self, task_name, substitutions):
        if task_name is not None and substitutions is not None:
            if task_name == 'defect_detection':
                interface = {
                    r'{code}': str(substitutions.loc[substitutions['variable_name'] == 'source_1', 'variable_value'].iloc[0]), #
                    }
                return interface
            
            if task_name == 'clone_detection':
                interface = {
                    r'{code_snippet1}': str(substitutions.loc[substitutions['variable_name'] == 'source_1', 'variable_value'].iloc[0]),
                    r'{code_snippet2}': str(substitutions.loc[substitutions['variable_name'] == 'source_2', 'variable_value'].iloc[0]),
                    }
                return interface
            
            if task_name == 'exception_type':
                interface = {
                    r'{code}': str(substitutions.loc[substitutions['variable_name'] == 'source_1', 'variable_value'].iloc[0]),
                    }
                return interface
            
            if task_name == 'code_question_answering':
                interface = {
                    r'{code}': str(substitutions.loc[substitutions['variable_name'] == 'source_1', 'variable_value'].iloc[0]),
                    r'{question}': str(substitutions.loc[substitutions['variable_name'] == 'nl', 'variable_value'].iloc[0]), #
                    }
                return interface
            
            if task_name == 'code_search':
                interface = {
                    r'{query}': str(substitutions.loc[substitutions['variable_name'] == 'nl', 'variable_value'].iloc[0]), #
                    }
                return interface
            
            if task_name == 'code_to_code_retrieval':
                interface = {
                    r'{code}': str(substitutions.loc[substitutions['variable_name'] == 'source_1', 'variable_value'].iloc[0]),
                    }
                return interface
            
            if task_name == 'code_translation':
                source_language, target_language = self.language.split(' --> ')
                interface = {
                    r'{code}': str(substitutions.loc[substitutions['variable_name'] == 'source_1', 'variable_value'].iloc[0]), #
                    r'{source_language}': source_language.replace('.java', 'java').replace('.cs', 'c#'),
                    r'{target_language}': target_language.replace('.java', 'java').replace('.cs', 'c#'),
                    }
                return interface
            
            if task_name == 'bug_fixing':
                interface = {
                    r'{code}': str(substitutions.loc[substitutions['variable_name'] == 'source_1', 'variable_value'].iloc[0]),
                    }
                return interface
            
            if task_name == 'mutant_generation':
                interface = {
                    r'{code}': str(substitutions.loc[substitutions['variable_name'] == 'source_1', 'variable_value'].iloc[0]),
                    }
                return interface
            
            if task_name == 'assert_generation':
                interface = {
                    r'{code}': str(substitutions.loc[substitutions['variable_name'] == 'source_1', 'variable_value'].iloc[0]),
                    }
                return interface
            ###########
            if task_name == 'code_summarization':
                interface = {
                    r'{code}': str(substitutions.loc[substitutions['variable_name'] == 'source_1', 'variable_value'].iloc[0]),
                    }
                return interface
            ###########
            elif task_name == 'code_generation':
                interface = {
                    r'{task_description}': str(substitutions.loc[substitutions['variable_name'] == 'nl', 'variable_value'].iloc[0]), #
                    }
                return interface

            raise Exception(f"Incorrect_task_name: {task_name}")


class Table:
    def __init__(self, table_name, df_table_content):
        self.name = table_name
        self.content = df_table_content
        self.general_relevant_data = {
            'task_instance_id': self.content['idx'],
            'dataset_id': self.content['dataset_id'],
            'language': self.content['language'],
            'task_name': self.content['task'],
            'source_1': self.content['source_1'],
            'source_2': self.content['source_2'],
            "nl": self.content['nl'],
            'target': self.content['target'],
        }

   
    def export_relevant_source_data(self):
        df_export = pd.DataFrame(self.general_relevant_data)
        df_export = df_export.reset_index(drop=True)  # Ensure a clean 0-based index
        df_export['group_id'] = (df_export.index % 10) + 1
        pivoted_content = df_export.melt(
            id_vars=['task_instance_id', 'dataset_id', 'language','task_name', 'group_id'],
            value_vars=['source_1','source_2','target','nl'],
            var_name='variable_name',
            value_name='variable_value'
        )
        pivoted_content.dropna(inplace=True)
        final_export = pivoted_content.to_dict(orient='records')
        return final_export

class FileParser:
    def __init__(self, file_path, import_tag):
        """
        Initialize the FileParser class with a file path.

        Args:
            file_path (str): Path to the file to be processed.
        """
        self.file_path = file_path
        self.import_tag = import_tag
        self.technique = None
        self.task_name = None
        self.raw_file_content = None
        self.invalid_starting_tokens = ['---', '**', '-', '1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ', '10. ', '11. ', '12. ', '13. ', '    - ', 'variation ', 'Variation ', 'Below ', 'Each ', '─', '•', 'End of Variations', 'Each of ', '–']
        self.invalid_tokens = ['—', '“', '”']
        
        self.variations = {
            'defect_detection': [],
            'clone_detection': [],
            'exception_type': [],
            'code_question_answering': [],
            'code_search': [],
            'code_to_code_retrieval': [],
            'code_translation': [],
            'bug_fixing': [],
            'mutant_generation': [],
            'assert_generation': [],
            'code_summarization': [],
            'code_generation': [],
            'code_completion': [],
        }
        
        self.task_filenames = {
            'defect_detection': ["Defect_Detection", "Defect_detection"],            
            'clone_detection': ["Clone_Detection", 'clone_detection'],            
            'exception_type': ["Exception_Type", "Exception_Prediction",  "exception_prediction", 'exception_type_prediction'],            
            'code_question_answering': ["CodeQA", 'code_qa'],            
            'code_search': ["Code_Search"],            
            'code_to_code_retrieval': ["Code_Code_Retrieval", "Code-to-Code_Retrieval", "code_retrieval"],            
            'code_translation': ["Code_Translation"],            
            'bug_fixing': ["Bug_Fixing", "bug_fix"],            
            'mutant_generation': ["Mutant_Generation"],            
            'assert_generation': ["Assert_Generation"],            
            'code_summarization': ["Code_Summarization"],            
            'code_generation': ["Code_Generation", 'code_generation'],            
            'code_completion': ["Code Completion", 'Code_Completion'],    
        }
        
        self._extract_raw_filecontent()
            
    # def save_file_data(self, file_data, db):
    #     for prompt_template_text in file_data:
            
    #     return db
    
    def _extract_raw_filecontent(self):
        """
        Parse the file path to extract directory name, file name, and content.
        """
        # Extract the directory name (technique)
        if self.import_tag == 'consenso':
            file_key = os.path.splitext(os.path.basename(self.file_path))[0]
            self.technique = os.path.basename(os.path.dirname(self.file_path))
            
            for key, values in self.task_filenames.items():
                if file_key in values:
                    self.task_name = key
                    break
             
            if self.task_name == None:
                raise Exception(f'did not find the correct name {os.path.splitext(os.path.basename(self.file_path))[0]}')
            
        elif self.import_tag == 'reference':
            self.technique = os.path.splitext(os.path.basename(self.file_path))[0].replace('_replicated_report', '')
            self.task_name = os.path.basename(os.path.dirname(self.file_path))
        
        try:
            with open(self.file_path, 'r') as file:
                self.raw_file_content = file.read()
                self.lines_to_write = self.raw_file_content.splitlines()
        except Exception as e:
            print(f"Error reading file {self.file_path}: {e}")
            
    # def _run_syntax_correction_AI(self):    
    #     self.lines_to_write = []
    #     modification_count = 0
            
    #     if self.raw_file_content:
    #         lines = self.raw_file_content.splitlines()
    #         for line in lines:  
    #             if "AIMessagePromptTemplate.from_template(" in line:
    #                 line_w = line 
    #                 self.lines_to_write.append(line_w + '\n')
                
    #             elif "AIMessagePromptTemplate" in line:
    #                 if '#' in line:
    #                     line_m = line.split('#')[0]
    #                 else:
    #                     line_m = line   
                         
    #                 if '.' in line_m:
    #                     components = line_m.split('.')
    #                     for component in components:
    #                         if 'AIMessagePromptTemplate' in component:
    #                             line_w = f"{component.replace(',', '').rstrip()}.from_template('prompt')," 
    #                             modification_count += 1 
    #                         else:
    #                             if not component.endswith(','):
    #                                 line_w = f"{components[0]}.from_template('{component}')," 
    #                             else:
    #                                 component_ = component.replace(',', '')
    #                                 line_w = f"{components[0]}.from_template('{component_}')," 
    #                         self.lines_to_write.append(line_w + '\n')   
    #                         modification_count += 1
                        
    #                 else:
    #                     line_w = f"{line_m.replace(',', '').rstrip()}.from_template('prompt'),"
    #                     self.lines_to_write.append(line_w + '\n')   
    #                     modification_count += 1 
    #             else:
    #                 line_w = line 
    #                 self.lines_to_write.append(line_w + '\n')
                    
    #         print(f'Modification count: {modification_count} \nfor {self.file_path}')         
                     
                     
    #     if modification_count > 0:
    #         with open(self.file_path, 'w') as file:
    #             file.writelines(self.lines_to_write)
    #         return True
    #     else:
    #         return False
            
    def get_equiv_task_name(self, task_name):
        for key, values in self.task_filenames.items():
            if task_name in values or task_name == key:
                return key
        raise Exception(f'Key not found for taskname {task_name}')
    
    def move_self_to_parent(self, filepath):
        current_dir = os.path.dirname(filepath)
        parent_dir = os.path.dirname(current_dir)
        filename = os.path.basename(filepath)
        destination = os.path.join(parent_dir, filename)
        if os.path.exists(destination):
            counter = 1
            new_filename = f"{counter}_{filename}"
            new_destination = os.path.join(parent_dir, new_filename)
            while os.path.exists(new_destination):
                counter += 1
                new_filename = f"{counter}_{filename}"
                new_destination = os.path.join(parent_dir, new_filename)
            destination = new_destination
        
        print(f"Moving file from:\n  {filepath}\nto:\n  {destination}")
        try:
            shutil.move(filepath, destination)
            print("Move successful!")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    
    def _extract_variations(self):
        import threading
        threads = []
        try:
            lines = self.lines_to_write
            variation_lines = []
            variation_id = 0
            current_task_name = ''
            current_task_technique_count = {}
            for line in lines:
                if "ChatPromptTemplate.from_messages(" in line:
                    if '_template_' not in line:
                        raise Exception(f'ChatPromptTemplate line not assigned to variable with "_template_" in its name. {line}')
                    
                    new_task_name = line.split('_template_')[0].strip()
                    sub_technique_name = line.split('_template_')[1].strip()
                    
                    if new_task_name != self.task_name:
                        # self.move_self_to_parent(self.file_path)
                        raise Exception(f'ERROR: new_task_name {new_task_name} is not equal to the current task being processed {self.task_name}. \nfilename is {self.file_path}')

                    if variation_lines and current_task_name != '':  
                        task_equiv_name = self.get_equiv_task_name(current_task_name)
                        if task_equiv_name not in current_task_technique_count:
                            current_task_technique_count[task_equiv_name] = {}
                        if self.technique not in current_task_technique_count[task_equiv_name]:
                            current_task_technique_count[task_equiv_name][self.technique] = 0
                        
                        current_task_technique_count[task_equiv_name][self.technique] += 1
                        index = current_task_technique_count[task_equiv_name][self.technique]
                        
                        parsed_data = output_parsed_data(variation_lines, self.file_path, task_equiv_name)
                        
                        # t = threading.Thread(
                        #     target=output_parsed_data, 
                        #     args=(variation_lines, self.file_path, task_equiv_name),
                        # ).start()
                        # threads.append(t)
                        
                        for parsed_item in parsed_data:
                            parsed_item.update({
                                'technique_variation_id': index,
                                'technique_variation_id_idx': None,
                                'technique_name': self.technique,
                                'task_name': task_equiv_name,
                                'obs':  None,
                            })
                            
                            if current_task_name in self.variations:
                                self.variations[current_task_name].append(parsed_item)
                            else:
                                equiv_current_task_name = self.get_equiv_task_name(current_task_name)
                                self.variations[equiv_current_task_name].append(parsed_item)
                        
                    current_task_name = new_task_name   
                    variation_lines = [] 
                                
                for invalid_token in self.invalid_starting_tokens:        
                    if line.startswith(invalid_token):
                        line = line.replace(invalid_token,f'# {invalid_token}')
                        
                for invalid_token in self.invalid_tokens:
                    if not line.startswith(invalid_token):
                        line = line.replace(invalid_token,f'')  
                                
                variation_lines.append(line)

            # Append the last variation if any
            if variation_lines:
                
                task_equiv_name = self.get_equiv_task_name(current_task_name)
                if task_equiv_name not in current_task_technique_count:
                    current_task_technique_count[task_equiv_name] = {}
                if self.technique not in current_task_technique_count[task_equiv_name]:
                    current_task_technique_count[task_equiv_name][self.technique] = 0
                
                current_task_technique_count[task_equiv_name][self.technique] += 1
                index = current_task_technique_count[task_equiv_name][self.technique]
                parsed_data = output_parsed_data(variation_lines, self.file_path, task_equiv_name)
                
                # t = threading.Thread(
                #         target=output_parsed_data, 
                #         args=(variation_lines, self.file_path, task_equiv_name),
                #     ).start()
                # threads.append(t)
                
                for parsed_item in parsed_data:
                    parsed_item.update({
                        'technique_variation_id': index,
                        'technique_variation_id_idx': None,
                        'technique_name': self.technique,
                        'task_name': current_task_name,
                        'obs':  None,
                    })
                    if current_task_name in self.variations:
                        self.variations[current_task_name].append(parsed_item)
                    else:
                        equiv_current_task_name = self.get_equiv_task_name(current_task_name)
                        self.variations[equiv_current_task_name].append(parsed_item)
                    
            # for t in threads:
            #     t.join()
            # print(f'this is the variations: {self.variations}')
            return self.variations
        
        except Exception as e:
            traceback.print_exc()
            print(f'Found the exception above: {e} while parsing file: {self.file_path}')
            # raise Exception
            
def output_parsed_data(variation_lines, file_path, task_equiv_name):
    variation_parser = VariationParser(variation_lines, file_path, task_equiv_name)
    return variation_parser.parsed_data

class VariationParser:
    def __init__(self, variation_lines, file_path, current_task_name):
        started = False
        variation_lines_validated = []
        
        for variation_line in variation_lines:
            
            if '```' in variation_line and not '```python' in variation_line:
                break
            
            if started:
                variation_lines_validated.append(variation_line)
                
            if 'ChatPromptTemplate' in variation_line:
                variation_lines_validated.append(variation_line)
                started = True
            
        # print(f'these are the variation lines validated: {variation_lines_validated}, \n\nfrom variation lines: {variation_lines}')
        self.task_name = current_task_name
        self.file_path = file_path
        self.parsed_data = []
        self.variation_lines = "\n".join(variation_lines_validated)
        
        self._parse_variation()
        
    def _parse_variation(self):
        """
        Parse the variation to extract the type and content of each message template.
        """
        self.status = 'ready'
        try:
            # Parse the variation string into an abstract syntax tree (AST)
            tree = ast.parse(self.variation_lines)
            piece_id = 0
            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                    if node.func.attr == "from_template":
                        # Extract the message type (e.g., SystemMessagePromptTemplate or HumanMessagePromptTemplate)
                        message_type = node.func.value.id if isinstance(node.func.value, ast.Name) else None
                        # Extract the template content (first argument to the call)
                        if node.args and isinstance(node.args[0], ast.Constant):
                            message_content = node.args[0].value
                            
                            self.parsed_data.append({
                                'message_template_type': message_type,
                                'piece_content': message_content,
                                'piece_id': piece_id,
                                'status':  self.status,
                            })
                            piece_id += 1

        except Exception as e:
            print(f"Error parsing variation: {e}, from file: {self.file_path}\n Variation lines: {self.variation_lines}")
            traceback.print_exc()
    
    def _replicate_parsed_variation(self):
        from langchain_core.output_parsers import StrOutputParser
        from langchain_openai import ChatOpenAI
        from langchain_core.prompts import ChatPromptTemplate
        from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
        
        model = ChatOpenAI(model='o3-mini')
        output_parser = StrOutputParser()
        prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", f"You will receive a prompt template used to measure LLMs performance in a given task, your mission is to read it carefully and rephrase the strings within the SystemMessagePromptTemplate and HumanMessagePromptTemplate, leaving the AIMessagePromptTemplate untouched. Make sure to not interfere with the task or prompt technique being used since the prompt technique is also object of our study. At the end output the whole chat prompt template as in the format I gave to you and the rephrased strings. You will need to generate a total of 15 new prompt templates including the template I sent that you also should return as variation zero. Please do not alter the name of the variable that contain the prompt template"),
                ("user", "{variation_zero}"),
            ]
        )
        chain = prompt_template | model | output_parser
        
        print(f'sending prompt')
        input_data = {'variation_zero': self.variation_lines}
        output = chain.invoke(input_data)
        
        print(f'Received: {output}')
        return output
        
        
    def _generate_replication_report(self, variation_lines_objects):
        dir_path = os.path.join(os.path.dirname(self.file_path), self.task_name)
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)
        save_report_path = os.path.join(dir_path, os.path.basename(self.file_path.replace('.md', f'_replicated_report.md')))    

        with open(save_report_path, 'w') as file:
            file.write(variation_lines_objects)

        
class DatasetExtractor:
    def __init__(self):
        pass

    def run(self, source_path, target_path, task):
        """
        Parses a dataset file based on the task.

        Args:
            source_path (str): Path to the dataset file.
            task (str): Name of the task (e.g., "defect", "translation").

        Returns:
            list[dict]: Parsed dataset content as a list of dictionaries.
        """
        if not os.path.exists(source_path):
            raise FileNotFoundError(f"Dataset path does not exist: {source_path}")

        # Parse the dataset based on the task
        if task == "defect_detection":
            return self._parse_defect(source_path, task)
        elif task == "clone_detection":
            return self._parse_clone(source_path, task)
        elif task == "exception_type":
            return self._parse_exception(source_path, task)
        elif task ==  "code_question_answering":
            return self._parse_cosqa(source_path, target_path, task)
        elif task ==  "code_search":
            return self._parse_search(source_path, task)
        elif task == "code_to_code_retrieval":
            return self._parse_retrieval(source_path, task)
        elif task in ["code_translation", "bug_fixing", "mutant_generation", "assert_generation"]:
            return self._parse_seq2seq(source_path, target_path, task)
        elif task in ["code_summarization", "code_generation"]:
            return self._parse_summarization_or_generation(source_path, task)
        else:
            raise ValueError(f"Unsupported task: {task}")

    def _parse_defect(self, path, task):
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            
        data = []
        print(f'path {path}')
        filename = os.path.basename(path)
        for idx, line in enumerate(tqdm(lines, desc="Parsing defect data")):
            js = json.loads(line.strip())
            # code = " ".join(js["func"].split())
            # label = int(js["target"])
            # data.append({
            #     "idx": js["idx"],
            #     "task": task,
            #     "dataset_id": filename,
            #     "language": 'c',
            #     "source_1": code,
            #     "source_2": None,
            #     "target": "true" if label == 1 else "false",
            #     'obs': None,
            #     'nl': None,
            #     'status': None
            # })                   Correct
            data.append({
                "idx": idx,
                "task": task,
                "dataset_id": filename,
                "language": 'python',
                "source_1": js["function"],
                "source_2": None,
                "target": "###FALSE###" if js["label"] == 'Correct' else '###TRUE###',
                'obs': None,
                'nl': None,
                'status': None
            })
            
        return data

    def _parse_clone(self, path, task):
        idx_to_code = {}
        data_dir = os.path.dirname(path)
        with open(os.path.join(data_dir, "data.jsonl"), mode="r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in tqdm(lines, total=len(lines), desc="Loading raw data"):
                js = json.loads(line.strip())
                code = ' '.join(js['func'].split())
                idx_to_code[js['idx']] = code
    
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        data = []
        filename = os.path.basename(path)
        for idx, line in enumerate(tqdm(lines, desc="Parsing clone data")):
            url1, url2, label = line.strip().split('\t')
            if url1 not in idx_to_code or url2 not in idx_to_code:
                continue
            label = int(label)
            data.append({
                "idx": idx,
                "task": task,
                "dataset_id": filename,
                "language": 'java',
                "source_1": idx_to_code[url1],
                "source_2": idx_to_code[url2],
                "target": "###TRUE###" if str(label) == '1' else "###FALSE###",
                'obs': None,
                'nl': None,
                'status': None
            })
        return data

    def _parse_exception(self, path, task):
        # data_dir = os.path.dirname(path)
        # with open(os.path.join(data_dir, "types.txt"), mode="r", encoding="utf-8") as f:
        #     type_list = f.read().split()
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        data = []
        filename = os.path.basename(path)
        for idx, line in enumerate(tqdm(lines, desc="Parsing exception data")):
            js = json.loads(line.strip())
            code = " ".join(js["function"].split())
            target_txt = js["label"]
            data.append({
                "idx": idx,
                "task": task,
                "dataset_id": filename,
                "language": 'python',
                "source_1": code,
                "source_2": None,
                "target": f'''###{target_txt}###''',
                'obs': None,
                'nl': None,
                'status': None
            })
        return data

    def _parse_cosqa(self, source_path, target_path, task):
        test_answers = {}
        if target_path is None:
            with open(source_path, "r", encoding="utf-8") as source_f:
                source_data = json.load(source_f)
                target_lines = None
        else:
            with open(source_path, "r", encoding="utf-8") as source_f:
                source_data = json.load(source_f) 
                
            with open(target_path, "r", encoding="utf-8") as target_f:
                for line in target_f:
                    idx, label = line.strip().split("\t")
                    test_answers[idx] = int(label)    
        data = []   
        filename = os.path.basename(source_path)        
        for js in tqdm(source_data, total=len(source_data)):
            code = "".join(js["code"])
            nl = "".join(js["doc"])
            idx = js["idx"]
            if target_path is not None:
                label = test_answers[idx]
            else:
                label = js["label"]
            data.append({
                'idx': idx,
                "task": task,
                "dataset_id": filename,
                "language": 'python',
                "source_1": code,
                "source_2": None,
                "target": "###TRUE###" if str(label) == '1' else "###FALSE###",
                "nl": nl,
                'obs': None,
                'status': None
            })
        return data
    
    def _parse_search(self, path, task):
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        data = []
        count = 0
        filename = os.path.basename(path)
        for line in tqdm(lines, desc="Parsing retrieval/search data"):
            js = json.loads(line.strip())
            if 'code_tokens' in js:
                target = ''.join(js['code'])
            else:
                target = ''.join(js['function'])
            doc = ''.join(js['docstring_tokens'])
            language = js["language"]
             
            data.append({
                "idx": str(js.get("idx", count)),
                "task": task,
                "dataset_id": filename,
                "language": language,
                "source_1": None,
                "source_2": None,
                "target": target,
                'obs': None,
                'nl': doc,
                'status': None
            })
            count += 1
        return data
    
    def _parse_retrieval(self, path, task):
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        data = []
        filename = os.path.basename(path)
        for line in tqdm(lines, desc="Parsing retrieval/search data"):
            js = json.loads(line.strip())
            code = "".join(js["code"].split())
            data.append({
                "idx": js.get("index", None),
                "task": task,
                "dataset_id": filename,
                "language": 'c/c++',
                "source_1": code,
                "source_2": None,
                "target": js.get("label", None),
                'obs': None,
                'nl': None,
                'status': None
            })
        return data
    
    def _parse_seq2seq(self, source_path, target_path, task):
        # For seq2seq tasks like translation, fixing, mutant, assert
        with open(source_path, "r", encoding="utf-8") as source_f, \
             open(target_path, "r", encoding="utf-8") as target_f:
            source_lines = source_f.readlines()
            target_lines = target_f.readlines()
        
        assert len(source_lines) == len(target_lines)
        
        data = []

        if task == 'code_translation':
            source_lang = os.path.splitext(source_path)[1]
            target_lang = os.path.splitext(target_path)[1]
            language = f'{source_lang} --> {target_lang}'
        elif task == 'bug_fixing':
            language = 'java'
        elif task == 'mutant_generation':
            language = 'java'
        elif task == 'assert_generation':
            language = 'java'
        
        source_filename = os.path.basename(source_path)
        target_filename = os.path.basename(target_path)
        
        for idx, (source_line, target_line) in enumerate(zip(source_lines, target_lines)):
            data.append({
                "idx": str(idx),
                "task": task,
                "dataset_id": f'{source_filename} --> {target_filename}',
                "language": language,
                "source_1": source_line.strip(),
                "source_2": None,
                "target": target_line.strip(),
                'obs': None,
                'nl': None,
                'status': None
            })
        return data

    def _parse_summarization_or_generation(self, path, task):
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        data = []
        filename = os.path.basename(path)
        for idx, line in enumerate(tqdm(lines, desc="Parsing summarization/generation data")):
            js = json.loads(line.strip())

            if task == 'code_summarization':  
                source = " ".join(js["code_tokens"])
                target = " ".join(js["docstring_tokens"])
                language = js["language"]
                nl = None
                
            elif task == 'code_generation':
                # print(f' THIS IS THE path {path}')
                source = None
                nl = " ".join(js["nl"].split())
                target = "".join(js["code"].split())
                language = 'java'
                
            data.append({
                "idx": idx,
                "task": task,
                "dataset_id": filename,
                "language": language,
                "source_1": source,
                "source_2": None,
                "target": target,
                'obs': None,
                'nl': nl,
                'status': None
            })
        return data

# Example usage
# Assuming a file path like "/path/to/technique/task_name.txt"
if __name__ == "__main__":
    file_path = "/path/to/technique/task_name.txt"
    parser = FileParser(file_path)
    print("Technique:", parser.technique)
    print("Task Name:", parser.task_name)
    print("Raw File Content:", parser.raw_file_content)
    parser.extract_variations()
    print("Variations:", parser.variations)
