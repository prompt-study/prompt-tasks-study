from tools.database import Database
import os
import pandas as pd
from datetime import datetime
from tqdm import tqdm
import ast
import re
import traceback
from tools.evaluation.general import acc, p_r_f1, map_score, mrr, exact_match
from tools.evaluation.google_bleu import google_bleu
from tools.evaluation.smooth_bleu import smooth_bleu
from tools.evaluation.rouge import rouge_l
from tools.evaluation.CodeBLEU.calc_code_bleu import code_bleu
from tools.report_rq1 import *
from tools.report_rq3 import *
import numpy as np


    
class ResultsRoutine:
    def __init__(self, source_db_path, target_db_path):
        self.prompts_db = Database(source_db_path)
        self.results_db = Database(target_db_path)
        # self.prompts_db_path = os.path.join(os.getcwd(), 'prompts.db')
        # self.prompts_db = Database(self.prompts_db_path)
        self.report_db_path = os.path.join(os.getcwd(), 'reports.db')
        self.report_db = Database(self.report_db_path)
        # self.backup_db_path = os.path.join(os.getcwd(), 'backup.db')
        # self.backup_db = Database(self.backup_db_path)
        self.prompts_table_name = '_prompts_ready'
        self.excluded_tasks = "('code_search', 'code_to_code_retrieval', 'code_completion')"
        self.techniques_selected = "('exemplar_selection_knn', 'few_shot_contrastive_cot', 'tree_of_thought', 'self_ask', 'universal_self_consistency', 'self_refine', 'sg_in_context_learning', 'thread_of_thought', 'step_back_prompting', 'analogical_prompting', 'prompt_paraphrasing', 'emotional_prompting', 'style_prompting', 'rephrase_and_respond', 'role_prompting', 'reverse_cot')" 
        self.llms_used = "('deepseek-ai/DeepSeek-V3', 'o3-mini', 'Qwen/Qwen2.5-Coder-32B-Instruct', 'meta-llama/Llama-3.3-70B-Instruct-Turbo')"
        self.max_fallbacks = {
            'defect_detection': 10,
            'clone_detection': 10,
            'exception_type': 10,
            'code_question_answering': 10,
            'code_translation': 2,
            'bug_fixing': 2,
            'mutant_generation': 2,
            'assert_generation': 3,
            'code_summarization': 10,
            'code_generation': 2,
        }

    
    def create_result_table(self, task_name):
        if task_name in ['defect_detection', 'clone_detection', 'exception_type', 'code_question_answering']:
            query =f'''
            CREATE TABLE IF NOT EXISTS '{task_name}_result' (
                llm	TEXT NOT NULL,
                task_name	TEXT NOT NULL,
                technique_name	TEXT NOT NULL,
                language	TEXT,
                status TEXT NOT NULL,
                {task_name}_acc REAL,
                {task_name}_precision REAL,
                {task_name}_recall REAL,
                {task_name}_f1 REAL,
                number_excluded INTEGER,
                avg_tokens_sent INTEGER,
                avg_tokens_received INTEGER,
                avg_total_tokens INTEGER,
                avg_cost INTEGER,
                std_dev_cost INTEGER,
                avg_prompt_time INTEGER,
                std_dev_prompt_time INTEGER,
                obs	TEXT,
            PRIMARY KEY (llm, task_name, technique_name, language)
            );'''
           
        elif task_name in ['code_translation', 'bug_fixing', 'code_generation']:
            query =f'''
            CREATE TABLE IF NOT EXISTS '{task_name}_result' (
                llm	TEXT NOT NULL,
                task_name	TEXT NOT NULL,
                technique_name	TEXT NOT NULL,
                language	TEXT,
                status TEXT NOT NULL,
                {task_name}_em TEXT,
                {task_name}_google_bleu REAL,
                {task_name}_smooth_bleu REAL,
                {task_name}_rouge_l REAL,
                {task_name}_codebleu REAL,
                {task_name}_cdb_ngram_match_score REAL,
                {task_name}_cdb_weighted_ngram_match_score REAL,
                {task_name}_cdb_syntax_match_score REAL,
                {task_name}_cdb_dataflow_match_score REAL,
                number_excluded INTEGER,
                avg_tokens_sent INTEGER,
                avg_tokens_received INTEGER,
                avg_total_tokens INTEGER,
                avg_cost INTEGER,
                std_dev_cost INTEGER,
                avg_prompt_time INTEGER,
                std_dev_prompt_time INTEGER,
                obs	TEXT,
            PRIMARY KEY (llm, task_name, technique_name, language)
            );'''
            
        elif task_name in ['mutant_generation', 'assert_generation', 'code_summarization']:
            query =f'''
            CREATE TABLE IF NOT EXISTS '{task_name}_result' (
                llm	TEXT NOT NULL,
                task_name	TEXT NOT NULL,
                technique_name	TEXT NOT NULL,
                language	TEXT,
                status TEXT NOT NULL,
                {task_name}_em TEXT,
                {task_name}_google_bleu REAL,
                {task_name}_smooth_bleu REAL,
                {task_name}_rouge_l REAL,
                {task_name}_codebleu REAL,
                number_excluded INTEGER,
                avg_tokens_sent INTEGER,
                avg_tokens_received INTEGER,
                avg_total_tokens INTEGER,
                avg_cost INTEGER,
                std_dev_cost INTEGER,
                avg_prompt_time INTEGER,
                std_dev_prompt_time INTEGER,
                obs	TEXT,
            PRIMARY KEY (llm, task_name, technique_name, language)
            );'''
            
        
        self.results_db.execute_sql(query)
        
    
    def create_table(self, table_name):
        # query = f'''
        #     DROP TABLE IF EXISTS '{table_name}';'''
        # self.results_db.execute_sql(query)
        
        query =f'''
            CREATE TABLE IF NOT EXISTS '{table_name}' (
                llm	TEXT NOT NULL,
                task_name	TEXT NOT NULL,
                task_instance_id	TEXT NOT NULL,
                technique_name	TEXT NOT NULL,
                technique_variation_id TEXT NOT NULL,
                technique_variation_id_idx TEXT,
                language	TEXT,
                response	TEXT,
                parsed_response TEXT,
                clean_response	TEXT,
                target	TEXT NOT NULL,
                prompt_time REAL NOT NULL,
                input_tokens INTEGER NOT NULL,
                output_tokens INTEGER NOT NULL,
                cost REAL NOT NULL,
                timestamp TEXT,
                obs	TEXT,
            PRIMARY KEY (llm, task_name, task_instance_id, technique_name, language)
            );'''
        
        self.results_db.execute_sql(query)
    
    def begin_eval(self):
        # df_prompts = self.fetch_new_data()
        # self.preprocess_data(df_prompts)
        # # print(f'WARNING: skipping preprocessing data')
        # self.eval_results()
        self.extract_reports()
        
    def create_table_report_rq3(self):
        table_name = 'rq3_report'
        query =f'''
            CREATE TABLE IF NOT EXISTS '{table_name}' (
                llm	TEXT NOT NULL,
                task_name	TEXT NOT NULL,
                technique_name	TEXT NOT NULL,
                language	TEXT,
                status TEXT NOT NULL,
                metric_name TEXT,
                number_excluded REAL,
                performance_result REAL,
                performance_over_token REAL,
                performance_over_time REAL,
                z_performance_result REAL,
                z_performance_over_token REAL,
                z_performance_over_time REAL,
                obs	TEXT,
            PRIMARY KEY (llm, task_name, technique_name, language)
            );'''
        
        self.results_db.execute_sql(query)
        
        query =f'''
            CREATE TABLE IF NOT EXISTS 'agg_ranked_performance' (
                technique_name	TEXT NOT NULL,
                z_performance_result REAL,
                placement	INTEGER,
            PRIMARY KEY (technique_name)
            );'''
        
        self.results_db.execute_sql(query)
        
        query =f'''
            CREATE TABLE IF NOT EXISTS 'agg_ranked_performance_token' (
                technique_name	TEXT NOT NULL,
                z_performance_over_token REAL,
                placement	INTEGER,
            PRIMARY KEY (technique_name)
            );'''
        
        self.results_db.execute_sql(query)
        
        query =f'''
            CREATE TABLE IF NOT EXISTS 'agg_ranked_performance_time' (
                technique_name	TEXT NOT NULL,
                z_performance_over_time REAL,
                placement	INTEGER,
            PRIMARY KEY (technique_name)
            );'''
        
        self.results_db.execute_sql(query)
        return table_name
    
    
    def create_table_report_rq1(self):
        table_name = 'rq1_report'
        query =f'''
            CREATE TABLE IF NOT EXISTS '{table_name}' (
                llm	TEXT NOT NULL,
                task_name	TEXT NOT NULL,
                technique_name	TEXT NOT NULL,
                language	TEXT,
                status TEXT NOT NULL,
                metric_name TEXT,
                metric_result REAL,
                number_excluded REAL,
                placement INTEGER,
                avg_tokens_sent REAL,
                avg_tokens_received REAL,
                avg_total_tokens REAL,
                avg_cost REAL,
                std_dev_cost REAL,
                avg_prompt_time REAL,
                std_dev_prompt_time REAL,
                obs	TEXT,
            PRIMARY KEY (llm, task_name, technique_name, language)
            );'''
        
        self.results_db.execute_sql(query)
        return table_name
    
    def select_metric_column(self, columns, affix, task_metric):
        for column in columns:
            if affix.lower() in column.lower():
                return column
        raise Exception(f'ERROR: weird affix {affix}, task metric: {task_metric}')
    
    def extract_reports(self):
        task_metric = {
            'defect_detection': '_acc',
            'clone_detection': '_f1',
            'exception_type': '_acc',
            'code_question_answering': '_acc',
            'code_translation': '_codebleu',
            'bug_fixing': '_codebleu', 
            'mutant_generation': '_smooth_bleu',
            'assert_generation': '_smooth_bleu',
            'code_summarization': '_smooth_bleu',
            'code_generation': '_codebleu',
        }
        
        progress_bar_done = tqdm(total=len(task_metric), position=0, unit=("table rq1"))
        results_tablenames = [results_tablename for results_tablename in self.results_db.list_tables() if '_results' not in results_tablename and '_result' in results_tablename and 'report' not in results_tablename]
        
        for results_tablename in results_tablenames:
            task_name = results_tablename.replace('_result', '')
            metric_affix = task_metric[task_name]
            df_results = self.results_db.to_df(results_tablename)
            columns = df_results.columns
            column_metric_name = self.select_metric_column(columns, metric_affix, task_name)
            result = report_rq1(df_results, column_metric_name)
            if result is not None:
                rq1_tablename = self.create_table_report_rq1()
                self.results_db.cache(result, rq1_tablename)
                self.results_db.save()  
                
            progress_bar_done.update(1)
            
        global_results_df = self.results_db.to_df(rq1_tablename)    
        result = complementary_report_rq1(global_results_df)
        self.results_db.cache(result, rq1_tablename)
        self.results_db.save()
        
        progress_bar_done = tqdm(total=len(task_metric), position=0, unit=("table rq3"))
        for results_tablename in results_tablenames:
            task_name = results_tablename.replace('_result', '')
            metric_affix = task_metric[task_name]
            df_results = self.results_db.to_df(results_tablename)
            columns = df_results.columns
            column_metric_name = self.select_metric_column(columns, metric_affix, task_name)
            result = report_rq3(df_results, column_metric_name)
            if result is not None:
                rq3_tablename = self.create_table_report_rq3()
                self.results_db.cache(result, rq3_tablename)
                self.results_db.save()  
                
            progress_bar_done.update(1)
            
        global_results_df = self.results_db.to_df(rq3_tablename)    
        results = complementary_report_rq3(global_results_df)
        print(f'run')
        for key, df in results.items():
            self.results_db.cache(df, key)
            self.results_db.save()
        
        # for results_tablename in results_tablenames:
        #     task_name = results_tablename.replace('_result', '')
        #     metric_affix = task_metric[task_name]
        #     df_results = self.results_db.to_df(results_tablename)
        #     columns = df_results.columns
        #     column_metric_name = self.select_metric_column(columns, metric_affix, task_name)
        #     result = report_rq1(df_results, column_metric_name)
        #     if result is not None:
        #         rq1_tablename = self.create_table_report_rq1()
        #         self.results_db.cache(result, rq1_tablename)
        #         self.results_db.save()  
                
        #     progress_bar_done.update(1)
            
        
    def fetch_new_data(self):
        df_preprocessed_prompt_data = self.results_db.to_df('prompting_results')
        df_prompts = self.prompts_db.to_df(self.prompts_table_name)
        raw_prompt_numbers = len(df_prompts)
        df_prompts = df_prompts[df_prompts['response'].notna()].copy()
        prompts_done_numbers = len(df_prompts)
        if prompts_done_numbers != raw_prompt_numbers:
            print(f'WARNING: gathering incomplete prompt results report')
            unit = "INCOMPLETE REPORT LINES"
        
        if len(df_preprocessed_prompt_data) == 0:
            return df_prompts
        
        else:        
            df_preprocessed_prompt_data['timestamp'] = pd.to_datetime(
                df_preprocessed_prompt_data['timestamp'], format='%Y-%m-%d %H:%M:%S.%f'
            )
            df_prompts['time_prompt_received'] = pd.to_datetime(
                df_prompts['time_prompt_received'], format='%Y-%m-%d %H:%M:%S.%f'
            )
            
            match_cols = [
                'llm', 'task_name', 'technique_name', 'language', 
                'task_instance_id', 'technique_variation_id', 'technique_variation_id_idx'
            ]
            
            merged = pd.merge(
                df_prompts,
                df_preprocessed_prompt_data[['timestamp'] + match_cols],
                on=match_cols,
                how='left'
            )
            
            selected = merged[
                (merged['timestamp'].isna()) | (merged['timestamp'] < merged['time_prompt_received'])
            ]

            df_prompts_done_new = selected[df_prompts.columns]
            # print("Merged DataFrame:")
            # print(merged)
            # print("\nSelected rows based on conditions:")
            # print(df_prompts_done_new)
            return df_prompts_done_new
            
            
    def preprocess_data(self, df_prompts_done):
        unit = 'lines'
        prompts_done_numbers = len(df_prompts_done)
        if prompts_done_numbers == 0:
            return
        progress_bar_done = tqdm(total=prompts_done_numbers, position=0, unit=unit)
        tables = set()
        processed_table = []
        
        for index, row in df_prompts_done.iterrows():
            result = Result(row)
            
            if result.task_name == 'defect_detection' and not result.error:
                result = self.clean_defect_detection(result)
                
            elif result.task_name == 'clone_detection' and not result.error:
                result = self.clean_clone_detection(result)
                
            elif result.task_name == 'exception_type' and not result.error:
                result = self.clean_exception_type(result)
                
            elif result.task_name == 'code_question_answering' and not result.error:
                result = self.clean_code_question_answering(result)
                
            elif result.task_name == 'code_translation' and not result.error:
                result = self.clean_code_translation(result)
                
            elif result.task_name == 'bug_fixing' and not result.error:
                result = self.clean_bug_fixing(result)
                
            elif result.task_name == 'mutant_generation' and not result.error:
                result = self.clean_mutant_generation(result)
                
            elif result.task_name == 'assert_generation' and not result.error:
                result = self.clean_assert_generation(result)
                
            elif result.task_name == 'code_summarization' and not result.error:
                result = self.clean_code_summarization(result)
                
            elif result.task_name == 'code_generation' and not result.error:
                result = self.clean_code_generation(result)
            
            table_name = 'prompting_results'
            self.create_table(table_name)
                
            self.results_db.cache(result.get_result(), table_name)
            progress_bar_done.update(1)
        
        self.results_db.save()
            
    # def eval_results(self):
        from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
        
        futures = []
        dfs_done = {}
        df_to_eval = self.results_db.to_df('prompting_results')
        df_to_eval_grouped = df_to_eval.groupby(["technique_name", "llm", "task_name"], )
        # modes = ['clean_response', 'parsed_response']
        # for mode in modes:
        len_df = len(df_to_eval_grouped)
        progress_bar_done = tqdm(total=len_df, position=0, unit='evaluations')
        df_llms_finished = self.report_db.to_df('progress_by_llm')
        df_llms_finished = df_llms_finished[df_llms_finished['prompts_remaining'].astype(int) <= 10]
        
        with ProcessPoolExecutor(max_workers=8) as executor:
            for group_name, group in df_to_eval_grouped:
                technique_name, llm, task_name = group_name
                table_name = task_name + '_result'
                if table_name not in dfs_done:
                    dfs_done[table_name] = self.results_db.to_df(table_name)
                    
                redo = True
                current_df_status = dfs_done[table_name].copy()
                for column_name in current_df_status.columns:
                    if '_f1' in column_name:
                        curr_to_do = current_df_status[
                            (current_df_status['technique_name'] == technique_name) &
                            (current_df_status['llm'] == llm) &
                            (current_df_status['task_name'] == task_name) 
                        ]
                        if len(curr_to_do) == 1 and curr_to_do[column_name].iloc[0] is not None and float(curr_to_do[column_name].iloc[0]) == 1:
                            redo = True
                        elif len(curr_to_do) > 1:
                            print(f'ERROR: len curr to do: {len(curr_to_do)}')
                            
                # redo = task_name in ['defect_detection', 'clone_detection', 'exception_type', 'code_question_answering']
                # print(f'for: {technique_name}, {llm}, {task_name}')
                if len(current_df_status) > 0:
                    # print(f'len current status > 0')
                    done = any((current_df_status['technique_name'] == technique_name) &
                        (current_df_status['llm'] == llm) &
                        (current_df_status['task_name'] == task_name) &
                        (current_df_status['status'] == 'success')) and any(df_llms_finished['llm'] == llm)
                    # print(f"debugging done: technique_name {any(current_df_status['technique_name'] == technique_name)}")
                    # print(f"debugging done: llm {any(current_df_status['llm'] == llm)}")
                    # print(f"debugging done: task_name {any(current_df_status['task_name'] == task_name)}")
                    # print(f"debugging done: status {any(current_df_status['status'] == 'success')}")
                    # print(f"debugging done: llms finished {any(df_llms_finished['llm'] == llm)}")
                    
                else:
                    done = False
                    
                # print(f'done value returned {done}, redo {redo}')        
                if not done or redo:    
                    # print(f'technique_name is {technique_name}, llm is {llm}, task_name is {task_name}, status is success')
                    # result = evaluate_task_results(task_name, technique_name, llm, group, mode=None)
                    max_fallback_no = self.max_fallbacks[task_name]
                    future = executor.submit(evaluate_task_results, task_name, technique_name, llm, group, max_fallback_no, mode=None)
                    futures.append(future)
                else:
                    progress_bar_done.update(1)
                    
            for future in as_completed(futures):
                result, task_name = future.result()      
                table_name = task_name + '_result'
                progress_bar_done.update(1)
                if result is not None:
                    self.create_result_table(task_name)
                    self.results_db.cache(result, table_name)
                    self.results_db.save()  

    
    def clean_defect_detection(self, result):
        parsed_response = result.response
        result.target = self.to_binary(result.target)
        
        response_result, response_status = self.get_bool_outcome(parsed_response, separator='###')
        if not response_status:
            result.increment_fallback(response_result)
        else:
            result.set_clean_response(response_result)
            return result
        
        response_result, response_status = self.find_and_return_separators_content(parsed_response)
        if not response_status:
            result.increment_fallback(response_result)
            
        else:
            response_result, response_status = self.get_bool_outcome(response_result)
            if not response_status:
                result.increment_fallback(response_result)
            else:
                result.set_clean_response(response_result)
                return result
        
        response_result, response_status = self.get_bool_outcome(parsed_response)
        if not response_status:
            result.increment_fallback(response_result)
            result.set_clean_response(parsed_response)
        else:
            result.set_clean_response(response_result)
            return result
        
        return result

    def clean_clone_detection(self, result):        
        parsed_response = result.response
        result.target = self.to_binary(result.target)
        
        response_result, response_status = self.get_bool_outcome(parsed_response, separator='###')
        if not response_status:
            result.increment_fallback(response_result)
        else:
            result.set_clean_response(response_result)
            return result
        
        response_result, response_status = self.find_and_return_separators_content(parsed_response)
        if not response_status:
            result.increment_fallback(response_result)
            
        else:
            response_result, response_status = self.get_bool_outcome(response_result)
            if not response_status:
                result.increment_fallback(response_result)
            else:
                result.set_clean_response(response_result)
                return result
        
        response_result, response_status = self.get_bool_outcome(parsed_response)
        if not response_status:
            result.increment_fallback(response_result)
            result.set_clean_response(parsed_response)
        else:
            result.set_clean_response(response_result)
            return result
        
        return result

    def clean_exception_type(self, result):
        parsed_response = result.response
        target = result.target
        
        response_result, response_status = self.find_and_return_separators_content(parsed_response)
        if response_status:
            separator_usage = 'separators_present'
            parsed_response = response_result
            
        else:
            separator_usage = response_result
            
        if target.lower() in parsed_response.lower():
            response_result, response_status = True, f'target in response, {separator_usage}'
            result.set_clean_response(target.replace('#', ''))
        
        else:
            response_result, response_status = False, f'target not in response,  {separator_usage}'
            result.set_clean_response(parsed_response.replace('#', ''))
        
        return result

    def clean_code_question_answering(self, result):
        parsed_response = result.response
        result.target = self.to_binary(result.target)
        
        response_result, response_status = self.get_bool_outcome(parsed_response, separator='###')
        if not response_status:
            result.increment_fallback(response_result)
        else:
            result.set_clean_response(response_result)
            return result
        
        response_result, response_status = self.find_and_return_separators_content(parsed_response)
        if not response_status:
            result.increment_fallback(response_result)
            
        else:
            response_result, response_status = self.get_bool_outcome(response_result)
            if not response_status:
                result.increment_fallback(response_result)
            else:
                result.set_clean_response(response_result)
                return result
        
        response_result, response_status = self.get_bool_outcome(parsed_response)
        if not response_status:
            result.increment_fallback(response_result)
            result.set_clean_response(parsed_response)
        else:
            result.set_clean_response(response_result)
            return result
        
        return result

    def clean_code_translation(self, result):
        parsed_response = result.response
        if result.language == '.java --> .cs':
            separator_1 = '```csharp'
            separator_2 = '```'
            
        if result.language == '.cs --> .java':
            separator_1 = '```java'
            separator_2 = '```'
            
        response_result, response_status = self.find_and_return_separators_content(parsed_response, separator_1=separator_1, separator_2=separator_2)
        if not response_status:
            result.increment_fallback(response_result)
        else:
            result.set_clean_response(response_result)
            return result
        
        response_result, response_status = self.find_and_return_separators_content(parsed_response)    
        if not response_status:
            result.increment_fallback(response_result)
        else:
            result.set_clean_response(response_result)
            return result

        result.set_clean_response(parsed_response)
        return result

    def clean_bug_fixing(self, result):
        parsed_response = result.response
        response_result, response_status = self.find_and_return_separators_content(parsed_response, separator_1='```java', separator_2='```')
        if not response_status:
            result.increment_fallback(response_result)
        else:
            result.set_clean_response(response_result)
            return result
        
        response_result, response_status = self.find_and_return_separators_content(parsed_response)    
        if not response_status:
            result.increment_fallback(response_result)
        else:
            result.set_clean_response(response_result)
            return result

        result.set_clean_response(parsed_response)
        return result

    def clean_mutant_generation(self, result):
        parsed_response = result.response
        response_result, response_status = self.find_and_return_separators_content(parsed_response, separator_1='```java', separator_2='```')
        if not response_status:
            result.increment_fallback(response_result)
        else:
            result.set_clean_response(response_result)
            return result
        
        response_result, response_status = self.find_and_return_separators_content(parsed_response)    
        if not response_status:
            result.increment_fallback(response_result)
        else:
            result.set_clean_response(response_result)
            return result

        result.set_clean_response(parsed_response)
        return result

    def clean_assert_generation(self, result):
        parsed_response = result.response
        response_result, response_status = self.find_and_return_separators_content(parsed_response, separator_1='```java', separator_2='```')
        if not response_status:
            result.increment_fallback(response_result)
        else:
            result.set_clean_response(response_result)
            return result
        
        response_result, response_status = self.find_and_return_separators_content(parsed_response, separator_1='`', separator_2='`')
        if not response_status:
            result.increment_fallback(response_result)
        else:
            result.set_clean_response(response_result)
            return result
        
        response_result, response_status = self.find_and_return_separators_content(parsed_response)    
        if not response_status:
            result.increment_fallback(response_result)
        else:
            result.set_clean_response(response_result)
            return result

    
        response_result = parsed_response.replace('#', '').replace('FINISHED', '')
        result.set_clean_response(response_result)
        
        return result
    
    def clean_code_summarization(self, result):
        parsed_response = result.response
        result.set_clean_response(parsed_response)
        return result

    def clean_code_generation(self, result):
        parsed_response = result.response
        response_result, response_status = self.find_and_return_separators_content(parsed_response, separator_1='```java', separator_2='```')
        if not response_status:
            result.increment_fallback(response_result)
        else:
            result.set_clean_response(response_result)
            return result
        
        response_result, response_status = self.find_and_return_separators_content(parsed_response)    
        if not response_status:
            result.increment_fallback(response_result)
        else:
            result.set_clean_response(response_result)
            return result

        result.set_clean_response(parsed_response)
        return result

    def find_and_return_separators_content(self, message, separator_1='###', separator_2='###'):
        if separator_1 not in message or separator_2 not in message:
            return f'ERROR: separators: {separator_1} or {separator_2} not present in message {message}', False
        
        if separator_1 == separator_2:
            occurrences = message.count(separator_1)
            if occurrences != 2:
                return (f"ERROR: Expected exactly 2 occurrences of separator '{separator_1}' in message, found {occurrences}."), False
            
            first_index = message.find(separator_1)
            second_index = message.find(separator_1, first_index + len(separator_1))
            content = message[first_index + len(separator_1): second_index]
            return content.strip(), True
        
        else:
            pattern = f"(?P<sep1>{re.escape(separator_1)})|(?P<sep2>{re.escape(separator_2)})"
            matches = list(re.finditer(pattern, message))
            sep1_matches = [m for m in matches if m.group('sep1')]
            sep2_matches = [m for m in matches if m.group('sep2')]

            if len(sep1_matches) != 1 or len(sep2_matches) != 1:
                return (
                    f"ERROR: Expected exactly 1 occurrence of each separator, but found {len(sep1_matches)} of '{separator_1}' and {len(sep2_matches)} of '{separator_2}'.",
                    False,
                )
            if sep1_matches[0].start() > sep2_matches[0].start():
                return (
                    f"ERROR: Separator '{separator_1}' should appear before '{separator_2}' in message {message}.",
                    False,
                )

            content = message[sep1_matches[0].end() : sep2_matches[0].start()]
            return content.strip(), True

    def get_bool_outcome(self, string, separator=''):
        contains_false_response = f'{separator}false{separator}' in string.lower()
        contains_true_response = f'{separator}true{separator}' in string.lower()
        
        if contains_false_response and contains_true_response:
            result = f'ERROR: input contains both true and false {string}'
            return result, False
            
        elif not contains_false_response and not contains_true_response:
            result = f'ERROR: input contains neither true or false {string}'
            return result, False
            
        elif contains_false_response and not contains_true_response:
            return False, True
            
        elif not contains_false_response and contains_true_response:
            return True, True
            
    def to_binary(self, s):
        s = s.strip().lower().replace('#', '')
        binary_equivalence = {
            'true': 1,
            '1': 1,
            'yes': 1,
            'false': 0,
            '0': 0,
            'no': 0,
        }
        for key, value in binary_equivalence.items():
            if s == key:
                return value
        else:
            raise ValueError(f"Unexpected value: {s}")
        
        
class Result:
    def __init__(self, row):
        self.row = row
        self.llm = row['llm']
        self.task_name = row['task_name']
        self.language = row['language']
        self.input_tokens = row['tokens_sent']
        self.output_tokens = row['tokens_received']
        self.cost = self.get_cost()
        self.fallback_number = 0
        self.fallback = False
        self.error = False
        self.clean_response = None
        self.response = self._response_parser(row['response'])
        self.target = row['target']
        time_prompt_received = datetime.strptime(str(row['time_prompt_received']), '%Y-%m-%d %H:%M:%S.%f')
        
        time_prompt_sent = datetime.strptime(row['time_prompt_sent'], '%Y-%m-%d %H:%M:%S.%f')
        self.prompt_time = time_prompt_received - time_prompt_sent
    
    def get_cost(self):
        million_tokens = 1000000
        cost_table = {
            'deepseek-ai/DeepSeek-V3': 
                {'input': 1.25/million_tokens, 
                'output': 1.25/million_tokens},
            'o3-mini': 
                {'input': 1.10/million_tokens, 
                'output': 4.40/million_tokens},
            'Qwen/Qwen2.5-Coder-32B-Instruct': 
                {'input': 1.20/million_tokens, 
                'output': 1.20/million_tokens}, 
            'meta-llama/Llama-3.3-70B-Instruct-Turbo': 
                {'input': 0.88/million_tokens, 
                'output': 0.88/million_tokens}, 
        }
        
        cost = (self.output_tokens * cost_table[self.llm]['output']) + (self.input_tokens * cost_table[self.llm]['input'])
        return cost
        
    def increment_fallback(self, fallback):
        if not self.error:
            self.fallback_number += 1
            self.fallback = fallback
        else:
            raise Exception('tried to increment fallback on Result class with error')
        
    def set_error(self, error):
        self.error = error
        
    def _get_obs(self):
        if self.error and not self.fallback:
            return f'ERROR: {str(self.error)} \nLast fallback_number {self.fallback_number}'
        
        elif not self.error and self.fallback:
            return f'success: Fallback Number: {self.fallback_number}\nInfo: {str(self.fallback)}'
        
        elif not self.error and not self.fallback:
            return f'success'
        
        else:
            raise Exception (f'ERROR: error and fallback not none')
        
        
    def _response_parser(self, response):
        try:
            messages = ast.literal_eval(response)
            
        except Exception as e:
            self.set_error(f"Invalid response format. Unable to parse as list: \n{e}")
            return 
        
        pattern = re.compile(r"^---<class '.*\.(\w+)'>\s*---\s*(.*)$", re.DOTALL)
        
        parsed_response = []
        for msg in messages:
            match = pattern.match(msg)
            if match:
                msg_type = match.group(1)
                content = match.group(2).strip()  
                parsed_response.append((msg_type, content))
            else:
                parsed_response.append(("unknown", msg.strip()))
        
        return parsed_response[-1][-1]
    
    def set_clean_response(self, clean_response):
        if not self.error:
            self.clean_response = clean_response   
        else:
            raise Exception('tried to set_clean_response on Result class with error')
    
    def get_result(self):
            
        result = {
                "llm": self.llm, 
                "task_name": self.task_name, 
                "task_instance_id": self.row['task_instance_id'], 
                'technique_variation_id': self.row['technique_variation_id'], 
                'technique_variation_id_idx': self.row['technique_variation_id_idx'], 
                "technique_name": self.row['technique_name'], 
                "language": self.language, 
                "response": self.row['response'], 
                "parsed_response": self.response, 
                "clean_response": self.clean_response, 
                "target": str(self.target).replace('#',''), 
                "obs": self._get_obs(), 
                "input_tokens": self.input_tokens ,
                "output_tokens": self.output_tokens,
                "cost": self.cost,
                'prompt_time': str(self.prompt_time),
                'timestamp': str(self.row['time_prompt_received'])
            }   

        return result
    
def get_fallback_number(fallback_string):
    
    if 'Fallback' not in fallback_string:
        return None
    
    for num in range(0, 10):
        if f'Fallback Number: {num}' in fallback_string:
            return int(num)
    print(f'Warning: fallback number not found')
    return False

def filter_bool_data(preds, golds):
    clean_preds = []
    clean_golds = []
    number_excluded = 0
    for pred, gold in zip(preds, golds):
        if str(pred) in ['0', '1'] and str(gold) in ['0', '1']:
            clean_preds.append(to_binary(pred))
            clean_golds.append(to_binary(gold))
        else:
            number_excluded += 1
    
    return clean_preds, clean_golds, number_excluded

def filter_invalid_data(preds, golds, max_fallback_no, obs):
    clean_preds = []
    clean_golds = []
    number_excluded = 0
    for pred, gold, current_obs in zip(preds, golds, obs):
        current_fallback_no = get_fallback_number(current_obs)
        if current_fallback_no is None or current_fallback_no <= max_fallback_no:
            clean_preds.append(pred)
            clean_golds.append(gold)
        else:
            number_excluded += 1
            
    return clean_preds, clean_golds, number_excluded

def evaluate_task_results(task_name, technique_name, llm, group, max_fallback_no, mode=None):
    if mode == 'clean_response':
        preds = group[mode].tolist()
        golds = group['target'].tolist()
        llm = llm + f'_{mode}'
        
    elif mode == 'parsed_response':
        preds = group[mode].tolist()
        golds = group['target'].tolist()
        llm = llm + f'_{mode}'
    
    else:
        preds = group['clean_response'].tolist()
        golds = group['target'].tolist()
        
    obs = group['obs']     
       
    group['prompt_time'] = pd.to_timedelta(group['prompt_time'])  

    group['prompt_time_seconds'] = group['prompt_time'].dt.total_seconds()

    results = {
        f'{task_name}_acc': None,
        f'{task_name}_precision': None,
        f'{task_name}_recall': None,
        f'{task_name}_f1': None,
        f'{task_name}_em': None,
        f'{task_name}_google_bleu': None,
        f'{task_name}_smooth_bleu': None,
        f'{task_name}_rouge_l': None,
        f'{task_name}_codebleu': None,
        f'avg_tokens_sent': group["input_tokens"].astype(int).mean(),
        f'avg_tokens_received': group["output_tokens"].astype(int).mean(),
        f'avg_total_tokens': (group["input_tokens"].astype(int) + group["output_tokens"].astype(int)).mean(),
        f'avg_cost': group["cost"].astype(float).mean(),
        f'std_dev_cost': group["cost"].astype(float).std(),
        f'avg_prompt_time': group['prompt_time_seconds'].mean(),
        f'std_dev_prompt_time': group['prompt_time_seconds'].std(),
    }
    if technique_name == 'prompt_paraphrasing':
        print(f'warning: skipping prompt paraphrasing')
        return {}
    
    if None in preds:
        raise Exception(f'None present in preds')
    if None in golds:
        raise Exception(f'None present in golds')
    
    if task_name in ['defect_detection']:
        try:
            clean_preds, clean_golds, number_excluded = filter_bool_data(preds, golds)
            lang = group['language'].tolist()[0]
            if ' --> ' in lang:
                lang = lang.split(' --> ')[0]
                lang = lang.replace('.java','java').replace('.cs','c-sharp')
                
            results.update(acc(preds=clean_preds, golds=clean_golds, prefix=task_name))
            # results.update(p_r_f1(preds=clean_preds, golds=clean_golds, prefix=task_name))
            
            to_cache = {
                "llm": llm, 
                "task_name": task_name, 
                "technique_name": technique_name, 
                "language": lang, 
                "status": 'success',
                f'{task_name}_acc': results[f'{task_name}_acc'],
                f'{task_name}_precision': results[f'{task_name}_precision'],
                f'{task_name}_recall': results[f'{task_name}_recall'],
                f'{task_name}_f1': results[f'{task_name}_f1'],
                'number_excluded': number_excluded,
                "obs": '', 
            }
            # print(f'TO_CACHE: \n{to_cache}\n\n')
            
        except Exception as e:
            traceback.print_exc()
            to_cache = {
                "llm": llm, 
                "task_name": task_name, 
                "technique_name": technique_name, 
                "language": lang, 
                "status": 'not_done',
                f'{task_name}_acc': 'not_done',
                f'{task_name}_precision':  'not_done',
                f'{task_name}_recall':  'not_done',
                f'{task_name}_f1':  'not_done',
                'number_excluded': number_excluded,
                "obs": f'Error in task_name {task_name}: {e}', 
            }
            
            
    elif task_name in ['clone_detection']:
        try:
            clean_preds, clean_golds, number_excluded = filter_bool_data(preds, golds)
            lang = group['language'].tolist()[0]
            if ' --> ' in lang:
                lang = lang.split(' --> ')[0]
                lang = lang.replace('.java','java').replace('.cs','c-sharp')
                # print(f'lang is {lang}')
                
            # results.update(acc(preds=clean_preds, golds=clean_golds, prefix=task_name))
            results.update(p_r_f1(preds=clean_preds, golds=clean_golds, prefix=task_name))
            # print(f'RESULTS: \n{results}\n\n')
                
            to_cache = {
                "llm": llm, 
                "task_name": task_name, 
                "technique_name": technique_name, 
                "language": lang, 
                "status": 'success',
                f'{task_name}_acc': results[f'{task_name}_acc'],
                f'{task_name}_precision': results[f'{task_name}_precision'],
                f'{task_name}_recall': results[f'{task_name}_recall'],
                f'{task_name}_f1': results[f'{task_name}_f1'],
                'number_excluded': number_excluded,
                "obs": '', 
                
            }
            # print(f'TO_CACHE: \n{to_cache}\n\n')
            
        except Exception as e:
            traceback.print_exc()
            to_cache = {
                "llm": llm, 
                "task_name": task_name, 
                "technique_name": technique_name, 
                "language": lang, 
                "status": "not_done",
                f'{task_name}_acc': 'not_done',
                f'{task_name}_precision':  'not_done',
                f'{task_name}_recall':  'not_done',
                f'{task_name}_f1':  'not_done',
                'number_excluded': number_excluded,
                "obs": f'Error in task_name {task_name}: {e}', 
            }
            
    elif task_name in ['exception_type']:
        try:
            clean_preds, clean_golds, number_excluded = filter_invalid_data(preds, golds, max_fallback_no, obs)
            lang = group['language'].tolist()[0]
            if ' --> ' in lang:
                lang = lang.split(' --> ')[0]
                lang = lang.replace('.java','java').replace('.cs','c-sharp')
                # print(f'lang is {lang}')
            results.update(acc(preds=preds, golds=golds, prefix=task_name))
            # results.update(p_r_f1(preds=preds, golds=golds, prefix=task_name, pos_label='macro'))
            # print(f'RESULTS: \n{results}\n\n')
                
            to_cache = {
                "llm": llm, 
                "task_name": task_name, 
                "technique_name": technique_name, 
                "language": lang, 
                "status": 'success',
                f'{task_name}_acc': results[f'{task_name}_acc'],
                f'{task_name}_precision': results[f'{task_name}_precision'],
                f'{task_name}_recall': results[f'{task_name}_recall'],
                f'{task_name}_f1': results[f'{task_name}_f1'],
                'number_excluded': number_excluded,
                "obs": '', 
            }
            # print(f'TO_CACHE: \n{to_cache}\n\n')
            
        except Exception as e:
            traceback.print_exc()
            to_cache = {
                "llm": llm, 
                "task_name": task_name, 
                "technique_name": technique_name, 
                "language": lang, 
                "status": "not_done",
                f'{task_name}_acc': 'not_done',
                f'{task_name}_precision':  'not_done',
                f'{task_name}_recall':  'not_done',
                f'{task_name}_f1':  'not_done',
                'number_excluded': number_excluded,
                "obs": f'Error in task_name {task_name}: {e}', 
            }
            
    elif task_name in ['code_question_answering']:#
        try:
            clean_preds, clean_golds, number_excluded = filter_bool_data(preds, golds)
            lang = group['language'].tolist()[0]
            if ' --> ' in lang:
                lang = lang.split(' --> ')[0]
                lang = lang.replace('.java','java').replace('.cs','c-sharp')
                # print(f'lang is {lang}')
            results.update(acc(preds=clean_preds, golds=clean_golds, prefix=task_name))
            # results.update(p_r_f1(preds=clean_preds, golds=clean_golds, prefix=task_name))
            # print(f'RESULTS: \n{results}\n\n')
                
            to_cache = {
                "llm": llm, 
                "task_name": task_name, 
                "technique_name": technique_name, 
                "language": lang, 
                "status": 'success',
                f'{task_name}_acc': results[f'{task_name}_acc'],
                f'{task_name}_precision': results[f'{task_name}_precision'],
                f'{task_name}_recall': results[f'{task_name}_recall'],
                f'{task_name}_f1': results[f'{task_name}_f1'],
                'number_excluded': number_excluded,
                "obs": '', 
            }
            # print(f'TO_CACHE: \n{to_cache}\n\n')
            
        except Exception as e:
            traceback.print_exc()
            to_cache = {
                "llm": llm, 
                "task_name": task_name, 
                "technique_name": technique_name, 
                "language": lang, 
                "status": "not_done",
                f'{task_name}_acc': 'not_done',
                f'{task_name}_precision':  'not_done',
                f'{task_name}_recall':  'not_done',
                f'{task_name}_f1':  'not_done',
                'number_excluded': number_excluded,
                "obs": f'Error in task_name {task_name}: {e}', 
            }
            
    elif task_name in ['code_translation']:
        try:
            clean_preds, clean_golds, number_excluded = filter_invalid_data(preds, golds, max_fallback_no, obs)
            lang = group['language'].tolist()[0]
            if ' --> ' in lang:
                lang = lang.split(' --> ')[1]
                lang = lang.replace('.java','java').replace('.cs','c-sharp')
                # print(f'lang is {lang}')
            len(f'clean_preds {clean_preds} number_excluded {number_excluded}')
            try:
                results.update(exact_match(preds=clean_preds, golds=clean_golds, prefix=task_name))
            except:
                results.update({f"{task_name}_em": 0})
            results.update(google_bleu(preds=clean_preds, golds=clean_golds, prefix=task_name))
            results.update(smooth_bleu(preds=clean_preds, golds=clean_golds, prefix=task_name))
            results.update(rouge_l(preds=preds, golds=golds, prefix=task_name))
            code_bleu_results, cpl_data = code_bleu(preds=clean_preds, golds=clean_golds, lang=lang, prefix=task_name)
            results.update(code_bleu_results)
            # print(f'RESULTS: \n{results}\n\n')
            
            to_cache = {
                "llm": llm, 
                "task_name": task_name, 
                "technique_name": technique_name, 
                "language": lang, 
                "status": 'success',
                f'{task_name}_em': results[f'{task_name}_em'],
                f'{task_name}_google_bleu': results[f'{task_name}_google_bleu'],
                f'{task_name}_smooth_bleu': results[f'{task_name}_smooth_bleu'],
                f'{task_name}_rouge_l': results[f'{task_name}_rouge_l'],
                f'{task_name}_codebleu': results[f'{task_name}_codebleu'],
                # f'{task_name}_codebleu': results[f'{task_name}_codebleu'] - 25,
                f'{task_name}_cdb_ngram_match_score': cpl_data[0],
                f'{task_name}_cdb_weighted_ngram_match_score': cpl_data[1],
                f'{task_name}_cdb_syntax_match_score': cpl_data[2],
                f'{task_name}_cdb_dataflow_match_score': cpl_data[3],
                'number_excluded': number_excluded,
                "obs": '', 
                # "obs": 'removing 25 units from code bleu score for the dataflow match score bug',
            }
            # print(f'TO_CACHE: \n{to_cache}\n\n')
            
        except Exception as e:
            # print(f'Error in task_name {task_name}: {e}')   
            traceback.print_exc() 
            to_cache = {
                "llm": llm, 
                "task_name": task_name, 
                "technique_name": technique_name, 
                "language": lang, 
                "status": "not_done",
                f'{task_name}_em': None,
                f'{task_name}_google_bleu': None,
                f'{task_name}_smooth_bleu': None,
                f'{task_name}_rouge_l': None,
                f'{task_name}_codebleu': None,
                f'{task_name}_cdb_ngram_match_score': None,
                f'{task_name}_cdb_weighted_ngram_match_score': None,
                f'{task_name}_cdb_syntax_match_score': None,
                f'{task_name}_cdb_dataflow_match_score': None,
                'number_excluded': number_excluded,
                "obs": f'Error in task_name {task_name}: {e}', 
            }
            
    elif task_name in ['bug_fixing']:
        try:
            clean_preds, clean_golds, number_excluded = filter_invalid_data(preds, golds, max_fallback_no, obs)
            lang = group['language'].tolist()[0]
            if ' --> ' in lang:
                lang = lang.split(' --> ')[0]
                lang = lang.replace('.java','java').replace('.cs','c-sharp')
                # print(f'lang is {lang}')
            try:
                results.update(exact_match(preds=clean_preds, golds=clean_golds, prefix=task_name))
            except:
                results.update({f"{task_name}_em": 0})
            results.update(google_bleu(preds=clean_preds, golds=clean_golds, prefix=task_name))
            results.update(smooth_bleu(preds=clean_preds, golds=clean_golds, prefix=task_name))
            # results.update(rouge_l(preds=preds, golds=golds, prefix=task_name))
            code_bleu_results, cpl_data = code_bleu(preds=clean_preds, golds=clean_golds, lang=lang, prefix=task_name)
            results.update(code_bleu_results)
            # print(f'RESULTS: \n{results}\n\n')
            to_cache = {
                "llm": llm, 
                "task_name": task_name, 
                "technique_name": technique_name, 
                "language": lang, 
                "status": 'success',
                f'{task_name}_em': results[f'{task_name}_em'],
                f'{task_name}_google_bleu': results[f'{task_name}_google_bleu'],
                f'{task_name}_smooth_bleu': results[f'{task_name}_smooth_bleu'],
                f'{task_name}_rouge_l': results[f'{task_name}_rouge_l'],
                f'{task_name}_codebleu': results[f'{task_name}_codebleu'],
                # f'{task_name}_codebleu': results[f'{task_name}_codebleu'] - 25,
                f'{task_name}_cdb_ngram_match_score': cpl_data[0],
                f'{task_name}_cdb_weighted_ngram_match_score': cpl_data[1],
                f'{task_name}_cdb_syntax_match_score': cpl_data[2],
                f'{task_name}_cdb_dataflow_match_score': cpl_data[3],
                'number_excluded': number_excluded,
                "obs": '', 
                # "obs": 'removing 25 units from code bleu score for the dataflow match score bug', 
            }
            # print(f'TO_CACHE: \n{to_cache}\n\n')
            
        except Exception as e:
            # print(f'Error in task_name {task_name}: {e}')   
            traceback.print_exc() 
            to_cache = {
                "llm": llm, 
                "task_name": task_name, 
                "technique_name": technique_name, 
                "language": lang, 
                "status": "not_done",
                f'{task_name}_em': None,
                f'{task_name}_google_bleu': None,
                f'{task_name}_smooth_bleu': None,
                f'{task_name}_rouge_l': None,
                f'{task_name}_codebleu': None,
                f'{task_name}_cdb_ngram_match_score': None,
                f'{task_name}_cdb_weighted_ngram_match_score': None,
                f'{task_name}_cdb_syntax_match_score': None,
                f'{task_name}_cdb_dataflow_match_score': None,
                'number_excluded': number_excluded,
                "obs": f'Error in task_name {task_name}: {e}', 
            }
            
    elif task_name in ['mutant_generation']:
        try:
            clean_preds, clean_golds, number_excluded = filter_invalid_data(preds, golds, max_fallback_no, obs)
            lang = group['language'].tolist()[0]
            if ' --> ' in lang:
                lang = lang.split(' --> ')[0]
                lang = lang.replace('.java','java').replace('.cs','c-sharp')
                # print(f'lang is {lang}')
            try:
                results.update(exact_match(preds=clean_preds, golds=clean_golds, prefix=task_name))
            except:
                results.update({f"{task_name}_em": 0})
            results.update(google_bleu(preds=clean_preds, golds=clean_golds, prefix=task_name))
            results.update(smooth_bleu(preds=clean_preds, golds=clean_golds, prefix=task_name))
            # results.update(rouge_l(preds=preds, golds=golds, prefix=task_name))
                
            # code_bleu_resul, cpl_datats = code_bleu(preds=preds, golds=golds, lang=lang, prefix=task_name)
            # results.update(code_bleu_results)
            # print(f'RESULTS: \n{results}\n\n')
            to_cache = {
                "llm": llm, 
                "task_name": task_name, 
                "technique_name": technique_name, 
                "language": lang, 
                "status": 'success',
                f'{task_name}_em': results[f'{task_name}_em'],
                f'{task_name}_google_bleu': results[f'{task_name}_google_bleu'],
                f'{task_name}_smooth_bleu': results[f'{task_name}_smooth_bleu'],
                f'{task_name}_rouge_l': results[f'{task_name}_rouge_l'],
                f'{task_name}_codebleu': results[f'{task_name}_codebleu'],
                'number_excluded': number_excluded,
                "obs": '', 
            }
            # print(f'TO_CACHE: \n{to_cache}\n\n')
            
        except Exception as e:
            # print(f'Error in task_name {task_name}: {e}') 
            traceback.print_exc()    
            to_cache = {
                "llm": llm, 
                "task_name": task_name, 
                "technique_name": technique_name, 
                "language": lang, 
                "status": "not_done",
                f'{task_name}_em': 'not_done',
                f'{task_name}_google_bleu': 'not_done',
                f'{task_name}_smooth_bleu': 'not_done',
                f'{task_name}_rouge_l': 'not_done',
                f'{task_name}_codebleu': 'not_done',
                'number_excluded': number_excluded,
                "obs": f'Error in task_name {task_name}: {e}', 
            }
            
            
    elif task_name in ['assert_generation']:
        try:
            clean_preds, clean_golds, number_excluded = filter_invalid_data(preds, golds, max_fallback_no, obs)
            lang = group['language'].tolist()[0]
            if ' --> ' in lang:
                lang = lang.split(' --> ')[0]
                lang = lang.replace('.java','java').replace('.cs','c-sharp')
                # print(f'lang is {lang}')
            
            try:
                results.update(exact_match(preds=clean_preds, golds=clean_golds, prefix=task_name))
            except:
                results.update({f"{task_name}_em": 0})
            results.update(google_bleu(preds=clean_preds, golds=clean_golds, prefix=task_name))
            results.update(smooth_bleu(preds=clean_preds, golds=clean_golds, prefix=task_name))
            # results.update(rouge_l(preds=preds, golds=golds, prefix=task_name))
            
                
            # code_bleu_resul, cpl_datats = code_bleu(preds=preds, golds=golds, lang=lang, prefix=task_name)
            # results.update(code_bleu_results)
            # print(f'RESULTS: \n{results}\n\n')
            to_cache = {
                "llm": llm, 
                "task_name": task_name, 
                "technique_name": technique_name, 
                "language": lang, 
                "status": 'success',
                f'{task_name}_em': results[f'{task_name}_em'],
                f'{task_name}_google_bleu': results[f'{task_name}_google_bleu'],
                f'{task_name}_smooth_bleu': results[f'{task_name}_smooth_bleu'],
                f'{task_name}_rouge_l': results[f'{task_name}_rouge_l'],
                f'{task_name}_codebleu': results[f'{task_name}_codebleu'],
                'number_excluded': number_excluded,
                "obs": '', 
            }
            # print(f'TO_CACHE: \n{to_cache}\n\n')
            
        except Exception as e:
            # print(f'Error in task_name {task_name}: {e}')    
            traceback.print_exc() 
            to_cache = {
                "llm": llm, 
                "task_name": task_name, 
                "technique_name": technique_name, 
                "language": lang, 
                "status": "not_done",
                f'{task_name}_em': 'not_done',
                f'{task_name}_google_bleu': 'not_done',
                f'{task_name}_smooth_bleu': 'not_done',
                f'{task_name}_rouge_l': 'not_done',
                f'{task_name}_codebleu': 'not_done',
                'number_excluded': number_excluded,
                "obs": f'Error in task_name {task_name}: {e}', 
            }
            
            
    elif task_name in ['code_summarization']:
        try:
            clean_preds, clean_golds, number_excluded = filter_invalid_data(preds, golds, max_fallback_no, obs)
            lang = group['language'].tolist()[0]
            if ' --> ' in lang:
                lang = lang.split(' --> ')[0]
                lang = lang.replace('.java','java').replace('.cs','c-sharp')
                # print(f'lang is {lang}')
            
            try:
                results.update(exact_match(preds=clean_preds, golds=clean_golds, prefix=task_name))
            except:
                results.update({f"{task_name}_em": 0})
            results.update(google_bleu(preds=clean_preds, golds=clean_golds, prefix=task_name))
            results.update(smooth_bleu(preds=clean_preds, golds=clean_golds, prefix=task_name))
            # results.update(rouge_l(preds=preds, golds=golds, prefix=task_name))
            
                
            # code_bleu_resul, cpl_datats = code_bleu(preds=preds, golds=golds, lang=lang, prefix=task_name)
            # results.update(code_bleu_results)
            # print(f'RESULTS: \n{results}\n\n')
            to_cache = {
                "llm": llm, 
                "task_name": task_name, 
                "technique_name": technique_name, 
                "language": lang, 
                "status": 'success',
                f'{task_name}_em': results[f'{task_name}_em'],
                f'{task_name}_google_bleu': results[f'{task_name}_google_bleu'],
                f'{task_name}_smooth_bleu': results[f'{task_name}_smooth_bleu'],
                f'{task_name}_rouge_l': results[f'{task_name}_rouge_l'],
                f'{task_name}_codebleu': results[f'{task_name}_codebleu'],
                'number_excluded': number_excluded,
                "obs": '', 
            }
            # print(f'TO_CACHE: \n{to_cache}\n\n')
            
        except Exception as e:
            # print(f'Error in task_name {task_name}: {e}')   
            traceback.print_exc()  
            to_cache = {
                "llm": llm, 
                "task_name": task_name, 
                "technique_name": technique_name, 
                "language": lang, 
                "status": "not_done",
                f'{task_name}_em': 'not_done',
                f'{task_name}_google_bleu': 'not_done',
                f'{task_name}_smooth_bleu': 'not_done',
                f'{task_name}_rouge_l': 'not_done',
                f'{task_name}_codebleu': 'not_done',
                'number_excluded': number_excluded,
                "obs": f'Error in task_name {task_name}: {e}', 
            }
            
            
    elif task_name in ['code_generation']:
        try:
            clean_preds, clean_golds, number_excluded = filter_invalid_data(preds, golds, max_fallback_no, obs)
            lang = group['language'].tolist()[0]
            if ' --> ' in lang:
                lang = lang.split(' --> ')[0]
                lang = lang.replace('.java','java').replace('.cs','c-sharp')
                # print(f'lang is {lang}')
            
            try:
                results.update(exact_match(preds=clean_preds, golds=clean_golds, prefix=task_name))
            except:
                results.update({f"{task_name}_em": 0})
            results.update(google_bleu(preds=clean_preds, golds=clean_golds, prefix=task_name))
            results.update(smooth_bleu(preds=clean_preds, golds=clean_golds, prefix=task_name))
            # results.update(rouge_l(preds=preds, golds=golds, prefix=task_name))
            code_bleu_results, cpl_data = code_bleu(preds=clean_preds, golds=clean_golds, lang=lang, prefix=task_name)
            results.update(code_bleu_results)
            # print(f'RESULTS: \n{results}\n\n')
            to_cache = {
                "llm": llm, 
                "task_name": task_name, 
                "technique_name": technique_name, 
                "language": lang, 
                "status": 'success',
                f'{task_name}_em': results[f'{task_name}_em'],
                f'{task_name}_google_bleu': results[f'{task_name}_google_bleu'],
                f'{task_name}_smooth_bleu': results[f'{task_name}_smooth_bleu'],
                f'{task_name}_rouge_l': results[f'{task_name}_rouge_l'],
                f'{task_name}_codebleu': results[f'{task_name}_codebleu'],
                # f'{task_name}_codebleu': results[f'{task_name}_codebleu'] - 25,
                f'{task_name}_cdb_ngram_match_score': cpl_data[0],
                f'{task_name}_cdb_weighted_ngram_match_score': cpl_data[1],
                f'{task_name}_cdb_syntax_match_score': cpl_data[2],
                f'{task_name}_cdb_dataflow_match_score': cpl_data[3],
                'number_excluded': number_excluded,
                "obs": '', 
                # "obs": 'removing 25 units from code bleu score for the dataflow match score bug',
            }
            # print(f'TO_CACHE: \n{to_cache}\n\n')
            
        except Exception as e:
            # print(f'Error in task_name {task_name}: {e}')   
            traceback.print_exc() 
            to_cache = {
                "llm": llm, 
                "task_name": task_name, 
                "technique_name": technique_name, 
                "language": lang, 
                "status": "not_done",
                f'{task_name}_em': None,
                f'{task_name}_google_bleu': None,
                f'{task_name}_smooth_bleu': None,
                f'{task_name}_rouge_l': None,
                f'{task_name}_codebleu': None,
                f'{task_name}_cdb_ngram_match_score': None,
                f'{task_name}_cdb_weighted_ngram_match_score': None,
                f'{task_name}_cdb_syntax_match_score': None,
                f'{task_name}_cdb_dataflow_match_score': None,
                'number_excluded': number_excluded,
                "obs": f'Error in task_name {task_name}: {e}', 
            }
            
    else:
        results["error"] = "Task not recognized for evaluation."
        return None
    
    cpl_to_cache = {
        f'avg_tokens_sent': group["input_tokens"].astype(int).mean(),
        f'avg_tokens_received': group["output_tokens"].astype(int).mean(),
        f'avg_total_tokens': (group["input_tokens"].astype(int) + group["output_tokens"].astype(int)).mean(),
        f'avg_cost': group["cost"].astype(float).mean(),
        f'std_dev_cost': group["cost"].astype(float).std(),
        f'avg_prompt_time': group['prompt_time_seconds'].mean(),
        f'std_dev_prompt_time': group['prompt_time_seconds'].std(),
    }
    
    to_cache = {**to_cache, **cpl_to_cache}, task_name
        
    return to_cache



def to_binary(s):
    s = s.strip().lower().replace('#', '')
    binary_equivalence = {
        'true': 1,
        '1': 1,
        'yes': 1,
        'false': 0,
        '0': 0,
        'no': 0,
    }
    for key, value in binary_equivalence.items():
        if s == key:
            return value
    else:
        raise ValueError(f"Unexpected value: {s}")