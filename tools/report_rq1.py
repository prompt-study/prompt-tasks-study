
import pandas as pd

def report_rq1(df_results, column_metric_name):
    df_results[column_metric_name] = pd.to_numeric(df_results[column_metric_name], errors='coerce')

    df_results['placement'] = df_results.groupby(['llm', 'task_name'])[column_metric_name] \
                                        .rank(method='first', ascending=False)
    
    
    agg_dict = {
        column_metric_name: 'mean',
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
    
    avg_df['placement'] = avg_df.groupby(['llm', 'task_name'])[column_metric_name] \
                                    .rank(method='first', ascending=False)

    df_results = df_results._append([avg_df], ignore_index=True)
    
    rq1_data = {
        "llm": df_results['llm'],
        "task_name": df_results['task_name'],
        "technique_name": df_results['technique_name'],
        "language": df_results['language'],
        "status": df_results['status'],
        "metric_name": column_metric_name,
        "metric_result": df_results[column_metric_name],
        "number_excluded": df_results['number_excluded'],
        "placement": df_results['placement'],
        "avg_tokens_sent": df_results['avg_tokens_sent'],
        "avg_tokens_received": df_results['avg_tokens_received'],
        "avg_total_tokens": df_results['avg_total_tokens'],
        "avg_cost": df_results['avg_cost'],
        "std_dev_cost": df_results['std_dev_cost'],
        "avg_prompt_time": df_results['avg_prompt_time'],
        "std_dev_prompt_time": df_results['std_dev_prompt_time'],
        "obs": df_results['obs'],
    }
    
    df_rq1_report = pd.DataFrame(rq1_data)
    return df_rq1_report

def complementary_report_rq1(global_results_df):
    global_results_df = global_results_df[global_results_df['llm']=='aggregate']        
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
        'avg_tokens_sent': 'mean',
        'avg_tokens_received': 'mean',
        'avg_total_tokens': 'mean',
        'avg_cost': 'mean',
        'std_dev_cost': 'mean',
        'avg_prompt_time': 'mean',
        'std_dev_prompt_time': 'mean',
        'obs': 'first',
        
    }
    print(f'report df {global_results_df}') 
    global_results_df = global_results_df.groupby(['task_name', 'technique_name'], as_index=False).agg(agg_dict)
    
    print(f'report df {len(global_results_df)}')
    global_results_df['llm'] = 'aggregate'
    global_results_df['placement'] = global_results_df.groupby(['task_name'])['metric_result'].rank(method='first', ascending=False)
    
    rq1_data = {
        "llm": global_results_df['llm'],
        "task_name": global_results_df['task_name'],
        "technique_name": global_results_df['technique_name'],
        "language": global_results_df['language'],
        "status": global_results_df['status'],
        "metric_name": 'normalized_mean',
        "metric_result": global_results_df['metric_result'],
        "number_excluded": global_results_df['number_excluded'],
        "placement": global_results_df['placement'],
        "avg_tokens_sent": global_results_df['avg_tokens_sent'],
        "avg_tokens_received": global_results_df['avg_tokens_received'],
        "avg_total_tokens": global_results_df['avg_total_tokens'],
        "avg_cost": global_results_df['avg_cost'],
        "std_dev_cost": global_results_df['std_dev_cost'],
        "avg_prompt_time": global_results_df['avg_prompt_time'],
        "std_dev_prompt_time": global_results_df['std_dev_prompt_time'],
        "obs": global_results_df['obs'],
    }
    
    df_rq1_report = pd.DataFrame(rq1_data)
    return df_rq1_report