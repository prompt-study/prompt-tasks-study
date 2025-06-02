
import pandas as pd
import os

def report_rq2(df_results, column_metric_name):
    df_results[column_metric_name] = pd.to_numeric(df_results[column_metric_name], errors='coerce')

    df_results['performance_over_token'] = (
        df_results[column_metric_name] / df_results['avg_total_tokens']
    )
    
    df_results['performance_over_time'] = (
        df_results[column_metric_name] / df_results['avg_prompt_time']
    )
    
    std_1 = df_results[column_metric_name].std()
    df_results['z_performance_result'] = (df_results[column_metric_name] - df_results[column_metric_name].mean()) / std_1
    
    std_2 = df_results['performance_over_time'].std()
    df_results['z_performance_over_time'] = (df_results['performance_over_time'] - df_results['performance_over_time'].mean()) / std_2
    
    std_3 = df_results['performance_over_token'].std()
    df_results['z_performance_over_token'] = (df_results['performance_over_token'] - df_results['performance_over_token'].mean()) / std_3
    
    
    rq3_data = {
        "llm": df_results['llm'],
        "task_name": df_results['task_name'],
        "technique_name": df_results['technique_name'],
        "language": df_results['language'],
        "status": df_results['status'],
        "metric_name": column_metric_name,
        "number_excluded": df_results['number_excluded'],
        "performance_result": df_results[column_metric_name],
        "performance_over_token": df_results['performance_over_token'],
        "performance_over_time": df_results['performance_over_time'],
        "z_performance_result": df_results['z_performance_result'],
        "z_performance_over_token": df_results['z_performance_over_token'],
        "z_performance_over_time": df_results['z_performance_over_time'],
        "obs": df_results['obs'],
    }
    
    df_rq3_report = pd.DataFrame(rq3_data)
    return df_rq3_report

def complementary_report_rq2(global_results_df):
    create_scatterplots(global_results_df)
    rank_and_correlate_tasks(global_results_df)
    result = report_aggregate_performance_placement(global_results_df)
    return result
    
def create_scatterplots(global_results_df):
    import matplotlib.pyplot as plt
    import os
    
    techniques = global_results_df['technique_name'].unique()
    cmap = plt.cm.get_cmap("gist_ncar", len(techniques))
    color_dict = {technique: cmap(i) for i, technique in enumerate(techniques)}
    
    for llm in global_results_df['llm'].unique():
        scatter_plot_general_performance_df = global_results_df[global_results_df['llm'] == llm].copy()
        
        plt.figure(figsize=(12, 8))
        for technique in techniques:
            subset = scatter_plot_general_performance_df[scatter_plot_general_performance_df['technique_name'] == technique]
            plt.scatter(subset['task_name'], subset['z_performance_result'], 
                        label=technique, 
                        color=color_dict[technique], 
                        s=100,      
                        edgecolors='k') 
        print(f'llm {llm}')   
        plt.xlabel("Task", fontsize=18)
        plt.ylabel("Normalized Performance Metric", fontsize=18)
        plt.xticks(rotation=45, fontsize=18)
        plt.yticks(fontsize=18)
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=18)
        plt.tight_layout()
        
        cwd = os.getcwd()
        llm_name = llm.replace('.','').replace('-','').replace('/','')[:20]
        plt.savefig(os.path.join(cwd, f"{llm_name}_scatterplot_performance.png"))
        plt.close() 
        
    scatter_plot_general_performance_df = global_results_df.groupby(
            ['technique_name', 'task_name'], as_index=False
        ).agg({
            'z_performance_result': 'mean',
            'z_performance_over_token': 'mean',
            'z_performance_over_time': 'mean'
        })
    

    plt.figure(figsize=(12, 8))
    for technique in techniques:
        subset = scatter_plot_general_performance_df[scatter_plot_general_performance_df['technique_name'] == technique]
        plt.scatter(subset['task_name'], subset['z_performance_result'], 
                    label=technique, 
                    color=color_dict[technique], 
                    s=100,      
                    edgecolors='k') 
    plt.xlabel("Task", fontsize=15)
    plt.ylabel("Normalized Performance Metric", fontsize=15)
    plt.xticks(rotation=45)  
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    
    cwd = os.getcwd()
    plt.savefig(os.path.join(cwd, "scatterplot_aggregate_performance.png"))
    plt.close()  

def rank_and_correlate_tasks(global_results_df):
    import os
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.cluster import SpectralBiclustering

    techniques = global_results_df['technique_name'].unique()

    performance_matrix = global_results_df.groupby(
        ['technique_name', 'task_name'], as_index=False
    ).agg({
        'z_performance_result': 'mean'
    }).pivot(index='technique_name', columns='task_name', values='z_performance_result')

    n_clusters = 10  
    model = SpectralBiclustering(n_clusters=n_clusters, method='log', random_state=0)
    model.fit(performance_matrix)

    row_order = np.argsort(model.row_labels_)
    col_order = np.argsort(model.column_labels_)
    biclustered_matrix = performance_matrix.iloc[row_order, :]
    biclustered_matrix = biclustered_matrix.iloc[:, col_order]

    plt.figure(figsize=(12, 8))

    # Set global seaborn font scale
    sns.set(font_scale=1.5)  # Adjust the overall font scale here

    ax = sns.heatmap(
        biclustered_matrix, cmap="viridis", annot=True, 
        annot_kws={"fontsize": 10},  # Annotation font size
        cbar_kws={"shrink": 0.8}
    )

    # Modify tick labels and axes labels font size
    ax.set_xticklabels(ax.get_xticklabels(), fontsize=11, rotation=45, ha='right')
    ax.set_yticklabels(ax.get_yticklabels(), fontsize=11)

    # Optional axis labels
    ax.set_xlabel('Task Name', fontsize=14)
    ax.set_ylabel('Technique Name', fontsize=14)

    plt.tight_layout()
    plt.savefig(os.path.join(os.getcwd(), f"bicluster_heatmap_{n_clusters}.png"))
    plt.close()


    def compute_reconstruction_error(model, data):
        error = 0.0
        data_values = data.values
        for i in range(model.n_clusters):
            for j in range(model.n_clusters):
                mask = np.outer(model.row_labels_ == i, model.column_labels_ == j)
                if np.any(mask):
                    block_values = data_values[mask]
                    block_mean = block_values.mean()
                    error += np.sum((block_values - block_mean) ** 2)
        return error

    candidate_ns = list(range(2, 11))  
    best_n = None
    best_error = np.inf
    errors = {}

    for candidate in candidate_ns:
        candidate_model = SpectralBiclustering(n_clusters=candidate, method='log', random_state=0)
        candidate_model.fit(performance_matrix)
        err = compute_reconstruction_error(candidate_model, performance_matrix)
        errors[candidate] = err
        if err < best_error:
            best_error = err
            best_n = candidate
            
def report_aggregate_performance_placement(global_results_df):
    ranked_aggregate_global_performance = global_results_df.groupby(
            ['technique_name'], as_index=False
        ).agg({
            'z_performance_result': 'mean',
        }).copy()
    ranked_aggregate_global_performance['placement'] = ranked_aggregate_global_performance['z_performance_result'].rank(method='first', ascending=False)
    
    save_path = os.path.join(os.getcwd(), f"placement_performance.tex")
    latex_table = get_top_and_bottom(ranked_aggregate_global_performance).to_latex(
        index=False, 
        caption="Top and bottom 3 most performant techniques", 
        label="tab:top_bot3_perf_agg",
        float_format="%.2f"
    )
    with open(save_path, "w") as f:
        f.write(latex_table)
    

    ranked_aggregate_global_token = global_results_df.groupby(
            ['technique_name'], as_index=False
        ).agg({
            'z_performance_over_token': 'mean',
        }).copy()
    ranked_aggregate_global_token['placement'] = ranked_aggregate_global_token['z_performance_over_token'].rank(method='first', ascending=False)
    save_path = os.path.join(os.getcwd(), "placement_token_performance.tex")
    latex_table = get_top_and_bottom(ranked_aggregate_global_token).to_latex(
        index=False, 
        caption="Top 3 best performance/token cost techniques", 
        label="tab:top_bot3_perf_token_agg",
        float_format="%.2f"
    )
    with open(save_path, "w") as f:
        f.write(latex_table)
    
    
    ranked_aggregate_global_time = global_results_df.groupby(
            ['technique_name'], as_index=False
        ).agg({
            'z_performance_over_time': 'mean'
        }).copy()
    ranked_aggregate_global_time['placement'] = ranked_aggregate_global_time['z_performance_over_time'].rank(method='first', ascending=False)
    save_path = os.path.join(os.getcwd(), "placement_time_performance.tex")
    latex_table = get_top_and_bottom(ranked_aggregate_global_time).to_latex(
        index=False, 
        caption="Top 3 best performance/time cost techniques", 
        label="tab:top_bot3_perf_time_agg",
        float_format="%.2f"
    )
    with open(save_path, "w") as f:
        f.write(latex_table)
    
    output = {
        'agg_ranked_performance_report': ranked_aggregate_global_performance,
        'agg_ranked_performance_token_report': ranked_aggregate_global_token,
        'agg_ranked_performance_time_report': ranked_aggregate_global_time,
    }
    return output
    
def get_top_and_bottom(df, rank_col='placement', top_n=15):
    def filter_group(group):
        group_sorted = group.sort_values(rank_col)
        top = group_sorted.head(top_n)
        # bottom = group_sorted.tail(top_n)
        # return pd.concat([top, bottom])
        # bottom = group_sorted.tail(top_n)
        return top
    
    filtered_df = filter_group(df)
    filtered_df[rank_col] = filtered_df[rank_col].astype(int)
    
    return filtered_df.sort_values(rank_col)
 
def export_tables(db):
    custom_task_order = ['Defect detection', 'Clone detection', 'Exception type', 'Code QA', 'Code understanding group', 'Code translation', 'Bug fixing', 'Mutant generation', 'Assert generation', 'Code summarization', 'Code generation', 'Code generation group']
    
    tablenames_and_details = {
        'rq1_optimal_prompting_techniques': {
            'index': False,
            'caption': "Optimal Prompting Techniques for Various Tasks Across Different LLMs",
            'label': 'tab:optimal_prompting_techniques',
            'column_format': "p{2.5cm}lccccc", 
            'escape': True, 
            'bold_rows': False,  
            'float_format': "%.2f",
            'ordering': custom_task_order,
            'ordering_column': 'Task_name',
        }, 
        'rq1_aggregate_technique_performance': {
            'index': False,
            'caption': "Aggregate performance data for the best prompting techniques",
            'label': 'aggregate_performance_data',
            'column_format': "p{2.5cm}lcccc", 
            'escape': True, 
            'bold_rows': False,  
            'float_format': "%.2f",
            'ordering': custom_task_order,
            'ordering_column': 'Task_name',
        }, 
    }
    
    
    csv_path = os.path.join(os.getcwd(), 'exported_csv')
    os.makedirs(csv_path, exist_ok=True)
    latex_tables_path = os.path.join(os.getcwd(), 'exported_latex_tables')
    os.makedirs(latex_tables_path, exist_ok=True)
    export_tablenames = [export_tablename for export_tablename in db.list_tables() if '_export' in export_tablename]
    
    for export_tablename in export_tablenames:
        df = db.to_df(export_tablename)

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
