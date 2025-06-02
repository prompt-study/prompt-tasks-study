Below you will find 15 complete variations of the original prompt template. In each one the strings given to the SystemMessagePromptTemplate and HumanMessagePromptTemplate have been rephrased while the AIMessagePromptTemplate remains unchanged. The original template is labeled as variation 0.

--------------------------------------------------
Variation 0:
--------------------------------------------------
code_summarization_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Walk me through this code in manageable parts, summarizing and analyzing its functionality as we go.
Finally, provide a concise summary.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------
Variation 1:
--------------------------------------------------
code_summarization_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Please guide me through this code step by step. Break it down into sections, evaluate each part, and then wrap up with a brief summary.'''
    ),
    HumanMessagePromptTemplate.from_template("Here is the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------
Variation 2:
--------------------------------------------------
code_summarization_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Step through this code piece by piece, examining each segment’s functionality and offering analysis along the way. End with a short overall summary.'''
    ),
    HumanMessagePromptTemplate.from_template("Please review the following code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------
Variation 3:
--------------------------------------------------
code_summarization_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Explain this code in segments, detailing the functionality and rationale behind each part. Conclude with a brief summary.'''
    ),
    HumanMessagePromptTemplate.from_template("Consider the code below: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------
Variation 4:
--------------------------------------------------
code_summarization_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Walk through the code carefully, dividing it into clear sections while discussing the purpose of each segment. Finally, provide a concise overview.'''
    ),
    HumanMessagePromptTemplate.from_template("Take a look at this snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------
Variation 5:
--------------------------------------------------
code_summarization_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Decompose the code into manageable parts, offering insights and analysis for each segment. End with a succinct summary.'''
    ),
    HumanMessagePromptTemplate.from_template("The code to analyze is as follows: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------
Variation 6:
--------------------------------------------------
code_summarization_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Guide me through each section of this code; for every part, explain its function and analyze its behavior. Conclude with a brief overall summary.'''
    ),
    HumanMessagePromptTemplate.from_template("Review this code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------
Variation 7:
--------------------------------------------------
code_summarization_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Please analyze the code step-by-step by breaking it into segments, discussing the role of each portion, and finishing with a short summary.'''
    ),
    HumanMessagePromptTemplate.from_template("Here is the code segment: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------
Variation 8:
--------------------------------------------------
code_summarization_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Examine this code by dividing it into clear portions, describing the functionality of each, and ending with a concise summary.'''
    ),
    HumanMessagePromptTemplate.from_template("Below is the code for consideration: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------
Variation 9:
--------------------------------------------------
code_summarization_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Break down the code into smaller, understandable segments, analyze each part, and then provide a summary of the overall functionality.'''
    ),
    HumanMessagePromptTemplate.from_template("Consider the following code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------
Variation 10:
--------------------------------------------------
code_summarization_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Provide a detailed walkthrough of this code by segmenting it, explaining the purpose of each section, and capping it off with a brief summary.'''
    ),
    HumanMessagePromptTemplate.from_template("Examine this code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------
Variation 11:
--------------------------------------------------
code_summarization_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Please walk me through the code in sequential parts; analyze the function of each segment and then summarize the overall operation in a few words.'''
    ),
    HumanMessagePromptTemplate.from_template("The code snippet is provided here: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------
Variation 12:
--------------------------------------------------
code_summarization_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Step through each section of the code, clarifying how each part works and contributes to the whole, then finish with a brief summary.'''
    ),
    HumanMessagePromptTemplate.from_template("Please see the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------
Variation 13:
--------------------------------------------------
code_summarization_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Carefully analyze the code, breaking it into parts and explaining the functionality of each segment. End your explanation with a concise final overview.'''
    ),
    HumanMessagePromptTemplate.from_template("Analyze this piece of code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------
Variation 14:
--------------------------------------------------
code_summarization_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Guide me through this code by splitting it into its components, discussing the role of every segment, and concluding with a short summary.'''
    ),
    HumanMessagePromptTemplate.from_template("Review the following snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])