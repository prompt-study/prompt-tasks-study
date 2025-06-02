
```python
assert_generation_template_assert_generation_variant0 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine the correct assertion that should replace <AssertPlaceHolder> in the given code.
Provide only the assertion statement.'''
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
assert_generation_template_assert_generation_variant1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Identify the appropriate assertion to replace <AssertPlaceHolder> in the code below.
Return only the assertion statement.'''
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
assert_generation_template_assert_generation_variant2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine which assertion should substitute for <AssertPlaceHolder> in the given code.
Return only the assertion statement.'''
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
assert_generation_template_assert_generation_variant3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Find the correct assertion that must replace <AssertPlaceHolder> in the provided code.
Respond with only the assertion statement.'''
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
assert_generation_template_assert_generation_variant4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Ascertain the proper assertion to use in place of <AssertPlaceHolder> in the code.
Provide solely the assertion statement.'''
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
assert_generation_template_assert_generation_variant5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Decide on the correct assertion to substitute for <AssertPlaceHolder> in the following code snippet.
Output only the assertion statement.'''
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
assert_generation_template_assert_generation_variant6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Figure out the appropriate assertion to replace <AssertPlaceHolder> in the code below.
Provide only the assertion statement.'''
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
assert_generation_template_assert_generation_variant7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine the proper assertion that should take the place of <AssertPlaceHolder> in the provided code.
Return solely the assertion statement.'''
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
assert_generation_template_assert_generation_variant8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Select the appropriate assertion to fill in for <AssertPlaceHolder> in the code snippet.
Respond providing only the assertion statement.'''
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
assert_generation_template_assert_generation_variant9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Establish which assertion is best suited to replace <AssertPlaceHolder> in the code.
Answer using only the assertion statement.'''
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
assert_generation_template_assert_generation_variant10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Decide which assertion should be used to replace <AssertPlaceHolder> in the code.
Provide exclusively the assertion statement.'''
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
assert_generation_template_assert_generation_variant11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Identify the assertion that correctly replaces <AssertPlaceHolder> in the provided code.
Answer only with the assertion statement.'''
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
assert_generation_template_assert_generation_variant12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine the assertion that must replace <AssertPlaceHolder> in the given code.
Return your answer solely as the assertion statement.'''
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
assert_generation_template_assert_generation_variant13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Figure out the appropriate assertion to insert in place of <AssertPlaceHolder> in the code.
Respond with only the assertion statement.'''
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
assert_generation_template_assert_generation_variant14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Ascertain the correct assertion that belongs in place of <AssertPlaceHolder> in the code.
Provide only the assertion statement.'''
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
