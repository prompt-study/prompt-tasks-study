Below are 15 complete prompt template variants. Variation 0 is exactly the original, and Variations 1–14 include rephrased strings for the system and human messages while keeping the AI messages unchanged.

──────────────────────────────
Variation 0:
──────────────────────────────
code_generation_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Generate code for the given task. Provide only the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Task:\n{task_description}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),  # pgen

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Review the code. If there's a flaw, provide specific feedback.
Otherwise, confirm correctness.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),  # pfb

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Refine the code based on feedback. Provide only the improved code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),  # prefine
])

──────────────────────────────
Variation 1:
──────────────────────────────
code_generation_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Develop code for the outlined task. Present only the code in your response.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Task Requirements:\n{task_description}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Examine the code. If you notice any mistakes, supply clear and specific feedback.
Otherwise, affirm that it is correct.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Revise the code based on the received feedback. Return only the revised code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 2:
──────────────────────────────
code_generation_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Produce code that fulfills the described task. Include only the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Assignment Details:\n{task_description}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Assess the code provided. Should you detect any issues, offer detailed critiques;
otherwise, confirm its accuracy.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Update the code utilizing the feedback given. Provide solely the updated code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 3:
──────────────────────────────
code_generation_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Write code addressing the specified task. Your answer should be limited to the code only.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Project Brief:\n{task_description}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Evaluate the code. If errors are found, give clear corrective notes;
if it’s flawless, note that accordingly.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Modify the code as per the feedback. Return just the enhanced code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 4:
──────────────────────────────
code_generation_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Create code based on the task provided. Only include code in your submission.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Task Description:\n{task_description}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Inspect the code. Provide detailed error feedback if needed,
otherwise confirm that it works as intended.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Refine the code using the feedback provided. Submit only the improved version of the code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 5:
──────────────────────────────
code_generation_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Generate a code solution for the given task. Provide solely the code in your answer.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Task Summary:\n{task_description}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Go over the code carefully. If issues are identified, offer precise feedback;
if it is correct, state that explicitly.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Adjust the code in light of the feedback. Return only the modified code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 6:
──────────────────────────────
code_generation_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Develop a code snippet that solves the task given. Ensure that only the code is presented.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Instructions:\n{task_description}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Review the generated code. If you spot problems, include specific feedback;
if the code is fine, confirm its validity.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Amend the code based on the comments received. Provide only the final corrected code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 7:
──────────────────────────────
code_generation_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Craft code to complete the specified task. Only deliver the coding segment in your answer.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Assignment:\n{task_description}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Examine the generated code. If any errors are observed, share detailed feedback;
if no errors are found, simply confirm.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Enhance the code as per the supplied feedback. Provide just the refined code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 8:
──────────────────────────────
code_generation_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Write a program that fulfills the task instructions. Please include only the source code in your response.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Problem Statement:\n{task_description}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Critically review the code. If there are any mistakes, offer precise feedback;
otherwise, confirm that the code is accurate.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Improve the code based on the feedback received and return only the enhanced code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 9:
──────────────────────────────
code_generation_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Construct code addressing the provided task. Output solely the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Task Outline:\n{task_description}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Analyze the code thoroughly. If any faults are detected, provide specific and detailed feedback;
if none are found, affirm its correctness.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Rework the code based on the feedback to deliver only the updated version.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 10:
──────────────────────────────
code_generation_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Develop a solution in code for the described task. Your answer should consist exclusively of code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Description of Task:\n{task_description}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Inspect the code carefully. Should you find any discrepancies or errors, give pinpointed feedback;
otherwise, confirm it's correct.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Revise the code according to the feedback. Present only the refined code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 11:
──────────────────────────────
code_generation_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Create a code implementation for the task provided. Only include code in your final response.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Task Overview:\n{task_description}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Review the generated code, and if there are any flaws, provide detailed, actionable feedback;
if not, simply confirm its accuracy.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Adjust the code based on the critique received. Supply only the updated version.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 12:
──────────────────────────────
code_generation_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Write a code solution for this task. Return only the code in your response.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Task Details:\n{task_description}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Scrutinize the code for potential errors. If you uncover any issues, offer detailed feedback;
otherwise, confirm the code's correctness.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Refactor the code using the provided feedback. Output only the modified code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 13:
──────────────────────────────
code_generation_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Generate a code answer for the described task. Your response should consist solely of code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Task Information:\n{task_description}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Look over the code responsibly. If you identify any mistakes, deliver specific feedback;
if not, confirm its accuracy.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Update the code based on the feedback. Provide only the updated code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 14:
──────────────────────────────
code_generation_template_self_refine = ChatPromptTemplate.from_messages([
    # Step 1: Initial Generation
    SystemMessagePromptTemplate.from_template(
        '''Craft a code solution that meets the task requirements. Provide only the actual code in your answer.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Task Brief:\n{task_description}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 2: Feedback
    HumanMessagePromptTemplate.from_template(
        '''Examine the code provided. If any issues arise, supply clear and precise feedback;
if not, confirm its validity.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # Step 3: Refinement
    HumanMessagePromptTemplate.from_template(
        '''Modify the code according to the feedback received and return only the new code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

Each variant preserves the original prompt structure and the AI message identifiers while rephrasing the system and human instructions as required.