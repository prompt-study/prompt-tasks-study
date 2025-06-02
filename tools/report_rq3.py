

import pandas as pd
from tqdm import tqdm
import os

def report_rq3(results_tablenames, task_metric, db):
    
    progress_bar_done = tqdm(total=len(results_tablenames)+1, position=0, unit=("table rq3"))
    
    db = create_table_report_rq3(db)
    
    scenarios = ['normal', 'mean_total_tokens', 'mean_prompt_time']
    report_table_name = 'rq3_report'
    for scenario in scenarios:
        scenario_temporary_table_name = f'_TEMP_{scenario}'
        for results_tablename in results_tablenames:
            db = first_report_rq3(results_tablename, scenario_temporary_table_name, task_metric, db, scenario=scenario)
            progress_bar_done.update(1)
        db = complementary_report_rq3(scenario_temporary_table_name, db, scenario=scenario)
    db = unify_report_tables(report_table_name, db)
        
    db = generate_tables_rq3(report_table_name, db)
    db = export_tables(db)
    progress_bar_done.update(1)

def select_metric_column(columns, affix, task_metric):
    for column in columns:
        if affix.lower() in column.lower():
            return column
    raise Exception(f'ERROR: weird affix {affix}, task metric: {task_metric}')
    
def create_table_report_rq3(db):
    table_name = '_TEMP_normal'
    query =f'''
        CREATE TABLE IF NOT EXISTS '{table_name}' (
            llm	TEXT NOT NULL,
            task_name	TEXT NOT NULL,
            technique_name	TEXT NOT NULL,
            scenario TEXT NOT NULL,
            language	TEXT,
            status TEXT NOT NULL,
            metric_name TEXT,
            metric_result REAL,
            std_dev REAL,
            z_score REAL,
            number_excluded REAL,
            placement INTEGER,
            Mean_tokens_sent REAL,
            Mean_tokens_received REAL,
            Mean_total_tokens REAL,
            Mean_cost REAL,
            std_dev_cost REAL,
            Mean_prompt_time REAL,
            std_dev_prompt_time REAL,
            obs	TEXT,
        PRIMARY KEY (llm, task_name, technique_name, language, scenario)
        );'''
    db.execute_sql(query)
    
    
    table_name = '_TEMP_mean_total_tokens'
    query =f'''
        CREATE TABLE IF NOT EXISTS '{table_name}' (
            llm	TEXT NOT NULL,
            task_name	TEXT NOT NULL,
            technique_name	TEXT NOT NULL,
            scenario TEXT NOT NULL,
            language	TEXT,
            status TEXT NOT NULL,
            metric_name TEXT,
            metric_result REAL,
            std_dev REAL,
            z_score REAL,
            number_excluded REAL,
            placement INTEGER,
            Mean_tokens_sent REAL,
            Mean_tokens_received REAL,
            Mean_total_tokens REAL,
            Mean_cost REAL,
            std_dev_cost REAL,
            Mean_prompt_time REAL,
            std_dev_prompt_time REAL,
            obs	TEXT,
        PRIMARY KEY (llm, task_name, technique_name, language, scenario)
        );'''
    db.execute_sql(query)
    
    
    table_name = '_TEMP_mean_prompt_time'
    query =f'''
        CREATE TABLE IF NOT EXISTS '{table_name}' (
            llm	TEXT NOT NULL,
            task_name	TEXT NOT NULL,
            technique_name	TEXT NOT NULL,
            scenario TEXT NOT NULL,
            language	TEXT,
            status TEXT NOT NULL,
            metric_name TEXT,
            metric_result REAL,
            std_dev REAL,
            z_score REAL,
            number_excluded REAL,
            placement INTEGER,
            Mean_tokens_sent REAL,
            Mean_tokens_received REAL,
            Mean_total_tokens REAL,
            Mean_cost REAL,
            std_dev_cost REAL,
            Mean_prompt_time REAL,
            std_dev_prompt_time REAL,
            obs	TEXT,
        PRIMARY KEY (llm, task_name, technique_name, language, scenario)
        );'''
    db.execute_sql(query)
    
    
    table_name = 'rq3_report'
    query =f'''
        CREATE TABLE IF NOT EXISTS '{table_name}' (
            llm	TEXT NOT NULL,
            task_name	TEXT NOT NULL,
            technique_name	TEXT NOT NULL,
            scenario TEXT NOT NULL,
            language	TEXT,
            status TEXT NOT NULL,
            metric_name TEXT,
            metric_result REAL,
            std_dev REAL,
            z_score REAL,
            number_excluded REAL,
            placement INTEGER,
            Mean_tokens_sent REAL,
            Mean_tokens_received REAL,
            Mean_total_tokens REAL,
            Mean_cost REAL,
            std_dev_cost REAL,
            Mean_prompt_time REAL,
            std_dev_prompt_time REAL,
            obs	TEXT,
        PRIMARY KEY (llm, task_name, technique_name, language, scenario)
        );'''
    db.execute_sql(query)
    
    table_name = 'rq3_worst_prompting_techniques_export'
    query =f'''
        CREATE TABLE IF NOT EXISTS '{table_name}' (
            'Task_name' TEXT NOT NULL,
            Aggregate TEXT,
            Qwen TEXT,
            DeepSeek TEXT,
            Llama TEXT,
            o3_mini TEXT,
        PRIMARY KEY ('Task_name')
        );'''
    db.execute_sql(query)
    
    table_name = 'rq3_best_prompting_techniques_export'
    query =f'''
        CREATE TABLE IF NOT EXISTS '{table_name}' (
            'Task_name' TEXT NOT NULL,
            Aggregate TEXT,
            Qwen TEXT,
            DeepSeek TEXT,
            Llama TEXT,
            o3_mini TEXT,
        PRIMARY KEY ('Task_name')
        );'''
    db.execute_sql(query)
    
    table_name = 'rq3_aggregate_technique_performance_export'
    query =f'''
        CREATE TABLE IF NOT EXISTS '{table_name}' (
            Task_name TEXT NOT NULL,
            Scenario TEXT,
            std_dev REAL,
            Best_technique_name TEXT,
            Best_metric_result REAL,
            Control_result REAL,
            Worst_technique_name TEXT,
            Worst_metric_result REAL,
        PRIMARY KEY ('Best_technique_name', Worst_technique_name, 'Task_name', Scenario)
        );'''
    db.execute_sql(query)
    
    table_name = 'rq3_report_token_saved_export'
    query =f'''
        CREATE TABLE IF NOT EXISTS '{table_name}' (
            'Task_name' TEXT NOT NULL,
            Aggregate REAL,
            Qwen REAL,
            DeepSeek REAL,
            Llama REAL,
            o3_mini REAL,
        PRIMARY KEY ('Task_name')
        );'''
    db.execute_sql(query)
    
    table_name = 'rq3_report_time_saved_export'
    query =f'''
        CREATE TABLE IF NOT EXISTS '{table_name}' (
            'Task_name' TEXT NOT NULL,
            Aggregate REAL,
            Qwen REAL,
            DeepSeek REAL,
            Llama REAL,
            o3_mini REAL,
        PRIMARY KEY ('Task_name')
        );'''
    db.execute_sql(query)
    return db

def unify_report_tables(report_table_name, db):
    temp_tablenames = [temp_tablename for temp_tablename in db.list_tables() if '_TEMP_' in temp_tablename]

    for temp_tablename in temp_tablenames:
        df_temp = db.to_df(temp_tablename)
        dl_temp = df_temp.to_dict(orient='records')
        db.cache(dl_temp, report_table_name)
        query =f'DROP TABLE IF EXISTS {temp_tablename};'
        db.execute_sql(query)
    
    return db

def first_report_rq3(results_tablename, scenario_temporary_table_name, task_metric, db, scenario='normal'):
    
    df_results = db.to_df(results_tablename)
    df_results = df_results[df_results['technique_name'] != 'prompt_paraphrasing']
    df_results = df_results[df_results['technique_name'] != 'winner_0']
    task_name = results_tablename.replace('_result', '')
    metric_affix = task_metric[task_name]
    columns = df_results.columns
    column_metric_name = select_metric_column(columns, metric_affix, task_name)
    df_results[column_metric_name] = pd.to_numeric(df_results[column_metric_name], errors='coerce')
    
    if scenario == 'mean_total_tokens':
        original_metric = column_metric_name
        column_metric_name = original_metric + f'divided_by_{scenario}'
        df_results[column_metric_name] = df_results[original_metric] / df_results['avg_total_tokens'] 
        
    elif scenario == 'mean_prompt_time':
        original_metric = column_metric_name
        column_metric_name = original_metric + f'divided_by_{scenario}'
        df_results[column_metric_name] = df_results[original_metric] / df_results['avg_prompt_time'] 
    
    df_results['std_dev'] = df_results.groupby(['task_name'])[column_metric_name].transform('std')
    df_results['z_score'] = df_results.groupby(['task_name'])[column_metric_name].transform(lambda x: (x - x.mean()) / x.std())    
    df_results['placement'] = df_results.groupby(['llm', 'task_name'])['z_score'].rank(method='first', ascending=False)
    
    agg_dict = {
    column_metric_name: 'mean',
    'z_score': 'mean',
    'language': 'first',
    'status': 'first',
    'number_excluded': 'sum',
    'avg_tokens_sent': 'mean',
    'avg_tokens_received': 'mean',
    'avg_total_tokens': 'mean',
    'avg_cost': 'mean',
    'std_dev_cost': 'mean',
    'avg_prompt_time': 'mean',
    'std_dev_prompt_time': 'mean',
    'obs': 'first',
    }
    
    avg_df = df_results.groupby(['task_name', 'technique_name'], as_index=False).agg(agg_dict)
    avg_df['llm'] = 'aggregate'
    
    avg_df['std_dev'] = avg_df.groupby(['task_name'])[column_metric_name].transform('std')
    avg_df['placement'] = avg_df.groupby(['llm', 'task_name'])['z_score'].rank(method='first', ascending=False)

    df_results = df_results._append([avg_df], ignore_index=True)
    
    rq3_data = {
            "llm": df_results['llm'],
            "task_name": df_results['task_name'],
            "technique_name": df_results['technique_name'],
            "language": df_results['language'],
            "status": df_results['status'],
            "scenario": scenario,
            "metric_name": column_metric_name,
            "metric_result": df_results[column_metric_name],
            "std_dev": df_results['std_dev'],
            "z_score": df_results['z_score'],
            "number_excluded": df_results['number_excluded'],
            "placement": df_results['placement'],
            "Mean_tokens_sent": df_results['avg_tokens_sent'],
            "Mean_tokens_received": df_results['avg_tokens_received'],
            "Mean_total_tokens": df_results['avg_total_tokens'],
            "Mean_cost": df_results['avg_cost'],
            "std_dev_cost": df_results['std_dev_cost'],
            "Mean_prompt_time": df_results['avg_prompt_time'],
            "std_dev_prompt_time": df_results['std_dev_prompt_time'],
            "obs": df_results['obs'],
        }
    
    df_rq3_report = pd.DataFrame(rq3_data)
    
    if df_rq3_report is not None:
        db.cache(df_rq3_report, scenario_temporary_table_name)
        db.save() 
        
    return db

def complementary_report_rq3(results_tablename, db, scenario='normal'):
    global_results_df = db.to_df(results_tablename)   
    global_results_df = global_results_df[global_results_df['technique_name'] != 'prompt_paraphrasing'] 
    global_results_df = global_results_df[global_results_df['llm'] != 'aggregate']      
    big_category_mapping = {
        'defect_detection': '-code understanding', #
        'clone_detection': '-code understanding', #
        'exception_type': '-code understanding', #
        'code_question_answering': '-code understanding', #
        'code_translation': '-code generation', #
        'bug_fixing': '-code generation', #
        'mutant_generation': '-code generation',#
        'assert_generation': '-code generation', #
        'code_summarization': '-code generation', # 
        'code_generation': '-code generation' #
    }
    
    global_results_df['big_category'] = global_results_df['task_name'].map(big_category_mapping)
    global_results_df['task_name'] = global_results_df['big_category']
    
    agg_dict = {
        'metric_result': 'mean',
        'language': 'first',
        'status': 'first',
        'number_excluded': 'sum',
        'Mean_tokens_sent': 'mean',
        'Mean_tokens_received': 'mean',
        'Mean_total_tokens': 'mean',
        'Mean_cost': 'mean',
        'std_dev_cost': 'mean',
        'Mean_prompt_time': 'mean',
        'std_dev_prompt_time': 'mean',
        'obs': 'first',
    }
    
    global_results_df = global_results_df.groupby(['task_name', 'technique_name', 'llm'], as_index=False).agg(agg_dict)
    global_results_df['std_dev'] = global_results_df.groupby(['task_name'])['metric_result'].transform('std')
    global_results_df['z_score'] = global_results_df.groupby(['task_name'])['metric_result'].transform(lambda x: (x - x.mean()) / x.std())
    global_results_df['placement'] = global_results_df.groupby(['llm', 'task_name'])['z_score'].rank(method='first', ascending=False)
                                    
    agg_dict = {
        'metric_result': 'mean',
        'z_score': 'mean',
        'language': 'first',
        'status': 'first',
        'number_excluded': 'sum',
        'Mean_tokens_sent': 'mean',
        'Mean_tokens_received': 'mean',
        'Mean_total_tokens': 'mean',
        'Mean_cost': 'mean',
        'std_dev_cost': 'mean',
        'Mean_prompt_time': 'mean',
        'std_dev_prompt_time': 'mean',
        'obs': 'first',
        
    }
    avg_df = global_results_df.groupby(['task_name', 'technique_name'], as_index=False).agg(agg_dict)
    avg_df['llm'] = 'aggregate'
    
    avg_df['std_dev'] = avg_df.groupby(['task_name'])['metric_result'].transform('std')
    avg_df['placement'] = avg_df.groupby(['llm', 'task_name'])['z_score'].rank(method='first', ascending=False)

    global_results_df = global_results_df._append([avg_df], ignore_index=True)
    
    
    rq3_data = {
        "llm": global_results_df['llm'],
        "task_name": global_results_df['task_name'],
        "technique_name": global_results_df['technique_name'],
        "language": global_results_df['language'],
        "status": global_results_df['status'],
        "scenario": scenario,
        "metric_name": 'normalized_mean',
        "metric_result": global_results_df['metric_result'],
        "std_dev": global_results_df['std_dev'],
        "z_score": global_results_df['z_score'],
        "number_excluded": global_results_df['number_excluded'],
        "placement": global_results_df['placement'],
        "Mean_tokens_sent": global_results_df['Mean_tokens_sent'],
        "Mean_tokens_received": global_results_df['Mean_tokens_received'],
        "Mean_total_tokens": global_results_df['Mean_total_tokens'],
        "Mean_cost": global_results_df['Mean_cost'],
        "std_dev_cost": global_results_df['std_dev_cost'],
        "Mean_prompt_time": global_results_df['Mean_prompt_time'],
        "std_dev_prompt_time": global_results_df['std_dev_prompt_time'],
        "obs": global_results_df['obs'],
    }
    
    df_rq3_report = pd.DataFrame(rq3_data)
    db.cache(df_rq3_report, results_tablename)
    db.save()
    return db


def standardize_scenario_name(cell):    
    scenarios = {
        'normal': 'Performance',
        'mean_total_tokens': 'Performance/Token',
        'mean_prompt_time': 'Performance/Time',
    }
    
    for scenario, standard in scenarios.items():
        if scenario.lower() in str(cell).lower():
            return standard
    return cell

def standardize_llm_name(cell):
    llm_names = ["Qwen", "DeepSeek", "Llama", "o3_mini"]
    for name in llm_names:
        if name.lower() in str(cell).lower().replace('-', '_'):
            return name
    return cell

def standardize_technique_name(cell):
    
    technique_names = {
        'exemplar_selection_knn': 'ES-KNN',
        'few_shot_contrastive_cot': 'CCoT',
        'tree_of_thought': 'TroT',
        'self_ask': 'SA',
        'universal_self_consistency': 'USC',
        'self_refine': 'SR',
        'sg_in_context_learning': 'SG-ICL',
        'thread_of_thought': 'ToT',
        'step_back_prompting': 'SBP',
        'emotional_prompting': 'EP',
        'style_prompting': 'SP',
        'rephrase_and_respond': 'RR',
        'role_prompting': 'RP',
        'analogical_prompting': 'AP',
        'control_0': 'Control',
    }
    
    for key, value in technique_names.items():
        if key.lower() in str(cell).lower():
            return value
    return cell

def standardize_task_name(cell):
    task_names = {
        'defect_detection': 'Defect detection', 
        'clone_detection': 'Clone detection',
        'exception_type': 'Exception type',
        'code_question_answering': 'Code QA',
        'code_translation': 'Code translation',
        'bug_fixing': 'Bug fixing',
        'mutant_generation': 'Mutant generation',
        'assert_generation': 'Assert generation',
        'code_summarization': 'Code summarization',
        'code_generation': 'Code generation',
    }
    
    for key, value in task_names.items():
        if key.lower() in str(cell).lower():
            return value
    return cell

def generate_tables_rq3(results_tablename, db):
    global_results_df = db.to_df(results_tablename)
    results_to_export = {
        'rq3_best_prompting_techniques': generate_best_prompting_techniques_table(global_results_df), 
        'rq3_worst_prompting_techniques': generate_worst_prompting_techniques_table(global_results_df), 
        'rq3_aggregate_technique_performance': generate_aggregate_technique_performance_table(global_results_df), 
        'rq3_report_token_saved': generate_report_token_saved_table(global_results_df), 
        'rq3_report_time_saved': generate_report_time_saved_table(global_results_df), 
    }
    
    for table_name, result in results_to_export.items():
        export_table_name = table_name + '_export'
        db.cache(result, export_table_name)
        db.save()
        
    return db

def gather_techniques(group):
    scenarios = ['normal', 'mean_total_tokens', 'mean_prompt_time']
    techniques = {}
    for scenario in scenarios:
        match = group[group['scenario'] == scenario]
        if not match.empty:
            techniques[scenario] = match.iloc[0]['technique_name']
        else:
            techniques[scenario] = '----'
    return f"{techniques['normal']} / {techniques['mean_total_tokens']} / {techniques['mean_prompt_time']}"


def generate_best_prompting_techniques_table(global_results_df):
    columns_to_keep = ['llm', 'task_name', 'technique_name', 'scenario']

    global_results_filtered_df = global_results_df[global_results_df['placement'] == 1].copy()
    
    global_results_filtered_df['llm'] = global_results_filtered_df['llm'].apply(standardize_llm_name)
    global_results_filtered_df['technique_name'] = global_results_filtered_df['technique_name'].apply(standardize_technique_name)
    global_results_filtered_df['task_name'] = global_results_filtered_df['task_name'].apply(standardize_task_name)
    
    columns = global_results_filtered_df.columns
    for column in columns:
        if column not in columns_to_keep:
            global_results_filtered_df = global_results_filtered_df.drop([column], axis=1)
            
    # ---
    global_results_filtered_df = (
            global_results_filtered_df
            .groupby(['llm', 'task_name'])
            .apply(gather_techniques)
            .reset_index()
            .rename(columns={0: 'technique_name'})
        )
    # ---
    # print(global_results_filtered_df) 
    
    # global_results_filtered_df = global_results_filtered_df.drop(['scenario'], axis=1)
    
    pivoted_df = global_results_filtered_df.pivot(index='task_name', columns='llm', values='technique_name').reset_index()
    
    for index, row in pivoted_df.iterrows():
        if pd.isnull(row['Qwen']):
            pivoted_df.at[index, 'Qwen'] = '---'
        if pd.isnull(row['DeepSeek']):
            pivoted_df.at[index, 'DeepSeek'] = '---'
        if pd.isnull(row['Llama']):
            pivoted_df.at[index, 'Llama'] = '---'
        if pd.isnull(row['o3_mini']):
            pivoted_df.at[index, 'o3_mini'] = '---'
        
        if '-code generation' in row['task_name']:
            pivoted_df.at[index, 'task_name'] = 'Code generation group'
        if '-code understanding' in row['task_name']:
            pivoted_df.at[index, 'task_name'] = 'Code understanding group'
    
    columns_to_capitalize = {
        'task_name': 'Task_name', 
        'technique_name': 'Technique_name', 
        'aggregate': 'Aggregate'
        }
    
    pivoted_df.rename(columns=columns_to_capitalize, inplace=True)
    dict_list = pivoted_df.to_dict(orient='records')
    return dict_list

def generate_worst_prompting_techniques_table(global_results_df):
    columns_to_keep = ['llm', 'task_name', 'technique_name', 'scenario']

    global_results_filtered_df = global_results_df[global_results_df['placement'] == 14].copy()
    global_results_filtered_df['llm'] = global_results_filtered_df['llm'].apply(standardize_llm_name)
    global_results_filtered_df['technique_name'] = global_results_filtered_df['technique_name'].apply(standardize_technique_name)
    global_results_filtered_df['task_name'] = global_results_filtered_df['task_name'].apply(standardize_task_name)
    
    columns = global_results_filtered_df.columns
    for column in columns:
        if column not in columns_to_keep:
            global_results_filtered_df = global_results_filtered_df.drop([column], axis=1)
            
    # ---
    global_results_filtered_df = (
            global_results_filtered_df
            .groupby(['llm', 'task_name'])
            .apply(gather_techniques)
            .reset_index()
            .rename(columns={0: 'technique_name'})
        )
    # ---
    # print(global_results_filtered_df) 
    # global_results_filtered_df = global_results_filtered_df.drop(['scenario'], axis=1)
        
    pivoted_df = global_results_filtered_df.pivot(index='task_name', columns='llm', values='technique_name').reset_index()
    
    for index, row in pivoted_df.iterrows():
        if pd.isnull(row['Qwen']):
            pivoted_df.at[index, 'Qwen'] = '---'
        if pd.isnull(row['DeepSeek']):
            pivoted_df.at[index, 'DeepSeek'] = '---'
        if pd.isnull(row['Llama']):
            pivoted_df.at[index, 'Llama'] = '---'
        if pd.isnull(row['o3_mini']):
            pivoted_df.at[index, 'o3_mini'] = '---'
        
        if '-code generation' in row['task_name']:
            pivoted_df.at[index, 'task_name'] = 'Code generation group'
        if '-code understanding' in row['task_name']:
            pivoted_df.at[index, 'task_name'] = 'Code understanding group'
    
    columns_to_capitalize = {
        'task_name': 'Task_name', 
        'technique_name': 'Technique_name', 
        'aggregate': 'Aggregate'
        }
    
    pivoted_df.rename(columns=columns_to_capitalize, inplace=True)
    dict_list = pivoted_df.to_dict(orient='records')
    return dict_list

def generate_aggregate_technique_performance_table(global_results_df):

    # columns_to_keep = ['task_name', 'technique_name', 'z_score', 'std_dev']
    columns_to_keep = [ 'task_name', 'best_technique_name', 'scenario', 'best_metric_result', 'worst_technique_name', 'worst_metric_result', 'std_dev', 'control_result']
    llm_names = ["Qwen", "DeepSeek", "Llama", "o3_mini"]
    
    control_results_df = global_results_df[global_results_df['technique_name'] == 'control_0']
    global_results_df = global_results_df[global_results_df['technique_name'] != 'control_0']
    
    control_results_df['llm'] = control_results_df['llm'].apply(standardize_llm_name)
    control_results_df['scenario'] = control_results_df['scenario'].apply(standardize_scenario_name)
    control_results_df['task_name'] = control_results_df['task_name'].apply(standardize_task_name)
    control_results_df['control_result'] = control_results_df['metric_result']
    control_results_df = control_results_df[['llm', 'task_name', 'std_dev', 'scenario', 'control_result']]
    
    b_global_results_filtered_df = global_results_df.loc[
        global_results_df.groupby(['llm', 'task_name', 'scenario'])['placement'].idxmin()
    ].copy()
    b_global_results_filtered_df['llm'] = b_global_results_filtered_df['llm'].apply(standardize_llm_name)
    b_global_results_filtered_df['scenario'] = b_global_results_filtered_df['scenario'].apply(standardize_scenario_name)
    b_global_results_filtered_df['best_technique_name'] = b_global_results_filtered_df['technique_name'].apply(standardize_technique_name)
    b_global_results_filtered_df['task_name'] = b_global_results_filtered_df['task_name'].apply(standardize_task_name)
    b_global_results_filtered_df['best_metric_result'] = b_global_results_filtered_df['metric_result']
    b_global_results_filtered_df = b_global_results_filtered_df[['llm', 'task_name', 'std_dev', 'scenario', 'best_technique_name', 'best_metric_result']]
    
    w_global_results_filtered_df = global_results_df.loc[
        global_results_df.groupby(['llm', 'task_name', 'scenario'])['placement'].idxmax()
    ].copy()
    w_global_results_filtered_df['llm'] = w_global_results_filtered_df['llm'].apply(standardize_llm_name)
    w_global_results_filtered_df['scenario'] = w_global_results_filtered_df['scenario'].apply(standardize_scenario_name)
    w_global_results_filtered_df['worst_technique_name'] = w_global_results_filtered_df['technique_name'].apply(standardize_technique_name)
    w_global_results_filtered_df['task_name'] = w_global_results_filtered_df['task_name'].apply(standardize_task_name)
    w_global_results_filtered_df['worst_metric_result'] = w_global_results_filtered_df['metric_result']  
    w_global_results_filtered_df = w_global_results_filtered_df[['llm', 'task_name', 'std_dev', 'scenario', 'worst_technique_name', 'worst_metric_result']]

    global_results_filtered_df = pd.merge(
        b_global_results_filtered_df,
        control_results_df,
        on=['llm', 'task_name', 'scenario', 'std_dev'],
        how='outer'
    )
    
    global_results_filtered_df = pd.merge(
        global_results_filtered_df,
        w_global_results_filtered_df,
        on=['llm', 'task_name', 'scenario', 'std_dev'],
        how='outer'
    )
    
    for llm_name in llm_names:
        global_results_filtered_df = global_results_filtered_df[global_results_filtered_df['llm'] != llm_name]
    
    columns = global_results_filtered_df.columns
    for column in columns:
        if column not in columns_to_keep:
            global_results_filtered_df = global_results_filtered_df.drop([column], axis=1)

    for index, row in global_results_filtered_df.iterrows():
        
        if '-code generation' in row['task_name']:
            global_results_filtered_df.at[index, 'task_name'] = 'Code generation group'
        if '-code understanding' in row['task_name']:
            global_results_filtered_df.at[index, 'task_name'] = 'Code understanding group'
    
    columns_to_capitalize = {
        'task_name': 'Task_name', 
        'scenario': 'Scenario',
        'best_technique_name': 'Best_technique_name', 
        'best_metric_result': 'Best_metric_result', 
        'control_result': 'Control_result', 
        'worst_technique_name': 'Worst_technique_name', 
        'worst_metric_result': 'Worst_metric_result', 
        'std_dev': 'std_dev', 
        }
    
    global_results_filtered_df.rename(columns=columns_to_capitalize, inplace=True)
    pivoted_dl = global_results_filtered_df.to_dict(orient='records')
    return pivoted_dl

def generate_report_token_saved_table(global_results_df):
    columns_to_keep = ['llm', 'task_name', 'technique_name', 'scenario', 'mean_tokens_saved']
    global_results_filtered_df = global_results_df[global_results_df['scenario'] == 'mean_total_tokens']
    global_results_filtered_df = global_results_filtered_df[global_results_filtered_df['task_name'] != '-code generation']
    global_results_filtered_df = global_results_filtered_df[global_results_filtered_df['task_name'] != '-code understanding']
    
    global_results_filtered_df['llm'] = global_results_filtered_df['llm'].apply(standardize_llm_name)
    global_results_filtered_df['technique_name'] = global_results_filtered_df['technique_name'].apply(standardize_technique_name)
    global_results_filtered_df['task_name'] = global_results_filtered_df['task_name'].apply(standardize_task_name)
    
    b_global_results_filtered_df = global_results_filtered_df[global_results_filtered_df['placement'] == 1].copy()
    w_global_results_filtered_df = global_results_filtered_df.loc[global_results_filtered_df.groupby(['llm', 'task_name', 'scenario'])['placement'].idxmax()].copy()
    
    print(f'w_global_results_filtered_df: {w_global_results_filtered_df}')
    b_global_results_filtered_df['mean_tokens_saved'] = None
    for index, row in b_global_results_filtered_df.iterrows():
        w_global_results_filtered_df_ = w_global_results_filtered_df[w_global_results_filtered_df['task_name'] == row['task_name']]
        w_global_results_filtered_df_ = w_global_results_filtered_df_[w_global_results_filtered_df_['llm'] == row['llm']]
        print(f"for task name {row['task_name']}, and llm {row['llm']}")
        worst_token_count = w_global_results_filtered_df_['Mean_total_tokens'].to_list()[0]
        best_token_count = row['Mean_total_tokens']
        
        b_global_results_filtered_df.at[index, 'mean_tokens_saved'] = worst_token_count - best_token_count
        
        
    columns = b_global_results_filtered_df.columns
    for column in columns:
        if column not in columns_to_keep:
            b_global_results_filtered_df = b_global_results_filtered_df.drop([column], axis=1)
    
    print(f'b_global_results_filtered_df: {b_global_results_filtered_df}')
    pivoted_df = b_global_results_filtered_df.pivot(index='task_name', columns='llm', values='mean_tokens_saved').reset_index()
    
    columns_to_capitalize = {
        'task_name': 'Task_name', 
        'technique_name': 'Technique_name', 
        'aggregate': 'Aggregate'
        }
    
    pivoted_df.rename(columns=columns_to_capitalize, inplace=True)
    dict_list = pivoted_df.to_dict(orient='records')
    return dict_list

def generate_report_time_saved_table(global_results_df):
    columns_to_keep = ['llm', 'task_name', 'technique_name', 'scenario', 'mean_time_saved']
    global_results_filtered_df = global_results_df[global_results_df['scenario'] == 'mean_prompt_time']
    global_results_filtered_df = global_results_filtered_df[global_results_filtered_df['task_name'] != '-code generation']
    global_results_filtered_df = global_results_filtered_df[global_results_filtered_df['task_name'] != '-code understanding']

    global_results_filtered_df['llm'] = global_results_filtered_df['llm'].apply(standardize_llm_name)
    global_results_filtered_df['technique_name'] = global_results_filtered_df['technique_name'].apply(standardize_technique_name)
    global_results_filtered_df['task_name'] = global_results_filtered_df['task_name'].apply(standardize_task_name)
    
    b_global_results_filtered_df = global_results_filtered_df[global_results_filtered_df['placement'] == 1].copy()
    w_global_results_filtered_df = global_results_filtered_df.loc[global_results_filtered_df.groupby(['llm', 'task_name', 'scenario'])['placement'].idxmax()].copy()
    
    b_global_results_filtered_df['mean_time_saved'] = None
    for index, row in b_global_results_filtered_df.iterrows():
        w_global_results_filtered_df_ = w_global_results_filtered_df[w_global_results_filtered_df['task_name'] == row['task_name']]
        w_global_results_filtered_df_ = w_global_results_filtered_df_[w_global_results_filtered_df_['llm'] == row['llm']]
        worst_time = w_global_results_filtered_df_['Mean_prompt_time'].to_list()[0]
        best_time = row['Mean_prompt_time']
        
        b_global_results_filtered_df.at[index, 'mean_time_saved'] = worst_time - best_time
        
    columns = b_global_results_filtered_df.columns
    for column in columns:
        if column not in columns_to_keep:
            b_global_results_filtered_df = b_global_results_filtered_df.drop([column], axis=1)
            
    print(f'b_global_results_filtered_df: {b_global_results_filtered_df.head()}')
    pivoted_df = b_global_results_filtered_df.pivot(index='task_name', columns='llm', values='mean_time_saved').reset_index()
    columns_to_capitalize = {
        'task_name': 'Task_name', 
        'technique_name': 'Technique_name', 
        'aggregate': 'Aggregate'
        }

    
    pivoted_df.rename(columns=columns_to_capitalize, inplace=True)
    dict_list = pivoted_df.to_dict(orient='records')
    return dict_list

def export_tables(db):
    custom_task_order = ['Defect detection', 'Clone detection', 'Exception type', 'Code QA', 'Code understanding group', 'Code translation', 'Bug fixing', 'Mutant generation', 'Assert generation', 'Code summarization', 'Code generation', 'Code generation group']
    custom_task_order_2 = ['Defect detection', 'Clone detection', 'Exception type', 'Code QA',  'Code translation', 'Bug fixing', 'Mutant generation', 'Assert generation', 'Code summarization', 'Code generation']
    scenario_order = ['Performance', 'Performance/Token', 'Performance/Time']

    tablenames_and_details = {
        'rq3_best_prompting_techniques': {
            'index': False,
            'caption': "Best performant techniques on the three scenarios: (default / token / time)",
            'label': 'tab:best_cost_benefit_prompting_techniques',
            'column_format': "lcccccc", 
            'escape': True, 
            'bold_rows': False,  
            'float_format': "%.2f",
            'ordering_task': custom_task_order,
            'ordering_column': 'Task_name',
        }, 
        
        'rq3_worst_prompting_techniques': {
            'index': False,
            'caption': "Worst performant techniques on the three scenarios: (default / token / time)",
            'label': 'tab:worst_cost_benefit_prompting_techniques',
            'column_format': "lcccccc", 
            'escape': True, 
            'bold_rows': False,  
            'float_format': "%.2f",
            'ordering_task': custom_task_order,
            'ordering_column': 'Task_name',
        }, 
        
        'rq3_aggregate_technique_performance': {
            'index': False,
            'caption': "Aggregate comparison to token and time cost-benefit performance",
            'label': 'aggregate_performance_data',
            'column_format': "lccccc", 
            'escape': True, 
            'bold_rows': False,  
            'float_format': "%.2f",
            'ordering_task': custom_task_order,
            'ordering_scenario': scenario_order,
            'ordering_column': 'Task_name',
        }, 
        
        'rq3_report_token_saved': {
            'index': False,
            'caption': "Mean number of tokens saved per prompt",
            'label': 'tab:tokens_saved',
            'column_format': "lcccccc", 
            'escape': True, 
            'bold_rows': False,  
            'float_format': "%.2f",
            'ordering_task': custom_task_order_2,
            'ordering_column': 'Task_name',
        }, 
        'rq3_report_time_saved': {
            'index': False,
            'caption': "Mean value of time saved per prompt",
            'label': 'tab:time_saved',
            'column_format': "lcccccc", 
            'escape': True, 
            'bold_rows': False,  
            'float_format': "%.2f",
            'ordering_task': custom_task_order_2,
            'ordering_column': 'Task_name',
        }, 
    }
    # f"{techniques['normal']} / {techniques['mean_total_tokens']} / {techniques['mean_prompt_time']}"
    
    csv_path = os.path.join(os.getcwd(), 'exported_csv')
    os.makedirs(csv_path, exist_ok=True)
    latex_tables_path = os.path.join(os.getcwd(), 'exported_latex_tables')
    os.makedirs(latex_tables_path, exist_ok=True)
    export_tablenames = [export_tablename for export_tablename in db.list_tables() if '_export' in export_tablename and 'rq3' in export_tablename]
    
    for export_tablename in export_tablenames:
        df = db.to_df(export_tablename)
        table_name = export_tablename.replace('_export', '')
        current_table_details = tablenames_and_details[table_name]
        print(f'for this table {table_name}')
        export_csv(df, table_name, csv_path)
        export_latex(df, table_name, latex_tables_path, current_table_details)
    
def export_csv(df, table_name, path):
    csv_path = os.path.join(path, f"{table_name}.csv")
    df.to_csv(csv_path, index=False)
    
def export_latex(df, table_name, path, current_table_details):
    latex_path = os.path.join(path, f"{table_name}.tex")
    ordering = current_table_details['ordering_task']
    ordering_column = current_table_details['ordering_column']
    
    if table_name == 'rq3_aggregate_technique_performance':
        ordering_task = current_table_details['ordering_task']
        ordering_scenario = current_table_details['ordering_scenario']
        task_order_map = {task: i for i, task in enumerate(ordering_task)}
        scenario_order_map = {sc: i for i, sc in enumerate(ordering_scenario)}
        
        ordering_column = current_table_details['ordering_column']
        
        df['__task_order'] = df[ordering_column].map(task_order_map)
        df['__scenario_order'] = df['Scenario'].map(scenario_order_map)
        df.sort_values(['__task_order', '__scenario_order'], inplace=True)
        df.drop(['__task_order', '__scenario_order'], axis=1, inplace=True)
        
    elif ordering is not None:
        df.set_index(ordering_column, inplace=True)
        df = df.reindex(ordering)
        df.reset_index(inplace=True)
    
    latex_code = df.to_latex(
        index=current_table_details['index'],       
        caption=current_table_details['caption'],  
        label=current_table_details['label'],  
        column_format=current_table_details['column_format'],  
        escape=current_table_details['escape'],  
        bold_rows=current_table_details['bold_rows'],  
        float_format=current_table_details['float_format'], 
    )
    
    latex_code = latex_code.replace("\\begin{table}", "\\begin{table}\n\\centering\n\\footnotesize")
    
    latex_code = latex_code.replace(
        'Code understanding group',
        r'\textbf{Code understanding group}'
    )
    
    latex_code = latex_code.replace(
        'Code generation group',
        r'\textbf{Code generation group}'
    )
    
    with open(latex_path, "w", encoding="utf-8") as f:
        f.write(latex_code)
