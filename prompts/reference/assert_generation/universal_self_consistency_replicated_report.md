
──────────────────────────────
Variation 0:
──────────────────────────────
assert_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Analyze the given code snippet and generate the correct assertion statement to replace <AssertPlaceHolder>."
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have generated the following responses to the question above: {output_text}\n select the most consistent response based on majority consensus"),
    AIMessagePromptTemplate.from_template('prompt_with_output_text'),
])

──────────────────────────────
Variation 1:
──────────────────────────────
assert_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Inspect the provided code snippet and craft the appropriate assertion statement to substitute <AssertPlaceHolder>."
    ),
    HumanMessagePromptTemplate.from_template("Here’s the code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I produced these answers for the aforementioned query: {output_text}\n choose the answer most in line with the prevailing consensus."),
    AIMessagePromptTemplate.from_template('prompt_with_output_text'),
])

──────────────────────────────
Variation 2:
──────────────────────────────
assert_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Examine the code snippet provided and create a valid assertion statement to replace the placeholder <AssertPlaceHolder>."
    ),
    HumanMessagePromptTemplate.from_template("Source Code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("Below are the responses I derived for the above question: {output_text}\n pick the answer that best matches the majority’s opinion."),
    AIMessagePromptTemplate.from_template('prompt_with_output_text'),
])

──────────────────────────────
Variation 3:
──────────────────────────────
assert_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Review the supplied code snippet and formulate the correct assertion statement meant to replace <AssertPlaceHolder>."
    ),
    HumanMessagePromptTemplate.from_template("Code sample:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have produced the following outputs for the query: {output_text}\n select the response that most aligns with consensus."),
    AIMessagePromptTemplate.from_template('prompt_with_output_text'),
])

──────────────────────────────
Variation 4:
──────────────────────────────
assert_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Evaluate the included code snippet and generate an accurate assertion statement to stand in for <AssertPlaceHolder>."
    ),
    HumanMessagePromptTemplate.from_template("Provided Code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("These are the responses I came up with for the above question: {output_text}\n choose the one that reflects the majority's view."),
    AIMessagePromptTemplate.from_template('prompt_with_output_text'),
])

──────────────────────────────
Variation 5:
──────────────────────────────
assert_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Assess the given code snippet and derive the proper assertion statement to take the place of <AssertPlaceHolder>."
    ),
    HumanMessagePromptTemplate.from_template("Here is the snippet:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("Below are the candidate responses for the question above: {output_text}\n select the option that resonates with the majority's consensus."),
    AIMessagePromptTemplate.from_template('prompt_with_output_text'),
])

──────────────────────────────
Variation 6:
──────────────────────────────
assert_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Inspect the provided snippet of code and construct the correct assertion statement to replace <AssertPlaceHolder>."
    ),
    HumanMessagePromptTemplate.from_template("Snippet:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have assembled these responses to the prior query: {output_text}\n choose the one that best reflects group consensus."),
    AIMessagePromptTemplate.from_template('prompt_with_output_text'),
])

──────────────────────────────
Variation 7:
──────────────────────────────
assert_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Critique the following code snippet and produce the proper assertion statement to replace the <AssertPlaceHolder> marker."
    ),
    HumanMessagePromptTemplate.from_template("Listing Code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have compiled these answers for the earlier question: {output_text}\n select the answer that mirrors the majority opinion."),
    AIMessagePromptTemplate.from_template('prompt_with_output_text'),
])

──────────────────────────────
Variation 8:
──────────────────────────────
assert_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Review the code snippet presented and produce the appropriate assertion statement to stand in for <AssertPlaceHolder>."
    ),
    HumanMessagePromptTemplate.from_template("Code Details:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I generated these potential answers for the above question: {output_text}\n pick the one most in line with overall consensus."),
    AIMessagePromptTemplate.from_template('prompt_with_output_text'),
])

──────────────────────────────
Variation 9:
──────────────────────────────
assert_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Examine the accompanying code snippet and produce a valid assertion statement to substitute <AssertPlaceHolder>."
    ),
    HumanMessagePromptTemplate.from_template("Source Code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I constructed the following answers for the given query: {output_text}\n select the response that best matches the majority view."),
    AIMessagePromptTemplate.from_template('prompt_with_output_text'),
])

──────────────────────────────
Variation 10:
──────────────────────────────
assert_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Look at the provided code snippet and formulate the accurate assertion statement to replace <AssertPlaceHolder>."
    ),
    HumanMessagePromptTemplate.from_template("See the code below:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("The following responses were generated for the prior question: {output_text}\n pick the reply that corresponds with majority agreement."),
    AIMessagePromptTemplate.from_template('prompt_with_output_text'),
])

──────────────────────────────
Variation 11:
──────────────────────────────
assert_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Examine the included snippet and write the appropriate assertion statement to swap out <AssertPlaceHolder>."
    ),
    HumanMessagePromptTemplate.from_template("Displayed Code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("Below, you will find my generated responses for the question above: {output_text}\n select the one that aligns with the majority."),
    AIMessagePromptTemplate.from_template('prompt_with_output_text'),
])

──────────────────────────────
Variation 12:
──────────────────────────────
assert_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Inspect the given snippet of code and derive the correct assertion statement intended to replace <AssertPlaceHolder>."
    ),
    HumanMessagePromptTemplate.from_template("Presented Code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have come up with these responses for the previous question: {output_text}\n choose the one most in tune with majority consensus."),
    AIMessagePromptTemplate.from_template('prompt_with_output_text'),
])

──────────────────────────────
Variation 13:
──────────────────────────────
assert_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Analyze this code snippet and produce the proper assertion statement that should replace <AssertPlaceHolder>."
    ),
    HumanMessagePromptTemplate.from_template("Code provided:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("The following are the responses I generated for the above query: {output_text}\n pick the one that reflects the group consensus."),
    AIMessagePromptTemplate.from_template('prompt_with_output_text'),
])

──────────────────────────────
Variation 14:
──────────────────────────────
assert_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Review the attached code snippet and generate a fitting assertion statement to take the place of <AssertPlaceHolder>."
    ),
    HumanMessagePromptTemplate.from_template("Here’s the provided code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have assembled these responses to the query above: {output_text}\n choose the answer that best corresponds with the majority."),
    AIMessagePromptTemplate.from_template('prompt_with_output_text'),
])
