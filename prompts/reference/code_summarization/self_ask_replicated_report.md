Below are 15 variations of the original chat prompt template. Variation 0 is the original template, and variations 1–14 contain rephrased strings for the SystemMessagePromptTemplate and the HumanMessagePromptTemplate while leaving the AIMessagePromptTemplate unchanged.

──────────────────────────────
Variation 0:
──────────────────────────────
code_summarization_template_self_ask = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before summarizing, consider if any follow-up questions are needed to clarify the code. If so, ask and answer them before providing the final summary.
Provide a summary of the following code.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 1:
──────────────────────────────
code_summarization_template_self_ask_v1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Prior to summarizing, check if any clarifying questions are required to better understand the code. If so, ask and answer them before delivering your final summary.
Provide a summary of the following code.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly enter the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 2:
──────────────────────────────
code_summarization_template_self_ask_v2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you offer a summary, verify whether additional questions could clarify the code. If needed, pose and answer those questions first.
Summarize the following code.'''
    ),
    HumanMessagePromptTemplate.from_template("Input the following code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 3:
──────────────────────────────
code_summarization_template_self_ask_v3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Evaluate if any follow-up queries are necessary to fully grasp the code before summarizing it. If they are, ask and answer those queries prior to summarizing.
Provide a summary of the code shown below.'''
    ),
    HumanMessagePromptTemplate.from_template("Submit the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 4:
──────────────────────────────
code_summarization_template_self_ask_v4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Assess if extra questions are needed to clear any ambiguities in the code before you proceed with summarization. If extra inquiries are warranted, address them first.
Then, deliver a summary of the code below.'''
    ),
    HumanMessagePromptTemplate.from_template("Please insert the code here: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 5:
──────────────────────────────
code_summarization_template_self_ask_v5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before summarizing, determine whether any clarifying questions should be raised about the code. If clarification is needed, ask and answer them first.
Then, provide a summary of the following code.'''
    ),
    HumanMessagePromptTemplate.from_template("Include the code here: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 6:
──────────────────────────────
code_summarization_template_self_ask_v6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Prior to summarization, check if further questions are necessary to ensure a clearer understanding of the code. If so, ask and resolve them before composing your summary.
Provide a summary of the code below.'''
    ),
    HumanMessagePromptTemplate.from_template("Forward the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 7:
──────────────────────────────
code_summarization_template_self_ask_v7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before drafting your summary, inspect the code to determine if any follow-up inquiries are needed for better clarity. If required, address them first.
Summarize the code provided below.'''
    ),
    HumanMessagePromptTemplate.from_template("Enter the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 8:
──────────────────────────────
code_summarization_template_self_ask_v8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before writing the summary, consider whether additional inquiries might help clarify the code's functionality. If needed, ask and answer these questions first.
Then, offer your summary of the code below.'''
    ),
    HumanMessagePromptTemplate.from_template("Present the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 9:
──────────────────────────────
code_summarization_template_self_ask_v9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Check if any further questions could assist in clarifying the code before composing your summary. If that is the case, resolve those questions first.
Provide a summary of the code that follows.'''
    ),
    HumanMessagePromptTemplate.from_template("Supply the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 10:
──────────────────────────────
code_summarization_template_self_ask_v10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Assess if additional clarification is needed by asking further questions about the code before summarizing. If such questions are necessary, answer them prior to delivering your final summary.
Summarize the code outlined below.'''
    ),
    HumanMessagePromptTemplate.from_template("Insert the given code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 11:
──────────────────────────────
code_summarization_template_self_ask_v11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''First, review the code and decide whether extra questions are needed to clarify its details. If so, ask and answer these questions before summarizing.
Then, provide your summary.'''
    ),
    HumanMessagePromptTemplate.from_template("Please supply the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 12:
──────────────────────────────
code_summarization_template_self_ask_v12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before summarizing the code, determine if any follow-up questions are necessary for enhanced understanding. If so, ensure these questions are asked and answered prior to your summary.
Then, summarize the following code.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly provide the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 13:
──────────────────────────────
code_summarization_template_self_ask_v13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Prior to producing your summary, decide if additional queries are needed to clarify any uncertainties in the code. If required, ask and answer these queries before summarizing.
Provide a summary of the following code.'''
    ),
    HumanMessagePromptTemplate.from_template("Enter the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 14:
──────────────────────────────
code_summarization_template_self_ask_v14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before generating your summary, review the code to determine if supplemental questions could help clarify its intent. If necessary, ask and answer these questions prior to summarizing.
Summarize the subsequent code.'''
    ),
    HumanMessagePromptTemplate.from_template("Present the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

Each template maintains the original structure and technique while offering different rephrased directives in the system and human messages.