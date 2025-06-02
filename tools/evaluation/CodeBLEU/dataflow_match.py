# Copyright (c) Microsoft Corporation. 
# Licensed under the MIT license.

from pathlib import Path
from tree_sitter import Language, Parser
import tree_sitter_python as tspython
import tree_sitter_java as tsjava
import tree_sitter_c_sharp as ts_c_sharp
import traceback
from tools.evaluation.CodeBLEU.parser import (
    DFG_python,
    DFG_java,
    DFG_ruby, DFG_go,
    DFG_php,
    DFG_javascript,
    DFG_csharp,
    remove_comments_and_docstrings,
    tree_to_token_index,
    index_to_code_token,
    tree_to_variable_index
)

dfg_function = {
    'python': DFG_python,
    'java': DFG_java,
    'ruby': DFG_ruby,
    'go': DFG_go,
    'php': DFG_php,
    'javascript': DFG_javascript,
    'c-sharp': DFG_csharp,
}

root_directory = Path(__file__).parents[2]
PARSER_LOCATION = root_directory.joinpath("evaluation/CodeBLEU/parser/my-languages.so")


def calc_dataflow_match(references, candidate, lang):
    return corpus_dataflow_match([references], [candidate], lang)


def corpus_dataflow_match(references, candidates, lang):
    if lang == 'c-sharp':
        LANGUAGE = Language(ts_c_sharp.language())
    elif lang == 'java':
        LANGUAGE = Language(tsjava.language())
    elif lang == 'python':
        LANGUAGE = Language(tspython.language())
    parser = Parser(LANGUAGE)
    parser = [parser, dfg_function[lang]]
    match_count = 0
    total_count = 0
    # print(f"DEBUG [len_references] len: {len(references)} lang {lang}")
    # print(f"DEBUG [head_references] len: {references[0:4]} lang {lang}")
    # print(f"DEBUG [len_candidates] len: {len(candidates)} lang {lang}")
    # print(f"DEBUG [head_candidates] len: {candidates[0:4]} lang {lang}")

    # for i in range(len(candidates)):
    #     references_sample = references[i]
    #     candidate = candidates[i]
    #     for reference in references_sample:
    
    for candidate, reference in zip(candidates, references):
        try:
            # print(f"DEBUG [cand_rem] len: {len(candidate)}, cand string: {candidate} lang {lang}")
            candidate = remove_comments_and_docstrings(candidate, lang)
            # print(f"DEBUG [cand_rem] len: {len(candidate)}, cand string: {candidate} lang {lang}")
        except:
            pass
        try:
            # print(f"DEBUG [ref_rem] len: {len(reference)}, ref string: {reference} lang {lang}")
            reference = remove_comments_and_docstrings(reference, lang)
            # print(f"DEBUG [ref_rem] len: {len(reference)}, ref string: {reference} lang {lang}")
        except:
            pass

        cand_dfg = get_data_flow(candidate, parser, mode='cand')
        ref_dfg = get_data_flow(reference, parser, mode='ref')
        # print(f"DEBUG [cand_dfg] len: {len(cand_dfg)} lang {lang}")
        # print(f"DEBUG [ref_dfg] len: {len(ref_dfg)} lang {lang}")

        normalized_cand_dfg = normalize_dataflow(cand_dfg)
        normalized_ref_dfg = normalize_dataflow(ref_dfg)
        # print(f"DEBUG [normalized_cand_dfg] len: {len(normalized_cand_dfg)}")
        # print(f"DEBUG [normalized_ref_dfg] len: {len(normalized_ref_dfg)}")

        if len(normalized_ref_dfg) > 0:
            total_count += len(normalized_ref_dfg)
            for dataflow in normalized_ref_dfg:
                if dataflow in normalized_cand_dfg:
                    match_count += 1
                    normalized_cand_dfg.remove(dataflow)

    score = match_count / total_count if total_count > 0 else 1.0
    return score


def get_data_flow(code, parser, mode=None):
    try:
        tree = parser[0].parse(bytes(code, 'utf8'))
        root_node = tree.root_node
        tokens_index = tree_to_token_index(root_node)
        # print(f"DEBUG {mode} [tokens_index] len: {len(tokens_index)}")
        
        # Split code into lines (new list)
        code = code.split('\n')
        # print(f"DEBUG {mode} [code_lines] len: {len(code)}")
        
        # Generate code tokens from tokens_index (new list)
        code_tokens = [index_to_code_token(x, code) for x in tokens_index]
        # print(f"DEBUG {mode} [code_tokens] len: {len(code_tokens)}")
        
        index_to_code = {}
        for idx, (index, code_line) in enumerate(zip(tokens_index, code_tokens)):
            index_to_code[index] = (idx, code_line)
        try:
            DFG, _ = parser[1](root_node, index_to_code, {})
        except Exception as e:
            DFG = []
            print(f'FAIL HERE 2 exception {e}')
            traceback.print_exc()
        DFG = sorted(DFG, key=lambda x: x[1])
        # print(f"DEBUG {mode} [DFG sorted] len: {len(DFG)}")
        
        indexs = set()
        for d in DFG:
            if len(d[-1]) != 0:
                indexs.add(d[1])
            for x in d[-1]:
                indexs.add(x)
        new_DFG = []
        for d in DFG:
            if d[1] in indexs:
                new_DFG.append(d)
        # print(f"DEBUG {mode} [new_DFG] len: {len(new_DFG)}")
        
        codes = code_tokens  # reusing the list of code tokens
        dfg = new_DFG
    except Exception as e:
        codes = code.split()
        dfg = []
        print(f'FAIL HERE exception {e}')
        traceback.print_exc()
    
    # merge nodes
    dic = {}
    for d in dfg:
        if d[1] not in dic:
            dic[d[1]] = d
        else:
            dic[d[1]] = (d[0], d[1], d[2],
                         list(set(dic[d[1]][3] + d[3])),
                         list(set(dic[d[1]][4] + d[4])))
    DFG = []
    for d in dic:
        DFG.append(dic[d])
    # print(f"DEBUG {mode} [merged DFG] len: {len(DFG)}")
    dfg = DFG
    return dfg



def normalize_dataflow_item(dataflow_item):
    var_name = dataflow_item[0]
    var_pos = dataflow_item[1]
    relationship = dataflow_item[2]
    par_vars_name_list = dataflow_item[3]
    par_vars_pos_list = dataflow_item[4]

    var_names = list(set(par_vars_name_list + [var_name]))
    norm_names = {}
    for i in range(len(var_names)):
        norm_names[var_names[i]] = 'var_' + str(i)

    norm_var_name = norm_names[var_name]
    relationship = dataflow_item[2]
    norm_par_vars_name_list = [norm_names[x] for x in par_vars_name_list]

    return (norm_var_name, relationship, norm_par_vars_name_list)


def normalize_dataflow(dataflow):
    var_dict = {}
    i = 0
    normalized_dataflow = []
    for item in dataflow:
        var_name = item[0]
        relationship = item[2]
        par_vars_name_list = item[3]
        for name in par_vars_name_list:
            if name not in var_dict:
                var_dict[name] = 'var_' + str(i)
                i += 1
        if var_name not in var_dict:
            var_dict[var_name] = 'var_' + str(i)
            i += 1
        normalized_dataflow.append((var_dict[var_name], relationship, [var_dict[x] for x in par_vars_name_list]))
    return normalized_dataflow
