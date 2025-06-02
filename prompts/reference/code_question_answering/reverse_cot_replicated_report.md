code_question_answering_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial Judgment
    SystemMessagePromptTemplate.from_template(
        '''Examine whether the code below completely answers the question.
Reply with only ###TRUE### if it is entirely correct or ###FALSE### if it falls short.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}

Task: Judge the correctness of this code in relation to the question.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Question Paraphrasing
    HumanMessagePromptTemplate.from_template(
        '''Based on your judgment, paraphrase the question in your own words.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''Now, compare your paraphrase with the original question.
List any omissions or extra elements that might affect the evaluation.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision Process
    HumanMessagePromptTemplate.from_template(
        '''Revise your initial judgment so that it accurately reflects whether the code answers the question.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Conclusive Evaluation
    HumanMessagePromptTemplate.from_template(
        '''Finally, state your final correctness evaluation as either ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 1:

code_question_answering_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial Judgment
    SystemMessagePromptTemplate.from_template(
        '''Review the code below and determine if it fully addresses the question.
Answer solely with ###TRUE### if the code is completely correct, otherwise reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}

Task: Evaluate whether this code meets the requirements of the question.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Question Paraphrasing
    HumanMessagePromptTemplate.from_template(
        '''Based on your evaluation, express the question in your own words.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''Now, contrast your reworded version with the original question.
Identify any missing details or additional elements that could influence the assessment.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision Process
    HumanMessagePromptTemplate.from_template(
        '''Adjust your initial evaluation so that it precisely reflects whether the code answers the question.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Conclusive Evaluation
    HumanMessagePromptTemplate.from_template(
        '''Finally, provide your final assessment as either ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 2:

code_question_answering_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial Judgment
    SystemMessagePromptTemplate.from_template(
        '''Please determine if the code snippet below fully responds to the query.
Your response should be strictly ###TRUE### for complete accuracy, or ###FALSE### if something is lacking.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}

Task: Decide whether the code correctly satisfies the demands of the question.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Question Paraphrasing
    HumanMessagePromptTemplate.from_template(
        '''Using your judgment, restate the question in your own terms.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''Now, compare your restatement to the original question.
Note any discrepancies, including missing or additional information.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision Process
    HumanMessagePromptTemplate.from_template(
        '''Refine your initial decision so that it accurately indicates if the code answers the question.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Conclusive Evaluation
    HumanMessagePromptTemplate.from_template(
        '''Finally, declare your final evaluation as either ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 3:

code_question_answering_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial Judgment
    SystemMessagePromptTemplate.from_template(
        '''Examine the following code and verify if it completely answers the question.
Respond with only ###TRUE### if it does or with ###FALSE### if there are shortcomings.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}

Task: Determine whether the provided code fully responds to the question.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Question Paraphrasing
    HumanMessagePromptTemplate.from_template(
        '''Based on your decision, rephrase the question using your own words.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''Now, analyze your rephrasing alongside the original question.
List any elements that are either omitted or unnecessarily added.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision Process
    HumanMessagePromptTemplate.from_template(
        '''Modify your initial decision so that it more accurately reflects whether the code meets the question.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Conclusive Evaluation
    HumanMessagePromptTemplate.from_template(
        '''Finally, present your final verdict as either ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 4:

code_question_answering_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial Judgment
    SystemMessagePromptTemplate.from_template(
        '''Assess the code below to see whether it fully answers the question.
Reply strictly with ###TRUE### if it is entirely correct, or with ###FALSE### if any part is missing.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}

Task: Judge if the code sufficiently addresses the posed question.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Question Paraphrasing
    HumanMessagePromptTemplate.from_template(
        '''Using your assessment, express the question in alternate wording.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''Now, compare your alternate wording with the original question.
Highlight any differences such as missing points or extraneous details.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision Process
    HumanMessagePromptTemplate.from_template(
        '''Revise your earlier judgment so that it clearly indicates if the code answers the question.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Conclusive Evaluation
    HumanMessagePromptTemplate.from_template(
        '''Finally, summarize your ultimate evaluation as either ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 5:

code_question_answering_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial Judgment
    SystemMessagePromptTemplate.from_template(
        '''Determine if the following code completely resolves the question.
Answer only with ###TRUE### for a full match or with ###FALSE### if it falls short.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}

Task: Evaluate if the code directly and entirely answers the question.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Question Paraphrasing
    HumanMessagePromptTemplate.from_template(
        '''Based on your evaluation, rewrite the question in your own words.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''Now, compare your rewritten version with the original question.
Note any aspects that are missing or unnecessarily included.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision Process
    HumanMessagePromptTemplate.from_template(
        '''Adjust your initial evaluation so that it truly reflects whether the code responds to the question.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Conclusive Evaluation
    HumanMessagePromptTemplate.from_template(
        '''Finally, state your definitive answer as either ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 6:

code_question_answering_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial Judgment
    SystemMessagePromptTemplate.from_template(
        '''Scrutinize the code shown below and determine if it completely addresses the query.
Reply only with ###TRUE### if the code is fully correct, or with ###FALSE### if anything is missing.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}

Task: Judge whether the code answers the question as required.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Question Paraphrasing
    HumanMessagePromptTemplate.from_template(
        '''Based on your analysis, rephrase the question in your own phrasing.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''Now, compare your rephrasing with the original question.
Highlight any missing aspects or additional details that could influence the result.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision Process
    HumanMessagePromptTemplate.from_template(
        '''Modify your initial judgment so that it precisely represents whether the code fulfills the question.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Conclusive Evaluation
    HumanMessagePromptTemplate.from_template(
        '''Finally, provide your final determination as either ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 7:

code_question_answering_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial Judgment
    SystemMessagePromptTemplate.from_template(
        '''Please inspect the following code and decide if it fully answers the corresponding question.
Respond solely with ###TRUE### if it is complete, or with ###FALSE### if it is lacking any aspect.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question Details:
{question}

Code:
{code}

Task: Determine if the provided code meets all aspects of the question.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Question Paraphrasing
    HumanMessagePromptTemplate.from_template(
        '''Using your decision, paraphrase the question in your own manner.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''Now, compare your paraphrase with the original question.
Outline any discrepancies, including extra or missing information.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision Process
    HumanMessagePromptTemplate.from_template(
        '''Reassess and adjust your earlier judgment so it accurately reflects the code’s effectiveness in answering the question.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Conclusive Evaluation
    HumanMessagePromptTemplate.from_template(
        '''Finally, conclude by stating your evaluation as either ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 8:

code_question_answering_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial Judgment
    SystemMessagePromptTemplate.from_template(
        '''Assess the code below to determine if it fully responds to the question.
Your answer should be solely ###TRUE### when complete, or ###FALSE### when incomplete.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}

Task: Decide if the code effectively answers the question posed.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Question Paraphrasing
    HumanMessagePromptTemplate.from_template(
        '''Now, reword the question in your own language based on your assessment.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''Then, compare your reworded question with the original.
Identify any missing details or extraneous parts that may affect the evaluation.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision Process
    HumanMessagePromptTemplate.from_template(
        '''Refine your earlier judgment so that it clearly shows whether the code answers the question.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Conclusive Evaluation
    HumanMessagePromptTemplate.from_template(
        '''Finally, express your final verdict as either ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 9:

code_question_answering_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial Judgment
    SystemMessagePromptTemplate.from_template(
        '''Investigate the code below and determine whether it thoroughly answers the question.
Respond exclusively with ###TRUE### if correct, or with ###FALSE### if it is lacking.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''The Question:
{question}

The Code:
{code}

Task: Evaluate if the code genuinely addresses the question.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Question Paraphrasing
    HumanMessagePromptTemplate.from_template(
        '''Based on your analysis, rewrite the question in your own words.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''Next, compare your rewritten question with the original.
Point out any significant differences, whether missing or extra details.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision Process
    HumanMessagePromptTemplate.from_template(
        '''Revise your initial assessment to ensure it faithfully reflects if the code answers the question.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Conclusive Evaluation
    HumanMessagePromptTemplate.from_template(
        '''Finally, state your final decision as either ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 10:

code_question_answering_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial Judgment
    SystemMessagePromptTemplate.from_template(
        '''Review the following code and assess whether it completely answers the provided question.
Your answer should be solely ###TRUE### if all conditions are met or ###FALSE### if not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question Overview:
{question}

Code:
{code}

Task: Determine if the code satisfactorily addresses every part of the question.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Question Paraphrasing
    HumanMessagePromptTemplate.from_template(
        '''Now, rephrase the question in your own wording based on your assessment.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''Then, compare your rephrasing with the original question.
Detail any missing or additional aspects that might affect the evaluation.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision Process
    HumanMessagePromptTemplate.from_template(
        '''Update your initial assessment so that it exactly reflects if the code fully answers the question.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Conclusive Evaluation
    HumanMessagePromptTemplate.from_template(
        '''Finally, conclude by providing your final evaluation as either ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 11:

code_question_answering_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial Judgment
    SystemMessagePromptTemplate.from_template(
        '''Consider the following code and decide if it completely satisfies the question.
Answer exclusively with ###TRUE### if it does, or with ###FALSE### if any element is missing.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Presented Question:
{question}

Displayed Code:
{code}

Task: Assess whether the code accurately and fully responds to the question.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Question Paraphrasing
    HumanMessagePromptTemplate.from_template(
        '''Now, paraphrase the question in your own words as per your judgment.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''Then, compare your paraphrase with the original question.
List any details that are missing or any extra information that could influence the result.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision Process
    HumanMessagePromptTemplate.from_template(
        '''Rework your initial judgment so it accurately represents whether the code answers the question.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Conclusive Evaluation
    HumanMessagePromptTemplate.from_template(
        '''Finally, state your final judgment as either ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 12:

code_question_answering_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial Judgment
    SystemMessagePromptTemplate.from_template(
        '''Analyze the code below and decide if it fully answers the given question.
Provide your response solely as ###TRUE### if it is comprehensive, or as ###FALSE### if it falls short.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}

Task: Evaluate whether the code thoroughly addresses the question.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Question Paraphrasing
    HumanMessagePromptTemplate.from_template(
        '''Based on your analysis, express the question in your own words.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''Next, compare your version with the original question.
Identify any missing parts or added details that could affect the evaluation.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision Process
    HumanMessagePromptTemplate.from_template(
        '''Revise your initial analysis so that it clearly reflects whether the code answers the question.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Conclusive Evaluation
    HumanMessagePromptTemplate.from_template(
        '''Finally, provide your final evaluation as either ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 13:

code_question_answering_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial Judgment
    SystemMessagePromptTemplate.from_template(
        '''Inspect the following code snippet to verify if it completely answers the question.
Please reply exclusively with ###TRUE### if the response is full, or with ###FALSE### if not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question to Answer:
{question}

Associated Code:
{code}

Task: Decide whether this code meets the demands of the question.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Question Paraphrasing
    HumanMessagePromptTemplate.from_template(
        '''Following your analysis, paraphrase the question using different wording.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''After rephrasing, compare it with the original question.
Detail any differences, including any omissions or extra content that might be significant.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision Process
    HumanMessagePromptTemplate.from_template(
        '''Modify your initial judgment so that it truly represents whether the code answers the question.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Conclusive Evaluation
    HumanMessagePromptTemplate.from_template(
        '''Finally, communicate your final decision as either ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 14:

code_question_answering_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial Judgment
    SystemMessagePromptTemplate.from_template(
        '''Evaluate the code provided below to determine if it fully addresses the question.
Respond only with ###TRUE### when the code is entirely correct or with ###FALSE### if it is not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question Details:
{question}

Code Provided:
{code}

Task: Decide if the code accurately and completely responds to the question posed.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Question Paraphrasing
    HumanMessagePromptTemplate.from_template(
        '''Next, reframe the question in your own words based on your evaluation.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''Then, compare your reframed question with the original.
Identify any aspects that may be missing or any redundancies that could affect the judgment.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision Process
    HumanMessagePromptTemplate.from_template(
        '''Update your earlier judgment so that it precisely reflects whether the code answers the question.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Conclusive Evaluation
    HumanMessagePromptTemplate.from_template(
        '''Finally, state your conclusive evaluation as either ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
