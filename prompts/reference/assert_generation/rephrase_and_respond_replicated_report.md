Below are 15 complete prompt template variants. Variation 0 is the original, and Variations 1–14 are new versions with the SystemMessagePromptTemplate and HumanMessagePromptTemplate texts reworded while keeping the AIMessagePromptTemplate unchanged.

────────────────────────────────────────
Variation 0:
────────────────────────────────────────
assert_generation_template_rar_v2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine the correct assertion that should replace <AssertPlaceHolder> in the following code.
Reword the instruction with additional detail, then provide only the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────────────────
Variation 1:
────────────────────────────────────────
assert_generation_template_rar_v2_variation1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Identify the proper assertion to substitute <AssertPlaceHolder> in the code provided below.
Enhance the directive by rephrasing it with further specifics, and then supply solely the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Please provide the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────────────────
Variation 2:
────────────────────────────────────────
assert_generation_template_rar_v2_variation2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Review the following code and determine which assertion should replace <AssertPlaceHolder>.
Rewrite the instruction with added details, then output only the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Insert your code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────────────────
Variation 3:
────────────────────────────────────────
assert_generation_template_rar_v2_variation3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Examine the provided code and select the appropriate assertion to replace <AssertPlaceHolder>.
Rephrase the instruction with more explicit details, then return only the assertion.'''
    ),
    HumanMessagePromptTemplate.from_template("Include your code snippet here: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────────────────
Variation 4:
────────────────────────────────────────
assert_generation_template_rar_v2_variation4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Analyze the code provided and decide which assertion would correctly substitute <AssertPlaceHolder>.
Elaborate on the directive with added clarity before returning only the assertion text.'''
    ),
    HumanMessagePromptTemplate.from_template("Input the accompanying code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────────────────
Variation 5:
────────────────────────────────────────
assert_generation_template_rar_v2_variation5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Consider the given code snippet and determine the valid assertion to replace <AssertPlaceHolder>.
Clarify the instruction by expanding on the details, then present solely the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Supply the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────────────────
Variation 6:
────────────────────────────────────────
assert_generation_template_rar_v2_variation6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Inspect the following code and identify the correct assertion that should take the place of <AssertPlaceHolder>.
Reframe the instruction with extra clarity and detail, then output only the assertion line.'''
    ),
    HumanMessagePromptTemplate.from_template("Submit your code here: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────────────────
Variation 7:
────────────────────────────────────────
assert_generation_template_rar_v2_variation7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Look over the code below and decide on the appropriate assertion to replace <AssertPlaceHolder>.
Modify the instructions by adding more detail, then provide only the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Provide the relevant code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────────────────
Variation 8:
────────────────────────────────────────
assert_generation_template_rar_v2_variation8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Review the given code and select the assertion appropriate to substitute for <AssertPlaceHolder>.
Expand the instruction with further details, then output solely the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Include the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────────────────
Variation 9:
────────────────────────────────────────
assert_generation_template_rar_v2_variation9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Analyze the provided code and determine the assertion that should supplant <AssertPlaceHolder>.
Restate the instruction with additional context, then return only the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Enter the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────────────────
Variation 10:
────────────────────────────────────────
assert_generation_template_rar_v2_variation10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Interpret the shown code and decide on the correct assertion to fill in for <AssertPlaceHolder>.
Recast the instruction with more comprehensive detail, then supply exclusively the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Present the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────────────────
Variation 11:
────────────────────────────────────────
assert_generation_template_rar_v2_variation11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Dissect the code example and pick the assertion apt for replacing <AssertPlaceHolder>.
Reformulate the instruction with extra detail, then output solely the assertion.'''
    ),
    HumanMessagePromptTemplate.from_template("Type the code here: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────────────────
Variation 12:
────────────────────────────────────────
assert_generation_template_rar_v2_variation12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Evaluate the code below to identify the proper assertion that can substitute for <AssertPlaceHolder>.
Reword the directive with further explanatory detail, then provide only the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Share the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────────────────
Variation 13:
────────────────────────────────────────
assert_generation_template_rar_v2_variation13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Study the provided code and decide which assertion should replace <AssertPlaceHolder>.
Enrich the instructions with additional specifics, then deliver only the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly provide your code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────────────────
Variation 14:
────────────────────────────────────────
assert_generation_template_rar_v2_variation14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Scrutinize the following code and select the assertion that best replaces <AssertPlaceHolder>.
Revise the instruction with more informative details, then simply return the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Paste the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

Each variant maintains the core task and template technique while offering unique rephrasings for the system and human instructions.