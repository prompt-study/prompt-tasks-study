
────────────────────────────
Variation 0:
────────────────────────────
code_question_answering_template_self_ask = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before answering, consider if any follow-up questions are needed to clarify the task. If so, ask and answer them before providing the final answer.
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

────────────────────────────
Variation 1:
────────────────────────────
code_question_answering_template_self_ask = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you respond, reflect on whether additional clarification through follow-up questions is needed. If clarification is required, both ask and address those queries before giving your final answer.
Evaluate if the provided code sufficiently answers the question.
Respond solely with ###TRUE### when it meets the requirements, or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question prompt:
{question}

Provided Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 2:
────────────────────────────
code_question_answering_template_self_ask = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Prior to answering, determine whether asking extra follow-up questions is necessary to fully understand the task. If it is, ask them and include the answers before your final response.
Check if the code presented adequately addresses the question.
Output only ###TRUE### if it does, otherwise output ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''The question is:
{question}

Here is the code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 3:
────────────────────────────
code_question_answering_template_self_ask = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before delivering your answer, verify if any supplemental follow-up questions are needed to clear up ambiguities in the task. If needed, pose and resolve those inquiries before your final response.
Determine if the following code adequately answers the given question.
Return only ###TRUE### if it completely meets the query's demands, or ###FALSE### if not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question details:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 4:
────────────────────────────
code_question_answering_template_self_ask = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you provide your answer, consider whether additional, clarifying questions should be asked. If so, both ask those follow-up questions and address them before concluding your answer.
Review whether the supplied code correctly resolves the question.
Answer exclusively with ###TRUE### if the code fully complies, otherwise answer with ###FALSE###.'''
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
Variation 5:
────────────────────────────
code_question_answering_template_self_ask = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you answer, think about whether further clarifications through follow-up questions are essential. If they are, please ask and respond to them before finalizing your answer.
Examine if the code given satisfactorily addresses the question.
Reply with only ###TRUE### if it is completely correct, or ###FALSE### if it isn’t.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Inquiry:
{question}

Programming Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 6:
────────────────────────────
code_question_answering_template_self_ask = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before providing your answer, check if any extra questions are necessary to clarify the task. If additional clarification is needed, ask and answer those questions before giving your final response.
Assess if the code provided fully addresses the question.
Your answer should be strictly ###TRUE### when appropriate, or ###FALSE### otherwise.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''The question:
{question}

The code to review:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 7:
────────────────────────────
code_question_answering_template_self_ask = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before responding, evaluate whether you need to ask further questions to clarify the request. If so, include those follow-up questions and your corresponding answers before finalizing your response.
Verify whether the code below meets the requirements of the question.
Return solely ###TRUE### if it meets all criteria, or ###FALSE### if it falls short.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Query:
{question}

Code provided:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 8:
────────────────────────────
code_question_answering_template_self_ask = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Prior to answering, reflect on whether the task demands any extra clarifying questions. If it does, ask and address those before delivering the ultimate answer.
Decide if the code given is a proper solution to the question.
Output strictly ###TRUE### when correct, or ###FALSE### if it is not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Question:
{question}

Relevant Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 9:
────────────────────────────
code_question_answering_template_self_ask = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you answer, reflect on whether any extra follow-up inquiries are necessary for a clearer understanding of the task. If they are needed, ask and answer them prior to your final response.
Determine if the code presented properly addresses the question.
Respond only with ###TRUE### if it completely satisfies the query, or with ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question description:
{question}

Code sample:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 10:
────────────────────────────
code_question_answering_template_self_ask = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before answering the query, ascertain if further clarifying questions are needed. If so, pose and settle those queries before issuing your final response.
Examine if the ensuing code properly answers the question.
Only respond with ###TRUE### if the code fulfills the requirements, or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question to be answered:
{question}

Code under review:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 11:
────────────────────────────
code_question_answering_template_self_ask = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Prior to delivering your answer, consider whether you need to ask additional clarifying questions. If such follow-up queries are necessary, include them and answer these supplemental questions before reaching a conclusion.
Analyze if the following code successfully answers the question.
Respond with only ###TRUE### if it does, or with ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Your question:
{question}

Corresponding code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 12:
────────────────────────────
code_question_answering_template_self_ask = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before formulating your answer, determine if additional follow-up questions are required to clarify any part of the task. Should they be needed, ask and resolve those questions before your final answer.
Review whether the provided code effectively resolves the question.
Answer exclusively with ###TRUE### when it is completely correct, or ###FALSE### if otherwise.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Query details:
{question}

Review the code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 13:
────────────────────────────
code_question_answering_template_self_ask = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you proceed with your response, assess if additional questions for clarification are needed. If they are, make sure to ask and answer them before providing your final submission.
Determine if the attached code effectively answers the question.
Output only the text ###TRUE### if it does, or ###FALSE### if it fails to meet the criteria.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''The question is as follows:
{question}

Below is the code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 14:
────────────────────────────
code_question_answering_template_self_ask = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before issuing your final answer, check if extra clarifying questions are warranted. If so, ask and resolve these follow-up questions prior to providing the complete answer.
Assess whether the submitted code completely satisfies the question's requirements.
Provide only ###TRUE### if the criteria are fully met, or ###FALSE### if they are not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Problem statement:
{question}

Code example:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 15:
────────────────────────────
code_question_answering_template_self_ask = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before crafting your answer, check if the situation calls for asking additional clarifying questions. If additional details are necessary, include those inquiries and answer them prior to your concluding response.
Verify if the following code fully responds to the question.
Respond exclusively with ###TRUE### if the code meets the query perfectly, or with ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Detailed question:
{question}

Examined code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
