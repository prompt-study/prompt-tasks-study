Below are 15 complete prompt template variations. Variation 0 is left exactly as originally provided. For each variation, only the strings in the SystemMessagePromptTemplate and HumanMessagePromptTemplate have been reworded (while keeping the AIMessagePromptTemplate unchanged).

────────────────────────
Variation 0 (original):
────────────────────────
defect_detection_template_rar_v2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Is there a defect in the code? Answer with TRUE or FALSE only, using the format: ###TRUE### or ###FALSE###.
Reword the question with added clarity, and then respond.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────
Variation 1:
────────────────────────
defect_detection_template_rar_v2_variant1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Does the code contain any errors? Please reply solely with TRUE or FALSE, exactly formatted as: ###TRUE### or ###FALSE###.
Restate the query more clearly before providing your answer.'''
    ),
    HumanMessagePromptTemplate.from_template("Please review the following code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────
Variation 2:
────────────────────────
defect_detection_template_rar_v2_variant2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Identify whether the code has a flaw. Respond only with TRUE or FALSE using this exact format: ###TRUE### or ###FALSE###.
Also, rephrase the question in clearer terms before answering.'''
    ),
    HumanMessagePromptTemplate.from_template("Here is the code that needs to be examined: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────
Variation 3:
────────────────────────
defect_detection_template_rar_v2_variant3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Examine the provided code for any defects. Answer strictly with TRUE or FALSE in the format: ###TRUE### or ###FALSE###.
Please paraphrase the inquiry to enhance clarity before responding.'''
    ),
    HumanMessagePromptTemplate.from_template("Consider this code snippet for analysis: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────
Variation 4:
────────────────────────
defect_detection_template_rar_v2_variant4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Assess whether the given code has any mistakes. Your response must be either TRUE or FALSE, formatted as: ###TRUE### or ###FALSE###.
Additionally, rewrite the question in clearer terms before answering.'''
    ),
    HumanMessagePromptTemplate.from_template("Evaluate the following code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────
Variation 5:
────────────────────────
defect_detection_template_rar_v2_variant5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Review the code and determine if a defect exists. Reply only with TRUE or FALSE, using the precise format: ###TRUE### or ###FALSE###.
Please also rephrase the prompt to make it clearer before providing your answer.'''
    ),
    HumanMessagePromptTemplate.from_template("Review this code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────
Variation 6:
────────────────────────
defect_detection_template_rar_v2_variant6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Check the code for any errors. Your answer should be solely TRUE or FALSE, adhering strictly to the format: ###TRUE### or ###FALSE###.
Before replying, please reword the question to improve clarity.'''
    ),
    HumanMessagePromptTemplate.from_template("Analyze the subsequent code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────
Variation 7:
────────────────────────
defect_detection_template_rar_v2_variant7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Does the code exhibit any defects? Answer exclusively with TRUE or FALSE, formatted as: ###TRUE### or ###FALSE###.
Also, paraphrase the question for added clarity prior to your response.'''
    ),
    HumanMessagePromptTemplate.from_template("Examine the following code segment: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────
Variation 8:
────────────────────────
defect_detection_template_rar_v2_variant8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine if there is an error within the code. Provide your answer strictly as TRUE or FALSE using the format: ###TRUE### or ###FALSE###.
Furthermore, reword the query to ensure clarity and then answer.'''
    ),
    HumanMessagePromptTemplate.from_template("Consider this snippet of code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────
Variation 9:
────────────────────────
defect_detection_template_rar_v2_variant9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Is there an issue in the code? Respond solely with TRUE or FALSE in the format: ###TRUE### or ###FALSE###.
Also, rephrase the prompt to make it clearer before replying.'''
    ),
    HumanMessagePromptTemplate.from_template("Evaluate the following code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────
Variation 10:
────────────────────────
defect_detection_template_rar_v2_variant10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Inspect the code to see if it contains any defects. Answer only with TRUE or FALSE using the specified format: ###TRUE### or ###FALSE###.
Additionally, rewrite the question in more understandable terms before answering.'''
    ),
    HumanMessagePromptTemplate.from_template("Please analyze this code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────
Variation 11:
────────────────────────
defect_detection_template_rar_v2_variant11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Does the code have any errors? Reply only with TRUE or FALSE using the exact format: ###TRUE### or ###FALSE###.
Furthermore, rephrase the question for better clarity and then answer.'''
    ),
    HumanMessagePromptTemplate.from_template("Here is the code to inspect: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────
Variation 12:
────────────────────────
defect_detection_template_rar_v2_variant12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Scrutinize the code to check for any defects. Your answer must be only TRUE or FALSE, following the format: ###TRUE### or ###FALSE###.
Also, reword the original question to enhance clarity before replying.'''
    ),
    HumanMessagePromptTemplate.from_template("Review this code block: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────
Variation 13:
────────────────────────
defect_detection_template_rar_v2_variant13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Is there any fault in the provided code? Respond exclusively with TRUE or FALSE, using the format: ###TRUE### or ###FALSE###.
Additionally, paraphrase the query to ensure greater clarity before answering.'''
    ),
    HumanMessagePromptTemplate.from_template("Assess this coding snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────
Variation 14:
────────────────────────
defect_detection_template_rar_v2_variant14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Verify whether the code contains any mistakes. Please answer only with TRUE or FALSE, strictly using the format: ###TRUE### or ###FALSE###.
Also, rephrase the question to make it more comprehensible before replying.'''
    ),
    HumanMessagePromptTemplate.from_template("Here is the snippet to evaluate: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

