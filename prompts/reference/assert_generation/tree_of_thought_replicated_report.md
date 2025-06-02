
assert_generation_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''To solve the problem, break it down into multiple reasoning steps. For each potential step, generate and evaluate possible assertions to replace the placeholder, and decide which thought path to continue. Only output the final answer when the iterative process is complete.
Determine the correct assertion that should replace <AssertPlaceHolder> in the following code.
Provide only the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nNote: This task will undergo multiple iterations with intermediate reasoning. Only output the final assertion once all iterations are complete."
    ),
    HumanMessagePromptTemplate.from_template(
        "When finished, output ###FINISHED### alongside your final assertion statement."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

──────────────────────────── Variation 1 ────────────────────────────
assert_generation_template_tree_of_thought_1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Break the problem into several logical steps while reasoning iteratively. At each step, propose and assess potential assertions to substitute the placeholder, and select the appropriate reasoning track to proceed. Output only the final answer when the process is fully complete.
Identify the proper assertion to substitute <AssertPlaceHolder> in the provided code.
Return solely the assertion line.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nReminder: This assignment will be processed through several iterations with step-by-step reasoning. Display only the ultimate assertion after all iterations are done."
    ),
    HumanMessagePromptTemplate.from_template(
        "Upon completion, provide ###FINISHED### next to your final assertion statement."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

──────────────────────────── Variation 2 ────────────────────────────
assert_generation_template_tree_of_thought_2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Decompose the problem into a series of logical assessments. For each assessment, propose and appraise different assertions to fill the placeholder, then choose the reasoning path to continue. Only display the final result once every iteration is finished.
Pinpoint the accurate assertion to replace <AssertPlaceHolder> in the following snippet.
Respond solely with the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nNote: The task will be executed over multiple iterations with intermediate logical steps. Output solely the final assertion once every iteration is finished."
    ),
    HumanMessagePromptTemplate.from_template(
        "Once done, show ###FINISHED### along with your concluding assertion statement."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

──────────────────────────── Variation 3 ────────────────────────────
assert_generation_template_tree_of_thought_3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Approach this problem by dividing it into various sequential reasoning steps. At each phase, craft and evaluate potential assertion candidates to stand in for the placeholder, determining which direction to pursue. Reveal the final answer only after the complete iterative process.
Select the correct assertion to substitute for <AssertPlaceHolder> in the code below.
Supply just the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nPlease note: This activity involves successive iterations with interim reasoning. Only reveal the final assertion after all iterative steps are complete."
    ),
    HumanMessagePromptTemplate.from_template(
        "When you have finished, append ###FINISHED### with your final assertion."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

──────────────────────────── Variation 4 ────────────────────────────
assert_generation_template_tree_of_thought_4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Handle this task by segmenting the problem into distinct analytical steps. In every step, devise and scrutinize potential assertion options to replace the placeholder, then choose the reasoning thread to advance. Present your final answer only after the entire process is concluded.
Determine the right assertion that belongs in place of <AssertPlaceHolder> in the given code.
Submit exclusively the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nAttention: The problem will be tackled through several iterations that include intermediate reasoning. Only present the final assertion after completing all iterations."
    ),
    HumanMessagePromptTemplate.from_template(
        "When finalized, include ###FINISHED### alongside the final assertion statement."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

──────────────────────────── Variation 5 ────────────────────────────
assert_generation_template_tree_of_thought_5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Divide the problem into a sequence of logical reasoning segments. At each segment, construct and review a set of potential assertions to substitute the placeholder, then opt for the reasoning path most aligned with the solution. Only reveal the final conclusion following the iterative process.
Identify the assertion that should accurately replace <AssertPlaceHolder> in the code snippet below.
Return just the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nBe aware: This task goes through numerous iterative steps with intermediate explanations. Display only the final assertion once every iteration is concluded."
    ),
    HumanMessagePromptTemplate.from_template(
        "After finishing, output ###FINISHED### together with your final assertion statement."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

──────────────────────────── Variation 6 ────────────────────────────
assert_generation_template_tree_of_thought_6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Segment the challenge into multiple logical steps. For every step, formulate and analyze candidate assertions that might replace the placeholder, and decide which reasoning route to take forward. Only output the final result once the entire process is complete.
Figure out the correct assertion to replace <AssertPlaceHolder> in the ensuing code.
Offer solely the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nPlease note: The task will go through multiple iterations featuring intermediate reasoning. Only reveal the final assertion after all iterations are concluded."
    ),
    HumanMessagePromptTemplate.from_template(
        "When complete, attach ###FINISHED### next to your final assertion statement."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

──────────────────────────── Variation 7 ────────────────────────────
assert_generation_template_tree_of_thought_7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Approach the problem by splitting it into several reasoning phases. In each phase, generate possible assertion candidates to address the placeholder and evaluate them to decide the best reasoning route. Only display the final answer once the iterative procedures conclude.
Determine which assertion correctly fits in place of <AssertPlaceHolder> in the following code.
Provide only the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nReminder: This task involves several rounds of iterative reasoning. Only present the final assertion once all rounds are complete."
    ),
    HumanMessagePromptTemplate.from_template(
        "Once complete, print ###FINISHED### together with your final assertion."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

──────────────────────────── Variation 8 ────────────────────────────
assert_generation_template_tree_of_thought_8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Tackle the problem by breaking it into a number of consecutive reasoning steps. For each step, produce and assess various assertions meant to replace the placeholder, then choose the next reasoning direction accordingly. Only output the conclusive answer when all steps are finalized.
Identify the valid assertion to replace <AssertPlaceHolder> in the code below.
Supply solely the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nNotice: The task will undergo a series of iterations with step-by-step reasoning. Only show the final assertion after the entire process is finished."
    ),
    HumanMessagePromptTemplate.from_template(
        "Upon completion, include ###FINISHED### with your final assertion statement."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

──────────────────────────── Variation 9 ────────────────────────────
assert_generation_template_tree_of_thought_9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Analyze the problem by dividing it into several methodical reasoning steps. During each step, propose and evaluate different assertions to take over the placeholder, then decide on the most promising path to follow. Only print the final answer when the iterative process is finalized.
Specify the assertion that should correctly replace <AssertPlaceHolder> in the subsequent code.
Return only the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nFYI: The process will include multiple iterations with steps of reasoning. Only output the final assertion after completing the entire iterative procedure."
    ),
    HumanMessagePromptTemplate.from_template(
        "When done, output ###FINISHED### alongside your final assertion."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

──────────────────────────── Variation 10 ────────────────────────────
assert_generation_template_tree_of_thought_10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Break the problem into a chain of reasoning steps. At each step, generate potential assertion options to supplant the placeholder and critically assess them to choose the appropriate path. Only disclose the final answer when the entire iterative sequence is complete.
Identify the right assertion to substitute for <AssertPlaceHolder> in the provided code.
Present solely the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nNote: This assignment consists of several iterative steps with intermediate logic. Only present the final assertion after all iterations are completed."
    ),
    HumanMessagePromptTemplate.from_template(
        "Once finished, produce ###FINISHED### alongside your final assertion."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

──────────────────────────── Variation 11 ────────────────────────────
assert_generation_template_tree_of_thought_11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Deconstruct the issue into a series of logical reasoning steps. For every step, develop and assess several assertion options to replace the placeholder, and pick the subsequent reasoning trajectory. Only produce the final result when the series of iterations is done.
Determine the correct assertion that should replace <AssertPlaceHolder> in the code segment below.
Offer just the assertion line.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nReminder: This task will proceed in multiple iterative stages with progressive reasoning. Only output the final assertion after all stages are complete."
    ),
    HumanMessagePromptTemplate.from_template(
        "When you have finished, append ###FINISHED### with your final assertion."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

──────────────────────────── Variation 12 ────────────────────────────
assert_generation_template_tree_of_thought_12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Divide the challenge into an ordered series of reasoning steps. In each step, generate potential assertions to fill the placeholder and evaluate them thoroughly, then decide which reasoning avenue to pursue. Reveal the final answer only once the full process is complete.
Identify which assertion correctly substitutes <AssertPlaceHolder> in the code snippet.
Return only the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nAttention: The task will be solved through several iterations that include interim reasoning. Only output your final assertion when all iterations have been executed."
    ),
    HumanMessagePromptTemplate.from_template(
        "When complete, show ###FINISHED### alongside the final assertion."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

──────────────────────────── Variation 13 ────────────────────────────
assert_generation_template_tree_of_thought_13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Segment the problem into distinct logical steps. In every step, generate possible assertions to stand in for the placeholder and assess them to choose the optimal reasoning track. Only output the end result once your iterative reasoning is fully complete.
Ascertain the correct assertion to replace <AssertPlaceHolder> in the code provided.
Show only the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nNotice: This task involves multiple rounds of iterative reasoning. Only display the final assertion after every iteration is finished."
    ),
    HumanMessagePromptTemplate.from_template(
        "After completion, present ###FINISHED### with your final assertion."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

──────────────────────────── Variation 14 ────────────────────────────
assert_generation_template_tree_of_thought_14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Handle the problem by dividing it into multiple reasoning phases. At each phase, create and evaluate candidate assertions for the placeholder, then determine which reasoning thread to follow. Only reveal the final answer when the complete iterative sequence has been executed.
Choose the appropriate assertion to fill in for <AssertPlaceHolder> in the code below.
Submit exclusively the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nFYI: The problem requires multiple iterations with step-by-step reasoning. Only output the concluding assertion once every iteration is finalized."
    ),
    HumanMessagePromptTemplate.from_template(
        "When done, include ###FINISHED### alongside the final assertion."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

Each variant preserves the original structure and AI message while offering fresh wording for the system and human instructions.
