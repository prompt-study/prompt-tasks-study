
bug_fixing_template_universal_self_consistency = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Analyze the given code step by step to identify and fix any bugs."
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have generated the following responses to the question above: {output_text}\n select the most consistent response based on majority consensus"),
    AIMessagePromptTemplate.from_template('prompt'),
])

bug_fixing_template_universal_self_consistency_1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Examine the supplied code sequentially to pinpoint and correct any potential bugs."
    ),
    HumanMessagePromptTemplate.from_template("Code snippet:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have produced these responses for the question: {output_text}\n Please select the answer that most aligns with the majority."),
    AIMessagePromptTemplate.from_template('prompt'),
])

bug_fixing_template_universal_self_consistency_2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Review the provided code step by step to uncover and fix any errors."
    ),
    HumanMessagePromptTemplate.from_template("Provided Code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("The following outputs have been generated for the previous query: {output_text}\n Choose the response that appears most consistently."),
    AIMessagePromptTemplate.from_template('prompt'),
])

bug_fixing_template_universal_self_consistency_3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Inspect the code in a methodical manner to determine and resolve any bugs."
    ),
    HumanMessagePromptTemplate.from_template("Code sample:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have compiled several responses for the query above: {output_text}\n Pick the response that is most widely agreed upon."),
    AIMessagePromptTemplate.from_template('prompt'),
])

bug_fixing_template_universal_self_consistency_4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Go through the code piece by piece to detect and repair any bugs."
    ),
    HumanMessagePromptTemplate.from_template("Please find the code below:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("Here are multiple outputs generated for the mentioned question: {output_text}\n Select the response that reflects the broadest consensus."),
    AIMessagePromptTemplate.from_template('prompt'),
])

bug_fixing_template_universal_self_consistency_5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Break down the given code step by step to identify and remedy any bugs."
    ),
    HumanMessagePromptTemplate.from_template("The code is as follows:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have produced several answers to the above question: {output_text}\n Choose the one that demonstrates the highest agreement among responses."),
    AIMessagePromptTemplate.from_template('prompt'),
])

bug_fixing_template_universal_self_consistency_6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Examine the code methodically to uncover and rectify any errors."
    ),
    HumanMessagePromptTemplate.from_template("See the following code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("The responses generated for the earlier question are as follows: {output_text}\n Please select the one that reflects the majority view."),
    AIMessagePromptTemplate.from_template('prompt'),
])

bug_fixing_template_universal_self_consistency_7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Evaluate the supplied code in a systematic manner to identify and correct errors."
    ),
    HumanMessagePromptTemplate.from_template("Refer to the code below:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have generated a set of responses for the previous inquiry: {output_text}\n Kindly choose the response that holds the majority consensus."),
    AIMessagePromptTemplate.from_template('prompt'),
])

bug_fixing_template_universal_self_consistency_8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Assess the given code in detailed steps to locate and fix any bugs."
    ),
    HumanMessagePromptTemplate.from_template("Here is the code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("The following outcomes have been derived for the earlier question: {output_text}\n Please pick the response that most familiarly represents consensus."),
    AIMessagePromptTemplate.from_template('prompt'),
])

bug_fixing_template_universal_self_consistency_9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Step through the code meticulously to spot and correct any errors."
    ),
    HumanMessagePromptTemplate.from_template("Code provided:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have listed multiple outputs in response to the query: {output_text}\n Choose the answer that exhibits the greatest common agreement."),
    AIMessagePromptTemplate.from_template('prompt'),
])

bug_fixing_template_universal_self_consistency_10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Scrutinize the code sequentially to search for and mend any bugs."
    ),
    HumanMessagePromptTemplate.from_template("Script:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("Below are the results generated for the query above: {output_text}\n Select the one that aligns best with the majority."),
    AIMessagePromptTemplate.from_template('prompt'),
])

bug_fixing_template_universal_self_consistency_11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Go through the code systematically to detect and resolve any anomalies."
    ),
    HumanMessagePromptTemplate.from_template("Code example:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have prepared these responses for the aforementioned question: {output_text}\n Please choose the response that signifies the majority opinion."),
    AIMessagePromptTemplate.from_template('prompt'),
])

bug_fixing_template_universal_self_consistency_12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Methodically analyze the code to find and fix any issues."
    ),
    HumanMessagePromptTemplate.from_template("Here's the code snippet:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("Below are several answers produced for the previous inquiry: {output_text}\n Select the answer that best reflects consensus."),
    AIMessagePromptTemplate.from_template('prompt'),
])

bug_fixing_template_universal_self_consistency_13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Analyze the code in a sequential manner to identify and amend any bugs."
    ),
    HumanMessagePromptTemplate.from_template("Presented Code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have generated a set of responses for the question above: {output_text}\n Please pick the answer that most consistently shows majority agreement."),
    AIMessagePromptTemplate.from_template('prompt'),
])

bug_fixing_template_universal_self_consistency_14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Examine the code step-by-step to detect and remedy any errors."
    ),
    HumanMessagePromptTemplate.from_template("Contained Code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("Here are the outcomes provided for the earlier question: {output_text}\n Choose the option that corresponds to the majority consensus."),
    AIMessagePromptTemplate.from_template('prompt'),
])
