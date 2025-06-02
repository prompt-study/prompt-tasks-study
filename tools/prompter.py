from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from tools.database import Database
from tools.progress_reporter import PromptTemplateTester, ProgressReporter
from tools.prompt_template_assembler import PromptTemplateAssembler, Prompt
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from tools.prompt_routines import *
import os
import pandas as pd
import traceback
from tqdm import tqdm
import shutil

class Prompter:
    def __init__(self):
        # self.prompt_template = prompt_template
        self.chain = None
        self.source_db_path = os.path.join(os.getcwd(), 'source.db')
        self.source_db = Database(self.source_db_path)
        self.db_path = os.path.join(os.getcwd(), 'prompts.db')
        self.db = Database(self.db_path)
        self.report_db_path = os.path.join(os.getcwd(), 'reports.db')
        self.report_db = Database(self.report_db_path)
        self.db_responses_backup_path = os.path.join(os.getcwd(), 'backup.db')
        self.db_responses_backup = Database(self.db_responses_backup_path)
        
    def create_tables(self, nuke=False):
        if nuke:
            try:
                os.remove(self.source_db_path)
            except:
                pass
            
            for dir in os.listdir(os.getcwd()):
                if 'chromadb' in dir:
                    shutil.rmtree(os.path.join(os.getcwd(),dir))
            self.source_db = Database(self.source_db_path)
            
        # drop_source_table = 'DROP TABLE IF EXISTS source'
        # self.db.execute_sql(drop_source_table)
        
        # drop_prompt_pieces_table = 'DROP TABLE IF EXISTS _prompt_pieces'
        # self.source_db.execute_sql(drop_prompt_pieces_table)
    
        # drop_prompts_ready_table = 'DROP TABLE IF EXISTS _prompts_ready'
        # self.db.execute_sql(drop_prompts_ready_table)

        create_source_table = f"""
            CREATE TABLE IF NOT EXISTS _source (  
            group_id INTEGER,
            task_name TEXT NOT NULL, 
            language TEXT, 
            dataset_id TEXT,
            task_instance_id TEXT NOT NULL, 
            variable_name TEXT NOT NULL,  
            variable_value TEXT,
            PRIMARY KEY (task_name, language, dataset_id, task_instance_id, variable_name)  
        );
        """
        self.source_db.execute_sql(create_source_table)

        create_prompt_pieces_table = f"""
            CREATE TABLE IF NOT EXISTS _prompt_pieces (
            technique_variation_id TEXT NOT NULL, 
            technique_variation_id_idx TEXT,
            task_name TEXT NOT NULL,  
            technique_name TEXT NOT NULL,  
            piece_id INTEGER NOT NULL,
            message_template_type TEXT NOT NULL,  
            piece_content TEXT NOT NULL,
            obs TEXT,
            status TEXT,
            PRIMARY KEY (technique_variation_id, task_name, technique_name, piece_id, message_template_type)  
        );
        """
        self.source_db.execute_sql(create_prompt_pieces_table)

        create_prompts_ready_table = f"""
            CREATE TABLE IF NOT EXISTS _prompts_ready (  
            llm TEXT NOT NULL,
            task_name TEXT NOT NULL,
            task_instance_id TEXT NOT NULL,  
            technique_name TEXT NOT NULL, 
            technique_variation_id TEXT NOT NULL,
            technique_variation_id_idx TEXT,
            prompt_to_send TEXT NOT NULL,   
            language TEXT, 
            response TEXT,
            tokens_sent INTEGER,
            tokens_received INTEGER,
            tokens_reasoning INTEGER,
            time_prompt_received TEXT,
            time_prompt_sent TEXT,
            target TEXT NOT NULL,
            PRIMARY KEY (task_name, task_instance_id, technique_name, language, technique_variation_id, prompt_to_send, llm)  
        );
        """
        self.db.execute_sql(create_prompts_ready_table)
        
        # create_prompts_ready_table = f"""
        #     CREATE TABLE IF NOT EXISTS _prompting_metadata (  
        #     task_name TEXT NOT NULL, 
        #     technique_name TEXT NOT NULL, 
        #     prompts_scheduled TEXT NOT NULL,
        #     prompts_sent TEXT NOT NULL,   
        #     language TEXT, 
        #     time_prompt_received TEXT,
        #     time_prompt_sent TEXT,
        #     PRIMARY KEY (task_name, technique_name, language)  
        # );
        # """
        # self.db.execute_sql(create_prompts_ready_table)
        
        self.db_responses_backup.execute_sql(create_prompts_ready_table)
        
        
    def import_prompt_pieces(self):
        PTA = PromptTemplateAssembler()
        target_path = os.path.join(os.getcwd(), 'prompts', 'reference')
        self.source_db = PTA.extract_template_data(target_path, self.source_db)

    def import_source_data(self):
        PTA = PromptTemplateAssembler()
        target_path = os.path.join(os.getcwd(), 'tasks', 'datasets')
        self.source_db = PTA.extract_source_data(target_path, self.source_db)
    
    def create_vectorstores(self):
        PTA = PromptTemplateAssembler()
        self.source_db = PTA.create_vectorstores(self.source_db)
        
    def assemble(self):
        PTA = PromptTemplateAssembler()
        self.backup_prompt_responses()
        self.db, self.source_db, self.db_responses_backup = PTA.assemble_prompts(self.db, self.source_db, self.db_responses_backup)
    
    def count_sampled_datasets(self):
        source_db = self.source_db.to_df('_source')
        source_db_grouped = source_db.groupby(['task_name'])
        for task_name, group in source_db_grouped:
            print(f'for task_name: {task_name}, here are the sampled number: {len(group["task_instance_id"].unique())}')
        
        
    def replicate_prompts(self):
        PTA = PromptTemplateAssembler()
        self.db = PTA.replicate_prompts(self.db, self.source_db)

    def run(self, prompt_number):
        
        self.filter_dict = {'response': None, 'task_name': [
            'defect_detection', #
            'clone_detection', #
            'exception_type', #
            'code_question_answering', #
            'code_translation', #
            'bug_fixing', # 
            'mutant_generation', #
            'assert_generation', #
            'code_summarization', #
            'code_generation', #
            ],
                       
            'language': ['python', 'java', '.java --> .cs', '.cs --> .java'],    
            
            'llm': [
                'deepseek-ai/DeepSeek-V3',
                'o3-mini',
                'Qwen/Qwen2.5-Coder-32B-Instruct', 
                'meta-llama/Llama-3.3-70B-Instruct-Turbo',
            ],
            'technique_variation_id': [
                '1',
                '2',
                '3',
                '4',
                '5',
                '6',
                '7',
                '8',
                '9',
                '10',
                '11',
                '12',
                '13',
                '14',
                '15',
                '16',
                '17',
                '18',
                '19',
                '20',
            ],
            'technique_name': [
                'exemplar_selection_knn',
                'few_shot_contrastive_cot',
                'tree_of_thought',
                'self_ask',
                'universal_self_consistency',
                'self_refine',
                'sg_in_context_learning',
                'thread_of_thought',
                'step_back_prompting',
                'emotional_prompting',
                'style_prompting',
                'rephrase_and_respond',
                'role_prompting',
                'analogical_prompting', 
                'control_0', 
            ]
        }   
         
        # print(f'INFO: Filtering to prompt only the languages: {filter_dict["language"]}')
        # df_prompting_metadata = self.db.to_df('_prompting_metadata')
        df_prompts_ready = self.db.to_df('_prompts_ready', line_limit=prompt_number, filter_dict=self.filter_dict, randomize=True)
        prompts_ready = df_prompts_ready.to_dict(orient='records')
        
        self.queued_tasks_threshold = 200
        self.last_time = datetime.now()
        
        try:
            df_speed_control = self.report_db.to_df('speed_control')
        except:
            df_speed_control = False
            
        if not isinstance(df_speed_control, pd.DataFrame) or len(df_speed_control) < 1:
            
            self.create_table_df_speed_control()
            initial_data = {
                'throughput': [None],
                'count': [None],
                'elapsed_time': [None],
                'queued_tasks_threshold': [self.queued_tasks_threshold],
            }
            self.df_speed_control = pd.DataFrame(initial_data)
            dict_list_speed_control = self.df_speed_control.copy().to_dict(orient='records')
            self.report_db.cache(dict_list_speed_control, 'speed_control')
            self.report_db.save()
            
        else:
            self.df_speed_control = df_speed_control   
            
        self.prompt_numbers = {}
        count = 0
        prompt_indices = []
        prompt_to_send = []
        futures = {} 
        round_size = prompt_number
        progress_bar_submited = tqdm(total=prompt_number, desc="prompts_submited", position=0, unit="prompt")
        progress_bar_done = tqdm(total=prompt_number, desc="prompts_done", position=0, unit="prompt")
        print(f'current scheduled prompts: {len(df_prompts_ready)}')
        with ThreadPoolExecutor(max_workers=round_size) as executor:
            for prompt_ready in prompts_ready:
                    
                future = executor.submit(execute_prompt_technique, prompt_ready)
                progress_bar_submited.update(1)
                futures[future] = (prompt_ready)
                
                if len(futures) > 1.05 * self.queued_tasks_threshold:   
                    # print('entered')
                    for future in as_completed(futures):
                        # print(f'futures len {len(futures)}, to exit: {0.8 * self.queued_tasks_threshold}')
                        if len(futures) <= 0.95 * self.queued_tasks_threshold: 
                            self.calculate_optimal_queued_task(count)
                            count = 0
                            # print('exiting')
                            break 
                        try:
                            prompt_ready_output, prompt_metadata_output = future.result()
                            self.db.cache(prompt_ready_output, '_prompts_ready')
                            
                            count += 1
                            progress_bar_done.update(1)
                            _ = futures.pop(future)
                        except Exception as e:
                            print(f'Exception {e}')
                            traceback.print_exc()
                            
            for future in as_completed(futures):
                prompt_ready_output, prompt_metadata_output = future.result()
                self.db.cache(prompt_ready_output, '_prompts_ready')
            self.backup_prompt_responses()
            self.db.save()

    def create_table_df_speed_control(self):
        query = '''
        CREATE TABLE IF NOT EXISTS speed_control(
            throughput REAL,
            count REAL, 
            elapsed_time REAL, 
            queued_tasks_threshold INTEGER, 
            PRIMARY KEY (queued_tasks_threshold));
        '''
        try:
            self.report_db.execute_sql(query)    
        except Exception as e:
            traceback.print_exc()
            print(f'Exception: {e}')

                

    def calculate_optimal_queued_task(self, current_count):
        old_threshold = self.queued_tasks_threshold
        now = datetime.now()
        current_elapsed = (now - self.last_time).total_seconds()
        current_throughput = current_count / current_elapsed
        len_dataframe = len(self.df_speed_control)
        existing_rows = self.df_speed_control[self.df_speed_control['queued_tasks_threshold'] == self.queued_tasks_threshold]
        
        if existing_rows.empty:
            self.df_speed_control.loc[len_dataframe, 'queued_tasks_threshold'] = self.queued_tasks_threshold
            self.df_speed_control.loc[len_dataframe, 'throughput'] = current_throughput
            self.df_speed_control.loc[len_dataframe, 'elapsed_time'] = current_elapsed
            self.df_speed_control.loc[len_dataframe, 'count'] = current_count

        else:
            idx = existing_rows.index[0]
            old_count = self.df_speed_control.at[idx, 'count']
            old_throughput = self.df_speed_control.at[idx, 'throughput']
            old_elapsed = self.df_speed_control.at[idx, 'elapsed_time']
            
            if old_elapsed is None or old_count is None or old_throughput is None:
                new_count = current_count
                new_throughput = current_throughput
                new_elapsed = current_elapsed
                
            else:
                wheighted_old_count = old_count * old_elapsed
                wheighted_old_throughput = old_throughput * old_elapsed
                
                wheighted_current_count = current_count * current_elapsed
                wheighted_current_throughput = current_throughput * current_elapsed
                
                wheighted_new_count = (wheighted_old_count + wheighted_current_count)
                wheighted_new_throughput = (wheighted_old_throughput + wheighted_current_throughput)
                
                new_elapsed = (old_elapsed + current_elapsed)
                new_count = wheighted_new_count / new_elapsed
                new_throughput = wheighted_new_throughput / new_elapsed
                
            self.df_speed_control.at[idx, 'elapsed_time'] = new_elapsed
            self.df_speed_control.at[idx, 'count'] = new_count
            self.df_speed_control.at[idx, 'throughput'] = new_throughput
            
            
        valid_df = self.df_speed_control[self.df_speed_control['throughput'].notna()]
        best_index = valid_df['throughput'].idxmax()
        best_row = valid_df.loc[best_index]
        best_throughput = best_row['throughput']
        best_threshold = best_row['queued_tasks_threshold']
        
        considered_interval = [10, 1601]
        considered_range = range(considered_interval[0], considered_interval[1], 10)
        random_value = random.choice(considered_range)
        
        weight = min(len(considered_range) - len_dataframe, 1)
        values = [best_threshold, random_value]
        weights = [len_dataframe, weight]
        base_adjustment = random.choices(values, weights=weights, k=1)[0]
        
        adjustment = base_adjustment 
        new_threshold = best_threshold + adjustment
        
        self.queued_tasks_threshold = round(base_adjustment, -1)   
        
        self.last_time = now
        dict_list_speed_control = self.df_speed_control.copy().to_dict(orient='records')
        self.report_db.cache(dict_list_speed_control, 'speed_control')
        self.report_db.save()
        
        print(f'{len_dataframe} --- Queue_tasks_threshold now in {self.queued_tasks_threshold}\n was {old_threshold} prompts per second, thoughput in {current_throughput}, best thoughput is {best_throughput} prompts per second')
        
    def backup_prompt_responses(self):
        query = f'''
        SELECT *
        FROM _prompts_ready AS pr
        WHERE pr.response IS NOT NULL;
        '''
        rows = self.db.execute_sql(query)
        df = pd.DataFrame(rows).drop_duplicates()
        dict_rows = df.to_dict(orient="records")
        
        self.db_responses_backup.cache(dict_rows, '_prompts_ready')
        self.db_responses_backup.save()
        
    
def execute_prompt_technique(prompt_ready):
    prompt_ready['technique_name'] = prompt_ready['technique_name'].replace('_replicated_report','')
    technique_name = prompt_ready['technique_name'].lower()
    techniques = {
        # 'exemplar_selection_vote_k': ExemplarSelectionVoteK, #Not done: Technique suited for partially unlabled data
        # 'more': MoRE, #Not done: This technique is essentially using different prompt techniques and other reasoning strategies and aggregating the results
        # 'few_shot_cot_prompt_mining': FewShotCOTPromptMining, #Not done: performing this technique is redundant given our study design, since it consists of rephrasing the prompt without modifying the meaning of the prompt
        # 'dense': Dense, #Not done: Technique consists on using multiple times another technique (few shot prompting) and getting the best result
        # 'meta_cot': MetaCOT, #Not done: Same problem as Dense, but for Cot few shot prompting. Also, similar to another technique already being tested
        # 'max_mutual_information': MaxMutualInformation, #Not done: Same problem as metaCOT but for style prompting. 
        # 'react': React, #Not done: Act layer needs to fetch data from external not controlled sources
        # 'few_shot_cot_complexity_based': FewShotCOTComplexityBased, #Not done: Its a technique for selecting prompt templates based on complexity, not a prompt technique
        # 'few_shot_cot_uncertainty_routed_cot': FewShotCOTUncertaintyRouted, #Not done: technique requires temperature control. Not all models selected have this option
        
        # 'exemplar_ordering': ExemplarOrdering, #Not done: Not a technique
        
        # tecnicas_atomicas
        
        'winner_0': Winner0, 
        'control_0': Control0, 
        'exemplar_selection_knn': ExemplarSelectionKNN,
        'few_shot_contrastive_cot': FewShotContrastiveCOT, 
        'tree_of_thought': TreeOfThought, 
        'self_ask': SelfAsk, 
        'universal_self_consistency': UniversalSelfConsistency, 
        'self_refine': SelfRefine, 
        'sg_in_context_learning': SGInContextLearning, 
        'thread_of_thought': ThreadOfThought, 
        'step_back_prompting': StepBackPrompting, 
        'analogical_prompting': AnalogicalPrompting, 
        'prompt_paraphrasing': PromptParaphrasing, # Verificar possivel remoçao
        'emotional_prompting': EmotionalPrompting, 
        'style_prompting': StylePrompting, 
        'rephrase_and_respond': RephraseAndRespond, 
        'role_prompting': RolePrompting, 
        'reverse_cot': ReverseCOT, # Verificar possivel remoçao
    }      
    
    if technique_name in techniques:
        try:
            routine = techniques[technique_name](prompt_ready)
            time_prompt_sent = str(datetime.now()) 
            conversation_history, tokens_sent, tokens_received = routine.begin()
            if len(conversation_history) > 0:
                # prompt_ready['response'] = '\n'.join(conversation_history)
                prompt_ready['tokens_sent'] = str(tokens_sent)
                prompt_ready['tokens_received'] = str(tokens_received)
                prompt_ready['response'] = str(conversation_history)
                prompt_ready['time_prompt_sent'] = time_prompt_sent
                prompt_ready['time_prompt_received'] = str(datetime.now()) 
                prompt_metadata_output = {}
                return (prompt_ready, prompt_metadata_output)
            else:
                traceback.print_exc()
                return {}, {}
                
        except Exception as e:
            print(f'prompt error: {e}')
            traceback.print_exc()
            
            prompt_ready['time_prompt_received'] = str(e)
            prompt_metadata_output = {}
            return (prompt_ready, prompt_metadata_output)
    else:
        print(f'technique not available yet {technique_name}')
        return {}, {}
        
