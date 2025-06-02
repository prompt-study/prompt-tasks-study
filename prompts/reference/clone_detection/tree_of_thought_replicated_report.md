
────────────────────────
Variation 0:
────────────────────────
clone_detection_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''To solve the problem, break it down into multiple reasoning steps. For each potential step, explore different ways to assess whether the two code snippets are functionally equivalent, and decide which thought path to continue. Only output the final answer when the iterative process is complete.
Determine if the two code snippets are clones.
Answer with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Snippet 1:
{code_snippet1}

Code Snippet 2:
{code_snippet2}

Note: This task will undergo multiple iterations with intermediate reasoning. Only output the final answer once all iterations are complete.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "When finished, output ###FINISHED### alongside your final answer (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

────────────────────────
Variation 1:
────────────────────────
clone_detection_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Begin by decomposing the task into several logical steps. For every step you consider, evaluate various approaches to verify if the two provided code samples work the same, and choose the reasoning branch to follow. Only provide your final answer once the complete iterative process is done.
Decide if the two code samples are clones.
Respond with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Snippet One:
{code_snippet1}

Snippet Two:
{code_snippet2}

Reminder: This challenge involves several rounds of intermediate reasoning. Only submit your final answer after completing every step.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Upon completion, include ###FINISHED### along with your final answer (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

────────────────────────
Variation 2:
────────────────────────
clone_detection_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Approach this problem by splitting it into distinct reasoning phases. In each phase, consider multiple methods to determine if the two code segments function identically, and then select which line of thought to follow. Only emit the final result when the whole iterative reasoning is finished.
Assess whether the two code segments are clones.
Provide your answer as ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''First Code Block:
{code_snippet1}

Second Code Block:
{code_snippet2}

Note: The task will progress through several iterations with step-by-step reasoning. Provide only your final answer once every iteration is complete.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Once all steps are done, present ###FINISHED### together with your final answer (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

────────────────────────
Variation 3:
────────────────────────
clone_detection_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Deconstruct the challenge into multiple sequential reasoning steps. In each step, investigate different methods to check if the two code examples behave equivalently, and choose the subsequent line of reasoning accordingly. Only reveal the final decision after all iterations are complete.
Determine if these two code examples are clones.
Answer strictly with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Example Code 1:
{code_snippet1}

Example Code 2:
{code_snippet2}

Remember: This exercise will be conducted through several iterative reasoning rounds. Only deliver the final answer after every cycle is finished.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "When your analysis is complete, include ###FINISHED### together with your final answer (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

────────────────────────
Variation 4:
────────────────────────
clone_detection_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Solve the problem by breaking it into several reasoning steps. For each step, examine various approaches to decide if the provided code snippets are functionally identical, and then pick the best reasoning pathway. Do not output your final answer until the entire iterative process is complete.
Verify if the two code snippets are clones.
Respond with either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Example A:
{code_snippet1}

Code Example B:
{code_snippet2}

Note: This task is designed to involve multiple iterations with progressive reasoning. Only output your final decision after all reasoning steps have been executed.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "After completion, provide ###FINISHED### along with your final determination (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

────────────────────────
Variation 5:
────────────────────────
clone_detection_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Tackle the problem by segmenting it into several reasoning phases. Consider different ways in each phase to evaluate if the two snippets produce the same behavior, and then decide which analytical path to pursue. Only emit the final answer after all iterations are finished.
Conclude if the two code snippets are clones.
Your answer should be either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Source Code 1:
{code_snippet1}

Source Code 2:
{code_snippet2}

Note: This task will pass through several iterative reasoning rounds. Submit your final answer only after completing every iteration.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Once done, output ###FINISHED### together with your final answer (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

────────────────────────
Variation 6:
────────────────────────
clone_detection_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Address the problem by dividing it into a series of logical reasoning steps. For each step, investigate various methods to determine whether the two code fragments are equivalent in function, and then decide which line of thought to advance. Only reveal your final answer when the iterative investigation is complete.
Establish if the two code fragments are clones.
Answer with either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Block of Code 1:
{code_snippet1}

Block of Code 2:
{code_snippet2}

Reminder: This assignment will involve iterative rounds of reasoning. Only present your final answer after every iteration has been finalized.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "At the conclusion, output ###FINISHED### together with your final answer (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

────────────────────────
Variation 7:
────────────────────────
clone_detection_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Approach this challenge by partitioning it into successive reasoning steps. For each step, review several strategies to check if the two pieces of code exhibit identical functionality, and choose which thought process to pursue further. Only produce the final answer upon completing the full iterative sequence.
Decide if the two pieces of code are clones.
Output your answer as either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Program Segment 1:
{code_snippet1}

Program Segment 2:
{code_snippet2}

Note: The task will proceed with multiple iterations accompanied by intermediate analysis. Only provide your final answer once every iteration is done.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "When all iterations are complete, include ###FINISHED### with your final answer (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

────────────────────────
Variation 8:
────────────────────────
clone_detection_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Resolve the problem by breaking it into a chain of reasoning steps. At each step, consider several alternatives to determine if the two code sections function similarly, and then select the pathway for further analysis. Only share the final answer once the full iterative process is concluded.
Determine whether the two code sections are clones.
Respond with either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Snippet 1 Details:
{code_snippet1}

Snippet 2 Details:
{code_snippet2}

Keep in mind: This exercise will involve a series of iteration rounds with intermediate insights. Please output your final answer only after all rounds are finished.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Once finished, state ###FINISHED### along with your final answer (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

────────────────────────
Variation 9:
────────────────────────
clone_detection_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Break the problem into several clear reasoning phases. At each phase, explore different possibilities to check if the two given code samples perform equivalently, and decide which reasoning avenue to follow next. Only produce your final output once the entire iterative process is complete.
Assess if the two provided code samples are clones.
Answer solely with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Section 1:
{code_snippet1}

Code Section 2:
{code_snippet2}

Note: This task will progress through multiple iterations, each with its own reasoning. Ensure that you only emit the final answer after completing all iterations.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "When you are finished, output ###FINISHED### together with your final answer (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

────────────────────────
Variation 10:
────────────────────────
clone_detection_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Dissect the problem into several individual reasoning steps. In each step, review various methods to verify if the two snippets are functionally the same, and then determine the next reasoning path to adopt. Only disclose your final answer when every iterative step is finalized.
Decide if the two snippets are clones.
Your response should be either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Example 1:
{code_snippet1}

Code Example 2:
{code_snippet2}

Reminder: This exercise is structured into multiple rounds of reasoning. Only reveal your final answer after the completion of all rounds.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "After finishing the process, include ###FINISHED### with your final answer (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

────────────────────────
Variation 11:
────────────────────────
clone_detection_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Divide the problem into a series of analytical steps. In every step, consider several strategies to verify if the given code snippets exhibit the same behavior, and then choose the appropriate line of reasoning to continue with. Only reveal the final answer after the iterative process is entirely complete.
Check if the two code snippets are clones.
Answer exclusively with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Segment 1:
{code_snippet1}

Segment 2:
{code_snippet2}

Note: The task will proceed with multiple iterations, each involving intermediate reasoning. Ensure that you provide your final answer only after all iterations are finalized.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Once complete, output ###FINISHED### with your final answer (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

────────────────────────
Variation 12:
────────────────────────
clone_detection_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Attack the problem by splitting it into several stages of reasoning. At each stage, inspect different possibilities for verifying if the two code fragments are functionally identical, and select which reasoning route to continue down. Only provide your final answer after the complete iterative analysis.
Evaluate if the two code fragments are clones.
Respond with either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Version 1:
{code_snippet1}

Code Version 2:
{code_snippet2}

Note: This problem will be solved over multiple iteration rounds with step-by-step reasoning. Submit your final answer only after the entire process is complete.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Upon finishing, output ###FINISHED### along with your final answer (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

────────────────────────
Variation 13:
────────────────────────
clone_detection_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Resolve the issue by partitioning it into several logical steps. For each step, examine different techniques to assess if the two code blocks yield equivalent functionality, then decide which trail of thought to pursue. Only reveal your final decision when the complete iterative procedure has been concluded.
Verify whether the two code blocks are clones.
Answer using either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Block One:
{code_snippet1}

Code Block Two:
{code_snippet2}

Note: This task involves several rounds of reasoning. Please provide your final answer only after every iteration has been completed.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Once finished, output ###FINISHED### accompanied by your final answer (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

────────────────────────
Variation 14:
────────────────────────
clone_detection_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Break down the challenge into a series of reasoning segments. In each segment, deliberate on different methods to determine if the two pieces of code are functionally identical, and then select the reasoning path to follow next. Only present the final determination once the entire iterative process is complete.
Conclude if the two pieces of code are clones.
Your final output should be either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Programming Snippet 1:
{code_snippet1}

Programming Snippet 2:
{code_snippet2}

Note: This exercise will proceed with several iterative reasoning rounds. Only output your final answer after all iterations are completed.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "After all iterations, include ###FINISHED### with your final answer (either ###TRUE### or ###FALSE###)."
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])

