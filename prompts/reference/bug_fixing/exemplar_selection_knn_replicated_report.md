```python
bug_fixing_template_bug_fixing = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Fix the bug in the code and provide only the corrected version.'''
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
bug_fixing_template_bug_fixing_variant1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Identify and resolve the bug in the code; supply only the corrected code.'''
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
bug_fixing_template_bug_fixing_variant2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Rectify the error in the code and return only the fixed version.'''
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
bug_fixing_template_bug_fixing_variant3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Correct the bug present in the code and output only the amended version.'''
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
bug_fixing_template_bug_fixing_variant4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Locate and fix the error in the code. Provide only the revised code.'''
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
bug_fixing_template_bug_fixing_variant5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Resolve the bug in the code and present solely the corrected version.'''
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
bug_fixing_template_bug_fixing_variant6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Repair the bug in the code and return only the updated version.'''
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
bug_fixing_template_bug_fixing_variant7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Detect and correct the bug in the code; output only the fixed code.'''
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
bug_fixing_template_bug_fixing_variant8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Amend the code by fixing the bug, and provide only the corrected code.'''
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
bug_fixing_template_bug_fixing_variant9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Debug the code by fixing the issue and return only the corrected version.'''
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
bug_fixing_template_bug_fixing_variant10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Eliminate the bug in the code and provide only the revised, error-free version.'''
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
bug_fixing_template_bug_fixing_variant11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Address the bug in the code and supply only the corrected, functioning version.'''
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
bug_fixing_template_bug_fixing_variant12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Correct the identified bug in the code and output only the fixed version.'''
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
bug_fixing_template_bug_fixing_variant13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Resolve the coding error by fixing the bug, and return only the updated code.'''
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
bug_fixing_template_bug_fixing_variant14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Fix the bug in the code and return only the final, corrected version.'''
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
