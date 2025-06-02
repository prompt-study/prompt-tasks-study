
Below are the revised prompt templates. Only the system‐message texts have been modified where the emotional language was too similar. Each variant now employs a richer, more varied emotional appeal while leaving the other components unchanged.

────────────────────────────
**Variation 0 (Original – unchanged)**
```python
mutant_generation_template_emotion_v1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Generate a mutant of the following code by making small changes. Provide the mutated code only.
Are you sure that's your final answer? Consider double-checking.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

────────────────────────────
**Variation 1 (Modified emotional appeal)**
```python
mutant_generation_template_emotion_v1_variant1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Create a variant of the code below by introducing subtle alterations. Return solely the revised code.
Reflect on your modifications and trust your expertise to make a mutation that truly stands out.'''
    ),
    HumanMessagePromptTemplate.from_template("Here is the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

────────────────────────────
**Variation 2 (Modified emotional appeal)**
```python
mutant_generation_template_emotion_v1_variant2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Please develop a modified version of the provided code by implementing minor modifications. Output only the altered code.
Are you confident in your adjustments? Embrace the challenge with passion to create a subtle yet purposeful mutation.'''
    ),
    HumanMessagePromptTemplate.from_template("Submit your code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

────────────────────────────
**Variation 3 (Modified emotional appeal)**
```python
mutant_generation_template_emotion_v1_variant3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Take the supplied code and produce a mutant by applying slight edits. Include only the mutated version in the response.
This is very important to my career.'''
    ),
    HumanMessagePromptTemplate.from_template("Code input: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

────────────────────────────
**Variation 4 (Modified emotional appeal)**
```python
mutant_generation_template_emotion_v1_variant4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Alter the following code by making only small, thoughtful changes, and present the mutated code exclusively.
Focus on your work and let your determination shine; every small change can spark significant progress.'''
    ),
    HumanMessagePromptTemplate.from_template("The code to modify: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

────────────────────────────
**Variation 5 (Modified emotional appeal)**
```python
mutant_generation_template_emotion_v1_variant5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Mutate the given code by applying minimal modifications. Provide only the revised code.
This is very important to my career, so you'd better be sure.'''
    ),
    HumanMessagePromptTemplate.from_template("Original code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

────────────────────────────
**Variation 6 (Modified emotional appeal)**
```python
mutant_generation_template_emotion_v1_variant6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Transform the code below by introducing subtle changes. Return just the mutated version.
Trust your technical instincts and let your creativity flow; ensure every tweak aligns with a clear vision.'''
    ),
    HumanMessagePromptTemplate.from_template("Code provided: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

────────────────────────────
**Variation 7 (Modified emotional appeal)**
```python
mutant_generation_template_emotion_v1_variant7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Modify the provided code lightly to create a variant. Deliver only the modified code.
Step into the role of an innovator—confirm your alterations and let your confidence guide you to impactful changes.'''
    ),
    HumanMessagePromptTemplate.from_template("Your code sample: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

────────────────────────────
**Variation 8 (Modified emotional appeal)**
```python
mutant_generation_template_emotion_v1_variant8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Develop a mutated version of the code by making minor adjustments. Present solely the updated code.
Approach this challenge with resolve; examine your changes meticulously to craft a mutation that inspires.'''
    ),
    HumanMessagePromptTemplate.from_template("Insert the code here: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

────────────────────────────
**Variation 9 (Modified emotional appeal)**
```python
mutant_generation_template_emotion_v1_variant9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Design a subtle mutant of the following code by incorporating small adjustments. Return just the altered code.
You'd better be sure.'''
    ),
    HumanMessagePromptTemplate.from_template("Please provide the original code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

────────────────────────────
**Variation 10 (Modified emotional appeal)**
```python
mutant_generation_template_emotion_v1_variant10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Generate a slightly altered version of the code provided by applying minimal revisions. Include only the mutant code.
Have faith in your revisions—each careful update is a step toward a coherent and remarkable mutation.'''
    ),
    HumanMessagePromptTemplate.from_template("Code input for mutation: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

────────────────────────────
**Variation 11 (Modified emotional appeal)**
```python
mutant_generation_template_emotion_v1_variant11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Craft a discerning mutant of the following code through minor modifications. Submit only the updated code.
Review your modifications with a critical eye; let your dedication fuel a mutation that reflects your best work.'''
    ),
    HumanMessagePromptTemplate.from_template("Enter the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

────────────────────────────
**Variation 12 (Modified emotional appeal)**
```python
mutant_generation_template_emotion_v1_variant12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Produce a variant of the supplied code by making incremental changes. Respond with only the evolved code.
Focus intently on every detail; your precise modifications are the key to a mutation that truly makes an impact.'''
    ),
    HumanMessagePromptTemplate.from_template("The code is as follows: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

────────────────────────────
**Variation 13 (Modified emotional appeal)**
```python
mutant_generation_template_emotion_v1_variant13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Create a subtle mutant of the presented code through slight modifications. Return only the refined code.
Empower your creativity—validate each change to forge a mutation that embodies ingenuity and purpose.'''
    ),
    HumanMessagePromptTemplate.from_template("Provided code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

────────────────────────────
**Variation 14 (Modified emotional appeal)**
```python
mutant_generation_template_emotion_v1_variant14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Alter the given code by applying only modest tweaks to create a mutant version. Output solely the revised code.
Let your commitment to excellence drive you; scrutinize your alterations and present a mutation that sets a new standard.'''
    ),
    HumanMessagePromptTemplate.from_template("Insert code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```
