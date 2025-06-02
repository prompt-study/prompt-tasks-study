```python
# Variation 0 (original)
code_generation_template_style_variant0 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Write code in a straightforward, professional style for the following task.
Provide only the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Description:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 1 (Modified Tone)
code_generation_template_style_variant1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Generate code with a creative and engaging tone to complete the task below.
Return only the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Outline:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 2 (Unchanged)
code_generation_template_style_variant2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Develop code in a clean and authoritative style for the task described below.
Submit only the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Description of Task:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 3 (Modified Tone)
code_generation_template_style_variant3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Construct code using an innovative and intuitive approach for the assignment that follows.
Provide solely the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Project Details:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 4 (Modified Tone)
code_generation_template_style_variant4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Produce code in a sleek and modern style for the subsequent task.
Ensure that your answer includes only the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Specifications:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 5 (Modified Tone)
code_generation_template_style_variant5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Write concise code using a vibrant and energetic style to address the problem below.
Output only the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Problem Statement:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 6 (Modified Tone)
code_generation_template_style_variant6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Draft code in a methodical and pragmatic style for the given assignment.
Return just the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Assignment Description:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 7 (Modified Tone)
code_generation_template_style_variant7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Create code with a dynamic and innovative spirit to solve the task below.
Provide only the code in your response.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Synopsis:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 8 (Modified Tone)
code_generation_template_style_variant8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Write code in a succinct and articulate manner for the task outlined below.
Return solely the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Elaborated Task:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 9 (Modified Tone)
code_generation_template_style_variant9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Formulate code with precision and a modern pragmatic approach for the following task.
Include nothing but the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Snapshot:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 10 (Modified Tone)
code_generation_template_style_variant10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Code should be crafted with a decisive and innovative approach for the task provided.
Present only the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Project Overview:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 11 (Modified Tone)
code_generation_template_style_variant11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Develop code with a streamlined and modern approach for the task described.
Include just the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Project Information:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 12 (Modified Tone)
code_generation_template_style_variant12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Generate code with a fresh and creative perspective for the task specified below.
Return only the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Recap:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 13 (Modified Tone)
code_generation_template_style_variant13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Craft code with a refined and innovative style suited for the following task.
Submit only the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Concise Task Brief:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 14 (Modified Tone)
code_generation_template_style_variant14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Prepare code in a bold and contemporary manner to address the task presented below.
Offer only the code in your answer.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Insights:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```
