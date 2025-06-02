
──────────────────────────────
Variation 0 (Original):
──────────────────────────────
mutant_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Generate a mutant of the given code snippet by introducing small, meaningful changes."
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template('I have generated the following responses to the question above: {output_text}\n select the most consistent response based on majority consensus'),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 1:
──────────────────────────────
mutant_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Create an altered version of the provided code snippet by applying subtle yet significant modifications."
    ),
    HumanMessagePromptTemplate.from_template("Here is the code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have produced these answers based on the previous question: {output_text}\n Please choose the response that aligns best with the majority view."),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 2:
──────────────────────────────
mutant_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Produce a variant of the given code by introducing minor, yet effective, adjustments."
    ),
    HumanMessagePromptTemplate.from_template("Code provided:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("Below are the responses I generated for the earlier query: {output_text}\n Identify and select the answer with the closest common agreement."),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 3:
──────────────────────────────
mutant_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Form a mutant version of the supplied code snippet via careful, minor alterations."
    ),
    HumanMessagePromptTemplate.from_template("The code is as follows:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have created the following outputs in response to the above problem: {output_text}\n Select the answer that shows the strongest consensus."),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 4:
──────────────────────────────
mutant_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Devise an alternative version of the provided code segment by implementing subtle, deliberate tweaks."
    ),
    HumanMessagePromptTemplate.from_template("Provided Code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("These are the outputs I produced for the preceding question: {output_text}\n Please select the response that best matches the majority opinion."),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 5:
──────────────────────────────
mutant_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Invent a mutated version of the code snippet by incorporating minor yet impactful changes."
    ),
    HumanMessagePromptTemplate.from_template("Here is the provided code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I produced these responses for the above query: {output_text}\n Choose the response that exhibits the highest level of consensus."),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 6:
──────────────────────────────
mutant_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Create a code mutant by applying subtle but significant modifications to the snippet provided."
    ),
    HumanMessagePromptTemplate.from_template("The code is given below:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have compiled the following responses in reply to the above query: {output_text}\n Select the candidate that reflects the majority opinion."),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 7:
──────────────────────────────
mutant_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Generate an altered version of the presented code snippet by applying minor, significant modifications."
    ),
    HumanMessagePromptTemplate.from_template("Code snippet:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have generated these answers for the mentioned query: {output_text}\n Please select the response that is most widely supported."),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 8:
──────────────────────────────
mutant_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Craft a variant of the provided code snippet by making slight, yet meaningful, revisions."
    ),
    HumanMessagePromptTemplate.from_template("Here’s the code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("The following responses were generated for the previous prompt: {output_text}\n Identify the one with the strongest consensus."),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 9:
──────────────────────────────
mutant_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Develop a mutant form of the given code by integrating minor, yet purposeful, modifications."
    ),
    HumanMessagePromptTemplate.from_template("Here is the snippet:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have formulated these responses to the earlier query: {output_text}\n Choose the version that reflects the majority agreement."),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 10:
──────────────────────────────
mutant_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Construct a mutated variant of the provided code snippet by applying small but intentional adjustments."
    ),
    HumanMessagePromptTemplate.from_template("Please review the code below:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I generated these answers for the prior question: {output_text}\n Pick the one that most closely aligns with the overall consensus."),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 11:
──────────────────────────────
mutant_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Formulate a modified version of the supplied code by incorporating subtle, targeted adjustments."
    ),
    HumanMessagePromptTemplate.from_template("Access the code here:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("Below are the responses I produced for the previous question: {output_text}\n Please select the answer that best reflects majority consensus."),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 12:
──────────────────────────────
mutant_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Evolve the provided code snippet into a mutant by incorporating minor yet effective alterations."
    ),
    HumanMessagePromptTemplate.from_template("Here is the code snippet:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have generated the following candidate responses from the previous prompt: {output_text}\n Identify the option supported by the majority."),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 13:
──────────────────────────────
mutant_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Alter the given code into a mutant version by introducing small, impactful modifications."
    ),
    HumanMessagePromptTemplate.from_template("Code details:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I came up with the following outputs for the above query: {output_text}\n Please select the option that exhibits majority consensus."),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 14:
──────────────────────────────
mutant_generation_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Develop a variant of the provided code by introducing slight, purposeful alterations."
    ),
    HumanMessagePromptTemplate.from_template("Code snippet provided:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have produced these responses in reply to the previous question: {output_text}\n Choose the answer that best represents common agreement."),
    AIMessagePromptTemplate.from_template('prompt'),
])
