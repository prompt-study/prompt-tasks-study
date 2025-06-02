
clone_detection_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial Setup
    SystemMessagePromptTemplate.from_template(
        '''You are assigned to determine if two code snippets are clones.
Respond solely with TRUE (###TRUE###) or FALSE (###FALSE###).'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''First Code Snippet:
{code_snippet1}

Second Code Snippet:
{code_snippet2}

Question: Do these code snippets represent clones of one another?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Problem Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''Based on your answer, restate the problem in your own words.
What was the question you were solving?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''Now, compare your restatement with the original prompt.
Note any conditions or details that are missing or superfluous.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Feedback & Revision
    HumanMessagePromptTemplate.from_template(
        '''Modify your initial clone detection answer to resolve any discrepancies.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''Lastly, verify your final decision is coherent and state TRUE or FALSE.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
# Variation 1
──────────────────────────────
clone_detection_template_rcot_1 = ChatPromptTemplate.from_messages([

    # A) Initial Setup
    SystemMessagePromptTemplate.from_template(
        '''Your task is to assess whether two provided code samples are identical copies.
Please answer exclusively with TRUE (###TRUE###) or FALSE (###FALSE###).'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Snippet One:
{code_snippet1}

Code Snippet Two:
{code_snippet2}

Inquiry: Are these two code snippets clones?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Problem Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''Reflecting on your response, rephrase the problem in your own words.
What was the main question?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''Compare your rephrasing with the original instructions.
Identify any missing or extra details.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Feedback & Revision
    HumanMessagePromptTemplate.from_template(
        '''Revise your initial answer regarding clone detection to address any inconsistencies.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''Finally, confirm that your concluding decision is consistent and express it as TRUE or FALSE.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
# Variation 2
──────────────────────────────
clone_detection_template_rcot_2 = ChatPromptTemplate.from_messages([

    # A) Initial Setup
    SystemMessagePromptTemplate.from_template(
        '''You must decide if the pair of code extracts are duplicates.
Return only TRUE (###TRUE###) or FALSE (###FALSE###).'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Snippet 1:
{code_snippet1}

Snippet 2:
{code_snippet2}

Question: Are these two code pieces cloned?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Problem Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''Given your answer, express the problem in your own terms.
What inquiry were you addressing?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''Review your reworded version alongside the original question.
Highlight any omitted or redundant details.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Feedback & Revision
    HumanMessagePromptTemplate.from_template(
        '''Update your first clone verdict to address any differences found.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''Ultimately, validate that your final decision is coherent and provide it as TRUE or FALSE.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
# Variation 3
──────────────────────────────
clone_detection_template_rcot_3 = ChatPromptTemplate.from_messages([

    # A) Initial Setup
    SystemMessagePromptTemplate.from_template(
        '''Your assignment is to evaluate if the two code fragments are replicas.
Answer strictly with TRUE (###TRUE###) or FALSE (###FALSE###).'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Here is the first code snippet:
{code_snippet1}

And the second:
{code_snippet2}

Do they qualify as clones?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Problem Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''Considering your response, articulate the problem using your own words.
What was the question at hand?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''Contrast your interpretation with the original prompt.
Note discrepancies, either missing or extra conditions.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Feedback & Revision
    HumanMessagePromptTemplate.from_template(
        '''Alter your initial clone detection reply to reconcile any inconsistencies.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''Lastly, double-check your final verdict for consistency and reply with TRUE or FALSE.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
# Variation 4
──────────────────────────────
clone_detection_template_rcot_4 = ChatPromptTemplate.from_messages([

    # A) Initial Setup
    SystemMessagePromptTemplate.from_template(
        '''Determine if the two pieces of code are clones.
Provide your response solely as TRUE (###TRUE###) or FALSE (###FALSE###).'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Presenting Code Snippet A:
{code_snippet1}

Presenting Code Snippet B:
{code_snippet2}

Query: Do these code snippets mirror each other as clones?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Problem Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''From your answer, summarize the problem in your own words.
What was the question you tackled?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''Compare your expressed version of the problem with the given prompt.
Mention any details that aren’t aligned.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Feedback & Revision
    HumanMessagePromptTemplate.from_template(
        '''Refine your original answer on clone detection to eliminate discrepancies.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''Finally, review your final decision for coherence and clearly state either TRUE or FALSE.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
# Variation 5
──────────────────────────────
clone_detection_template_rcot_5 = ChatPromptTemplate.from_messages([

    # A) Initial Setup
    SystemMessagePromptTemplate.from_template(
        '''Your job is to figure out if the given code segments are clones.
Submit your answer in a single word: either TRUE (###TRUE###) or FALSE (###FALSE###).'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Provided Code Snippet 1:
{code_snippet1}

Provided Code Snippet 2:
{code_snippet2}

Is it true that these snippets are clones?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Problem Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''Based on what you answered, reword the problem in your own language.
What question did you address?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''Now, juxtapose your rephrasing with the original query.
Identify any details that might be missing or overly added.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Feedback & Revision
    HumanMessagePromptTemplate.from_template(
        '''Revise your initial clone detection answer to correct any misalignments.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''Finally, review your final answer for coherence and indicate TRUE or FALSE.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
# Variation 6
──────────────────────────────
clone_detection_template_rcot_6 = ChatPromptTemplate.from_messages([

    # A) Initial Setup
    SystemMessagePromptTemplate.from_template(
        '''Evaluate whether the following code snippets are clones.
Respond with nothing but TRUE (###TRUE###) or FALSE (###FALSE###).'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''First snippet:
{code_snippet1}

Second snippet:
{code_snippet2}

Question: Could these code samples be considered clones?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Problem Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''Using your answer, convey the problem in your own phrasing.
What key question were you solving?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''Assess your rephrasing relative to the original question.
Observe any discrepancies in details or conditions.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Feedback & Revision
    HumanMessagePromptTemplate.from_template(
        '''Edit your initial clone determination answer to resolve any perceived inconsistencies.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''In the end, confirm that your ultimate decision is solid and then indicate TRUE or FALSE.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
# Variation 7
──────────────────────────────
clone_detection_template_rcot_7 = ChatPromptTemplate.from_messages([

    # A) Initial Setup
    SystemMessagePromptTemplate.from_template(
        '''Your role is to judge if the two programming snippets are cloned versions.
Answer exclusively with TRUE (###TRUE###) or FALSE (###FALSE###).'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Here are the two code examples:
Original snippet: {code_snippet1}
Duplicate snippet: {code_snippet2}

Is one a clone of the other?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Problem Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''Reflect on your answer and restate the problem in simpler terms.
What was the question you attempted to answer?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''Assess your rephrasing relative to the original instructions.
Highlight any details that are either omitted or additional.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Feedback & Revision
    HumanMessagePromptTemplate.from_template(
        '''Change your early answer about detecting clones to address any discrepancies.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''Lastly, verify that your final judgement is coherent and explicitly respond with TRUE or FALSE.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
# Variation 8
──────────────────────────────
clone_detection_template_rcot_8 = ChatPromptTemplate.from_messages([

    # A) Initial Setup
    SystemMessagePromptTemplate.from_template(
        '''You're tasked with determining if the two code sections are clones.
Only answer with TRUE (###TRUE###) or FALSE (###FALSE###).'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Examine the following snippets:
Snippet One: {code_snippet1}

Snippet Two: {code_snippet2}

Should we consider these as clones?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Problem Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''Drawing from your response, describe the problem in your own words.
What was the central question?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''Align your restated problem with the original instructions.
Identify any elements that are omitted or extra.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Feedback & Revision
    HumanMessagePromptTemplate.from_template(
        '''Change your early answer about clone detection to resolve any discrepancies.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''Finally, ensure that your concluding decision makes sense, and reply solely with TRUE or FALSE.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
# Variation 9
──────────────────────────────
clone_detection_template_rcot_9 = ChatPromptTemplate.from_messages([

    # A) Initial Setup
    SystemMessagePromptTemplate.from_template(
        '''The objective is to check if both code snippets are clones.
Provide only one-word answers: TRUE (###TRUE###) or FALSE (###FALSE###).'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Displayed Code Snippet 1:
{code_snippet1}

Displayed Code Snippet 2:
{code_snippet2}

Question: Do they represent cloned code?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Problem Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''As per your answer, reframe the problem using your language.
What was being asked?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''Now, check your restatement against the original query.
Indicate any conditions that may be incomplete or redundant.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Feedback & Revision
    HumanMessagePromptTemplate.from_template(
        '''Tweak your initial response on whether the snippets are clones, correcting any issues.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''To conclude, check that your final answer is consistent and state TRUE or FALSE.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
# Variation 10
──────────────────────────────
clone_detection_template_rcot_10 = ChatPromptTemplate.from_messages([

    # A) Initial Setup
    SystemMessagePromptTemplate.from_template(
        '''You are required to decide whether the presented code snippets are clones.
Answer solely with either TRUE (###TRUE###) or FALSE (###FALSE###).'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''The two code snippets are as follows:
Snippet 1: {code_snippet1}
Snippet 2: {code_snippet2}

Are these clones of one another?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Problem Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''Based on what you answered, rephrase the problem in your own terms.
What question were you trying to resolve?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''Review your restatement and check it against the original prompt.
Detail any missing or superfluous elements.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Feedback & Revision
    HumanMessagePromptTemplate.from_template(
        '''Revamp your primary clone detection answer to account for and fix any inconsistencies.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''Lastly, affirm that your final decision is coherent, then respond with either TRUE or FALSE.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
# Variation 11
──────────────────────────────
clone_detection_template_rcot_11 = ChatPromptTemplate.from_messages([

    # A) Initial Setup
    SystemMessagePromptTemplate.from_template(
        '''Assess if the two provided snippets of code are clones.
Respond with either TRUE (###TRUE###) or FALSE (###FALSE###) only.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Initial code sample:
{code_snippet1}

Follow-up code sample:
{code_snippet2}

Inquiry: Do these samples duplicate each other?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Problem Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''Review your response and state the problem in your own words.
What was the challenge you were addressing?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''Compare your rewording with the original prompt.
Note any key conditions that might be lacking or excessive.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Feedback & Revision
    HumanMessagePromptTemplate.from_template(
        '''Reset your first clone detection response to resolve any noted discrepancies.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''Conclude by verifying that your final answer is logical and state it as TRUE or FALSE.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
# Variation 12
──────────────────────────────
clone_detection_template_rcot_12 = ChatPromptTemplate.from_messages([

    # A) Initial Setup
    SystemMessagePromptTemplate.from_template(
        '''Your task is to review if these two code blocks are identical clones.
Provide your answer exclusively as TRUE (###TRUE###) or FALSE (###FALSE###).'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Here is snippet one:
{code_snippet1}
And here is snippet two:
{code_snippet2}

Does this pair constitute clones?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Problem Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''Taking your answer into account, reword the question in your own style.
What problem did you intend to solve?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''Contrast your paraphrasing with the original instructions.
Highlight any discrepancies or unnecessary details.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Feedback & Revision
    HumanMessagePromptTemplate.from_template(
        '''Modify your initial conclusion about clone detection to reconcile all identified differences.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''Final step: ensure your last decision is consistent and answer with TRUE or FALSE.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
# Variation 13
──────────────────────────────
clone_detection_template_rcot_13 = ChatPromptTemplate.from_messages([

    # A) Initial Setup
    SystemMessagePromptTemplate.from_template(
        '''Your task is to review whether the given pair of code samples are clones.
Reply strictly with TRUE (###TRUE###) or FALSE (###FALSE###).'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Please examine the two provided snippets:
First: {code_snippet1}
Second: {code_snippet2}

Are they clones?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Problem Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''In light of your answer, reformulate the problem in your words.
Which question were you handling?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''Now, check your restatement against the original query.
Indicate any conditions that may be incomplete or redundant.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Feedback & Revision
    HumanMessagePromptTemplate.from_template(
        '''Adjust your early answer about clone identification to remove any inconsistencies.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''Lastly, validate that your ultimate answer is coherent and then provide either TRUE or FALSE.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
# Variation 14
──────────────────────────────
clone_detection_template_rcot_14 = ChatPromptTemplate.from_messages([

    # A) Initial Setup
    SystemMessagePromptTemplate.from_template(
        '''You are to determine if the two code examples are clones.
Reply with either TRUE (###TRUE###) or FALSE (###FALSE###) and nothing else.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Review the code samples:
Snippet A: {code_snippet1}
Snippet B: {code_snippet2}

Query: Are these two identical clones?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Problem Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''Reflect on your initial response and restate the challenge in your own words.
What was the original question?'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Detailed Comparison
    HumanMessagePromptTemplate.from_template(
        '''Evaluate your wording versus the original prompt and list any differences,
specifically noting missing or extra details.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Feedback & Revision
    HumanMessagePromptTemplate.from_template(
        '''Review and revise your original clone detection answer to ensure all discrepancies are resolved.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''Finally, check the coherence of your final decision and respond exclusively with TRUE or FALSE.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
