Below are 15 versions of the original prompt template. Variation 0 is the original, and variations 1–14 contain rephrased versions of the strings in the SystemMessagePromptTemplate and HumanMessagePromptTemplate (the AIMessagePromptTemplate remains unchanged).

------------------------------------------------------------
variation 0 (original):
------------------------------------------------------------
code_generation_template_rar_v3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Generate code for the following task. Provide the code only.
Restate the prompt with additional details, then supply the generated code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Description:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

------------------------------------------------------------
variation 1:
------------------------------------------------------------
code_generation_template_rar_v3_variation_1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Develop code for the given task. Output only the code.
Paraphrase the task prompt with further elaboration, then present the generated code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Details:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

------------------------------------------------------------
variation 2:
------------------------------------------------------------
code_generation_template_rar_v3_variation_2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Produce code that addresses the following task. Return solely the code.
Rewrite the prompt by adding extra insights before delivering the resulting code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Summary:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

------------------------------------------------------------
variation 3:
------------------------------------------------------------
code_generation_template_rar_v3_variation_3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Write a solution in code for the task described below. Provide only the code.
Expand on the prompt with additional specifics, then include the produced code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Description of Task:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

------------------------------------------------------------
variation 4:
------------------------------------------------------------
code_generation_template_rar_v3_variation_4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Generate a code solution for the subsequent task. Supply only the code.
Reframe the prompt with added context before displaying the final code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Outline:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

------------------------------------------------------------
variation 5:
------------------------------------------------------------
code_generation_template_rar_v3_variation_5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Create code that fulfills the following assignment. Return code exclusively.
Clarify the prompt with extra descriptors before outputting the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Assignment Details:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

------------------------------------------------------------
variation 6:
------------------------------------------------------------
code_generation_template_rar_v3_variation_6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Compose code to solve the task below. Provide only the code output.
Rephrase the prompt with supplementary details and then offer the generated code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Assignment Description:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

------------------------------------------------------------
variation 7:
------------------------------------------------------------
code_generation_template_rar_v3_variation_7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Craft a code implementation for the subsequent challenge. Only output the code.
Restate the provided prompt with further details, then deliver the resulting code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Challenge Description:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

------------------------------------------------------------
variation 8:
------------------------------------------------------------
code_generation_template_rar_v3_variation_8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Formulate code for the task outlined below. Present the code only.
Restate and elaborate on the prompt with additional specifics before showing the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Brief:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

------------------------------------------------------------
variation 9:
------------------------------------------------------------
code_generation_template_rar_v3_variation_9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Write code addressing the following problem. Return just the code.
Rephrase the task prompt by including further context, then provide the generated code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Problem Details:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

------------------------------------------------------------
variation 10:
------------------------------------------------------------
code_generation_template_rar_v3_variation_10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Develop a code snippet for the task provided. Output only the pure code.
Enhance the prompt with additional details before presenting the generated code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Problem Statement:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

------------------------------------------------------------
variation 11:
------------------------------------------------------------
code_generation_template_rar_v3_variation_11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Construct code for solving the following task. Deliver only the code.
Paraphrase the prompt with extra elaboration before supplying the generated code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Information:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

------------------------------------------------------------
variation 12:
------------------------------------------------------------
code_generation_template_rar_v3_variation_12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Assemble code to fulfill the task below. Return only the code.
Restate the prompt with additional context, then include the final code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Narrative:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

------------------------------------------------------------
variation 13:
------------------------------------------------------------
code_generation_template_rar_v3_variation_13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Generate programming code for the task specified below. Provide code exclusively.
Reframe the prompt with enhanced details before showing the finalized code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Overview:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

------------------------------------------------------------
variation 14:
------------------------------------------------------------
code_generation_template_rar_v3_variation_14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Create a code solution for the task listed below. Output exclusively the code.
Elaborate on the prompt with thorough details prior to delivering the final code solution.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Explanation:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
