
from tools.prompt_template_assembler import Prompt

from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, FewShotPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import traceback 

import time
import random
import re
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

class Routine:
    def __init__(self, row):
        self.information = row
        self.model_name = row['llm']
        self.technique = row['technique_name']
        self.task_name = row['task_name']
        self.tokens_sent = 0
        self.tokens_received = 0
        self.tokens_reasoning = 0
        
        self.llm_chain = self._setup_llm(row['llm'])
        self.to_prompt = []
        self.conversation_history = []
        self.output_answer = {'status': False, 'content': None}
        self.output_text = None
        
        self.prompt = Prompt()
        self.prompt.input_text(row['prompt_to_send'].strip())
        self.prompt_template = self.prompt.template_form
    
    def _setup_llm(self, model_name):
        self.max_retries = 10000000000
        if 'gpt' in model_name or model_name == 'o1' or model_name == 'o3-mini':
            if model_name == 'o1' or model_name == 'o3-mini':
                self.model = ChatOpenAI(model=model_name, max_retries=2, reasoning_effort='low', max_tokens=6000)
            elif 'gpt' in model_name:
                self.model = ChatOpenAI(model=model_name, max_retries=2, max_tokens=1000)
    
        else:
            from langchain_together import ChatTogether
            if 'deepseek' in model_name.lower() and 'r1' in model_name.lower(): 
                self.model = ChatTogether(model=model_name, max_tokens=6000)
            else:
                self.model = ChatTogether(model=model_name, max_tokens=1000)
           
        chain = self.model 
        
        return chain
    
    def clear_conversation(self):
        self.to_prompt = []
        
    def make_answer_available(self):
        self.output_answer['status'] = True
    
    def llm_chain_invoke(self, prompt_messages=None):  
        wait_time = 0.01
        
        for attempt in range(1, self.max_retries + 1):
            if wait_time > 0:
                # print(f"Attempt {attempt}: Waiting {wait_time:.2f} seconds before retrying.")
                time.sleep(wait_time)
            try:
                if prompt_messages is None:
                    result = self.llm_chain.invoke(self.to_prompt)
                else:
                    result = self.llm_chain.invoke(prompt_messages)
                    
                return result 
            
            except Exception as e:
                # print(f"Attempt {attempt} failed with error: {e}")
                # Increment wait time by a random amount between 1 and 3 seconds
                additional_delay = random.uniform(1, 5)
                wait_time += additional_delay
                # print(f"Incrementing wait time by {additional_delay:.2f} seconds (total: {wait_time:.2f} seconds).")
        
        raise Exception("Max retries reached. llm_chain invocation failed.") from e
                

        
        # if not ('gpt' in self.model_name or self.model_name == 'o1' or self.model_name == 'o3-mini'):
        #     time.sleep(0.3)  
        # else:
        #     time.sleep(0.1)
        # return self.llm_chain.invoke(self.to_prompt)
    
    def send_prompt(self):
        try:
            
            self.output_answer['content'] = self.llm_chain_invoke()
            # message = (AIMessage(content=self.output_answer['content']))
            message = self.output_answer['content']
            
            
            self.tokens_sent += message.usage_metadata['output_tokens']
            self.tokens_received += message.usage_metadata['input_tokens']
            # self.tokens_reasoning += message.usage_metadata['tokens']
            
            if len(message.content) == 0:
                raise Exception(f'Llm {self.model_name} returned message with zero len string. message: {message}')
            self.to_prompt.append(message)
            self.conversation_history.append(f'---{type(message)}\n---{message.content}\n\n')
        except Exception as e:
            print(f'Exception occurred: {e}, technique {self.technique}, task {self.task_name}')
            traceback.print_exc()   
            raise Exception
        
    def begin(self):
        count_1 = 0
        for message in self.prompt_template:
            if isinstance(message, SystemMessage) or isinstance(message, HumanMessage):

                if self.output_answer['status']:
                    message.content = message.content.replace('{output_answer}', self.output_answer['content'].content)
                    self.output_answer['status'] = False
                    
                if self.technique == 'universal_self_consistency' and self.output_text is not None:  
                    message.content = message.content.replace('{output_text}', self.output_text)
                    
                self.to_prompt.append(message)
                self.conversation_history.append(f'---{type(message)}---{message.content}\n')
                count_1 += 1
            else:
                self.run_keyword(message)
                
        return self.conversation_history, self.tokens_sent, self.tokens_received
              
    # _-_assistant_--_prompt_-_assistant_--_finish_-_

    def run_keyword(self, keyword): 
        # print(f'keyword {keyword}')  
        
        if keyword == 'prompt':
            self.send_prompt()
            
        elif keyword == 'erase_previous_content':
            self.clear_conversation()
        
        elif keyword == 'output_answer':
            self.make_answer_available()
            
        elif keyword in self.routine:
            self.routine[keyword]()    
            
        elif keyword == 'finish':
            return False
        
        return True
               
                    
    
class RephraseAndRespond(Routine):
    def __init__(self, row):
        super().__init__(row)
        self.routine = {
            
        }



class RolePrompting(Routine):
    def __init__(self, row):
        super().__init__(row)
        self.routine = {
            
        }



class ReverseCOT(Routine):
    def __init__(self, row):
        super().__init__(row)
        self.routine = {
            
        }
        
        
        
class StylePrompting(Routine):
    def __init__(self, row):
        super().__init__(row)
        self.routine = {
            
        }



class EmotionalPrompting(Routine):
    def __init__(self, row):
        super().__init__(row)
        self.routine = {
            
        }



class PromptParaphrasing(Routine):
    def __init__(self, row):
        super().__init__(row)
        self.routine = {
            
        }
        
        
        
class AnalogicalPrompting(Routine):
    def __init__(self, row):
        super().__init__(row)
        self.routine = {
            
        }



class StepBackPrompting(Routine):
    def __init__(self, row):
        super().__init__(row)
        self.routine = {
            
        }



class ThreadOfThought(Routine):
    def __init__(self, row):
        super().__init__(row)
        self.routine = {
            
        }
        
        
        
class SGInContextLearning(Routine):
    def __init__(self, row):
        super().__init__(row)
        self.routine = {
            
        }



class SelfRefine(Routine):
    def __init__(self, row):
        super().__init__(row)
        self.routine = {
            'repeat_self_refine': self.repeat_self_refine
        }
        
    def repeat_self_refine(self):
        count = 0
        max_count = 10
        to_repeat = self.to_prompt[-1]
        while True:
            self.send_prompt()
            possible_output = self.output_answer['content'].content
            count += 1
            if '###FINISHED###' in possible_output or count > max_count:
                break
            else:
                self.to_prompt.append(to_repeat)
        



class React(Routine):
    def __init__(self, row):
        super().__init__(row)
        self.routine = {
            'repeat_react': self.repeat_react
        }
        
    def repeat_react(self):
        count = 0
        max_count = 10
        while True:
            to_repeat = self.to_prompt[0:1]
            self.to_prompt.extend(to_repeat)
            self.send_prompt()
            possible_output = self.output_answer['content'].content
            count += 1
            if '###FINISHED###' in possible_output or count > max_count:
                break
        
class UniversalSelfConsistency(Routine):
    def __init__(self, row):
        super().__init__(row)
        self.routine = {
            'self_consistency_multi_prompt': self.self_consistency_multi_prompt,
            'prompt_with_output_text': self.prompt_with_output_text
        }
        
    def self_consistency_multi_prompt(self):
        count = 0
        max_count = 10
        to_repeat = self.to_prompt[0:2]
        outputs = []
        while True:
            outputs.append(self.llm_chain_invoke(prompt_messages=to_repeat).content)
            count += 1
            if count > max_count:
                self.output_text = '\n-- response: '.join(outputs)
                # content_used_in_legal = 'I have generated the following responses to the question above: {output_text}\n select the most consistent response based on majority consensus'
                # self.to_prompt.append(HumanMessage(content=content_used_in_legal.replace(r'{output_text}', self.output_text)))
                # self.send_prompt()
                break
                
    def prompt_with_output_text(self):
        # to_prompt = []
        # conversation_history = []
        
        # for index, _ in enumerate(self.to_prompt):
        #     message = self.to_prompt[index]
        #     conversation_history_message = self.conversation_history[index]
        #     if '{output_text}' in message.content:
        #         print(f'=={index}here is the old to_prompt: {message.content}')
        #         message.content = message.content.replace('{output_text}', self.output_text)
                
        #         print(f'=={index}also the old conversation history: {conversation_history_message}')
        #         conversation_history_message = conversation_history_message.replace('{output_text}', self.output_text) 
            
        #     to_prompt.append(message)  
        #     conversation_history.append(conversation_history_message) 
            
        # self.to_prompt = to_prompt
        # self.conversation_history = conversation_history
        self.send_prompt()


class ExemplarSelectionKNN(Routine):
    def __init__(self, row):
        super().__init__(row)
        self.routine = {
            
        }
        
        
        
class ExemplarSelectionVoteK(Routine):
    def __init__(self, row):
        super().__init__(row)
        self.routine = {
            
        }
        
        
        
class FewShotContrastiveCOT(Routine):
    def __init__(self, row):
        super().__init__(row)
        self.routine = {
            
        }



class Dense(Routine):
    def __init__(self, row):
        super().__init__(row)
        self.routine = {
            
        }
        
        
        
class ExemplarOrdering(Routine):
    def __init__(self, row):
        super().__init__(row)
        self.routine = {
            
        }
        
        
        
class SelfAsk(Routine):
    def __init__(self, row):
        super().__init__(row)
        self.routine = {
            
        }
        
        
        
class TreeOfThought(Routine):
    def __init__(self, row):
        super().__init__(row)
        self.routine = {
            'repeat_tot': self.repeat_tot
        }
        
    def repeat_tot(self):
        count = 0
        max_count = 10
        to_repeat = self.to_prompt[-1]
        while True:
            self.send_prompt()
            possible_output = self.output_answer['content'].content
            count += 1
            if '###FINISHED###' in possible_output or count > max_count:
                break
            else:
                self.to_prompt.append(to_repeat)
        
        
class MoRE(Routine):
    def __init__(self, row):
        super().__init__(row)
        self.routine = {
            
        }



class MetaCOT(Routine):
    def __init__(self, row):
        super().__init__(row)
        self.routine = {
            
        }
        
        
        
class FewShotCOTUncertaintyRouted(Routine):
    def __init__(self, row):
        super().__init__(row)
        self.routine = {
            
        }
        
        
        
class FewShotCOTPromptMining(Routine):
    def __init__(self, row):
        super().__init__(row)
        self.routine = {
            
        }
        
        
        
class FewShotCOTComplexityBased(Routine):
    def __init__(self, row):
        super().__init__(row)
        self.routine = {
            
        }
        
        