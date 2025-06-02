```python
code_translation_template_code_translation = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Translate the following code from {source_language} to {target_language}.
Provide only the translated code.'''
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
code_translation_template_code_translation_variant1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Convert the code below from {source_language} to {target_language}.
Return solely the translated code.'''
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
code_translation_template_code_translation_variant2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Translate the code provided from {source_language} into {target_language}.
Output only the translated version.'''
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
code_translation_template_code_translation_variant3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Please transform the given code from {source_language} to {target_language}.
Only include the translated code in your response.'''
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
code_translation_template_code_translation_variant4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Recast the following code from {source_language} to {target_language}.
Provide the output as just the translated code.'''
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
code_translation_template_code_translation_variant5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Shift the code from {source_language} to {target_language}.
Your answer should consist solely of the translated code.'''
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
code_translation_template_code_translation_variant6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Translate this code snippet from {source_language} to {target_language}.
Ensure that only the translated code is returned.'''
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
code_translation_template_code_translation_variant7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Convert the given code from {source_language} into {target_language}.
Only return the translated code.'''
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
code_translation_template_code_translation_variant8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Reproduce the following code in {target_language}, converting it from {source_language}.
Supply only the translated code.'''
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
code_translation_template_code_translation_variant9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Change the code from {source_language} into {target_language}.
Return exclusively the translated code.'''
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
code_translation_template_code_translation_variant10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Transform the provided code from {source_language} to {target_language}.
Provide only the translated version.'''
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
code_translation_template_code_translation_variant11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Render the following code from {source_language} into {target_language}.
Output only the translated code.'''
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
code_translation_template_code_translation_variant12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Convert the below code from {source_language} to {target_language}.
Present only the translated code.'''
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
code_translation_template_code_translation_variant13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Translate the code sample from {source_language} to {target_language}.
Your response should include only the translated code.'''
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
code_translation_template_code_translation_variant14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adapt the following code from {source_language} to {target_language}.
Return only the translated version of the code.'''
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
