
import os
from itertools import product
from datetime import datetime
base_dir = "../datasets"

# map the task to datasets
TASK_TO_DATASET = {
    # "defect": ["devign"] # removed the devign dataset since it was in C, swapped for the SO dataset which is in python,
    "defect": ["so", 'vmc', 'wbo'],
    "clone": ["bigclonebench"],
    "exception": ["exception"],
    # "retrieval": ["poj104"],
    # "search": ["advtest"],
    "cosqa": ["cosqa"],
    "translation": ["codetrans"],
    "fixing": ["bfp"],
    # "completion": ['py150'],
    "mutant": ["mutant"],
    "assert": ["assert"],
    "summarization": ["codesearchnet"],
    "generation": ["concode"]
}

# map the dataset to sub-tasks
DATASET_TO_SUBSET = {
    "codetrans": ["java-cs", "cs-java"],
    "bfp": ["small", "medium"],
    "assert": ["abs", "raw"],
    "codesearchnet": ["java", "python", "javascript", "php", "go", "ruby"]
}

TASK_TO_EXTENSION = {
    "defect": "jsontxt",
    "clone": ".txt",
    "exception": ".jsonl",
    # "retrieval": ".jsonl",
    # "search": ".jsonl",
    "cosqa": ".json", 
    "translation": ".java-cs.txt",
    "fixing": ".buggy-fixed",
    "mutant": ".txt",
    "assert": "_methods.txt",
    "summarization": ".jsonl",
    "generation": ".jsonl",
    # "completion": [".json", ".txt"],
}

def get_dataset_paths(tasks, base_dir="../datasets"):
    """
    Generate dataset paths based on tasks, datasets, subsets, and splits.

    Args:
        base_dir (str): Base directory containing all datasets.

    Returns:
        list: A list of dictionaries, each containing dataset metadata.
    """

    dataset_metadata = []

    for task, datasets in TASK_TO_DATASET.items():
        for dataset in datasets:
            base_task_dir = os.path.join(base_dir, task, dataset)
            subsets = DATASET_TO_SUBSET.get(dataset, [None])
            extension = TASK_TO_EXTENSION.get(task, "")

            for subset in subsets:
                if subset is not None and task != 'translation':
                    subset_dir = os.path.join(base_task_dir, subset)
                else:
                    subset_dir = base_task_dir
                    
                if task == 'defect':
                    split_cats = ["train", "dev", "eval"]
                    
                elif task == 'completion':
                    split_cats = ["train.txt", "dev.txt", "test.json"]
                    
                else:
                    split_cats = ["train", "valid", "test"]
                    
                for split in split_cats:
                    if task in ["translation", "fixing", "mutant", "assert", "cosqa"]:
                        if task == "cosqa":
                            # source_lang, target_lang = subset.split("-")
                            if split == 'test':
                                source_path = os.path.join(subset_dir, f"test_webquery{extension}")
                                target_path = os.path.join(subset_dir, f"answers.txt")
                            else:
                                source_path = os.path.join(subset_dir, f"cosqa-{split}{extension}")
                                target_path = None
                                
                        elif task == "translation":
                            source_lang, target_lang = subset.split("-")
                            source_path = os.path.join(subset_dir, f"{split}{extension}.{source_lang}")
                            target_path = os.path.join(subset_dir, f"{split}{extension}.{target_lang}")
                        
                        elif task == "fixing":
                            source_path = os.path.join(subset_dir, f"{split}{extension}.buggy")
                            target_path = os.path.join(subset_dir, f"{split}{extension}.fixed")
                        
                        elif task == "mutant":
                            source_path = os.path.join(subset_dir, f"{split}_fixed.txt")
                            target_path = os.path.join(subset_dir, f"{split}_buggy.txt")
                        
                        elif task == "assert":
                            source_path = os.path.join(subset_dir, f"{split}_methods.txt")
                            target_path = os.path.join(subset_dir, f"{split}_assert.txt")

                        dataset_metadata.append({
                            "source_path": source_path,
                            "target_path": target_path,
                            "task": tasks[task],
                            "timestamp": datetime.now().isoformat(),
                            "obs": None,
                            "status": None,
                        })
                        
                    else:
                        if task == 'defect':
                            
                            if dataset == 'so':
                                defect_type = 'swapped_operands_datasets'
                            elif dataset == 'wbo':
                                defect_type = 'wrong_binary_operator_datasets'
                            elif dataset == 'vmc':
                                defect_type = 'variable_misuse_datasets'
                                
                            parts = [ '0', '1', '2', '3']
                            for part_no in parts:
                                source_path = os.path.join(subset_dir, f"20200621_Python_{defect_type}_{split}.{extension}-0000{part_no}-of-00004")
                                dataset_metadata.append({
                                    "source_path": source_path,
                                    "target_path": None,
                                    "task": tasks[task],
                                    "timestamp": datetime.now().isoformat(),
                                    "obs": None,
                                    "status": None,
                                })
                                
                        elif task == 'completion':
                            source_path = os.path.join(subset_dir, f"{split}")
                            dataset_metadata.append({
                                "source_path": source_path,
                                "target_path": None,
                                "task": tasks[task],
                                "timestamp": datetime.now().isoformat(),
                                "obs": None,
                                "status": None,
                            })
                                    
                        else:
                            source_path = os.path.join(subset_dir, f"{split}{extension}")
                            dataset_metadata.append({
                                "source_path": source_path,
                                "target_path": None,
                                "task": tasks[task],
                                "timestamp": datetime.now().isoformat(),
                                "obs": None,
                                "status": None,
                            })

    return dataset_metadata

if __name__ == '__main__':
    all_paths = get_dataset_paths()
    for path in all_paths:
        print(path)