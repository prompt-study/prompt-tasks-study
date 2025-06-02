
import pandas as pd
from tqdm import tqdm
import os
from scipy.stats import spearmanr
from datetime import datetime
import numpy as np
'''
Rq 2 - compare the best and worst for each model, search for possible similarities

table with winners, losers, variance for each one, p value and mean diff between winners and losers
using cos similarity, token similarity, entropy score, other metrics
'''

def report_rq2(db, prompts_db):
    metrics_to_test = [
            # Quantitative metrics
        prompt_response_time,
        token_count,
        lexical_diversity,
        readability_scores,
        gunning_fog_index,
        flesch_reading_ease,
        
        
            # Semantic metrics
        # semantic_similarity,
        # named_entity_recognition,
        # sentiment_analysis,
        
            # Structural metrics
        # part_of_speech_tagging, 
        # syntatic_complexity,
        # dependency_parsing,
        
    ]
    
    progress_bar_done = tqdm(total=len(metrics_to_test), position=0, unit=("variables"))
    db = create_table_report_rq2(db)
    performance_data_df = db.to_df('rq1_report')
    performance_data_df = performance_data_df[performance_data_df['technique_name'] != 'prompt_paraphrasing']
    performance_data_df = performance_data_df[performance_data_df['technique_name'] != 'winner_0']
    # prompting_results_df = db.to_df('prompting_results')
    prompting_results_df = prompts_db.to_df('_prompts_ready')
    
    performance_data_df, prompting_results_df = prepare_dataframes(performance_data_df, prompting_results_df)
    
    for routine in metrics_to_test:
        performance_data_df_copy = performance_data_df.copy()
        prompting_results_df_copy = prompting_results_df.copy()
        lines = routine(performance_data_df_copy, prompting_results_df_copy)
        progress_bar_done.update(1)
        
        for line in lines:
            if line['p_value'] < 0.05:
                db.cache(line, 'rq2_correlations_report_export')
                db.save()
                
            # else:
            #     print(f'p value more than 0.05')

    # report_rq2 = db.to_df('rq2_report')
    export_tables(db)
    
def create_table_report_rq2(db):
    table_name = 'rq2_correlations_report_export'
    query =f'''
        CREATE TABLE IF NOT EXISTS '{table_name}' (
            grouping	TEXT NOT NULL,
            corr_metric_name TEXT,
            p_value REAL,
            corr_coef REAL,
            obs	TEXT,
            status TEXT NOT NULL,
        PRIMARY KEY (grouping, corr_metric_name)
        );'''
    db.execute_sql(query)
    return db      



def prepare_dataframes(performance_data_df, prompting_results_df):
    
    performance_data_df = performance_data_df[performance_data_df['technique_name'] != 'prompt_paraphrasing']
    performance_data_df = performance_data_df[performance_data_df['llm'] == 'aggregate']
    performance_data_df = performance_data_df[performance_data_df['task_name'] != '-code generation']
    performance_data_df = performance_data_df[performance_data_df['task_name'] != '-code understanding']
    
    prompting_results_df['token_count'] = prompting_results_df['tokens_sent'] + prompting_results_df['tokens_received']
    prompting_results_df = prompting_results_df[prompting_results_df['technique_name'] != 'prompt_paraphrasing']
    
    prompting_results_df['prompt_time'] = None
    
    prompting_results_df.loc[:, 'token_count'] = (
        prompting_results_df['tokens_sent'] + prompting_results_df['tokens_received']
    )
    prompting_results_df.loc[:, 'time_prompt_received'] = pd.to_datetime(
        prompting_results_df['time_prompt_received']
    )
    prompting_results_df['time_prompt_received'] = pd.to_datetime(prompting_results_df['time_prompt_received'])
    prompting_results_df['time_prompt_sent'] = pd.to_datetime(prompting_results_df['time_prompt_sent'])
    prompting_results_df['prompt_time'] = prompting_results_df['time_prompt_received'] - prompting_results_df['time_prompt_sent']

    return performance_data_df, prompting_results_df

def prompt_response_time(performance_data_df_copy, prompts_df_copy):
    corr_name = 'mean_prompt_time'
    mean_df = (
        prompts_df_copy
        .groupby(['task_name', 'technique_name'], as_index=False)['prompt_time']
        .mean()
        .rename(columns={'prompt_time': 'corr_metric_result'})
    )
    
    mean_df['corr_metric_name'] = corr_name
    
    corr_df = pd.merge(
        performance_data_df_copy,
        mean_df,
        on=['task_name', 'technique_name'],
        how='outer'
    )
    
    lines = [corr(corr_df, "global_aggregate", corr_name)]

    understanding_tasks = [
        "defect_detection", "clone_detection",
        "exception_type", "code_question_answering"
    ]
    lines.append(corr(corr_df[corr_df["task_name"].isin(understanding_tasks)],"code_understanding", corr_name))

    generation_tasks = [
        "code_translation", "bug_fixing", "mutant_generation",
        "assert_generation", "code_summarization", "code_generation"
    ]
    lines.append(corr(corr_df[corr_df["task_name"].isin(generation_tasks)], "code_generation", corr_name))
    
    return lines

def flesch_reading_ease(performance_df: pd.DataFrame, prompts_df: pd.DataFrame):
    import textstat
    corr_name = "mean_flesch_reading_ease"

    if "flesch_reading_ease" not in prompts_df.columns:
        prompts_df = prompts_df.copy()
        prompts_df["flesch_reading_ease"] = prompts_df["prompt_to_send"].apply(
            textstat.flesch_reading_ease
        )

    mean_df = (
        prompts_df
        .groupby(["task_name", "technique_name"], as_index=False)["flesch_reading_ease"]
        .mean()
        .rename(columns={"flesch_reading_ease": "corr_metric_result"})
        .assign(corr_metric_name=corr_name)
    )

    corr_df = performance_df.merge(
        mean_df, on=["task_name", "technique_name"], how="outer"
    )

    lines = [
        corr(corr_df, "aggregate", corr_name),
        corr(corr_df[corr_df["task_name"].isin([
            "defect_detection", "clone_detection",
            "exception_type", "code_question_answering"])],
             "code_understanding", corr_name),
        corr(corr_df[corr_df["task_name"].isin([
            "code_translation", "bug_fixing", "mutant_generation",
            "assert_generation", "code_summarization", "code_generation"])],
             "code_generation", corr_name)
    ]
    
    return lines


def token_count(performance_data_df_copy, prompts_df_copy):
    corr_name = 'mean_token_count'
    mean_df = (
        prompts_df_copy
        .groupby(['task_name', 'technique_name'], as_index=False)['token_count']
        .mean()
        .rename(columns={'token_count': 'corr_metric_result'})
    )
    
    mean_df['corr_metric_name'] = corr_name
    
    corr_df = pd.merge(
        performance_data_df_copy,
        mean_df,
        on=['task_name', 'technique_name'],
        how='outer'
    )
    
    lines = [corr(corr_df, "aggregate", corr_name)]

    understanding_tasks = [
        "defect_detection", "clone_detection",
        "exception_type", "code_question_answering"
    ]
    lines.append(corr(corr_df[corr_df['task_name'].isin(understanding_tasks)],"code_understanding", corr_name))

    generation_tasks = [
        "code_translation", "bug_fixing", "mutant_generation",
        "assert_generation", "code_summarization", "code_generation"
    ]
    lines.append(corr(corr_df[corr_df['task_name'].isin(generation_tasks)], "code_generation", corr_name))
    
    return lines


def lexical_diversity(performance_df, prompts_df):  
    from lexicalrichness import LexicalRichness
    corr_name = "mean_mtld"
    
    if "mtld" not in prompts_df.columns:
        prompts_df = prompts_df.copy()
        prompts_df["mtld"] = prompts_df["prompt_to_send"].apply(
            lambda txt: LexicalRichness(txt).mtld()
        )
    
    mean_df = (
        prompts_df
        .groupby(["task_name", "technique_name"], as_index=False)["mtld"]
        .mean()
        .rename(columns={"mtld": "corr_metric_result"})
        .assign(corr_metric_name=corr_name)
    )
    
    corr_df = performance_df.merge(
        mean_df, on=["task_name", "technique_name"], how="outer"
    )

    lines = [
        corr(corr_df, "aggregate", corr_name),
        corr(corr_df[corr_df["task_name"].isin([
            "defect_detection", "clone_detection",
            "exception_type", "code_question_answering"])],
              "code_understanding", corr_name),
        corr(corr_df[corr_df["task_name"].isin([
            "code_translation", "bug_fixing", "mutant_generation",
            "assert_generation", "code_summarization", "code_generation"])],
              "code_generation", corr_name)
    ]
    
    return lines

    
def readability_scores(performance_df: pd.DataFrame, prompts_df: pd.DataFrame):
    import textstat
    corr_name = "mean_fk_grade"

    if "fk_grade" not in prompts_df.columns:
        prompts_df = prompts_df.copy()
        prompts_df["fk_grade"] = prompts_df["prompt_to_send"].apply(
            textstat.flesch_kincaid_grade
        )

    mean_df = (
        prompts_df
        .groupby(["task_name", "technique_name"], as_index=False)["fk_grade"]
        .mean()
        .rename(columns={"fk_grade": "corr_metric_result"})
        .assign(corr_metric_name=corr_name)
    )

    corr_df = performance_df.merge(
        mean_df, on=["task_name", "technique_name"], how="outer"
    )

    lines = [
        corr(corr_df, "aggregate", corr_name),
        corr(corr_df[corr_df["task_name"].isin([
            "defect_detection", "clone_detection",
            "exception_type", "code_question_answering"])],
             "code_understanding", corr_name),
        corr(corr_df[corr_df["task_name"].isin([
            "code_translation", "bug_fixing", "mutant_generation",
            "assert_generation", "code_summarization", "code_generation"])],
             "code_generation", corr_name)
    ]
    
    
    return lines

def gunning_fog_index(performance_df: pd.DataFrame, prompts_df: pd.DataFrame):
    import textstat
    corr_name = "mean_gunning_fog"

    if "gunning_fog" not in prompts_df.columns:
        prompts_df = prompts_df.copy()
        prompts_df["gunning_fog"] = prompts_df["prompt_to_send"].apply(
            textstat.gunning_fog
        )

    mean_df = (
        prompts_df
        .groupby(["task_name", "technique_name"], as_index=False)["gunning_fog"]
        .mean()
        .rename(columns={"gunning_fog": "corr_metric_result"})
        .assign(corr_metric_name=corr_name)
    )

    corr_df = performance_df.merge(
        mean_df, on=["task_name", "technique_name"], how="outer"
    )

    lines = [
        corr(corr_df, "aggregate", corr_name),
        corr(corr_df[corr_df["task_name"].isin([
            "defect_detection", "clone_detection",
            "exception_type", "code_question_answering"])],
             "code_understanding", corr_name),
        corr(corr_df[corr_df["task_name"].isin([
            "code_translation", "bug_fixing", "mutant_generation",
            "assert_generation", "code_summarization", "code_generation"])],
             "code_generation", corr_name)
    ]
    
    return lines
    
def corr(df, group_label, corr_name):
    x = df["corr_metric_result"]
    y = df["metric_result"]

    # Convert x if timedelta
    if np.issubdtype(x.dtype, np.timedelta64):
        x = x.dt.total_seconds()
    # Convert y if timedelta
    if np.issubdtype(y.dtype, np.timedelta64):
        y = y.dt.total_seconds()
    # Drop rows with NaN
    mask = ~(x.isna() | y.isna())
    x = x[mask]
    y = y[mask]
    if len(x) < 2:  # Not enough data to correlate
        coef, p = np.nan, np.nan
    else:
        coef, p = spearmanr(x, y)
    return {
        "grouping": group_label,
        "corr_metric_name": corr_name,
        "p_value": p,
        "corr_coef": coef,
        "obs": None,
        "status": "success",
    }







def export_tables(db):
    custom_task_order = ['Defect detection', 'Clone detection', 'Exception type', 'Code QA', 'Code understanding group', 'Code translation', 'Bug fixing', 'Mutant generation', 'Assert generation', 'Code summarization', 'Code generation', 'Code generation group']
    tablenames_and_details = {
        'rq2_correlations_report': {
            'index': False,
            'caption': "Correlation between prompt performance and different textual metrics",
            'label': 'tab:correlations_with_text_metrics',
            'column_format': "p{2.5cm}lccccc", 
            'escape': True, 
            'bold_rows': False,  
            'float_format': "%.4f",
            'ordering': None,
            'ordering_column': 'Task_name',
        }, 
    }
    
    
    csv_path = os.path.join(os.getcwd(), 'exported_csv')
    os.makedirs(csv_path, exist_ok=True)
    latex_tables_path = os.path.join(os.getcwd(), 'exported_latex_tables')
    os.makedirs(latex_tables_path, exist_ok=True)
    export_tablenames = [export_tablename for export_tablename in db.list_tables() if '_export' in export_tablename and 'rq2' in export_tablename]
    
    for export_tablename in export_tablenames:
        
        df = db.to_df(export_tablename)
        
        df = df.rename(columns={
            'grouping': 'Groups',
            'corr_metric_name': 'Test',
            'p_value': 'p_value',      
            'corr_coef': 'corr_coef',  
        })
        if 'obs' in df:
            df = df.drop(columns=['obs'])
        if 'status' in df:
            df = df.drop(columns=['status'])
        df = df.sort_values(by="Groups", ascending=True)
        table_name = export_tablename.replace('_export', '')
        current_table_details = tablenames_and_details[table_name]
        export_csv(df, table_name, csv_path)
        export_latex(df, table_name, latex_tables_path, current_table_details)
    
def export_csv(df, table_name, path):
    csv_path = os.path.join(path, f"{table_name}.csv")
    df.to_csv(csv_path, index=False)
    
def export_latex(df, table_name, path, current_table_details):
    
    latex_path = os.path.join(path, f"{table_name}.tex")
    
    ordering = current_table_details['ordering']
    ordering_column = current_table_details['ordering_column']
    if ordering is not None:
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
