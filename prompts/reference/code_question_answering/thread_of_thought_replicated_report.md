

────────────────────────────
Variation 0:
────────────────────────────
code_question_answering_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Walk me through the question and the code in manageable parts, summarizing and analyzing as we go.
Then, assess whether the provided code correctly answers the question.
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

────────────────────────────
Variation 1:
────────────────────────────
code_question_answering_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Dissect the question and its code step by step, offering summaries and insights along the way.
Then, determine whether the given code effectively answers the question.
Answer solely with ###TRUE### if it completely meets the requirements, or with ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Problem:
{question}

Source Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 2:
────────────────────────────
code_question_answering_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Guide me through the question along with the code by breaking them into clear segments, providing brief summaries and analysis as you progress.
Then, decide if the provided code fully addresses the question.
Reply with only ###TRUE### if it does, or with ###FALSE### otherwise.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Query:
{question}

Software Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 3:
────────────────────────────
code_question_answering_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Please break down the question and the accompanying code into digestible parts, adding concise summaries and evaluations as you go.
Subsequently, evaluate if the code properly resolves the question.
Return solely ###TRUE### if it completely does so, or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Inquiry:
{question}

Program:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 4:
────────────────────────────
code_question_answering_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Elaborate on the question and its code by segmenting them into systematic parts, while providing concise summaries and analysis.
Then, verify whether the code completely answers the question.
Output only ###TRUE### if it does, or ###FALSE### if not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task:
{question}

Coding Implementation:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 5:
────────────────────────────
code_question_answering_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Analyze the question and the code sequentially, summarizing and highlighting key points along the way.
Then, judge if the code fully addresses the question.
Respond exclusively with ###TRUE### if it meets the criteria or with ###FALSE### if it falls short.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question Details:
{question}

Code Snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 6:
────────────────────────────
code_question_answering_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Step through the problem and its associated code piece by piece, offering summaries and critical analysis as you proceed.
Then, decide if the code adequately solves the query.
Answer only with ###TRUE### if it does entirely, or with ###FALSE### otherwise.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Problem Statement:
{question}

Code Provided:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 7:
────────────────────────────
code_question_answering_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Examine the question and the code in sequential segments, providing short summaries and evaluative comments throughout.
Then, assess whether the code effectively resolves the question.
Provide a response of only ###TRUE### if successful, or ###FALSE### if not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question Summary:
{question}

Code Example:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 8:
────────────────────────────
code_question_answering_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Walk through the query and its corresponding code in clear, step-by-step segments while offering brief evaluations and summaries.
Then, confirm if the code serves as a proper answer to the question.
Respond solely with ###TRUE### when it does, or with ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 9:
────────────────────────────
code_question_answering_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Step through the inquiry and its related code by breaking them into manageable parts, and provide succinct summaries and analysis.
Then, verify whether the code meets the requirements of the question.
Return only ###TRUE### if it does, otherwise return ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Problem:
{question}

Implementation:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 10:
────────────────────────────
code_question_answering_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Deconstruct the question and the provided code piece into logical sections, offering a summary and analysis for each part as you proceed.
Then, determine if the code answers the question completely.
Answer exclusively with ###TRUE### if it does, or with ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Prompt:
{question}

Program Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 11:
────────────────────────────
code_question_answering_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Methodically break down the question along with its code into clear steps, summarizing and providing analysis throughout.
Then, decide if the code entirely resolves the query.
Respond only with ###TRUE### for full correctness or with ###FALSE### if it does not meet the criteria.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Scenario:
{question}

Script:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 12:
────────────────────────────
code_question_answering_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Divide the question and its corresponding code into clear segments, providing brief summaries and evaluations for each section.
After this, determine whether the code fully addresses the query.
Reply solely with ###TRUE### if it does, or with ###FALSE### if it falls short.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Query Details:
{question}

Code Block:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 13:
────────────────────────────
code_question_answering_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Walk through the details of the question and its provided code in sequential segments, offering concise summaries and insights.
Then, ascertain if the code correctly answers the question.
Return only ###TRUE### upon complete success or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question Data:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 14:
────────────────────────────
code_question_answering_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Guide your analysis by reviewing the question and its accompanying code section by section, providing concise summaries and critiques.
Then, evaluate whether the code adequately answers the question.
Output only ###TRUE### if it fulfills the requirements, or output ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question Information:
{question}

Code Details:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
