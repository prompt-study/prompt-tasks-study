

──────────────────────────── Variation 0 ────────────────────────────
exception_type_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Predict the exception type for __HOLE__.
Provide only the format: ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Code:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),  # pgen

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Evaluate your chosen exception. If incorrect, specify changes needed.
Otherwise, confirm correctness.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),  # pfb

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Refine your exception type. Provide only ###ExceptionType###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),  # prefine
])

──────────────────────────── Variation 1 ────────────────────────────
exception_type_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Identify the appropriate exception type for __HOLE__.
Respond exclusively using the format: ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Please inspect the following code snippet:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Assess the exception you provided. If it is not correct, detail the required modifications;
if it is accurate, confirm it.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Improve your exception type answer. Reply solely with ###ExceptionType###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 2 ────────────────────────────
exception_type_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Determine the exception category for __HOLE__.
Return your answer strictly in the pattern: ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Here is the code:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Review the exception you selected. If it is off the mark, list the changes required;
otherwise, indicate that it is correct.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Update your exception category response. Provide solely ###ExceptionType###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 3 ────────────────────────────
exception_type_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Establish the correct exception type for __HOLE__.
Your answer should be exclusively formatted as ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Examine this code segment:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Verify the exception you determined. If it is mistaken, describe the necessary changes;
if it is right, simply confirm it.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Revise your exception type if needed. Respond solely with ###ExceptionType###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 4 ────────────────────────────
exception_type_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Ascertain the exception type corresponding to __HOLE__.
Format your reply strictly as ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Review the provided code snippet:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Evaluate your chosen exception. If the selection is not right, note what corrections are needed;
otherwise, confirm that it is correct.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Refine your response regarding the exception type. Return only ###ExceptionType###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 5 ────────────────────────────
exception_type_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Identify which exception type applies to __HOLE__.
Respond using exclusively the format: ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Consider the following code:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Examine your determined exception. If it turns out to be wrong, mention the necessary corrections;
if it is valid, verify its correctness.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Adjust your exception type response accordingly. Provide only ###ExceptionType###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 6 ────────────────────────────
exception_type_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Predict the proper exception type for __HOLE__.
Ensure your reply is exclusively in the format: ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Code snippet:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Scrutinize your chosen exception. If modifications are necessary, specify them;
if it is correct, acknowledge its accuracy.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Fine-tune your response for the exception type. Reply solely with ###ExceptionType###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 7 ────────────────────────────
exception_type_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Figure out the applicable exception type for __HOLE__.
Your output should be exactly: ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Here is the code to evaluate:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Check if your selected exception is correct. If not, outline the necessary modifications;
if it is, simply confirm it.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Modify your response if needed to yield only ###ExceptionType###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 8 ────────────────────────────
exception_type_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Commence by determining the exception type for __HOLE__.
Answer exclusively with the pattern: ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Inspect this code block:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Assess the validity of your proposed exception. If corrections are necessary, list them;
otherwise, indicate that it is correct.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Correct or confirm your exception output. Respond using only ###ExceptionType###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 9 ────────────────────────────
exception_type_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Analyze and pinpoint the exception type for __HOLE__.
Make sure your response is strictly formatted as ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Consider this segment of code:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Critically evaluate the exception you have provided. If adjustments are needed, detail them;
if not, affirm its correctness.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Rework your answer to reflect the exception type. Reply solely with ###ExceptionType###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 10 ────────────────────────────
exception_type_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Compute the correct exception type for __HOLE__.
Provide your answer simply as ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Review the following code segment:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Revisit your exception selection. If there is an error, specify the alterations needed;
if it is accurate, confirm your choice.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Amend your exception type response to include only ###ExceptionType###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 11 ────────────────────────────
exception_type_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Determine the fitting exception type for __HOLE__.
Your response must be formatted as: ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Examine the code below:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Evaluate whether the exception you chose is appropriate. If not, outline the corrections;
if it is acceptable, confirm it.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Revise your provided exception type so that only ###ExceptionType### is included.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 12 ────────────────────────────
exception_type_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Select the correct exception type for __HOLE__.
Limit your answer to the format: ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Inspect this snippet of code:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Critique the exception you selected. If there are issues, note the required modifications;
if it is correct, simply confirm it.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Update your answer so that it reflects only the exception type in the form ###ExceptionType###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 13 ────────────────────────────
exception_type_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Figure out the precise exception type applicable for __HOLE__.
Your output should be solely in the format: ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Take a look at the code below:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Review and validate your selected exception. If it is wrong, provide the needed amendments;
if it is suitable, confirm its correctness.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Adjust or reaffirm your answer so it consists solely of ###ExceptionType###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 14 ────────────────────────────
exception_type_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Determine and report the exception type for __HOLE__, using the exact format: ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Here is the code snippet for review:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Scrutinize your exception choice. If it isn’t correct, provide the necessary modifications;
if it is, simply confirm its accuracy.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Enhance your response so that it is confined to only ###ExceptionType###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

