Below are 15 variations of the original template. Variation 0 is identical to the original, and Variations 1–14 contain rephrased strings for the SystemMessagePromptTemplate and HumanMessagePromptTemplate entries. Note that the AIMessagePromptTemplate entries remain unchanged and the variable name stays as clone_detection_template_.

──────────────────────────── Variation 0 ────────────────────────────
clone_detection_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Compare the two code snippets to determine if they are functionally identical (clones), provide an answer: ###TRUE### (clones) or ###FALSE### (not clones)."
    ),
    HumanMessagePromptTemplate.from_template(
        "Code Snippet 1:\n{code_snippet1}\n\nCode Snippet 2:\n{code_snippet2}"
    ),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have generated the following responses to the question above: {output_text}\n select the most consistent response based on majority consensus"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 1 ────────────────────────────
clone_detection_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Evaluate the two code fragments to decide whether they function identically (i.e., are clones). Respond with ###TRUE### if they are clones or ###FALSE### if they are not."
    ),
    HumanMessagePromptTemplate.from_template(
        "Snippet 1 of the code:\n{code_snippet1}\n\nSnippet 2 of the code:\n{code_snippet2}"
    ),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("The responses below were generated in answer to the question above: {output_text}\nPlease choose the response that is most consistently supported by the majority."),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 2 ────────────────────────────
clone_detection_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Examine these two pieces of code and determine if they perform the same functions (clones). Your answer should be ###TRUE### for clones and ###FALSE### if they differ."
    ),
    HumanMessagePromptTemplate.from_template(
        "First Code Snippet:\n{code_snippet1}\n\nSecond Code Snippet:\n{code_snippet2}"
    ),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I produced the following answers for the previous question: {output_text}\nNow, pick the response with the highest consensus."),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 3 ────────────────────────────
clone_detection_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Assess the following two code samples to establish if they are functionally equivalent clones. Answer with ###TRUE### if they are the same clone, or ###FALSE### if they are not."
    ),
    HumanMessagePromptTemplate.from_template(
        "Code Sample 1:\n{code_snippet1}\n\nCode Sample 2:\n{code_snippet2}"
    ),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("Below are the generated answers to the prior question: {output_text}\nChoose the answer that appears most consistent with the majority."),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 4 ────────────────────────────
clone_detection_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Review the given code snippets and ascertain whether they are functionally identical. Use ###TRUE### for clones and ###FALSE### if not."
    ),
    HumanMessagePromptTemplate.from_template(
        "First snippet:\n{code_snippet1}\n\nSecond snippet:\n{code_snippet2}"
    ),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("Here are the possible responses to the question stated above: {output_text}\nSelect the response that aligns with the majority consensus."),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 5 ────────────────────────────
clone_detection_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Inspect both code segments to verify if they execute in the same manner (clones). Provide the answer as ###TRUE### (if clones) or ###FALSE### (if not)."
    ),
    HumanMessagePromptTemplate.from_template(
        "Displayed below are two code examples. Snippet 1:\n{code_snippet1}\n\nSnippet 2:\n{code_snippet2}"
    ),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("Displayed are the responses generated for the above query: {output_text}\nKindly select the answer that is most in line with the majority view."),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 6 ────────────────────────────
clone_detection_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Compare these two code blocks to check if they operate identically, meaning they are clones. Indicate your answer with ###TRUE### for clones and ###FALSE### for non-clones."
    ),
    HumanMessagePromptTemplate.from_template(
        "Here is the first code snippet:\n{code_snippet1}\n\nAnd here is the second code snippet:\n{code_snippet2}"
    ),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I present the following answers to the earlier question: {output_text}\nPick the answer that reflects the consensus among them."),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 7 ────────────────────────────
clone_detection_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Analyze the pair of code excerpts to see if they are functionally the same (i.e., clones). Answer either ###TRUE### for identical clones or ###FALSE### if they differ."
    ),
    HumanMessagePromptTemplate.from_template(
        "Code Example 1:\n{code_snippet1}\n\nCode Example 2:\n{code_snippet2}"
    ),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("The following answers have been generated for the question above: {output_text}\nPlease identify the answer that most strongly aligns with the majority."),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 8 ────────────────────────────
clone_detection_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Look at the two provided code segments to decide if they are functionally equivalent clones. Your answer should be either ###TRUE### or ###FALSE###."
    ),
    HumanMessagePromptTemplate.from_template(
        "Presented code snippet 1:\n{code_snippet1}\n\nPresented code snippet 2:\n{code_snippet2}"
    ),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("These responses were produced in reply to the previous question: {output_text}\nChoose the one that is most consistent with the majority."),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 9 ────────────────────────────
clone_detection_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Determine if the two presented code snippets have the same functionality (i.e., clones) and answer with ###TRUE### if they do, or ###FALSE### otherwise."
    ),
    HumanMessagePromptTemplate.from_template(
        "Snippet One:\n{code_snippet1}\n\nSnippet Two:\n{code_snippet2}"
    ),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have compiled these responses for the earlier question: {output_text}\nSelect the option that best matches the majority consensus."),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 10 ───────────────────────────
clone_detection_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Verify whether these two code snippets operate identically as clones. Answer with ###TRUE### if they are clones; otherwise, respond with ###FALSE###."
    ),
    HumanMessagePromptTemplate.from_template(
        "Below is the first code snippet:\n{code_snippet1}\n\nBelow is the second code snippet:\n{code_snippet2}"
    ),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("Here are several answers for the previously stated question: {output_text}\nPick the one that demonstrates the highest consensus."),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 11 ───────────────────────────
clone_detection_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Scrutinize the two code examples to decide if they are functionally the same (clones). Provide your answer as ###TRUE### if they match, or ###FALSE### if they do not."
    ),
    HumanMessagePromptTemplate.from_template(
        "The following is Code Snippet 1:\n{code_snippet1}\n\nAnd this is Code Snippet 2:\n{code_snippet2}"
    ),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("The following responses were generated for your preceding query: {output_text}\nIdentify the response that best represents the majority view."),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 12 ───────────────────────────
clone_detection_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Compare these two blocks of code to determine if they perform identically (i.e., clones). Answer by selecting ###TRUE### for clones or ###FALSE### if otherwise."
    ),
    HumanMessagePromptTemplate.from_template(
        "Refer to the first snippet:\n{code_snippet1}\n\nand to the second snippet:\n{code_snippet2}"
    ),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I created these responses for the question above: {output_text}\nNow, select the most consistently supported answer."),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 13 ───────────────────────────
clone_detection_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Examine these two code excerpts to ascertain if their functionality is identical, denoting them as clones. If so, respond with ###TRUE###; if not, use ###FALSE###."
    ),
    HumanMessagePromptTemplate.from_template(
        "Observe Code Snippet 1:\n{code_snippet1}\n\nand Code Snippet 2:\n{code_snippet2}"
    ),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("The following answers were derived from the previous question: {output_text}\nPlease choose the answer that reflects majority agreement."),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 14 ───────────────────────────
clone_detection_template_ = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Evaluate whether the two code snippets are clones, meaning functionally identical. Your response should be ###TRUE### if they match, or ###FALSE### if they differ."
    ),
    HumanMessagePromptTemplate.from_template(
        "Take a look at the following: Code Snippet 1:\n{code_snippet1}\n\nCode Snippet 2:\n{code_snippet2}"
    ),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have listed the responses generated for the above query: {output_text}\nSelect the one answer that is most in line with the majority consensus."),
    AIMessagePromptTemplate.from_template('prompt'),
])

Each variation keeps the overall structure and message order intact while only rephrasing the strings in the System and Human messages.