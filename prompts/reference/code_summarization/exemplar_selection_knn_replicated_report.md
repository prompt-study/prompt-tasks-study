```python
code_summarization_template_code_summarization_variant0 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Provide a summary of the following code.'''
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
code_summarization_template_code_summarization_variant1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Summarize the following code snippet.'''
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
code_summarization_template_code_summarization_variant2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Write a brief summary of the code provided below.'''
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
code_summarization_template_code_summarization_variant3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Generate a concise summary of the code shown below.'''
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
code_summarization_template_code_summarization_variant4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Provide a clear summary of the following code.'''
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
code_summarization_template_code_summarization_variant5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Summarize the functionality of the code provided below.'''
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
code_summarization_template_code_summarization_variant6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Offer a summary of the code displayed below.'''
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
code_summarization_template_code_summarization_variant7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Give a brief explanation of what the following code does.'''
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
code_summarization_template_code_summarization_variant8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Create a summary for the code provided below.'''
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
code_summarization_template_code_summarization_variant9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Deliver a summary of the code shown below.'''
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
code_summarization_template_code_summarization_variant10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Summarize the following code in a few sentences.'''
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
code_summarization_template_code_summarization_variant11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Provide an overview summary of the code below.'''
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
code_summarization_template_code_summarization_variant12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Generate an outline summary of the code presented below.'''
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
code_summarization_template_code_summarization_variant13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Offer a concise overview of the functionality of the code below.'''
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
code_summarization_template_code_summarization_variant14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Write a summary describing what the following code does.'''
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
