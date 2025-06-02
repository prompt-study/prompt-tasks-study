
mutant_generation_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial
    SystemMessagePromptTemplate.from_template(
        '''Generate a slightly altered version of the code provided below. Return only the mutated code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Provided:
{code}

Task: Create a mutant version of the code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''Now, articulate the mutant-generation request in your own words based on your initial response.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Comparison
    HumanMessagePromptTemplate.from_template(
        '''Compare your articulation with the original request.
Highlight any discrepancies, such as missing or additional modifications.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision
    HumanMessagePromptTemplate.from_template(
        '''Modify your mutant code to correct any discrepancies identified.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''Finally, confirm your modifications by providing the final mutated code, ensuring only minimal changes were introduced.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])


mutant_generation_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial
    SystemMessagePromptTemplate.from_template(
        '''Create a subtly revised version of the provided code snippet and return solely the modified code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Provided Code:
{code}

Objective: Develop a mutated variant of the code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''Please restate the request for mutant generation in your own terms, reflecting your initial answer.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Comparison
    HumanMessagePromptTemplate.from_template(
        '''Contrast your rewording with the original instruction, pointing out any differences like extra or missing modifications.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision
    HumanMessagePromptTemplate.from_template(
        '''Adjust your mutated code to rectify any noted differences.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''Lastly, verify your adjustments by presenting the final mutated code, making sure only minimal changes are applied.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])


mutant_generation_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial
    SystemMessagePromptTemplate.from_template(
        '''Produce a moderately modified version of the code shown below. Ensure to include only the transformed code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Here is the code:
{code}

Your task: Generate a mutant form of this code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''Now, describe the instructions for generating a mutant version as interpreted from your first response.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Comparison
    HumanMessagePromptTemplate.from_template(
        '''Now, compare your reformulated request with the original, emphasizing any inconsistencies or extra alterations.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision
    HumanMessagePromptTemplate.from_template(
        '''Revise the mutant version of your code to address any inconsistencies you identified.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''Provide the final mutant code as confirmation of your modifications, ensuring that only minor changes were made.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])


mutant_generation_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial
    SystemMessagePromptTemplate.from_template(
        '''Devise a lightly tweaked edition of the supplied code. Provide exclusively the revised code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Sample:
{code}

Assignment: Produce a mutated version of the above code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''In your own words, summarize the mutant-generation request based on your initial output.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Comparison
    HumanMessagePromptTemplate.from_template(
        '''Examine your own wording against the initial prompt and highlight any differences, including any missed or surplus modifications.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision
    HumanMessagePromptTemplate.from_template(
        '''Make modifications to your mutant code to fix any discrepancies mentioned.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''To conclude, supply the final version of your mutated code, ensuring that the modifications remain minimal.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])


mutant_generation_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial
    SystemMessagePromptTemplate.from_template(
        '''Craft a minimally altered form of the code presented below, outputting only the new version of the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Presented Code:
{code}

Instruction: Formulate a mutant iteration of the code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''Restate the requirements for creating a mutant version as per your original response, using your own phrasing.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Comparison
    HumanMessagePromptTemplate.from_template(
        '''Compare your restatement to the original request, noting any discrepancies, whether there are missing details or additional modifications.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision
    HumanMessagePromptTemplate.from_template(
        '''Update your mutated code to resolve any identified variances.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''Finally, present the finalized mutated code to confirm your changes, ensuring only slight alterations were made.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])


mutant_generation_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial
    SystemMessagePromptTemplate.from_template(
        '''Construct a gently modified variant of the following code and output only the updated code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code shown below:
{code}

Requirement: Craft a mutant variation of the provided code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''Articulate, in your own terms, the request for generating a mutant, as understood from your initial reply.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Comparison
    HumanMessagePromptTemplate.from_template(
        '''Evaluate your rephrasing alongside the initial instructions and indicate any variances, such as omitted or added changes.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision
    HumanMessagePromptTemplate.from_template(
        '''Please amend your mutant code to correct any discrepancies found.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''Wrap up by sharing your final mutant code, verifying that only minimal modifications have been implemented.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])


mutant_generation_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial
    SystemMessagePromptTemplate.from_template(
        '''Formulate a modestly changed version of the code given below, returning just the altered code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Displayed Code:
{code}

Task: Create a variation or mutant version of the code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''Express the mutant-code generation request in your own language based on your first answer.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Comparison
    HumanMessagePromptTemplate.from_template(
        '''Now, contrast your interpretation with the original instructions, indicating any divergences in terms of modifications.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision
    HumanMessagePromptTemplate.from_template(
        '''Modify the mutated version of your code to eliminate any identified issues.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''Conclude by delivering your final mutated code, confirming that the changes are minimal.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])


mutant_generation_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial
    SystemMessagePromptTemplate.from_template(
        '''Generate a delicately adjusted version of the following code snippet and return solely the altered output.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code snippet provided:
{code}

Objective: Derive a mutated variant of the code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''Now, reword the instructions for mutant creation, drawing from your initial output.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Comparison
    HumanMessagePromptTemplate.from_template(
        '''Review the differences between your articulation and the original prompt, especially any excess or lacking alterations.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision
    HumanMessagePromptTemplate.from_template(
        '''Apply adjustments to your mutant code to correct all noted inconsistencies.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''Lastly, output the final version of your mutant code, ensuring that only slight modifications have been introduced.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 8:
────────────────────────────
mutant_generation_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial
    SystemMessagePromptTemplate.from_template(
        '''Create a subtle reworking of the ensuing code. Output nothing but the modified code version.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Given Code:
{code}

Request: Develop a mutant version of the code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''In your own words, convey the request for code mutation as it emerged from your first response.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Comparison
    HumanMessagePromptTemplate.from_template(
        '''Contrast your version against the original request and note any inconsistencies, be it missing points or extra modifications.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision
    HumanMessagePromptTemplate.from_template(
        '''Refine your mutant code to fix any gaps or extra modifications you noted.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''To finish, provide the definitive mutant code, confirming that only minimal alterations were applied.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 9:
────────────────────────────
mutant_generation_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial
    SystemMessagePromptTemplate.from_template(
        '''Produce a slightly different version of the code below, ensuring you return only the code with minimal changes.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''The code is presented as follows:
{code}

Assignment: Generate a mutated iteration of the given code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''Please rephrase the mutant generation request based on your initial answer.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Comparison
    HumanMessagePromptTemplate.from_template(
        '''Compare your stated version with the initial request, emphasizing discrepancies including missing or extra modifications.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision
    HumanMessagePromptTemplate.from_template(
        '''Revise your mutant code accordingly to resolve any inconsistencies highlighted.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''Finally, supply the confirmed final mutant code, ensuring the modifications remain minor.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 10:
────────────────────────────
mutant_generation_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial
    SystemMessagePromptTemplate.from_template(
        '''Devise a softly altered rendition of the provided code. Only output the updated code variant.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Extract:
{code}

Instruction: Construct a mutant edition of the code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''Now, explain the instructions for generating a mutant version in your own words, as inferred from your original response.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Comparison
    HumanMessagePromptTemplate.from_template(
        '''Now, juxtapose your formulation with the original prompt, highlighting any differences like missing or additional alterations.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision
    HumanMessagePromptTemplate.from_template(
        '''Make appropriate changes to your mutant code to address the discrepancies.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''Conclude by presenting the end version of your mutated code, confirming minimal changes.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 11:
────────────────────────────
mutant_generation_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial
    SystemMessagePromptTemplate.from_template(
        '''Craft a mildly transformed version of the below code snippet, providing exclusively the adjusted code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Supplied Code:
{code}

Direction: Produce a mutant variant of the provided code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''Rephrase the request for creating a mutant code using your own language, considering your initial response.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Comparison
    HumanMessagePromptTemplate.from_template(
        '''Identify and highlight any divergences between your rewording and the initial instructions, especially regarding modifications.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision
    HumanMessagePromptTemplate.from_template(
        '''Adjust your mutant version to correct all discrepancies that were identified.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''Wrap up by giving the final mutated code, ensuring that only slight changes have been made.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 12:
────────────────────────────
mutant_generation_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial
    SystemMessagePromptTemplate.from_template(
        '''Construct a slightly reformed version of the code shown below, returning just the updated segment.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Here is the sample code:
{code}

Task: Create a version of the code with deliberate mutations.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''Articulate the mutant-generation instructions in your own style based on what you responded initially.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Comparison
    HumanMessagePromptTemplate.from_template(
        '''Compare your interpretation with the original request to flag any discrepancies such as lacking or added changes.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision
    HumanMessagePromptTemplate.from_template(
        '''Please alter your mutated code to correct any discrepancies you found.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''Ultimately, provide your final version of the mutant code, verifying that minimal alterations were introduced.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 13:
────────────────────────────
mutant_generation_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial
    SystemMessagePromptTemplate.from_template(
        '''Form a delicately modified version of the provided code, offering solely the newly altered code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Presented below is the code:
{code}

Objective: Develop a mutant version of this code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''Using your own words, restate the instructions for mutant generation as per your first reply.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Comparison
    HumanMessagePromptTemplate.from_template(
        '''Evaluate how your restatement differs from the original prompt, noting any omissions or superfluous modifications.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision
    HumanMessagePromptTemplate.from_template(
        '''Update your mutant code to remedy any deviations from the intended modifications.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''Finally, confirm your changes by sharing the final mutant code, ensuring only minor modifications.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

────────────────────────────
Variation 14:
────────────────────────────
mutant_generation_template_rcot = ChatPromptTemplate.from_messages([

    # A) Initial
    SystemMessagePromptTemplate.from_template(
        '''Produce a minimally reworked version of the below code and return only the updated, mutated code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Attached code:
{code}

Your goal: Devise a mutated variant of the code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # C) Reconstruction
    HumanMessagePromptTemplate.from_template(
        '''Now, describe the mutant code request in your words, reflecting on your initial answer.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # D) Comparison
    HumanMessagePromptTemplate.from_template(
        '''Now, review and compare your version with the original request, pinpointing any discrepancies like missing or extra adjustments.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # E) Revision
    HumanMessagePromptTemplate.from_template(
        '''Revise your mutant version to fix any differences identified.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),

    # F) Verification
    HumanMessagePromptTemplate.from_template(
        '''In conclusion, present the final mutated code to confirm your revisions, ensuring that only minimal alterations exist.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

Each variation preserves the original structure and technique while offering rephrased instructions for system and human messages.
