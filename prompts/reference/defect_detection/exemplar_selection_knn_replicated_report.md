
---



```python
defect_detection_template_defect_detection = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Is there a defect in the code?
Reply with ###TRUE### or ###FALSE### only.'''
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
defect_detection_template_defect_detection_variant1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Does the code contain a defect?
Answer exclusively with ###TRUE### or ###FALSE###.'''
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
defect_detection_template_defect_detection_variant2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Is the code defective?
Respond solely with ###TRUE### or ###FALSE###.'''
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
defect_detection_template_defect_detection_variant3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Does the provided code have any defects?
Reply with only ###TRUE### or ###FALSE###.'''
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
defect_detection_template_defect_detection_variant4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Identify if there is any defect in the code.
Provide your answer as either ###TRUE### or ###FALSE### only.'''
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
defect_detection_template_defect_detection_variant5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine whether the code has a defect.
Respond with either ###TRUE### or ###FALSE### exclusively.'''
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
defect_detection_template_defect_detection_variant6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Can you detect a defect in the code?
Your answer must be either ###TRUE### or ###FALSE### only.'''
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
defect_detection_template_defect_detection_variant7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Is there any flaw in the code?
Please reply using only ###TRUE### or ###FALSE###.'''
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
defect_detection_template_defect_detection_variant8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Review the code for any defects.
Answer strictly with ###TRUE### or ###FALSE###.'''
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
defect_detection_template_defect_detection_variant9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Does the code exhibit any defect?
Your response should be solely ###TRUE### or ###FALSE###.'''
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
defect_detection_template_defect_detection_variant10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Examine the code to determine if a defect is present.
Reply only with ###TRUE### or ###FALSE###.'''
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
defect_detection_template_defect_detection_variant11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Is a defect present in the code?
Please answer only with ###TRUE### or ###FALSE###.'''
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
defect_detection_template_defect_detection_variant12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Evaluate the code to ascertain if there is a defect.
Respond exclusively with ###TRUE### or ###FALSE###.'''
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
defect_detection_template_defect_detection_variant13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Assess the code to determine if it contains a defect.
Reply with just ###TRUE### or ###FALSE###.'''
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
defect_detection_template_defect_detection_variant14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Review the code and confirm whether a defect exists.
Answer exclusively with ###TRUE### or ###FALSE###.'''
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
