variation 0:
code_question_answering_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before answering, work through your reasoning process. For example:
Incorrect reasoning: "Assuming the code is correct based on a partial evaluation."
Correct reasoning: "Carefully reviewing every aspect of the code to determine whether it fully answers the question."
Assess whether the following code correctly answers the question.
Provide only ###TRUE### if the code fully satisfies the query or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

variation 1:
code_question_answering_template_contrastive_cot_variation1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before delivering your answer, walk through your thought process step by step. For instance:
Faulty logic: "Believing the code is correct based on a superficial check."
Sound logic: "Examining every component of the code meticulously to confirm it fully answers the question."
Decide if the given code completely meets the question’s requirements.
Respond with only ###TRUE### if it does, or ###FALSE### otherwise.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

variation 2:
code_question_answering_template_contrastive_cot_variation2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before providing your answer, detail your reasoning process. For example:
Imprecise approach: "Concluding the code is correct after a brief check."
Accurate approach: "Evaluating every part of the code thoroughly to establish that it completely addresses the query."
Judge whether the code fully solves the question.
Return only ###TRUE### if it does, and ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Inquiry:
{question}

Script:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

variation 3:
code_question_answering_template_contrastive_cot_variation3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before answering, outline the reasoning steps involved. Consider these examples:
Poor reasoning: "Assuming validity of the code from a cursory glance."
Robust reasoning: "Carefully checking every detail of the code to ensure it meets the question's criteria."
Decide if the presented code completely satisfies the query.
Answer only with ###TRUE### if it does, or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Query:
{question}

Program:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

variation 4:
code_question_answering_template_contrastive_cot_variation4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you provide an answer, explain your reasoning process in detail. For example:
Suboptimal reasoning: "Assuming the correctness of the code based on a limited look."
Optimal reasoning: "Reviewing each line of code carefully to confirm it fully addresses the question."
Evaluate whether the code meets the problem requirements.
Output solely ###TRUE### if it meets them completely, or ###FALSE### otherwise.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Problem:
{question}

Source:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

variation 5:
code_question_answering_template_contrastive_cot_variation5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Prior to answering, delineate your logical steps. For instance:
Faulty evaluation: "Assuming the code works correctly after a brief inspection."
Correct evaluation: "Scrutinizing every segment of the code to confirm it answers every part of the question."
Determine if the code completely addresses the query.
Respond with only ###TRUE### if it does, or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

variation 6:
code_question_answering_template_contrastive_cot_variation6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before presenting your answer, systematically detail your reasoning process. For example:
Flawed analysis: "Judging the code based only on a partial review."
Sound analysis: "Inspecting every detail of the code to verify it thoroughly answers the question."
Check if the provided code fully resolves the query.
Return exclusively ###TRUE### when it does, otherwise ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Inquiry:
{question}

Program Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

variation 7:
code_question_answering_template_contrastive_cot_variation7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you answer, ensure that your reasoning steps are clearly laid out. For instance:
Incorrect analysis: "Concluding that the code is correct after an incomplete verification."
Correct analysis: "Reviewing all parts of the code to ensure it thoroughly meets the question’s demands."
Determine if the code answers the question in full.
Provide only ###TRUE### if it does, or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code Provided:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

variation 8:
code_question_answering_template_contrastive_cot_variation8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you offer your answer, explain your reasoning in detail. For example:
Weak reasoning: "Relying on a quick check to assume the code is correct."
Strong reasoning: "Analyzing every aspect of the code carefully to ensure it completely satisfies the question."
Assess whether the code fully meets the inquiry.
Answer with only ###TRUE### if the condition is met or ###FALSE### if not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Query:
{question}

Code Snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

variation 9:
code_question_answering_template_contrastive_cot_variation9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Prior to responding, articulate your detailed thought process. For example:
Insufficient reasoning: "Assuming the code's validity from a quick overview."
Thorough reasoning: "Examining every detail of the code to ensure it completely addresses the question."
Evaluate if the provided code fully satisfies the query.
Return solely ###TRUE### if it meets all requirements, or ###FALSE### otherwise.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Implementation:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

variation 10:
code_question_answering_template_contrastive_cot_variation10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before answering, outline your reasoning process step by step. For example:
Erroneous approach: "Assuming the code works based on limited inspection."
Accurate approach: "Methodically checking every line of code to ensure it fully addresses the question."
Decide if the presented code fully meets the requirements.
Reply with only ###TRUE### if it does, or with ###FALSE### otherwise.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Problem Statement:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

variation 11:
code_question_answering_template_contrastive_cot_variation11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before offering an answer, detail your full reasoning process. For instance:
Faulty deduction: "Assuming code correctness after only a partial review."
Correct deduction: "Inspecting the entire code to confirm it holistically answers the query."
Determine if the code completely addresses the question.
Return solely ###TRUE### if it does, otherwise respond with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Inquiry:
{question}

Code Sample:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

variation 12:
code_question_answering_template_contrastive_cot_variation12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you formulate your final answer, explain your reasoning step by step. For example:
Inadequate reasoning: "Assuming that a brief review validates the code."
Comprehensive reasoning: "Thoroughly analyzing each element of the code to determine its full compliance with the question."
Assess whether the code completely meets the query.
Respond with only ###TRUE### if it does, or with ###FALSE### if any part is missing.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

variation 13:
code_question_answering_template_contrastive_cot_variation13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you provide your response, map out your reasoning process in detail. For example:
Misguided reasoning: "Assuming correctness after a cursory glance at the code."
Sound reasoning: "Evaluating every detail of the code to verify that it fully satisfies the requirements of the question."
Decide if the code as provided fully resolves the query.
Answer only with ###TRUE### if complete, otherwise answer with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

variation 14:
code_question_answering_template_contrastive_cot_variation14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before responding, walk through your complete thought process. For example:
Insufficient logic: "Inferring the code works based on a superficial check."
Robust logic: "Reviewing every component of the code to confirm it thoroughly answers the question."
Examine whether the code fully satisfies the question.
Provide only the output ###TRUE### if the code completely meets the query, or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Prompt:
{question}

Code Extract:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])