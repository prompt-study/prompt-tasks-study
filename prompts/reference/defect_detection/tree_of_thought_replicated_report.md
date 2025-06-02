Below is the full prompt template structure. Variation zero is exactly the original template you provided, and variations 1–14 are rephrased versions. Note that only the text strings inside SystemMessagePromptTemplate and HumanMessagePromptTemplate have been reworded; the AIMessagePromptTemplate remains unchanged.

──────────────────────────────
Variation 0 (Original):
──────────────────────────────
defect_detection_template_tree_of_thought_var0 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''To solve the problem, break it down into multiple reasoning steps. For each potential step, generate intermediate thoughts, evaluate their contribution, and decide which thought path to continue. Only output the final answer when the iterative process is complete.
Determine if there is a defect in the code.
Reply with ###TRUE### or ###FALSE### only.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nNote: This task will undergo multiple iterations with intermediate reasoning. Only output the final answer once all iterations are complete."
    ),
    HumanMessagePromptTemplate.from_template(
        "When finished, output ###FINISHED### alongside your final answer (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

──────────────────────────────
Variation 1:
──────────────────────────────
defect_detection_template_tree_of_thought_var1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Break the problem into several reasoning stages. In each stage, produce provisional thoughts, assess their merit, and choose the most promising trajectory to follow. Only present the final answer when your reasoning is fully complete.
Check whether the code contains a defect.
Answer exclusively with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nKeep in mind: This task will be tackled over several iterations with step-by-step reasoning. Provide your final answer only after all rounds are finished."
    ),
    HumanMessagePromptTemplate.from_template(
        "Upon finishing, output ###FINISHED### alongside your final answer (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

──────────────────────────────
Variation 2:
──────────────────────────────
defect_detection_template_tree_of_thought_var2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Approach the problem by segmenting it into distinct phases of reasoning. For every phase, outline intermediate ideas, evaluate their impact, and select the line of thought to pursue further. Only reveal your final answer when all phases are complete.
Determine if the code exhibits any defect.
Respond solely with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nReminder: This task involves multiple iterative steps with progressive reasoning. Provide the final answer only after every iteration is concluded."
    ),
    HumanMessagePromptTemplate.from_template(
        "After completing all iterations, output ###FINISHED### along with your final answer (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

──────────────────────────────
Variation 3:
──────────────────────────────
defect_detection_template_tree_of_thought_var3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Dissect the problem into a sequence of reasoning steps. For each step, develop intermediate insights, assess their effectiveness, and decide which reasoning path to continue. Only disclose your final answer once the entire process is complete.
Verify whether the code contains a defect.
Reply strictly with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nNote: The task will proceed through multiple cycles of intermediate reasoning. Provide your final answer only after all reasoning steps have been executed."
    ),
    HumanMessagePromptTemplate.from_template(
        "When complete, output ###FINISHED### along with your final answer (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

──────────────────────────────
Variation 4:
──────────────────────────────
defect_detection_template_tree_of_thought_var4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''To address the challenge, decompose it into sequential reasoning steps. In each step, articulate preliminary thoughts, evaluate their significance, and select the most viable route before moving on. Provide the final answer only upon completing the entire iterative process.
Determine if the code has any fault.
Respond with only ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nRemember: This task is designed for iterative reasoning through multiple stages. Submit the final answer only after all steps are finalized."
    ),
    HumanMessagePromptTemplate.from_template(
        "After finishing, please output ###FINISHED### together with your final result (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

──────────────────────────────
Variation 5:
──────────────────────────────
defect_detection_template_tree_of_thought_var5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Solve the problem by dividing it into discrete reasoning segments. For each segment, generate progressive thoughts, evaluate their relevance, and determine which path to extend. Only provide the final answer after the complete iterative analysis is concluded.
Ascertain whether the provided code is defective.
Answer exclusively with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nCaution: This task unfolds over several iterative rounds with intermediate steps. Deliver the final answer only after all rounds are completed."
    ),
    HumanMessagePromptTemplate.from_template(
        "When done, include ###FINISHED### alongside your final verdict (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

──────────────────────────────
Variation 6:
──────────────────────────────
defect_detection_template_tree_of_thought_var6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Approach this problem by splitting it into several reasoning steps. At each step, generate intermediate notions, assess their validity, and select the line of reasoning to proceed with. Only reveal the final answer after the entire process is complete.
Establish if a defect is present in the code.
Reply solely with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nPlease note: This task demands iterative reasoning across multiple steps. Provide the final answer only once all steps have been evaluated."
    ),
    HumanMessagePromptTemplate.from_template(
        "Once finished, output ###FINISHED### together with your final answer (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

──────────────────────────────
Variation 7:
──────────────────────────────
defect_detection_template_tree_of_thought_var7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Address the problem by partitioning it into several phases of reasoning. For each phase, craft intermediate thoughts, examine their importance, and pick the pathway to follow. Only disclose your final answer at the end of all iterative cycles.
Check for any defects in the code.
Respond only with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nReminder: This assignment consists of multiple rounds of iterative reasoning. Your final answer should be provided only after all rounds are completed."
    ),
    HumanMessagePromptTemplate.from_template(
        "After all work is done, output ###FINISHED### along with your final decision (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

──────────────────────────────
Variation 8:
──────────────────────────────
defect_detection_template_tree_of_thought_var8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Tackle this problem by breaking it into a series of reasoning steps. In each step, develop intermediate reflections, evaluate their usefulness, and choose the optimal path. Only share the final answer once the iterative process has concluded.
Determine whether the code shows any defect.
Answer exclusively with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nNote: This task is structured to use multiple iterations with intermediate reasoning. Provide your final answer only after completing all iterations."
    ),
    HumanMessagePromptTemplate.from_template(
        "Upon completion, output ###FINISHED### along with your final answer (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

──────────────────────────────
Variation 9:
──────────────────────────────
defect_detection_template_tree_of_thought_var9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Methodically fragment the problem into several reasoning stages. At every stage, generate partial thoughts, evaluate their contributions, and select the most effective reasoning path. Only offer the final answer after the entire process is done.
Decide if the code has a defect.
Reply solely with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nPlease note: This task requires iterative reasoning through distinct stages. Provide the final answer only when all stages are complete."
    ),
    HumanMessagePromptTemplate.from_template(
        "At the end, output ###FINISHED### alongside your final answer (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

──────────────────────────────
Variation 10:
──────────────────────────────
defect_detection_template_tree_of_thought_var10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Deconstruct the problem into progressive reasoning steps. For each step, generate initial insights, assess their value, and then determine the next reasoning route. Only submit the final answer after the complete iterative process is executed.
Examine whether the code is flawed.
Reply only with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nTake note: This challenge involves multiple iterative steps with interim reasoning. Provide your final answer only after all steps have been finalized."
    ),
    HumanMessagePromptTemplate.from_template(
        "Once finished, print ###FINISHED### along with your final response (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

──────────────────────────────
Variation 11:
──────────────────────────────
defect_detection_template_tree_of_thought_var11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Analyze the problem by breaking it into distinct reasoning phases. In every phase, produce intermediate thoughts, evaluate their significance, and pick the reasoning path to advance. Only share your final answer once the entire iterative process is complete.
Determine whether the code is defective.
Answer exclusively with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nKeep in mind: This task involves several iterative phases of reasoning. Provide your final answer only after all phases have been addressed."
    ),
    HumanMessagePromptTemplate.from_template(
        "Upon completion, output ###FINISHED### together with your final answer (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

──────────────────────────────
Variation 12:
──────────────────────────────
defect_detection_template_tree_of_thought_var12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Tackle the problem by dividing it into a series of reasoning steps. At each step, generate and appraise intermediate ideas, and decide which direction to follow next. Only deliver your final answer when every step in the process is complete.
Verify whether a defect exists in the code.
Respond solely with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nNote: This problem will be resolved via multiple rounds of intermediate reasoning. Provide your final answer only after every round is finished."
    ),
    HumanMessagePromptTemplate.from_template(
        "When finished, attach ###FINISHED### to your final answer (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

──────────────────────────────
Variation 13:
──────────────────────────────
defect_detection_template_tree_of_thought_var13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Solve the challenge by segmenting it into several reasoning steps. At each stage, formulate intermediate conclusions, assess their strengths, and choose which reasoning path to extend. Provide the final answer only after finishing the complete iterative process.
Ascertain if the code contains errors.
Respond strictly with either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nImportant: This challenge will be addressed through multiple iterations of reasoning. Only supply the final answer when all iterations have been completed."
    ),
    HumanMessagePromptTemplate.from_template(
        "Upon finishing, output ###FINISHED### along with your final decision (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

──────────────────────────────
Variation 14:
──────────────────────────────
defect_detection_template_tree_of_thought_var14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Approach this challenge by splitting it into distinct reasoning steps. For each step, express intermediate insights, evaluate their effectiveness, and select the best path for continued reasoning. Only release your final answer when the iterative process is fully complete.
Judge whether the code has any flaws.
Reply exclusively with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "{code}\n\nSide note: This challenge will progress through several iterations emphasizing intermediate reasoning. Provide your final answer only after all iterations are complete."
    ),
    HumanMessagePromptTemplate.from_template(
        "Once you are finished, output ###FINISHED### alongside your final answer (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

Each of these 15 templates preserves the original prompting structure while providing distinct wording within the system and human instructions.