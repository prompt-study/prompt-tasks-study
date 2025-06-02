```python
exception_type_template_exception_type_variant0 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine which exception type should replace __HOLE__ in the given code.
Respond with the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code:
    {input_1}

    Output:
    {output_1}

    Code:
    {input_2}

    Output:
    {output_2}

    Code:
    {input_3}

    Output:
    {output_3}

    Code:
    {input_4}

    Output:
    {output_4}

    Code:
    {input_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
exception_type_template_exception_type_variant1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Identify the proper exception type to substitute for __HOLE__ in the code provided.
Respond using the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code:
    {input_1}

    Output:
    {output_1}

    Code:
    {input_2}

    Output:
    {output_2}

    Code:
    {input_3}

    Output:
    {output_3}

    Code:
    {input_4}

    Output:
    {output_4}

    Code:
    {input_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
exception_type_template_exception_type_variant2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine the correct exception type to fill in for __HOLE__ in the given code.
Provide your answer using the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code:
    {input_1}

    Output:
    {output_1}

    Code:
    {input_2}

    Output:
    {output_2}

    Code:
    {input_3}

    Output:
    {output_3}

    Code:
    {input_4}

    Output:
    {output_4}

    Code:
    {input_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
exception_type_template_exception_type_variant3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Figure out which exception type should be inserted in place of __HOLE__ in the code below.
Answer in the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code:
    {input_1}

    Output:
    {output_1}

    Code:
    {input_2}

    Output:
    {output_2}

    Code:
    {input_3}

    Output:
    {output_3}

    Code:
    {input_4}

    Output:
    {output_4}

    Code:
    {input_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
exception_type_template_exception_type_variant4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Decide on the exception type that ought to replace __HOLE__ in the provided code snippet.
Respond using ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code:
    {input_1}

    Output:
    {output_1}

    Code:
    {input_2}

    Output:
    {output_2}

    Code:
    {input_3}

    Output:
    {output_3}

    Code:
    {input_4}

    Output:
    {output_4}

    Code:
    {input_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
exception_type_template_exception_type_variant5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Establish which exception type is appropriate to replace __HOLE__ in the code.
Your answer should follow the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code:
    {input_1}

    Output:
    {output_1}

    Code:
    {input_2}

    Output:
    {output_2}

    Code:
    {input_3}

    Output:
    {output_3}

    Code:
    {input_4}

    Output:
    {output_4}

    Code:
    {input_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
exception_type_template_exception_type_variant6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine the exception type that should substitute for __HOLE__ in the given code segment.
Reply using the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code:
    {input_1}

    Output:
    {output_1}

    Code:
    {input_2}

    Output:
    {output_2}

    Code:
    {input_3}

    Output:
    {output_3}

    Code:
    {input_4}

    Output:
    {output_4}

    Code:
    {input_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
exception_type_template_exception_type_variant7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Ascertain the correct exception type to use in place of __HOLE__ in the code provided.
Provide your answer in the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code:
    {input_1}

    Output:
    {output_1}

    Code:
    {input_2}

    Output:
    {output_2}

    Code:
    {input_3}

    Output:
    {output_3}

    Code:
    {input_4}

    Output:
    {output_4}

    Code:
    {input_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
exception_type_template_exception_type_variant8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Select the appropriate exception type to replace __HOLE__ in the code snippet.
Reply in the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code:
    {input_1}

    Output:
    {output_1}

    Code:
    {input_2}

    Output:
    {output_2}

    Code:
    {input_3}

    Output:
    {output_3}

    Code:
    {input_4}

    Output:
    {output_4}

    Code:
    {input_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
exception_type_template_exception_type_variant9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Identify which exception type is best suited to replace __HOLE__ in the code.
Answer using the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code:
    {input_1}

    Output:
    {output_1}

    Code:
    {input_2}

    Output:
    {output_2}

    Code:
    {input_3}

    Output:
    {output_3}

    Code:
    {input_4}

    Output:
    {output_4}

    Code:
    {input_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
exception_type_template_exception_type_variant10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Choose the correct exception type to fill the __HOLE__ in the code.
Respond solely in the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code:
    {input_1}

    Output:
    {output_1}

    Code:
    {input_2}

    Output:
    {output_2}

    Code:
    {input_3}

    Output:
    {output_3}

    Code:
    {input_4}

    Output:
    {output_4}

    Code:
    {input_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
exception_type_template_exception_type_variant11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine the exception type that should replace __HOLE__ in the provided code.
Return your answer using the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code:
    {input_1}

    Output:
    {output_1}

    Code:
    {input_2}

    Output:
    {output_2}

    Code:
    {input_3}

    Output:
    {output_3}

    Code:
    {input_4}

    Output:
    {output_4}

    Code:
    {input_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
exception_type_template_exception_type_variant12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Figure out the appropriate exception type to substitute for __HOLE__ in the code.
Answer in the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code:
    {input_1}

    Output:
    {output_1}

    Code:
    {input_2}

    Output:
    {output_2}

    Code:
    {input_3}

    Output:
    {output_3}

    Code:
    {input_4}

    Output:
    {output_4}

    Code:
    {input_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
exception_type_template_exception_type_variant13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Decide which exception type fits best to replace __HOLE__ in the given code.
Provide your answer as ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code:
    {input_1}

    Output:
    {output_1}

    Code:
    {input_2}

    Output:
    {output_2}

    Code:
    {input_3}

    Output:
    {output_3}

    Code:
    {input_4}

    Output:
    {output_4}

    Code:
    {input_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
exception_type_template_exception_type_variant14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Identify the exception type that should replace __HOLE__ in the code snippet.
Reply exclusively in the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code:
    {input_1}

    Output:
    {output_1}

    Code:
    {input_2}

    Output:
    {output_2}

    Code:
    {input_3}

    Output:
    {output_3}

    Code:
    {input_4}

    Output:
    {output_4}

    Code:
    {input_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```
