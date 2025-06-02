```python
code_generation_template_code_generation_variant1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Develop code to complete the following task.
Return only the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Task Description:
    {input_1}

    Output:
    {output_1}


    Task Description:
    {input_2}

    Output:
    {output_2}


    Task Description:
    {input_3}

    Output:
    {output_3}


    Task Description:
    {input_4}

    Output:
    {output_4}


    Task Description:
    {input_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_generation_template_code_generation_variant2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Generate a code solution for the task described below.
Provide only the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Task Description:
    {input_1}

    Output:
    {output_1}


    Task Description:
    {input_2}

    Output:
    {output_2}


    Task Description:
    {input_3}

    Output:
    {output_3}


    Task Description:
    {input_4}

    Output:
    {output_4}


    Task Description:
    {input_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Details:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_generation_template_code_generation_variant3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Compose code for the following assignment.
Output exclusively the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Task Description:
    {input_1}

    Output:
    {output_1}


    Task Description:
    {input_2}

    Output:
    {output_2}


    Task Description:
    {input_3}

    Output:
    {output_3}


    Task Description:
    {input_4}

    Output:
    {output_4}


    Task Description:
    {input_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Assignment Description:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_generation_template_code_generation_variant4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Produce code that fulfills the following task.
Include only the code in your output.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Task Description:
    {input_1}

    Output:
    {output_1}


    Task Description:
    {input_2}

    Output:
    {output_2}


    Task Description:
    {input_3}

    Output:
    {output_3}


    Task Description:
    {input_4}

    Output:
    {output_4}


    Task Description:
    {input_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Description of Task:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_generation_template_code_generation_variant5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Write a program to accomplish the task outlined below.
Provide just the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Task Description:
    {input_1}

    Output:
    {output_1}


    Task Description:
    {input_2}

    Output:
    {output_2}


    Task Description:
    {input_3}

    Output:
    {output_3}


    Task Description:
    {input_4}

    Output:
    {output_4}


    Task Description:
    {input_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Statement:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_generation_template_code_generation_variant6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Craft a code solution for the following task.
Return solely the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Task Description:
    {input_1}

    Output:
    {output_1}


    Task Description:
    {input_2}

    Output:
    {output_2}


    Task Description:
    {input_3}

    Output:
    {output_3}


    Task Description:
    {input_4}

    Output:
    {output_4}


    Task Description:
    {input_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_generation_template_code_generation_variant7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Implement code for the task described below.
Supply only the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Task Description:
    {input_1}

    Output:
    {output_1}


    Task Description:
    {input_2}

    Output:
    {output_2}


    Task Description:
    {input_3}

    Output:
    {output_3}


    Task Description:
    {input_4}

    Output:
    {output_4}


    Task Description:
    {input_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Description:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_generation_template_code_generation_variant8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Generate a complete code snippet to solve the following task.
Output only the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Task Description:
    {input_1}

    Output:
    {output_1}


    Task Description:
    {input_2}

    Output:
    {output_2}


    Task Description:
    {input_3}

    Output:
    {output_3}


    Task Description:
    {input_4}

    Output:
    {output_4}


    Task Description:
    {input_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Information:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_generation_template_code_generation_variant9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Create a code solution for the task below.
Present only the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Task Description:
    {input_1}

    Output:
    {output_1}


    Task Description:
    {input_2}

    Output:
    {output_2}


    Task Description:
    {input_3}

    Output:
    {output_3}


    Task Description:
    {input_4}

    Output:
    {output_4}


    Task Description:
    {input_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Requirements:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_generation_template_code_generation_variant10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Develop a program for the following task.
Provide solely the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Task Description:
    {input_1}

    Output:
    {output_1}


    Task Description:
    {input_2}

    Output:
    {output_2}


    Task Description:
    {input_3}

    Output:
    {output_3}


    Task Description:
    {input_4}

    Output:
    {output_4}


    Task Description:
    {input_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Assignment:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_generation_template_code_generation_variant11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Write a code snippet to execute the following task.
Return only the code snippet.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Task Description:
    {input_1}

    Output:
    {output_1}


    Task Description:
    {input_2}

    Output:
    {output_2}


    Task Description:
    {input_3}

    Output:
    {output_3}


    Task Description:
    {input_4}

    Output:
    {output_4}


    Task Description:
    {input_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Overview:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_generation_template_code_generation_variant12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Construct code to address the following task.
Submit only the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Task Description:
    {input_1}

    Output:
    {output_1}


    Task Description:
    {input_2}

    Output:
    {output_2}


    Task Description:
    {input_3}

    Output:
    {output_3}


    Task Description:
    {input_4}

    Output:
    {output_4}


    Task Description:
    {input_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_generation_template_code_generation_variant13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Program a solution for the following task.
Output exclusively the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Task Description:
    {input_1}

    Output:
    {output_1}


    Task Description:
    {input_2}

    Output:
    {output_2}


    Task Description:
    {input_3}

    Output:
    {output_3}


    Task Description:
    {input_4}

    Output:
    {output_4}


    Task Description:
    {input_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Details:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_generation_template_code_generation_variant14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Design and write code for the following task.
Provide only the translated code in your answer.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Task Description:
    {input_1}

    Output:
    {output_1}


    Task Description:
    {input_2}

    Output:
    {output_2}


    Task Description:
    {input_3}

    Output:
    {output_3}


    Task Description:
    {input_4}

    Output:
    {output_4}


    Task Description:
    {input_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Problem Statement:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```
