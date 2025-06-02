Below are 15 prompt template variants. Variation 0 is exactly as you provided, and Variations 1–14 have rephrased strings for the System and Human messages while keeping the AI message unchanged.

──────────────────────────
Variation 0:
──────────────────────────
mutant_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before answering, work through your reasoning process. For example:
Incorrect reasoning: "Introducing random changes without regard for the code’s structure."
Correct reasoning: "Identifying key parts of the code and making minimal, thoughtful modifications to create a valid mutant."
Generate a mutant of this code with small changes.
Provide only the mutated code.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────
Variation 1:
──────────────────────────
mutant_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you answer, carefully reflect on your thought process. For example:
An incorrect approach might be "Making arbitrary modifications without considering the code’s framework."
A correct approach is "Identifying crucial sections and applying minimal, well-considered changes to yield a valid mutant."
Now, create a mutant of this code with slight modifications.
Return only the updated code.'''
    ),
    HumanMessagePromptTemplate.from_template("The code to be modified: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────
Variation 2:
──────────────────────────
mutant_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Prior to responding, reflect on your internal reasoning. For instance:
A flawed thought process is "Randomly altering code without respecting its structure."
A sound approach is "Targeting significant segments and applying small, deliberate tweaks to produce a meaningful mutant."
Generate a mutant of the given code with minor edits.
Provide solely the mutant version.'''
    ),
    HumanMessagePromptTemplate.from_template("Here is the original code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────
Variation 3:
──────────────────────────
mutant_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before offering your answer, trace through your reasoning steps. For example:
An unsound reasoning would be "Making unsystematic changes without attention to the code’s design."
A correct line is "Identifying key parts of the code and applying minimal, deliberate modifications to form a valid mutant."
Produce a mutant version of this code with only subtle changes.
Output just the mutated code.'''
    ),
    HumanMessagePromptTemplate.from_template("Source code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────
Variation 4:
──────────────────────────
mutant_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you produce your answer, go through your reasoning process in detail. For example:
A poor example would be "Randomly modifying the code without structure."
A better strategy is "Isolating important code sections and making slight, careful adjustments to generate a valid mutant."
Create a mutant of the code by applying minimal changes.
Return only the modified code.'''
    ),
    HumanMessagePromptTemplate.from_template("Input code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────
Variation 5:
──────────────────────────
mutant_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before answering, examine your reasoning thoroughly. For instance:
One incorrect approach would be "Introducing arbitrary changes without worrying about the code’s structure."
In contrast, the correct reasoning is "Identifying key components and executing minimal, thoughtful modifications to achieve a valid mutant."
Generate a mutant of the code with only slight modifications.
Return exclusively the mutated code.'''
    ),
    HumanMessagePromptTemplate.from_template("Code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────
Variation 6:
──────────────────────────
mutant_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you respond, detail your internal thought process. For example:
An inappropriate strategy is "Changing code at random with no attention to its structure."
A proper method is "Pinpointing essential parts and applying subtle, deliberate tweaks to create a workable mutant."
Generate a mutant version of this code with minimal alterations.
Provide only the mutated code.'''
    ),
    HumanMessagePromptTemplate.from_template("The code provided: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────
Variation 7:
──────────────────────────
mutant_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you produce an answer, work carefully through your reasoning. For instance:
A misstep in reasoning might be "Enacting random modifications with disregard to the code’s design."
A correct approach is "Focusing on significant sections and carrying out small, thoughtful changes to produce a valid mutant."
Create a mutant of the code with minor adjustments.
Return only the altered code.'''
    ),
    HumanMessagePromptTemplate.from_template("Original code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────
Variation 8:
──────────────────────────
mutant_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before answering, take a moment to reflect on your reasoning. For example:
If you mistakenly reason by "randomly modifying the code without structure," instead, reason by "focusing on key segments and making subtle, accurate tweaks to generate a valid mutant."
Now, create a mutant of the code with small modifications.
Output only the mutant code.'''
    ),
    HumanMessagePromptTemplate.from_template("Please use the following code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────
Variation 9:
──────────────────────────
mutant_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you answer, reevaluate your reasoning process thoroughly. For instance:
An incorrect method would be "performing random adjustments without an understanding of the code’s framework."
A correct method is "highlighting vital sections and applying minimal, thoughtful changes to produce a functional mutant."
Develop a mutant code version with subtle edits.
Return only the mutated code.'''
    ),
    HumanMessagePromptTemplate.from_template("Code to modify: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────
Variation 10:
──────────────────────────
mutant_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before giving your answer, internally revisit your reasoning steps. For example:
Avoid flawed approaches such as "making uncoordinated changes with disregard for the code’s structure."
Instead, use an approach like "isolating key code segments and performing slight, intentional modifications to yield a valid mutant."
Generate a mutant version of this code with minimal changes.
Return solely the mutant code.'''
    ),
    HumanMessagePromptTemplate.from_template("Code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────
Variation 11:
──────────────────────────
mutant_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you answer, take a moment to detail your reasoning steps. For example:
A bad approach would be "altering the code arbitrarily."
A proper approach is "analyzing the code, identifying its key parts, and making only small, informed changes to create a mutant."
Now, produce a mutant of the code with only slight modifications.
Output just the mutated code.'''
    ),
    HumanMessagePromptTemplate.from_template("Here is the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────
Variation 12:
──────────────────────────
mutant_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before answering, carefully review your reasoning process. For instance:
An incorrect rationale would be "making random modifications without grasping the code’s design."
A correct rationale is "pinpointing crucial elements and executing minimal, precise alterations to form a valid mutant."
Generate a mutant version of this code with minor differences.
Return only the modified code.'''
    ),
    HumanMessagePromptTemplate.from_template("Original snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────
Variation 13:
──────────────────────────
mutant_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before generating your answer, iterate through your reasoning carefully. For example:
An improper method is "introducing random changes without considering the structure."
A proper method is "focusing on critical components and applying minimal, careful adjustments to generate a valid mutant."
Create a mutant of the provided code with slight modifications.
Return exclusively the altered code.'''
    ),
    HumanMessagePromptTemplate.from_template("Supplied code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────
Variation 14:
──────────────────────────
mutant_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you provide your answer, carefully walk through your internal reasoning. For example:
One should avoid reasoning like "randomly altering the code without any regard for its structure."
Instead, employ reasoning such as "identifying key sections of the code and making only small, precise modifications to develop a valid mutant."
Now, generate a mutant of the given code with minimal edits.
Return only the mutated code.'''
    ),
    HumanMessagePromptTemplate.from_template("Given code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────
End of Variations.
Each variant preserves the original AI message while rewording the System and Human directives.