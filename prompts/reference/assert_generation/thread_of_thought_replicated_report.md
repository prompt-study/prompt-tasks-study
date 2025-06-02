Below are 15 versions of the prompt template. Variation 0 is the original (unchanged), and variations 1–14 are rephrased versions. Note that only the strings in the SystemMessagePromptTemplate and HumanMessagePromptTemplate have been reworded while the AIMessagePromptTemplate remains intact.

──────────────────────────────
Variation 0:
──────────────────────────────
assert_generation_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Walk me through this code in manageable parts, summarizing its logic and analyzing where assertions are required.
Finally, determine the correct assertion that should replace <AssertPlaceHolder> and provide only the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 1:
──────────────────────────────
assert_generation_template_thot_v1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Guide me through this code piece by piece, summarizing its functionality and discussing where assertions should be applied.
In the end, identify the proper assertion that ought to replace <AssertPlaceHolder> and output only that assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Here's the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 2:
──────────────────────────────
assert_generation_template_thot_v2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Break down this code into clear segments, outlining its logic and pinpointing the areas where assertions are needed.
Finally, determine and return only the correct assertion that replaces <AssertPlaceHolder>.'''
    ),
    HumanMessagePromptTemplate.from_template("The following code is provided: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 3:
──────────────────────────────
assert_generation_template_thot_v3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Analyze the code step by step, summarizing its operation and identifying points that require assertions.
Then, supply solely the correct assertion statement to substitute <AssertPlaceHolder>.'''
    ),
    HumanMessagePromptTemplate.from_template("Code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 4:
──────────────────────────────
assert_generation_template_thot_v4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Dissect this code into manageable parts, summarizing its purpose and noting where assertions should be inserted.
Ultimately, output only the assertion statement meant to replace <AssertPlaceHolder>.'''
    ),
    HumanMessagePromptTemplate.from_template("Review this code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 5:
──────────────────────────────
assert_generation_template_thot_v5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Examine this code by breaking it into clear segments, detailing its logic and identifying where assertions are necessary.
Conclude by providing just the assertion that should stand in for <AssertPlaceHolder>.'''
    ),
    HumanMessagePromptTemplate.from_template("Examine the following code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 6:
──────────────────────────────
assert_generation_template_thot_v6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Step through the code in digestible parts, summarizing its logic and determining where assertion checks should be placed.
Finally, return only the appropriate assertion that replaces <AssertPlaceHolder>.'''
    ),
    HumanMessagePromptTemplate.from_template("Analyze this snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 7:
──────────────────────────────
assert_generation_template_thot_v7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Navigate through this code piece by piece, summarizing its functionality while identifying where assertions need to be applied.
At the end, leave only the proper assertion statement to replace <AssertPlaceHolder>.'''
    ),
    HumanMessagePromptTemplate.from_template("Here's the code fragment: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 8:
──────────────────────────────
assert_generation_template_thot_v8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Outline the code in clear steps, summarizing its functionality and highlighting the spots where assertions are required.
Then, provide solely the assertion statement that takes the place of <AssertPlaceHolder>.'''
    ),
    HumanMessagePromptTemplate.from_template("Code provided: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 9:
──────────────────────────────
assert_generation_template_thot_v9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Step through this code incrementally, explaining its logic and determining the instances where assertions should be used.
Finally, output only the exact assertion that should supplant <AssertPlaceHolder>.'''
    ),
    HumanMessagePromptTemplate.from_template("See the code below: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 10:
──────────────────────────────
assert_generation_template_thot_v10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Methodically analyze this code by breaking it into smaller sections, summarizing its functionality and identifying where assertions are warranted.
Subsequently, return just the assertion statement designated to replace <AssertPlaceHolder>.'''
    ),
    HumanMessagePromptTemplate.from_template("Presented code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 11:
──────────────────────────────
assert_generation_template_thot_v11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Review the code by segmenting it into logical parts, outlining its flow and pinpointing where assertions might be needed.
Then, provide solely the correct assertion to replace <AssertPlaceHolder>.'''
    ),
    HumanMessagePromptTemplate.from_template("Input code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 12:
──────────────────────────────
assert_generation_template_thot_v12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Disassemble the code into clear, manageable pieces, summarizing its operational logic and identifying potential assertion points.
Ultimately, return only the assertion statement intended to replace <AssertPlaceHolder>.'''
    ),
    HumanMessagePromptTemplate.from_template("The code is as follows: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 13:
──────────────────────────────
assert_generation_template_thot_v13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Break the code down systematically into understandable segments, outlining its logic and marking where assertions should be inserted.
Finally, output exclusively the assertion statement that serves as a substitute for <AssertPlaceHolder>.'''
    ),
    HumanMessagePromptTemplate.from_template("Refer to the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 14:
──────────────────────────────
assert_generation_template_thot_v14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Dissect and explain the code in successive, clear parts, summarizing its working principles and determining where assertion checks are needed.
At the end, furnish only the correct assertion statement to replace <AssertPlaceHolder>.'''
    ),
    HumanMessagePromptTemplate.from_template("Please review the following code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
──────────────────────────────
Variation 15:
──────────────────────────────
assert_generation_template_thot_v0 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Examine this code incrementally, breaking down its functionality and highlighting where assertions are necessary. Conclude by determining and returning only the correct assertion statement that should be used.'''
    ),
    HumanMessagePromptTemplate.from_template("Provided code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
