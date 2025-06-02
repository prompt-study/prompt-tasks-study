Below are the revised defect‐detection prompt templates. In each variation the explicit references to “analogical prompting” have been removed while preserving the intended structure and instructions.

────────────────────────────
**Variation 0**
```python
defect_detection_template_analogical = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Examine the code for defects.
First, create a simple, similar example of code that might have a defect.
Walk through how you'd detect that defect (including your reasoning steps).
Then, I'll give you the real snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Please provide your self-generated example and solution now."),
    AIMessagePromptTemplate.from_template('prompt'),  # LLM generates an analogous example + demonstration

    HumanMessagePromptTemplate.from_template(
        '''Here is the actual code snippet:
{code}

Using the same approach, is there a defect?
Answer with ###TRUE### or ###FALSE### only.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')  # LLM's final answer
])
```

────────────────────────────
**Variation 1**
```python
defect_detection_template_analogical_v1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Identify potential errors in code.
First, craft a straightforward, comparable code sample that could include a flaw.
Explain the process you would use to uncover this error, detailing your reasoning.
Afterwards, I will present you with the actual code snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly submit your generated example along with your explanatory process."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Below is the provided code snippet:
{code}

Using the same methodology, does this snippet have an error?
Respond solely with ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────
**Variation 2**
```python
defect_detection_template_analogical_v2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Apply a systematic approach to examine whether a given code sample is flawed.
Begin by creating a basic, similar example that might harbor an error.
Detail each step of your method for detecting the fault along with your reasoning.
I will then supply the actual code snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Please share your self-devised example along with your reasoning."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Here is the authentic code snippet:
{code}

Using the same procedure, can you confirm the presence of a defect?
Answer exactly with ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────
**Variation 3**
```python
defect_detection_template_analogical_v3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt a methodical approach to assess the code for defects.
Start by constructing a simple, comparable piece of code that may contain an error.
Walk us through your step-by-step process—including your reasoning—to locate that error.
Then, I will provide you with the real snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Submit your original example along with an explanation of your approach."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''This is the real code snippet:
{code}

Using the approach you've just described, does a defect exist?
Please answer solely with either ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────
**Variation 4**
```python
defect_detection_template_analogical_v4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Inspect code for potential errors.
Initially, generate a rudimentary example that mirrors the code and might contain a mistake.
Describe the process and reasoning you would follow to pinpoint that mistake.
Subsequently, I will show you the actual code snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Please present your self-crafted example along with your reasoning."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Below is the actual code snippet:
{code}

Adopt the same strategy: is there a defect in this code?
Respond with just ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────
**Variation 5**
```python
defect_detection_template_analogical_v5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Scrutinize code for hidden defects.
Start by producing a simple, similar code snippet that may feature an error.
Elaborate on your approach and the reasoning steps used to identify the flaw.
Later, I will share the genuine code snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly provide your generated code sample along with your explanation."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Here is the genuine code snippet:
{code}

Using the same method, does the snippet exhibit a defect?
Answer only with ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────
**Variation 6**
```python
defect_detection_template_analogical_v6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Implement a systematic approach to verify code for errors.
Begin by creating a basic, parallel code sample that might be flawed.
Detail your step-by-step process for detecting any defect, including your rationale.
Afterward, I will provide the actual code snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Please supply your self-created example along with your reasoning."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Here is the real code snippet:
{code}

Using the same procedure, is a defect evident?
Answer strictly with ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────
**Variation 7**
```python
defect_detection_template_analogical_v7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine if a segment of code has errors using a systematic approach.
Start by crafting a clear, similar example that might contain a defect.
Present your systematic approach and thought process for identifying the error.
Subsequently, I will present you with the actual code snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly share your self-generated example along with a detailed explanation."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Presenting the actual code snippet:
{code}

Using the same approach, can you confirm whether there is a defect?
Please answer with only ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────
**Variation 8**
```python
defect_detection_template_analogical_v8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Evaluate the code for any defects.
Begin by designing a simple, model code snippet that might exhibit an error.
Describe your thought process and the steps you undertake to detect the error.
Then, I will deliver the authentic code snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Please supply your self-produced example along with the reasoning behind it."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Here is the genuine code snippet:
{code}

Using this method, indicate whether the snippet contains a defect.
Respond solely with '###TRUE###' or '###FALSE###'.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────
**Variation 9**
```python
defect_detection_template_analogical_v9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Use a systematic method to inspect code for any errors.
First, generate a simple, comparable piece of code that might be defective.
Explain your thought process and the steps you would take to uncover the error.
Later, I will provide you with the actual snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly offer your self-generated code sample and explanation."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Below is the actual code:
{code}

Following the same technique, does this code exhibit a defect?
Reply solely with ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────
**Variation 10**
```python
defect_detection_template_analogical_v10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Employ a systematic approach to verify if the code contains a defect.
Initially, create an uncomplicated, similar code snippet that may include an error.
Detail your reasoning and step-by-step procedure used to identify any flaw.
Subsequently, I will present the authentic code snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Please offer your self-constructed example along with detailed reasoning."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Take a look at the actual code snippet:
{code}

Using the same method, determine if a defect is present.
Answer strictly with ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────
**Variation 11**
```python
defect_detection_template_analogical_v11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt a methodical approach to review the code for possible defects.
Begin by formulating a simple, parallel code example that might display a fault.
Walk through your process and thought steps for identifying the potential error.
Afterward, I will provide you with the true code snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Please provide the example you've created along with your explanatory process."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Now, consider the actual code snippet:
{code}

Employing the same approach, confirm whether a defect exists.
Respond solely with ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────
**Variation 12**
```python
defect_detection_template_analogical_v12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Utilize a systematic method to check the code for faults.
Start by drafting a basic example similar to the code that might include an error.
Describe in detail how you would detect such an error, outlining your reasoning.
Following that, I will share the actual code snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Submit your self-devised example and the steps of your reasoning."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Here is the genuine code snippet:
{code}

Using the same method, indicate if a defect is present.
Answer only with ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────
**Variation 13**
```python
defect_detection_template_analogical_v13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Employ a systematic strategy to assess whether code contains an error.
Initially, produce a simple, corresponding example that might be flawed.
Explain your logical steps and reasoning in detecting the error.
Later, I will provide you with the actual snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly present the example you created along with your thought process."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Below is the actual code snippet:
{code}

Following the same strategy, does this snippet have a defect?
Answer exclusively with either ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────
**Variation 14**
```python
defect_detection_template_analogical_v14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Scrutinize a section of code for potential flaws.
First, design a simple, comparable sample that might be compromised by an error.
Outline your step-by-step reasoning process to locate the defect.
After which, I will provide the real code snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Please share your self-generated example along with the reasoning behind your detection method."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''This is the actual code snippet:
{code}

Using the same analysis, determine if there is a defect.
Respond only with ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────
**Variation 15**
```python
defect_detection_template_analogical_v15 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Apply a systematic approach to decide whether the code contains an error.
Begin by crafting a simple, similar code snippet that might harbor an error.
Detail every step of your method and the reasoning behind identifying the flaw.
Then, I will share the actual code snippet with you.'''
    ),
    HumanMessagePromptTemplate.from_template("Share your self-crafted example along with the explanation of your method."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Here is the actual code snippet:
{code}

Following the same approach, indicate whether a defect exists.
Answer with exactly ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```
