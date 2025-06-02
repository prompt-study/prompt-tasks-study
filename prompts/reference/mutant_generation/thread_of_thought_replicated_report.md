Below are 15 complete prompt template variants. Variation 0 is exactly the one you provided, and Variations 1–14 are rephrased versions where only the strings inside SystemMessagePromptTemplate and HumanMessagePromptTemplate have been modified (the AI version remains unchanged).

──────────────────────────────
Variation 0:
──────────────────────────────
mutant_generation_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Walk me through this code in manageable parts, summarizing and analyzing possible small changes.
Finally, provide only the mutated code.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 1:
──────────────────────────────
mutant_generation_template_thot_variant_1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Please break down the given code into clear, manageable segments. Summarize each section and assess potential minor adjustments. Then, output solely the revised code.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly supply the source code here: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 2:
──────────────────────────────
mutant_generation_template_thot_variant_2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Detail the code step by step by partitioning it into small, understandable pieces. Offer summaries and evaluate potential tweaks for each section. End your response with only the updated code.'''
    ),
    HumanMessagePromptTemplate.from_template("Input your code snippet below: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 3:
──────────────────────────────
mutant_generation_template_thot_variant_3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Analyze the code by decomposing it into bite-sized parts, providing a brief overview and considering possible small modifications. Conclude by presenting only the mutated version.'''
    ),
    HumanMessagePromptTemplate.from_template("Enter the code to be processed: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 4:
──────────────────────────────
mutant_generation_template_thot_variant_4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Please review the following code in segments, with brief summaries and an analysis of possible minor modifications. Your final response should consist solely of the modified code.'''
    ),
    HumanMessagePromptTemplate.from_template("Here is the code to analyze: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 5:
──────────────────────────────
mutant_generation_template_thot_variant_5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Examine the provided code sequentially, dividing it into logical, digestible parts. Summarize and evaluate potential minor changes, and then return only the modified code.'''
    ),
    HumanMessagePromptTemplate.from_template("Provide the code for transformation: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 6:
──────────────────────────────
mutant_generation_template_thot_variant_6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Step through the code piece by piece, summarizing each segment and reviewing any potential subtle modifications. Finally, submit just the changed code.'''
    ),
    HumanMessagePromptTemplate.from_template("Share your code sample: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 7:
──────────────────────────────
mutant_generation_template_thot_variant_7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Dissect the code into manageable sections, offering concise summaries and assessing any possible modifications on a small scale. Your output should be limited to the mutated code.'''
    ),
    HumanMessagePromptTemplate.from_template("Present the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 8:
──────────────────────────────
mutant_generation_template_thot_variant_8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Break the code into smaller, understandable parts while summarizing and inspecting for any minor alterations that could be implemented. End your answer by providing only the updated code.'''
    ),
    HumanMessagePromptTemplate.from_template("Insert the code for analysis: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 9:
──────────────────────────────
mutant_generation_template_thot_variant_9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Proceed by dividing the code into clear-cut segments and summarizing each one, taking note of any scope for minor tweaks. Conclude with only the version of the code that has been mutated.'''
    ),
    HumanMessagePromptTemplate.from_template("Submit your code for mutation: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 10:
──────────────────────────────
mutant_generation_template_thot_variant_10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Go through the code step by step in easy-to-manage parts, including summaries and consideration for slight modifications. Your final result should only include the refined code.'''
    ),
    HumanMessagePromptTemplate.from_template("Please send the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 11:
──────────────────────────────
mutant_generation_template_thot_variant_11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Deconstruct the code into simple chunks, review each part with a brief summary and evaluate small prospective edits. End your explanation by providing just the altered code.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly enter the code to transform: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 12:
──────────────────────────────
mutant_generation_template_thot_variant_12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Analyze the provided code by segmenting it into digestible blocks, summarizing components and suggesting minimal adjustments. Finish with only the updated code displayed.'''
    ),
    HumanMessagePromptTemplate.from_template("Input the relevant code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 13:
──────────────────────────────
mutant_generation_template_thot_variant_13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Segment the code into clear, manageable parts. Provide summaries for each segment and assess possible slight modifications. Ultimately, return solely the modified code.'''
    ),
    HumanMessagePromptTemplate.from_template("Please supply your code module here: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 14:
──────────────────────────────
mutant_generation_template_thot_variant_14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Interpret the code by breaking it into distinct, digestible segments, summarizing key elements and exploring potential minor adjustments. Make sure to finish with only the revised code.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly provide the code excerpt: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 15:
──────────────────────────────
mutant_generation_template_thot_variant_15 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Step through the code methodically, splitting it into easy-to-understand sections, summarizing key points, and considering opportunities for slight modifications. Ultimately, deliver only the altered code at the end.'''
    ),
    HumanMessagePromptTemplate.from_template("Share the code for assessment: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

Each variant preserves the original task and structure while offering a different phrasing in the system and human instructions.