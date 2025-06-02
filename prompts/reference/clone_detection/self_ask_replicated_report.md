Below are 15 variants of the original prompt template. Note that Variation 0 is exactly the same as provided, while Variations 1–14 include rephrased strings in both the system and human messages. The AI message string remains unchanged in all cases.

---------------------------------------------------------
# Variation 0 (Original):

clone_detection_template_self_ask_0 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before answering, consider if any follow-up questions are needed to clarify the task. If so, ask and answer them before providing the final answer.
Determine if the two code snippets are clones.
Answer with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Snippet 1:
{code_snippet1}

Code Snippet 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

---------------------------------------------------------
# Variation 1:

clone_detection_template_self_ask_1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you respond, check whether any clarifying questions are necessary. If you identify any, ask and resolve them prior to giving your final answer.
Assess if these two pieces of code are identical clones.
Respond using either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Here is the first code snippet:
{code_snippet1}

And here is the second code snippet:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

---------------------------------------------------------
# Variation 2:

clone_detection_template_self_ask_2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before providing your answer, verify if additional questions are needed to better understand the task. Pose and answer them if required before giving the final result.
Decide whether the provided two code examples are clones.
Answer strictly with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Snippet One:
{code_snippet1}

Snippet Two:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

---------------------------------------------------------
# Variation 3:

clone_detection_template_self_ask_3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before giving your response, consider if any further questions are needed for clarification. If so, ask and settle them before your concluding answer.
Determine if the following two code samples are exact duplicates.
Your answer should be either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''First Code Block:
{code_snippet1}

Second Code Block:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

---------------------------------------------------------
# Variation 4:

clone_detection_template_self_ask_4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Prior to answering, reflect on whether any additional inquiry is necessary to clarify the details of the task. If you find any, ask them and provide responses before finalizing your answer.
Examine whether these two code fragments are clones.
Reply with either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Example 1:
{code_snippet1}

Code Example 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

---------------------------------------------------------
# Variation 5:

clone_detection_template_self_ask_5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Check first if any additional clarifying questions need to be asked before you answer. Address them if necessary, then provide your final response.
Identify if the two code snippets provided are essentially clones.
Use only ###TRUE### or ###FALSE### as your answer.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Provided below are two code segments:
Segment 1:
{code_snippet1}

Segment 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

---------------------------------------------------------
# Variation 6:

clone_detection_template_self_ask_6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before delivering your final answer, consider whether you need to ask any extra questions for clarity. If yes, ask and answer them first.
Determine if these two code sections are clones.
Answer solely with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Here are the two code snippets for analysis:
Code Snippet A:
{code_snippet1}

Code Snippet B:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

---------------------------------------------------------
# Variation 7:

clone_detection_template_self_ask_7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you provide an answer, check if you need to ask any further questions to clear up ambiguities. Should additional questions be needed, ask and answer them before coming to your final conclusion.
Decide whether the two code samples presented are clones.
Your response must be either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Examine the following code pieces:
First snippet:
{code_snippet1}

Second snippet:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

---------------------------------------------------------
# Variation 8:

clone_detection_template_self_ask_8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Prior to answering, take a moment to determine if any extra follow-up questions are needed to fully understand the task. If so, ask and resolve them before proceeding with your final statement.
Verify if the two given code snippets are clones.
Reply strictly with either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Segment 1:
{code_snippet1}

Code Segment 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

---------------------------------------------------------
# Variation 9:

clone_detection_template_self_ask_9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you answer, consider if there are any additional follow-up questions that could clarify the task. Ask and answer these if needed before providing your final response.
Assess if the two code snippets shown below are clones.
Respond with either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Take a look at these code excerpts:
Excerpt 1:
{code_snippet1}

Excerpt 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

---------------------------------------------------------
# Variation 10:

clone_detection_template_self_ask_10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before providing your answer, reflect on whether any additional questions are needed to remove uncertainty about the task. If necessary, ask and answer those queries first.
Decide if the two given code blocks are clones.
Your answer should be either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Presented below are two code blocks:
Block 1:
{code_snippet1}

Block 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

---------------------------------------------------------
# Variation 11:

clone_detection_template_self_ask_11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before finalizing your answer, consider if any questions should be asked to better understand the task at hand. If clarification is needed, ask and answer such questions before delivering your final answer.
Evaluate whether these two provided code snippets are clones.
Answer only with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Here are the two code examples:
Example 1:
{code_snippet1}

Example 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

---------------------------------------------------------
# Variation 12:

clone_detection_template_self_ask_12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you give your answer, check whether any additional inquiries are needed for clarity. If so, ask and answer those questions prior to your final response.
Determine whether the following two code excerpts are clones.
Answer with either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Here is the first code sample:
{code_snippet1}

Here is the second code sample:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

---------------------------------------------------------
# Variation 13:

clone_detection_template_self_ask_13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before answering, check if any supplementary questions are needed to fully understand the task. If further questions arise, ask and answer them first.
Check whether the two provided code snippets are equivalent clones.
Respond with either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Part 1:
{code_snippet1}

Code Part 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

---------------------------------------------------------
# Variation 14:

clone_detection_template_self_ask_14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Prior to offering your answer, consider whether more clarifying questions are necessary. If they are, ask them and include the answers prior to presenting your final conclusion.
Ascertain if these two code snippets are mere clones of each other.
Reply exclusively with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Example A:
{code_snippet1}

Code Example B:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

---------------------------------------------------------
# Variation 15:

clone_detection_template_self_ask_15 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you finalize your answer, reflect if any follow-up questions are needed to expand on the task details. If so, ask and resolve them before supplying your final answer.
Determine if the two presented code snippets are clones.
Your answer must be either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Review the following code fragments:
Fragment 1:
{code_snippet1}

Fragment 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

---------------------------------------------------------

Each of these variants maintains the original task and prompt strategy while using different wording for the system and human messages.