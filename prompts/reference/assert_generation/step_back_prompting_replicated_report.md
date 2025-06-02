
────────────────────────
Variation 0:
────────────────────────
assert_generation_template_step_back = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''Please discuss what considerations or rules you typically follow
when determining the correct assertion to replace <AssertPlaceHolder> in code.'''
    ),
    HumanMessagePromptTemplate.from_template("Describe those considerations."),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Now, apply those considerations to determine the correct assertion
that should replace <AssertPlaceHolder> in the following code.
Provide only the assertion statement.

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────
Variation 1:
────────────────────────
assert_generation_template_step_back_var1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Could you outline the guidelines or criteria you commonly adhere to when selecting the proper assertion to substitute for <AssertPlaceHolder> in code?'''
    ),
    HumanMessagePromptTemplate.from_template("List those guidelines and considerations."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Using these guidelines, identify the assertion that should replace <AssertPlaceHolder> in the code below.
Return only the assertion statement.

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────
Variation 2:
────────────────────────
assert_generation_template_step_back_var2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Explain which rules or factors you repeatedly consider when determining the appropriate assertion to use instead of <AssertPlaceHolder> in a code snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Outline the factors or rules involved."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Based on these factors, select the precise assertion that should be inserted in place of <AssertPlaceHolder> in the following code.
Provide only the assertion statement.

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────
Variation 3:
────────────────────────
assert_generation_template_step_back_var3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Discuss the key principles or conventions you typically follow when deciding on which assertion to replace <AssertPlaceHolder> in code.'''
    ),
    HumanMessagePromptTemplate.from_template("Elucidate those principles."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Apply those principles to select the assertion that must replace <AssertPlaceHolder> in the code below.
Return solely the assertion statement.

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────
Variation 4:
────────────────────────
assert_generation_template_step_back_var4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Share the criteria or best practices you depend on when determining the assertion to use in place of <AssertPlaceHolder> within code.'''
    ),
    HumanMessagePromptTemplate.from_template("Enumerate those criteria."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Now, employing those criteria, decide the proper assertion that should substitute <AssertPlaceHolder> in the provided code.
Return just the assertion statement.

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────
Variation 5:
────────────────────────
assert_generation_template_step_back_var5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Please describe the considerations or guidelines you generally apply when choosing the correct assertion to replace <AssertPlaceHolder> in a block of code.'''
    ),
    HumanMessagePromptTemplate.from_template("Detail those considerations."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Subsequently, use the described guidelines to determine the appropriate assertion that should substitute for <AssertPlaceHolder> in the following code.
Return only the assertion statement.

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────
Variation 6:
────────────────────────
assert_generation_template_step_back_var6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Outline the rules or standards you normally consider when selecting an assertion to replace <AssertPlaceHolder> in code.'''
    ),
    HumanMessagePromptTemplate.from_template("Specify those rules clearly."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Using these standards, choose the correct assertion to be used in place of <AssertPlaceHolder> in the code presented below.
Return only the assertion statement.

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────
Variation 7:
────────────────────────
assert_generation_template_step_back_var7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Describe the fundamental considerations or protocols you employ when selecting the right assertion to replace <AssertPlaceHolder> in code.'''
    ),
    HumanMessagePromptTemplate.from_template("Expand on those protocols."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Based on these protocols, choose the assertion that properly replaces <AssertPlaceHolder> in the code snippet below.
Provide only the assertion statement.

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────
Variation 8:
────────────────────────
assert_generation_template_step_back_var8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Could you explain which factors or best practices you typically use when selecting an assertion to substitute <AssertPlaceHolder> in a code segment?'''
    ),
    HumanMessagePromptTemplate.from_template("Share those factors and practices."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Now, use those factors to identify the appropriate assertion that should replace <AssertPlaceHolder> in the code below.
Return only the assertion statement.

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────
Variation 9:
────────────────────────
assert_generation_template_step_back_var9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Please explain the primary guidelines or rationale you follow when choosing the assertion to replace <AssertPlaceHolder> in code.'''
    ),
    HumanMessagePromptTemplate.from_template("Explain your rationale in detail."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Based on that rationale, determine the correct assertion to substitute in place of <AssertPlaceHolder> in the following code.
Return exclusively the assertion statement.

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────
Variation 10:
────────────────────────
assert_generation_template_step_back_var10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Explain the reasoning or criteria you usually consider when choosing an assertion to replace <AssertPlaceHolder> within code.'''
    ),
    HumanMessagePromptTemplate.from_template("Clarify those criteria."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Now, applying those criteria, identify the proper assertion that should substitute for <AssertPlaceHolder> in the code snippet below.
Return only the assertion statement.

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────
Variation 11:
────────────────────────
assert_generation_template_step_back_var11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Could you outline your typical approach or list the key factors you consider when selecting the correct assertion to replace <AssertPlaceHolder> in code?'''
    ),
    HumanMessagePromptTemplate.from_template("Summarize those key factors."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Next, based on those factors, choose the exact assertion that should replace <AssertPlaceHolder> in the provided code.
Return only the assertion statement.

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────
Variation 12:
────────────────────────
assert_generation_template_step_back_var12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''What considerations or rules do you typically follow when deciding on the correct assertion to place instead of <AssertPlaceHolder> in a code sample?'''
    ),
    HumanMessagePromptTemplate.from_template("Describe those rules in detail."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Now, using these considerations, determine the appropriate assertion that should take the place of <AssertPlaceHolder> in the code below.
Provide only the assertion statement.

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────
Variation 13:
────────────────────────
assert_generation_template_step_back_var13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Please share the considerations and guidelines you typically observe when choosing an assertion to replace <AssertPlaceHolder> in code.'''
    ),
    HumanMessagePromptTemplate.from_template("List those considerations and guidelines."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Using these guidelines, indicate the precise assertion that should replace <AssertPlaceHolder> in the code provided below.
Return only the assertion statement.

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────
Variation 14:
────────────────────────
assert_generation_template_step_back_var14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Explain the criteria or logical steps you follow when selecting an assertion to substitute for <AssertPlaceHolder> in a code snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Lay out those criteria or steps."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Then, apply these steps to select the correct assertion that should replace <AssertPlaceHolder> in the code below.
Provide only the assertion statement.

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

assert_generation_template_step_back_var15 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Could you explain the common strategies or factors you take into account when determining which assertion should replace one in a code block?'''
    ),
    HumanMessagePromptTemplate.from_template("Describe these strategies and factors."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Now, apply these strategies to identify the assertion that should replace <AssertPlaceHolder> in the following code. Provide only the assertion statement.

        Code: {code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------------------------------------------------------------------

assert_generation_template_step_back_var16 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''What are the general rules or methods you typically follow when selecting the appropriate assertion to use in code?'''
    ),
    HumanMessagePromptTemplate.from_template("Summarize those rules and methods."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Based on the rules outlined, choose the correct assertion to replace <AssertPlaceHolder> in the code below.
        Provide only the assertion statement.

        Code: {code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------------------------------------------------------------------
assert_generation_template_step_back_var17 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Could you list the important factors or criteria you consider when determining the correct assertion to use in place of one in the code?'''
    ),
    HumanMessagePromptTemplate.from_template("Outline these factors and criteria."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Using the factors outlined, decide the assertion that should replace <AssertPlaceHolder> in the provided code.
        Return only the assertion statement.

        Code: {code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------------------------------------------------------------------

assert_generation_template_step_back_var18 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Please clarify the criteria or principles you follow when determining which assertion is appropriate to replace within a block of code.'''
    ),
    HumanMessagePromptTemplate.from_template("Enumerate these criteria and principles."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Based on these criteria, select the assertion that should replace <AssertPlaceHolder> in the code below.
        Return only the assertion statement.

        Code: {code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

