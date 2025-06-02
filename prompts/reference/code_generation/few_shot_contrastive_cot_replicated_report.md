Below you will find the original template (labeled variation zero) followed by 14 additional versions. In each, only the strings for the SystemMessagePromptTemplate and HumanMessagePromptTemplate have been rephrased while the AIMessagePromptTemplate remains intact.

──────────────────────────────────────────────
Variation 0 (original):

code_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before answering, work through your reasoning process. For example:
Incorrect reasoning: "Generating code based on vague interpretations that may lead to inefficient or non-functional solutions."
Correct reasoning: "Thoroughly understanding the task requirements and writing clear, functional code that meets the specifications."
Write code for the following task.
Provide only the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Description:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────────────────────
Variation 1:

code_generation_template_contrastive_cot_variation_1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before providing an answer, carefully outline your thought process. For example:
Faulty approach: "Writing code based on uncertain assumptions that could result in inefficient or non-working solutions."
Ideal approach: "Deeply comprehending the task details and producing well-organized, working code that fulfills the requirements."
Now, write the code for the task.
Return only the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Info:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────────────────────
Variation 2:

code_generation_template_contrastive_cot_variation_2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Prior to answering, detail your internal reasoning. For example:
Incorrect method: "Drafting code from vague interpretations that might yield subpar or broken functionality."
Correct method: "Analyzing the task requirements thoroughly and coding clearly to meet the specified goals."
Write code for the following task.
Provide only the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Details:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────────────────────
Variation 3:

code_generation_template_contrastive_cot_variation_3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you respond, walk through your reasoning. For example:
Ineffective reasoning: "Generating code based on imprecise assumptions could produce inefficient results."
Effective reasoning: "Thoroughly examining the task specifics and creating precise, executable code."
Write the code needed for the task.
Return solely the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Details:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────────────────────
Variation 4:

code_generation_template_contrastive_cot_variation_4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before answering, articulate your reasoning process. For instance:
Poor approach: "Creating code based on a limited understanding might result in errors or inefficiencies."
Proper approach: "Examining the task carefully and writing intuitive, robust code that matches the specifications."
Now, write the code for the task.
Include only the code in your answer.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Overview:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────────────────────
Variation 5:

code_generation_template_contrastive_cot_variation_5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Prior to answering, reflect on your thought process. For instance:
Misguided reasoning: "Coding based on vague or incomplete analysis may lead to malfunctioning outputs."
Sound reasoning: "Fully understanding and dissecting the task requirements and then writing accurate, functional code."
Write the code for this task.
Return only the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Assignment Description:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────────────────────
Variation 6:

code_generation_template_contrastive_cot_variation_6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before delivering your answer, step through your reasoning. For example:
Faulty logic: "Developing code based on hazy interpretations may lead to bugs or inefficient solutions."
Solid logic: "Understanding the task completely and generating clear, error-free code that meets the objectives."
Write the code for the provided task.
Include only the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Assignment Details:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────────────────────
Variation 7:

code_generation_template_contrastive_cot_variation_7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before responding, outline your reasoning steps. For example:
Inadequate reasoning: "Jumping straight into code with an unclear direction may result in a flawed implementation."
Effective reasoning: "Analyzing every aspect of the task to produce concise, functional code."
Now, write the code for the task.
Return only the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Brief:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────────────────────
Variation 8:

code_generation_template_contrastive_cot_variation_8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before answering, explain your reasoning steps. For example:
Suboptimal reasoning: "Formulating code based on unclear insights may lead to inefficient or non-operational code."
Optimal reasoning: "Meticulously analyzing the task requirements and generating code that operates as intended."
Write the code for the given task.
Provide only the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Summary:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────────────────────
Variation 9:

code_generation_template_contrastive_cot_variation_9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Prior to responding, break down your thought process. For example:
Flawed approach: "Coding from an ambiguous understanding might lead to unreliable or inefficient solutions."
Correct approach: "Fully digesting the task and writing refined, reliable code that meets the specs."
Write the code for this task.
Return only the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Requirements:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────────────────────
Variation 10:

code_generation_template_contrastive_cot_variation_10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before answering, describe your internal reasoning. For example:
Inept approach: "Jumping into coding using vague interpretations can cause malfunctioning code."
Adept approach: "Thoroughly reviewing the task requirements to build clear, correct code."
Write the code for this task.
Return only the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Problem Description:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────────────────────
Variation 11:

code_generation_template_contrastive_cot_variation_11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before providing your answer, detail the reasoning behind it. For example:
Incomplete reasoning: "Generating code without a full understanding may result in buggy or slow solutions."
Complete reasoning: "Inspecting the task thoroughly to produce efficient and working code."
Write the code for the task.
Provide only the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Explanation:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────────────────────
Variation 12:

code_generation_template_contrastive_cot_variation_12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before answering, elucidate your reasoning process step by step. For example:
Limited reasoning: "Creating code without fully grasping the task could lead to issues or inefficiencies."
Comprehensive reasoning: "Evaluating the task details in-depth to write robust and functional code."
Write the code for the task.
Return only the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Narrative:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────────────────────
Variation 13:

code_generation_template_contrastive_cot_variation_13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before answering, articulate your chain of thought. For example:
Insufficient approach: "Attempting to generate code from only a superficial analysis might lead to errors."
Best approach: "Deeply examining the task requirements and constructing efficient, operational code."
Write the code for the task.
Include only the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Input:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────────────────────
Variation 14:

code_generation_template_contrastive_cot_variation_14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before responding, map out your reasoning clearly. For example:
Subpar reasoning: "Developing code based on a cursory understanding may lead to improper or ineffective outcomes."
Ideal reasoning: "Carefully reviewing the task requirements to design concise and functional code."
Write the code for the given task.
Return solely the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Data:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

Each of these 15 templates maintains the same operational structure—with only the system and human messages rephrased—to help study the impact of different prompt wordings while preserving the original task and prompt technique.