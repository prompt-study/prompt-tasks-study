

────────────────────────────────────────
Variation 0:
────────────────────────────────────────
mutant_generation_template_self_ask = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before answering, consider if any follow-up questions are needed to clarify the task. If so, ask and answer them before providing the final answer.
Generate a mutant of this code with small changes.
Provide only the mutated code.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────────────────
Variation 1:
────────────────────────────────────────
mutant_generation_template_self_ask_v1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you answer, evaluate whether additional questions are necessary to fully understand the task. If needed, ask and resolve them prior to your final response.
Create a variant of the code with minor modifications.
Return only the altered code.'''
    ),
    HumanMessagePromptTemplate.from_template("Provided code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────────────────
Variation 2:
────────────────────────────────────────
mutant_generation_template_self_ask_v2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before responding, check if follow-up inquiries are required to ensure a complete understanding of the task. If so, ask those questions and answer them before giving your final answer.
Produce a slightly modified version of this code.
Output only the revised code.'''
    ),
    HumanMessagePromptTemplate.from_template("The code is as follows: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────────────────
Variation 3:
────────────────────────────────────────
mutant_generation_template_self_ask_v3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Prior to answering, determine if additional questions are needed to clarify the requirements. If so, ask and resolve those questions before finalizing your response.
Construct a version of the code with subtle modifications.
Return solely the updated code.'''
    ),
    HumanMessagePromptTemplate.from_template("Code input: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────────────────
Variation 4:
────────────────────────────────────────
mutant_generation_template_self_ask_v4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before delivering your answer, reflect on whether extra questions might help clarify the task. If yes, pose and answer them prior to your final response.
Create a mutant version of the code with minimal adjustments.
Return just the mutated code.'''
    ),
    HumanMessagePromptTemplate.from_template("Inserted code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────────────────
Variation 5:
────────────────────────────────────────
mutant_generation_template_self_ask_v5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before providing your final answer, verify if any follow-up questions are needed for task clarity. If needed, ask and answer them first.
Generate a mutant of the provided code using small changes.
Present only the mutated code.'''
    ),
    HumanMessagePromptTemplate.from_template("Code provided: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────────────────
Variation 6:
────────────────────────────────────────
mutant_generation_template_self_ask_v6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Prior to answering, assess whether supplementary questions are required to clear up the task details. If so, ask them and address their answers before giving your final response.
Generate a version of this code with subtle modifications.
Supply only the modified code.'''
    ),
    HumanMessagePromptTemplate.from_template("The provided code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────────────────
Variation 7:
────────────────────────────────────────
mutant_generation_template_self_ask_v7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you reply, consider if additional questions could help clarify the assignment. If yes, ask and answer them before your final reply.
Develop a modified version of the code with minor tweaks.
Return only the changed code.'''
    ),
    HumanMessagePromptTemplate.from_template("Submitted code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────────────────
Variation 8:
────────────────────────────────────────
mutant_generation_template_self_ask_v8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before finalizing your response, determine whether any extra clarifications are needed through follow-up questions. If so, ask them and then provide your final answer.
Alter the code slightly to produce a mutant version.
Present solely the modified code.'''
    ),
    HumanMessagePromptTemplate.from_template("Here is the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────────────────
Variation 9:
────────────────────────────────────────
mutant_generation_template_self_ask_v9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before offering your answer, verify if any further clarifications via questions are necessary. If they are, ask and answer them prior to your final response.
Forge a mutant iteration of the given code with minor adjustments.
Return only the new version of the code.'''
    ),
    HumanMessagePromptTemplate.from_template("Code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────────────────
Variation 10:
────────────────────────────────────────
mutant_generation_template_self_ask_v10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before proceeding with your answer, check if additional questions would help clarify the task. If needed, ask and answer those questions before finalizing your response.
Produce a subtly altered mutant of this code.
Provide just the modified code.'''
    ),
    HumanMessagePromptTemplate.from_template("Input code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────────────────
Variation 11:
────────────────────────────────────────
mutant_generation_template_self_ask_v11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before answering, reflect on whether any follow-up inquiries are necessary to fully define the task. If so, ask and address them prior to your final answer.
Create a mutant version of the provided code with slight adaptations.
Output only the mutant code.'''
    ),
    HumanMessagePromptTemplate.from_template("Supplied code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────────────────
Variation 12:
────────────────────────────────────────
mutant_generation_template_self_ask_v12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Prior to giving an answer, decide if additional questions are needed for better clarity. If so, ask and answer them before your final output.
Generate a version of the code with small changes.
Return solely this modified version.'''
    ),
    HumanMessagePromptTemplate.from_template("The code is: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────────────────
Variation 13:
────────────────────────────────────────
mutant_generation_template_self_ask_v13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you provide your answer, assess whether any clarifying questions are essential to fully grasp the requirements. If they are needed, ask and address them before your final response.
Produce a mutant of the given code with minor changes.
Supply only the resultant modified code.'''
    ),
    HumanMessagePromptTemplate.from_template("Here is the original code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────────────────
Variation 14:
────────────────────────────────────────
mutant_generation_template_self_ask_v14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before producing your answer, evaluate if clarifying inquiries are required to better understand the task. If necessary, ask and answer those questions before your final answer.
Create a modified version of the supplied code with subtle adjustments.
Return only the modified code.'''
    ),
    HumanMessagePromptTemplate.from_template("Code for mutation: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

