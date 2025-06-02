```python
# Variation 0:
code_generation_template_analogical = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We are going to generate code using an example-based approach.
Begin by presenting a concise coding task example and explain your solution step by step.
After that, I will give you the actual task.'''
    ),
    HumanMessagePromptTemplate.from_template("Please provide your fabricated coding task along with its solution."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Now, here is the real task:
{task_description}

Generate the code. Provide only the code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 1:
code_generation_template_analogical_1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We will create code using an example-based method.
Start by illustrating a simple coding example and detailing your solution process.
Then, I will present you with the genuine task.'''
    ),
    HumanMessagePromptTemplate.from_template("Present your invented coding task and its solution process."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Here is the actual task:
{task_description}

Generate the code and include only the code in your answer.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 2:
code_generation_template_analogical_2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Our approach involves example-based code generation.
Firstly, craft a brief programming example and walk through your solution in steps.
Later, I will supply the real task.'''
    ),
    HumanMessagePromptTemplate.from_template("Share your made-up coding task along with its step-by-step solution."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''The genuine task is as follows:
{task_description}

Provide only the final code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 3:
code_generation_template_analogical_3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We will use an example-based approach to generate code.
Begin with a concise coding example and explain your solution step by step.
Afterwards, I will assign you the real task.'''
    ),
    HumanMessagePromptTemplate.from_template("Please share your fictional coding task and the accompanying solution."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Here is the actual assignment:
{task_description}

Return only the code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 4:
code_generation_template_analogical_4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Let’s generate code using an example-based method.
Initially, design a simple coding problem example and describe your solution step by step.
Then, I will provide the real task.'''
    ),
    HumanMessagePromptTemplate.from_template("Submit your contrived coding problem along with its step-by-step solution."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''This is the actual task:
{task_description}

Generate only the code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 5:
code_generation_template_analogical_5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We'll derive code using an example-based approach.
Start by producing a small programming problem example and explain your solution sequentially.
Afterwards, I will reveal the actual problem.'''
    ),
    HumanMessagePromptTemplate.from_template("Please provide your hypothetical coding problem and its solution."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Now, consider this actual task:
{task_description}

Output only the code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 6:
code_generation_template_analogical_6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Our goal is to generate code via an example-based approach.
Begin with a brief example of a coding task and describe your solution method in detail.
Subsequently, I will provide you with the real task.'''
    ),
    HumanMessagePromptTemplate.from_template("Share your crafted coding challenge along with its detailed solution."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Present the real task here:
{task_description}

Ensure that you only output the code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 7:
code_generation_template_analogical_7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We are set to produce code using an example-based approach.
Begin by outlining a small coding task example and explaining your approach step by step.
Then, the genuine task will be provided.'''
    ),
    HumanMessagePromptTemplate.from_template("Provide your invented coding challenge along with the solution steps."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Now, here's the actual task:
{task_description}

Supply only the code in your response.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 8:
code_generation_template_analogical_8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Let's develop code using an example-based approach.
First, illustrate a brief programming task example and detail your solution one step at a time.
Soon after, I will present the actual task.'''
    ),
    HumanMessagePromptTemplate.from_template("Present your designed coding challenge and its detailed solution process."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''The actual task is:
{task_description}

Generate the code and provide only the code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 9:
code_generation_template_analogical_9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We will be generating code by drawing parallels.
Begin with a concise coding example and walk through your solution thoroughly.
After that, I will deliver the actual assignment.'''
    ),
    HumanMessagePromptTemplate.from_template("Offer your designed coding task along with an explanation of your solution."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Here is the real assignment:
{task_description}

Provide only the code output.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 10:
code_generation_template_analogical_10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We intend to create code using an example-based approach.
Start with a simple programming example and describe your solution step by step.
Later, I will share the final task with you.'''
    ),
    HumanMessagePromptTemplate.from_template("Submit your invented coding problem along with its detailed solution."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Now, present the actual task:
{task_description}

Return only the code in your response.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 11:
code_generation_template_analogical_11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Our strategy is example-based code generation.
First, formulate a small coding challenge and explain your solution sequentially.
After this, I will reveal the real problem.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly provide your fictional coding challenge along with its solution steps."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Here is the genuine task:
{task_description}

Output only the code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 12:
code_generation_template_analogical_12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We will craft code by drawing on example-based inspiration.
Firstly, generate a minor coding task sample and walk through your methodical solution.
Then, I will describe the real task.'''
    ),
    HumanMessagePromptTemplate.from_template("Present your hypothetical coding challenge and its step-by-step resolution."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''The actual problem is:
{task_description}

Return only the code in your answer.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 13:
code_generation_template_analogical_13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Let's produce code using an example-based method.
Start by creating a brief programming task example and outlining your approach in clear steps.
Afterwards, I will present the actual task.'''
    ),
    HumanMessagePromptTemplate.from_template("Share your fabricated coding task with a detailed explanation of your solution."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Now, here is the actual exercise:
{task_description}

Provide only the code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 14:
code_generation_template_analogical_14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We shall generate code using an example-based approach.
Begin by drafting a small coding example and elaborating your solution step by step.
Afterwards, I will give you the true task.'''
    ),
    HumanMessagePromptTemplate.from_template("Deliver your invented coding task along with its detailed solution steps."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Now, the real challenge is:
{task_description}

Generate the code and output only the code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```
