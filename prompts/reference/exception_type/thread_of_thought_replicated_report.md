Below are 15 versions of the prompt template. Variation 0 is exactly as provided, and Variations 1–14 include rephrased strings for the SystemMessagePromptTemplate and the HumanMessagePromptTemplate while leaving the AIMessagePromptTemplate untouched.

----------------------------------------------------------------
variation 0:
----------------------------------------------------------------
exception_type_template_thot_variation_0 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Walk me through this code in manageable parts, summarizing its logic and analyzing potential exceptions.
Finally, determine which exception type should replace __HOLE__ and provide your answer in the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

----------------------------------------------------------------
variation 1:
----------------------------------------------------------------
exception_type_template_thot_variation_1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Break down the given code step by step, explaining its logic and identifying any possible exceptions that could occur.
Conclude by selecting the exception type to substitute __HOLE__ and return your answer formatted as ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("Please supply the code to analyze: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

----------------------------------------------------------------
variation 2:
----------------------------------------------------------------
exception_type_template_thot_variation_2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Please dissect this code into small, understandable segments, outlining its overall logic and examining possible exceptional cases.
At the end, decide on the appropriate exception type to replace __HOLE__ and report your answer in the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("Enter your code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

----------------------------------------------------------------
variation 3:
----------------------------------------------------------------
exception_type_template_thot_variation_3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Analyze the provided code by splitting it into clear stages, summarizing each section's logic and spotting any potential exceptions.
Lastly, specify which exception type should fill the __HOLE__ and present your answer in the following format: ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("Provide the code example: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

----------------------------------------------------------------
variation 4:
----------------------------------------------------------------
exception_type_template_thot_variation_4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Go through the code piece by piece, detailing the logic behind each part and noting any exceptions it might raise.
Finally, pinpoint the correct exception type to substitute __HOLE__ and format your response as ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("Share the code you want reviewed: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

----------------------------------------------------------------
variation 5:
----------------------------------------------------------------
exception_type_template_thot_variation_5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Examine and explain the code in small, digestible segments, highlighting its functionality and any potential exceptions involved.
In the end, indicate the proper exception type to replace __HOLE__ and format your answer as ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("Insert the code for examination: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

----------------------------------------------------------------
variation 6:
----------------------------------------------------------------
exception_type_template_thot_variation_6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Step through the code methodically, providing summaries for each segment's logic while also identifying any potential exceptions.
Conclude by choosing the exception type meant to replace __HOLE__ and presenting your response in the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("Paste the code segment here: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

----------------------------------------------------------------
variation 7:
----------------------------------------------------------------
exception_type_template_thot_variation_7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Please break down the code into logical segments, explaining the purpose of each part and noting any exceptions that might occur.
Wrap up by selecting the correct exception type for __HOLE__ and display your answer as ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("Add the specific code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

----------------------------------------------------------------
variation 8:
----------------------------------------------------------------
exception_type_template_thot_variation_8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Detail the operation of the provided code by dividing it into clear, manageable pieces, summarizing the underlying logic and flagging potential exceptions.
At last, decide which exception type is suitable to replace __HOLE__ and deliver your answer using the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("Deliver the code you'd like to analyze: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

----------------------------------------------------------------
variation 9:
----------------------------------------------------------------
exception_type_template_thot_variation_9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Systematically parse through the code in sections, summarizing the logic in each part and identifying any exceptions that could arise.
End your explanation by stating the exception type that should replace __HOLE__, formatted as ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("Attach the code sample here: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

----------------------------------------------------------------
variation 10:
----------------------------------------------------------------
exception_type_template_thot_variation_10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Walk through the code in step-by-step segments, clarifying its logic and noting any possible exceptions that may be raised.
Finally, determine the proper exception type to use in place of __HOLE__ and provide your answer formatted as ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("Input the code to be examined: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

----------------------------------------------------------------
variation 11:
----------------------------------------------------------------
exception_type_template_thot_variation_11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Divide the code into digestible parts and explain the purpose behind each section while checking for potential exceptions.
Finally, indicate which exception type should substitute __HOLE__ in the code, and format your answer as ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("Submit the code content: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

----------------------------------------------------------------
variation 12:
----------------------------------------------------------------
exception_type_template_thot_variation_12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Inspect the code in manageable sections, summarizing each segment's logic and calling attention to potential exceptions.
Wrap up by choosing the appropriate exception type to replace __HOLE__ and providing your answer in the ###ExceptionType### format.'''
    ),
    HumanMessagePromptTemplate.from_template("Type or paste the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

----------------------------------------------------------------
variation 13:
----------------------------------------------------------------
exception_type_template_thot_variation_13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Analyze the code closely by breaking it down into distinct parts, offering a summary of its logic and looking out for any exceptions.
Finish by identifying the proper exception type to replace __HOLE__ and present your answer in the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("Provide your code input: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

----------------------------------------------------------------
variation 14:
----------------------------------------------------------------
exception_type_template_thot_variation_14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Review the code step-by-step, outlining its logic and assessing any exceptional circumstances that might occur.
Finally, choose the exception type to substitute __HOLE__ and supply your answer in the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("Directly insert the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
