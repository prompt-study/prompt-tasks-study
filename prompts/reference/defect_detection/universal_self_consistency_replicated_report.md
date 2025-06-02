
defect_detection_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Analyze the given code to determine if it contains a defect. Provide the final answer as ###TRUE### (defective) or ###FALSE### (not defective)."
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have generated the following responses to the question above: {output_text}\n select the most consistent response based on majority consensus"),
    AIMessagePromptTemplate.from_template('prompt'),
])

defect_detection_template_1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Examine the provided code to check for any defects. Conclude your evaluation with ###TRUE### for defective or ###FALSE### for defect-free."
    ),
    HumanMessagePromptTemplate.from_template("Here's the code snippet:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("Below are various answers I obtained for the query: {output_text}\n choose the answer that most consistently aligns with the majority."),
    AIMessagePromptTemplate.from_template('prompt'),
])


defect_detection_template_2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Inspect the supplied code to decide if there is any defect present. Answer with ###TRUE### if a defect is found, or ###FALSE### if it is not."
    ),
    HumanMessagePromptTemplate.from_template("Presented code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I am showing the following outputs based on the earlier question: {output_text}\n please select the most widely agreed-upon response."),
    AIMessagePromptTemplate.from_template('prompt'),
])

defect_detection_template_3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Review the instance of code provided to ascertain whether it includes an error. Return ###TRUE### (for error detected) or ###FALSE### (for no error)."
    ),
    HumanMessagePromptTemplate.from_template("Please find the code below:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I've compiled these responses from the previous inquiry: {output_text}\n pick the one that the majority supports best."),
    AIMessagePromptTemplate.from_template('prompt'),
])


defect_detection_template_4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Evaluate the code snippet given to determine if any defect exists. Your answer should be either ###TRUE### (if defective) or ###FALSE### (if not defective)."
    ),
    HumanMessagePromptTemplate.from_template("The following is the code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have gathered the below responses to the prior question: {output_text}\n kindly choose the response most in agreement with the group."),
    AIMessagePromptTemplate.from_template('prompt'),
])


defect_detection_template_5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Assess the code provided for potential defects. Conclude by indicating ###TRUE### if a defect is found, or ###FALSE### if it is not."
    ),
    HumanMessagePromptTemplate.from_template("Here is the code block:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("These are the responses I generated for the query: {output_text}\n select the response that fits the majority consensus best."),
    AIMessagePromptTemplate.from_template('prompt'),
])

defect_detection_template_6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Scrutinize the code shown to you to determine whether it has any defects. Answer with ###TRUE### if a problem is identified or ###FALSE### if not."
    ),
    HumanMessagePromptTemplate.from_template("Check out this code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I produced the following answers for the question above: {output_text}\n please indicate the answer that reflects the consensus most accurately."),
    AIMessagePromptTemplate.from_template('prompt'),
])


defect_detection_template_7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Examine the attached code snippet to identify any defects. Finish your assessment with ###TRUE### if there's an error and ###FALSE### if no error exists."
    ),
    HumanMessagePromptTemplate.from_template("The code is as follows:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("These responses have been generated based on the previous problem: {output_text}\n now select the response that most aligns with the majority view."),
    AIMessagePromptTemplate.from_template('prompt'),
])

defect_detection_template_8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Look over the provided code to decide if it harbors a defect. Deliver your conclusion as ###TRUE### for a defect or ###FALSE### for absence of defect."
    ),
    HumanMessagePromptTemplate.from_template("Code provided:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("Below you see the generated outputs for the question: {output_text}\n pick the response that is most consistently favored."),
    AIMessagePromptTemplate.from_template('prompt'),
])

defect_detection_template_9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Review the given code sample to ascertain if any defect exists. Indicate your final decision with ###TRUE### (defect present) or ###FALSE### (defect absent)."
    ),
    HumanMessagePromptTemplate.from_template("Here’s the code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have generated these possible answers to the query: {output_text}\n select the answer which resonates best with the general consensus."),
    AIMessagePromptTemplate.from_template('prompt'),
])


defect_detection_template_10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Go through the supplied code carefully to determine if it is flawed. Present your final verdict as ###TRUE### (if flawed) or ###FALSE### (if flawless)."
    ),
    HumanMessagePromptTemplate.from_template("Code snippet provided here:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I obtained the following outputs from the previous inquiry: {output_text}\n please select the one that meets the majority agreement."),
    AIMessagePromptTemplate.from_template('prompt'),
])


defect_detection_template_11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Assess the attached code example to detect any potential defects. Conclude with ###TRUE### if an issue is found, or ###FALSE### if none is present."
    ),
    HumanMessagePromptTemplate.from_template("Below is the code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I’ve compiled a number of answers from the earlier question: {output_text}\n please choose the answer that the majority endorses."),
    AIMessagePromptTemplate.from_template('prompt'),
])


defect_detection_template_12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Examine the provided code excerpt to determine whether it contains any issues. End your analysis by stating ###TRUE### if a defect exists, else ###FALSE###."
    ),
    HumanMessagePromptTemplate.from_template("Please review the following code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("Here are the responses produced for the above query: {output_text}\n kindly select the one that most people agree with."),
    AIMessagePromptTemplate.from_template('prompt'),
])


defect_detection_template_13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Investigate the given block of code and decide if it has any defects. Your answer should be either ###TRUE### (if defective) or ###FALSE### (if not defective)."
    ),
    HumanMessagePromptTemplate.from_template("Code sample:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have these responses for the question above: {output_text}\n select the one that matches the majority opinion."),
    AIMessagePromptTemplate.from_template('prompt'),
])


defect_detection_template_14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Inspect the code provided to see if any flaw is present. Conclude your evaluation by stating ###TRUE### for a found defect, or ###FALSE### if it is defect-free."
    ),
    HumanMessagePromptTemplate.from_template("Here is the code provided:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I've collected the following outputs in response to the previous question: {output_text}\n please choose the answer that reflects the majority consensus."),
    AIMessagePromptTemplate.from_template('prompt'),
])
