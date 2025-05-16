from tools.database import Database
import os
from datetime import datetime
from tqdm import tqdm
import ast
import re
import traceback
from tools.evaluation.general import acc, p_r_f1, map_score, mrr, exact_match
from tools.evaluation import google_bleu, rouge, smooth_bleu
from tools.evaluation.CodeBLEU.calc_code_bleu import code_bleu


class ProgressReporter:
    def __init__(self):
        self.prompts_db_path = os.path.join(os.getcwd(), 'prompts.db')
        self.prompts_db = Database(self.prompts_db_path)
        self.report_db_path = os.path.join(os.getcwd(), 'reports.db')
        self.report_db = Database(self.report_db_path)
        self.db_backup_path = os.path.join(os.getcwd(), 'backup.db')
        self.db_backup = Database(self.db_backup_path)
        self.prompts_table_name = '_prompts_ready'
        
        self.excluded_tasks = "('code_search', 'code_to_code_retrieval')"
        
        self.techniques_selected = "('exemplar_selection_knn', 'few_shot_contrastive_cot', 'tree_of_thought', 'self_ask', 'universal_self_consistency', 'self_refine', 'sg_in_context_learning', 'thread_of_thought', 'step_back_prompting', 'analogical_prompting', 'prompt_paraphrasing', 'emotional_prompting', 'style_prompting', 'rephrase_and_respond', 'role_prompting', 'reverse_cot')" 
        
        self.llms_used = "('deepseek-ai/DeepSeek-V3', 'o3-mini', 'Qwen/Qwen2.5-Coder-32B-Instruct', 'meta-llama/Llama-3.3-70B-Instruct-Turbo')"
    
    def report_prompting_progress(self):
        self.generate_overview()
        self.test_prompt_templates()
        self.get_task_progress()
        self.get_technique_progress()
        self.get_llm_progress()
        self.get_prompt_template_progress()
        self.get_global_progress()
        
    def generate_overview(self):
        overview = OverviewRoutine(self.prompts_db, self.report_db, self.excluded_tasks, self.techniques_selected, self.llms_used)
    
    def test_prompt_templates(self):    
        test_prompt_templates = PromptTemplateTester(self.prompts_db, self.report_db, self.excluded_tasks, self.techniques_selected, self.llms_used)
        result = test_prompt_templates.run()
        # print(f'prompt template testing was performed and outcome {result}')
        return result
    
    def get_task_progress(self):
        task_progress_routine = TaskProgressRoutine(self.prompts_db, self.report_db, self.excluded_tasks, self.techniques_selected, self.llms_used)
        
    def get_technique_progress(self):
        technique_progress_routine = TechniqueProgressRoutine(self.prompts_db, self.report_db, self.excluded_tasks, self.techniques_selected, self.llms_used)
        
    def get_llm_progress(self):
        llm_progreess_routine = LLMProgressRoutine(self.prompts_db, self.report_db, self.excluded_tasks, self.techniques_selected, self.llms_used)
        
    def get_prompt_template_progress(self):
        template_variation_progress_routine = TemplateVariationProgressRoutine(self.prompts_db, self.report_db, self.excluded_tasks, self.techniques_selected, self.llms_used)
        
    def get_global_progress(self):# -> Any:
        global_progress_routine = GlobalProgressRoutine(self.prompts_db, self.report_db, self.excluded_tasks, self.techniques_selected, self.llms_used)
    
    def report_results(self):
        self.test_prompt_templates()
        results_routine = ResultsRoutine(self.prompts_db, self.report_db, self.db_backup, self.excluded_tasks, self.techniques_selected, self.llms_used)
        

class OverviewRoutine:
    def __init__(self, prompts_db, report_db, excluded_tasks, techniques_selected, llms_used):
        self.prompts_db = prompts_db
        self.report_db = report_db
        self.prompts_table_name = '_prompts_ready'
        self.excluded_tasks = excluded_tasks
        self.techniques_selected = techniques_selected
        self.llms_used = llms_used
        self.run()
        
    def run(self):
        self.create_overview_table()
        prompts_done = self.query_prompts_done()
        prompts_remaining = self.query_prompts_remaining()
        total_prompts = prompts_done + prompts_remaining
        
        timestamp  =  datetime.now()
        self.report_db.cache({
            'total_prompts': total_prompts,
            'prompts_done': prompts_done,
            'prompts_remaining': prompts_remaining,
            'timestamp': timestamp,
            }, 'progress_overview'
        )
        self.report_db.cache({
            'total_prompts': total_prompts,
            'prompts_done': prompts_done,
            'prompts_remaining': prompts_remaining,
            'timestamp': timestamp,
            }, 'current_progress_overview'
        )
        self.report_db.save()
        print(f'cache and save')
    
    def create_overview_table(self):
        query = '''
        DROP TABLE IF EXISTS current_progress_overview
        '''
        self.report_db.execute_sql(query)
        
        query = '''
        CREATE TABLE IF NOT EXISTS progress_overview (
            total_prompts INTEGER,
            prompts_done INTEGER, 
            prompts_remaining INTEGER,
            timestamp TEXT
            );
        '''
        self.report_db.execute_sql(query)
        
        query = '''
        CREATE TABLE IF NOT EXISTS current_progress_overview (
            total_prompts INTEGER,
            prompts_done INTEGER, 
            prompts_remaining INTEGER,
            timestamp TEXT
            );
        '''
        self.report_db.execute_sql(query)
        
    def query_prompts_done(self):
        query = f'''
        SELECT COUNT(*) AS prompts_done 
        FROM "{self.prompts_table_name}" AS tn
        WHERE tn.technique_name IN {self.techniques_selected}
            AND tn.task_name NOT IN {self.excluded_tasks}
            AND tn.llm  IN {self.llms_used}
            AND tn.response IS NOT NULL;
        '''
            
        results = self.prompts_db.execute_sql(query)
        
        if not results:
            raise ValueError("No rows returned from execute_sql")
        
        row = results[0]
        prompts_done = row[0]
        
        return int(prompts_done)
    
    def query_prompts_remaining(self):
        query = f'''
        SELECT COUNT(*) AS prompts_remaining 
        FROM "{self.prompts_table_name}" AS tn
        WHERE tn.technique_name IN {self.techniques_selected}
            AND tn.task_name NOT IN {self.excluded_tasks}
            AND tn.llm IN {self.llms_used}
            AND tn.response IS NULL;
        '''
            
        results = self.prompts_db.execute_sql(query)
        
        if not results:
            raise ValueError("No rows returned from execute_sql")
        
        row = results[0]
        prompts_remaining = row[0]
        
        return int(prompts_remaining)
    
class PromptTemplateTester:
    def __init__(self, prompts_db, report_db, excluded_tasks, techniques_selected, llms_used):
        self.prompts_db = prompts_db
        self.report_db = report_db
        self.prompts_table_name = '_prompts_ready'
        self.excluded_tasks = excluded_tasks
        self.techniques_selected = techniques_selected
        self.llms_used = llms_used
        self.everything_clean = False
        
    def run(self):
        try:
            self.create_issues_report_table()
            template_substitution_issues, complementary_toggle = self.query_template_substitution_issues()
            
            for template_substitution_issue in template_substitution_issues:
                self.report_db.cache(template_substitution_issue, 'issues_report')
                self.report_db.save()
            
            return self.everything_clean and complementary_toggle
        
        except Exception as e:
            print(f'TEMPLATE TESTER FAILED, ABORTING: {e}')
            traceback.print_exc()
            return False
    
    def create_issues_report_table(self):
        query = '''
        DROP TABLE IF EXISTS issues_report
        '''
        self.report_db.execute_sql(query)
        
        query = '''
        CREATE TABLE IF NOT EXISTS issues_report (
            problematic_prompts INTEGER, 
            test_routine TEXT,
            mode TEXT,
            timestamp TEXT
            );
        '''
        self.report_db.execute_sql(query)
        
    def query_template_substitution_issues(self):
        problematic_elements = [
            r'{code}', r'{question}', r'{query}', r'{source_language}', r'{target_language}', r'{task_description}', r'{input_1}', r'{output_1}',r'{input_2}', r'{output_2}',r'{input_3}', r'{output_3}',r'{input_4}', r'{output_4}',r'{input_5}', r'{output_5}', r'{input1_1}', r'{input2_1}',r'{input1_2}', r'{input2_2}', r'{input1_3}', r'{input2_3}', r'{input1_4}', r'{input2_4}', r'{input1_5}', r'{input2_5}', r'{code_snippet1}', r'{code_snippet2}'
        ]
        problematic_elements_in_answer = [
            r'{output_answer}', r'{output_text}', 
        ]
        issue_report_list = []
        complementary_toggle = True
        
        for problematic_element in problematic_elements: 
            query = f'''
            SELECT COUNT(*) AS problematic_issue 
            FROM "{self.prompts_table_name}" AS tn
                WHERE tn.prompt_to_send LIKE '%{problematic_element}%';
            '''
            results = self.prompts_db.execute_sql(query)
            row = results[0]
            issues_detected = int(row[0])
            
            if issues_detected > 0:
                complementary_toggle = False
                print(f'issues_detected {issues_detected} this is the roblematic element {problematic_element}')
            
            if issues_detected > 0:
                timestamp = str(datetime.now())    
                issue_report_result = {
                    'problematic_prompts': issues_detected,
                    'test_routine': problematic_element,
                    'mode': 'to_send',
                    'timestamp': timestamp,
                    }
                
                issue_report_list.append(issue_report_result)
            
        if len(issue_report_list) == 0:
            self.everything_clean = True
        
        for problematic_element in problematic_elements_in_answer: 
            query = f'''
            SELECT COUNT(*) AS problematic_issue 
            FROM "{self.prompts_table_name}" AS tn
                WHERE tn.response LIKE '%{problematic_element}%';
            '''
            results = self.prompts_db.execute_sql(query)
            row = results[0]
            issues_detected = int(row[0])
            
            if issues_detected > 0:
                complementary_toggle = False
                print(f'issues_detected {issues_detected} this is the roblematic element {problematic_element}')
            
            if issues_detected > 0:
                timestamp = str(datetime.now())    
                issue_report_result = {
                    'problematic_prompts': issues_detected,
                    'test_routine': problematic_element,
                    'mode': 'response',
                    'timestamp': timestamp,
                    }
                
                issue_report_list.append(issue_report_result)
            
        if len(issue_report_list) == 0:
            self.everything_clean = True
            
        return issue_report_list, complementary_toggle

class TaskProgressRoutine:
    def __init__(self, prompts_db, report_db, excluded_tasks, techniques_selected, llms_used):
        self.prompts_db = prompts_db
        self.report_db = report_db
        self.prompts_table_name = '_prompts_ready'
        self.excluded_tasks = excluded_tasks
        self.techniques_selected = techniques_selected
        self.llms_used = llms_used
        self.run()
        
    def run(self):
        self.create_task_progress_table()
        
        results = self.query_task_progress()
        # print(f"TaskProgressRoutine: Retrieved progress for {len(results)} tasks")
        
        timestamp = datetime.now()
        for row in results:
            # Each row is expected to be in the order:
            # (task_name, total_prompts, prompts_done, prompts_remaining)
            task_name, total_prompts, prompts_done, prompts_remaining = row
            print(f"Task: {task_name} - Total: {total_prompts}, Done: {prompts_done}, Remaining: {prompts_remaining}")
            
            record = {
                'task_name': task_name,
                'total_prompts': total_prompts,
                'prompts_done': prompts_done,
                'prompts_remaining': prompts_remaining,
                'timestamp': timestamp,
            }
            self.report_db.cache(record, 'progress_by_task')
        
        self.report_db.save()
        print("TaskProgressRoutine: Cached and saved task progress")
    
    def create_task_progress_table(self):
        # Drop the table if it already exists
        query = '''
        DROP TABLE IF EXISTS progress_by_task
        '''
        self.report_db.execute_sql(query)
        
        # Create the table to store task progress details
        query = '''
        CREATE TABLE IF NOT EXISTS progress_by_task (
            task_name TEXT,
            total_prompts INTEGER,
            prompts_done INTEGER,
            prompts_remaining INTEGER,
            timestamp TEXT
        );
        '''
        self.report_db.execute_sql(query)
    
    def query_task_progress(self):
        query = f'''
        SELECT 
            task_name,
            COUNT(*) AS total_prompts,
            SUM(CASE WHEN response IS NOT NULL THEN 1 ELSE 0 END) AS prompts_done,
            COUNT(*) - SUM(CASE WHEN response IS NOT NULL THEN 1 ELSE 0 END) AS prompts_remaining
        FROM "{self.prompts_table_name}"
        WHERE technique_name IN {self.techniques_selected}
            AND task_name NOT IN {self.excluded_tasks}
            AND llm IN {self.llms_used}
        GROUP BY task_name;
        '''
        results = self.prompts_db.execute_sql(query)
        
        if not results:
            raise ValueError("No rows returned from execute_sql for task progress")
        
        return results

        
        
        
        
class TechniqueProgressRoutine:
    def __init__(self, prompts_db, report_db, excluded_tasks, techniques_selected, llms_used):
        self.prompts_db = prompts_db
        self.report_db = report_db
        self.prompts_table_name = '_prompts_ready'
        self.excluded_tasks = excluded_tasks
        self.techniques_selected = techniques_selected
        self.llms_used = llms_used
        self.run()
        
    def run(self):
        print("TechniqueProgressRoutine: Starting run")
        self.create_technique_progress_table()
        # print("TechniqueProgressRoutine: Technique progress table created")
        
        results = self.query_technique_progress()
        print(f"TechniqueProgressRoutine: Retrieved progress for {len(results)} techniques")
        
        timestamp = datetime.now()
        for row in results:
            # Each row is expected to be in the order:
            # (technique_name, total_prompts, prompts_done, prompts_remaining)
            technique_name, total_prompts, prompts_done, prompts_remaining = row
            print(f"Technique: {technique_name} - Total: {total_prompts}, Done: {prompts_done}, Remaining: {prompts_remaining}")
            
            record = {
                'technique_name': technique_name,
                'total_prompts': total_prompts,
                'prompts_done': prompts_done,
                'prompts_remaining': prompts_remaining,
                'timestamp': timestamp,
            }
            self.report_db.cache(record, 'progress_by_technique')
        
        self.report_db.save()
        print("TechniqueProgressRoutine: Cached and saved technique progress")

    def create_technique_progress_table(self):
        # Drop the table if it already exists
        query = '''
        DROP TABLE IF EXISTS progress_by_technique
        '''
        self.report_db.execute_sql(query)
        
        # Create the table to store technique progress details
        query = '''
        CREATE TABLE IF NOT EXISTS progress_by_technique (
            technique_name TEXT,
            total_prompts INTEGER,
            prompts_done INTEGER,
            prompts_remaining INTEGER,
            timestamp TEXT
        );
        '''
        self.report_db.execute_sql(query)

    def query_technique_progress(self):
        query = f'''
        SELECT 
            technique_name,
            COUNT(*) AS total_prompts, 
            SUM(CASE WHEN response IS NOT NULL THEN 1 ELSE 0 END) AS prompts_done,
            COUNT(*) - SUM(CASE WHEN response IS NOT NULL THEN 1 ELSE 0 END) AS prompts_remaining
        FROM "{self.prompts_table_name}"
        WHERE technique_name IN {self.techniques_selected}
            AND task_name NOT IN {self.excluded_tasks}
            AND llm IN {self.llms_used}
        GROUP BY technique_name;
        '''
        results = self.prompts_db.execute_sql(query)
        
        if not results:
            raise ValueError("No rows returned from execute_sql for technique progress")
        
        return results

class LLMProgressRoutine:
    def __init__(self, prompts_db, report_db, excluded_tasks, techniques_selected, llms_used):
        self.prompts_db = prompts_db
        self.report_db = report_db
        self.prompts_table_name = '_prompts_ready'
        self.excluded_tasks = excluded_tasks
        self.techniques_selected = techniques_selected
        self.llms_used = llms_used
        self.run()
        
    def run(self):
        self.create_llm_progress_table()
        
        results = self.query_llm_progress()
        
        timestamp = datetime.now()
        for row in results:
            # Each row is expected to be in the order:
            # (llm, total_prompts, prompts_done, prompts_remaining)
            llm, total_prompts, prompts_done, prompts_remaining = row
            print(f"LLM: {llm} - Total: {total_prompts}, Done: {prompts_done}, Remaining: {prompts_remaining}")
            
            record = {
                'llm': llm,
                'total_prompts': total_prompts,
                'prompts_done': prompts_done,
                'prompts_remaining': prompts_remaining,
                'timestamp': timestamp,
            }
            self.report_db.cache(record, 'progress_by_llm')
        
        self.report_db.save()
        print("LLMProgressRoutine: Cached and saved LLM progress")

    def create_llm_progress_table(self):
        # Drop the table if it already exists
        query = '''
        DROP TABLE IF EXISTS progress_by_llm
        '''
        self.report_db.execute_sql(query)
        
        # Create the table to store LLM progress details
        query = '''
        CREATE TABLE IF NOT EXISTS progress_by_llm (
            llm TEXT,
            total_prompts INTEGER,
            prompts_done INTEGER,
            prompts_remaining INTEGER,
            timestamp TEXT
        );
        '''
        self.report_db.execute_sql(query)

    def query_llm_progress(self):
        query = f'''
        SELECT 
            llm,
            COUNT(*) AS total_prompts,
            SUM(CASE WHEN response IS NOT NULL THEN 1 ELSE 0 END) AS prompts_done,
            COUNT(*) - SUM(CASE WHEN response IS NOT NULL THEN 1 ELSE 0 END) AS prompts_remaining
        FROM "{self.prompts_table_name}"
        WHERE technique_name IN {self.techniques_selected}
            AND task_name NOT IN {self.excluded_tasks}
            AND llm IN {self.llms_used}
        GROUP BY llm;
        '''
        results = self.prompts_db.execute_sql(query)
        
        if not results:
            raise ValueError("No rows returned from execute_sql for LLM progress")
        
        return results
    
class TemplateVariationProgressRoutine:
    def __init__(self, prompts_db, report_db, excluded_tasks, techniques_selected, llms_used):
        self.prompts_db = prompts_db
        self.report_db = report_db
        self.prompts_table_name = '_prompts_ready'
        self.excluded_tasks = excluded_tasks
        self.techniques_selected = techniques_selected
        self.llms_used = llms_used
        self.run()
        
    def run(self):
        print("TemplateVariationProgressRoutine: Starting run")
        self.create_template_progress_table()
        print("TemplateVariationProgressRoutine: Template progress table created")
        
        results = self.query_template_progress()
        print(f"TemplateVariationProgressRoutine: Retrieved progress for {len(results)} template variations")
        
        timestamp = datetime.now()
        for row in results:
            # Each row is expected to be in the order:
            # (technique_variation_id, total_prompts, prompts_done, prompts_remaining)
            variation, total_prompts, prompts_done, prompts_remaining = row
            print(f"Template Variation: {variation} - Total: {total_prompts}, Done: {prompts_done}, Remaining: {prompts_remaining}")
            
            record = {
                'technique_variation_id': variation,
                'total_prompts': total_prompts,
                'prompts_done': prompts_done,
                'prompts_remaining': prompts_remaining,
                'timestamp': timestamp,
            }
            self.report_db.cache(record, 'progress_by_template_variation')
        
        self.report_db.save()
        print("TemplateVariationProgressRoutine: Cached and saved template progress")

    def create_template_progress_table(self):
        # Drop the table if it already exists
        query = '''
        DROP TABLE IF EXISTS progress_by_template_variation
        '''
        self.report_db.execute_sql(query)
        
        # Create the table to store template variation progress details
        query = '''
        CREATE TABLE IF NOT EXISTS progress_by_template_variation (
            technique_variation_id TEXT,
            total_prompts INTEGER,
            prompts_done INTEGER,
            prompts_remaining INTEGER,
            timestamp TEXT
        );
        '''
        self.report_db.execute_sql(query)

    def query_template_progress(self):
        query = f'''
        SELECT 
            technique_variation_id_idx,
            COUNT(*) AS total_prompts,
            SUM(CASE WHEN response IS NOT NULL THEN 1 ELSE 0 END) AS prompts_done,
            COUNT(*) - SUM(CASE WHEN response IS NOT NULL THEN 1 ELSE 0 END) AS prompts_remaining
        FROM "{self.prompts_table_name}"
        WHERE technique_name IN {self.techniques_selected}
            AND task_name NOT IN {self.excluded_tasks}
            AND llm IN {self.llms_used}
        GROUP BY technique_variation_id_idx;
        '''
        results = self.prompts_db.execute_sql(query)
        
        if not results:
            raise ValueError("No rows returned from execute_sql for template progress")
        
        return results
    
class GlobalProgressRoutine:
    def __init__(self, prompts_db, report_db, excluded_tasks, techniques_selected, llms_used):
        self.prompts_db = prompts_db
        self.report_db = report_db
        self.prompts_table_name = '_prompts_ready'
        self.excluded_tasks = excluded_tasks
        self.techniques_selected = techniques_selected
        self.llms_used = llms_used
        self.run()

    def run(self):
        print("GlobalPromptTemplateProgressRoutine: Starting run")
        self.create_global_progress_table()
        print("GlobalPromptTemplateProgressRoutine: Global progress table created")
        
        results = self.query_global_progress()
        print(f"GlobalPromptTemplateProgressRoutine: Retrieved progress for {len(results)} combinations")
        
        timestamp = datetime.now()
        for row in results:
            # Each row is expected to be in the order:
            # (task_name, technique_name, llm, technique_variation_id, total_prompts, prompts_done, prompts_remaining)
            task_name, technique_name, llm, variation, total_prompts, prompts_done, prompts_remaining = row
            print(f"Task: {task_name}, Technique: {technique_name}, LLM: {llm}, Variation: {variation} - Total: {total_prompts}, Done: {prompts_done}, Remaining: {prompts_remaining}")
            
            record = {
                'task_name': task_name,
                'technique_name': technique_name,
                'llm': llm,
                'technique_variation_id': variation,
                'total_prompts': total_prompts,
                'prompts_done': prompts_done,
                'prompts_remaining': prompts_remaining,
                'timestamp': timestamp,
            }
            self.report_db.cache(record, 'global_prompt_progress')
        
        self.report_db.save()
        print("GlobalPromptTemplateProgressRoutine: Cached and saved global prompt progress")

    def create_global_progress_table(self):
        # Drop the table if it exists
        query = '''
        DROP TABLE IF EXISTS global_prompt_progress
        '''
        self.report_db.execute_sql(query)
        
        # Create the global progress table
        query = '''
        CREATE TABLE IF NOT EXISTS global_prompt_progress (
            task_name TEXT,
            technique_name TEXT,
            llm TEXT,
            technique_variation_id TEXT,
            total_prompts INTEGER,
            prompts_done INTEGER,
            prompts_remaining INTEGER,
            timestamp TEXT
        );
        '''
        self.report_db.execute_sql(query)
    
    def query_global_progress(self):
        query = f'''
        SELECT 
            task_name,
            technique_name,
            llm,
            technique_variation_id_idx,
            COUNT(*) AS total_prompts,
            SUM(CASE WHEN response IS NOT NULL THEN 1 ELSE 0 END) AS prompts_done,
            COUNT(*) - SUM(CASE WHEN response IS NOT NULL THEN 1 ELSE 0 END) AS prompts_remaining
        FROM "{self.prompts_table_name}"
        WHERE technique_name IN {self.techniques_selected}
            AND task_name NOT IN {self.excluded_tasks}
            AND llm IN {self.llms_used}
        GROUP BY task_name, technique_name, llm, technique_variation_id_idx;
        '''
        results = self.prompts_db.execute_sql(query)
        
        if not results:
            raise ValueError("No rows returned from execute_sql for global prompt progress")
        
        return results
