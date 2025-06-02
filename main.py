from tools.prompter import Prompter
from tools.progress_reporter import ProgressReporter
from tools.results_reporter import ResultsRoutine
import sys
import os

def main():
    print(f'received: {sys.argv}')
    if len(sys.argv) >= 3:
        command = sys.argv[1]
        context = sys.argv[2]
        if len(sys.argv) == 4:
            prompt_number = int(sys.argv[3])
        else:
            prompt_number = 30
            
        if command == "prompter":
            prompter = Prompter()
            
            if context == 'create_tables':
                prompter.create_tables()
                
            elif context == 'setup':
                prompter.create_tables()
                prompter.import_prompt_pieces()
                prompter.import_source_data()
                prompter.create_vectorstores()
                prompter.assemble()
                
            elif context == 'import_prompt_pieces':
                prompter.import_prompt_pieces()
                
            elif context == 'import_source_data':
                prompter.import_source_data()
                
            elif context == 'create_vectorstores':
                prompter.create_vectorstores()
                
            elif context == 'assemble':
                prompter.assemble()
                
            elif context == 'run':
                prompter.run(prompt_number=prompt_number) 
                
            elif context == 'run_equalized':
                prompter.run(equalized=True, prompt_number=prompt_number) 
                # print(f'backing up responses')   
                # prompter.backup_prompt_responses()
                
            elif context == 'backup_prompt_responses':
                prompter.backup_prompt_responses()
                
            elif context == 'count_sampled_datasets':
                prompter.count_sampled_datasets()
                
            # elif context == 'nuke_restart':
            #     prompter.create_tables(nuke=True)
            #     prompter.import_prompt_pieces()
            #     prompter.import_source_data()
            #     prompter.create_vectorstores()
            #     prompter.assemble()
            
            # elif context == 'soft_restart':
            #     prompter.create_tables(nuke=False)
            #     prompter.import_prompt_pieces()
            #     prompter.import_source_data()
            #     prompter.create_vectorstores()
            #     prompter.assemble()
            
        if command == "progress":
            reporter = ProgressReporter()
            if context == 'report':
                reporter.report_prompting_progress()    
                
        if command == 'result':
            if context == 'report':
                source_db_path = os.path.join(os.getcwd(), 'prompts.db')
                target_db_path = os.path.join(os.getcwd(), 'results.db')
                reporter = ResultsRoutine(source_db_path, target_db_path)
                reporter.begin_eval()
                
            if context == 'test_report':
                source_db_path = os.path.join(os.getcwd(), 'backup.db')
                target_db_path = os.path.join(os.getcwd(), 'test_results.db')
                reporter = ResultsRoutine(source_db_path, target_db_path)
                reporter.begin_eval()
    else:
        print("Please provide instructions.\nInstructions:\nprompter [context] -> contexts = [import_prompt_pieces, import_source_data, assemble, run, create_tables]")
        sys.exit(1)

if __name__ == '__main__':
    main()