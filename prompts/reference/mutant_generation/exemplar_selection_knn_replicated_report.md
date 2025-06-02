```python
mutant_generation_template_mutant_generation = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Generate a mutant of this code with small changes.
Provide only the mutated code.'''
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
mutant_generation_template_mutant_generation_variant1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Create a variant of the given code by making subtle modifications.
Return solely the mutated code.'''
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
mutant_generation_template_mutant_generation_variant2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Develop a mutant version of this code by applying minor alterations.
Output only the mutated code.'''
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
mutant_generation_template_mutant_generation_variant3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Produce a modified version of the code with slight adjustments.
Provide only the altered code.'''
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
mutant_generation_template_mutant_generation_variant4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Construct a mutant of the code by introducing small changes.
Submit only the mutated code.'''
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
mutant_generation_template_mutant_generation_variant5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Generate an altered version of the code with minimal modifications.
Return just the mutated code.'''
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
mutant_generation_template_mutant_generation_variant6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Derive a mutant version of the code through minor tweaks.
Deliver only the updated code.'''
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
mutant_generation_template_mutant_generation_variant7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Create a mutated variant of this code by applying small modifications.
Output solely the mutated code.'''
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
mutant_generation_template_mutant_generation_variant8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Formulate a mutant of the given code with slight revisions.
Provide exclusively the mutated code.'''
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
mutant_generation_template_mutant_generation_variant9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Craft a mutated version of this code using small changes.
Return only the modified code.'''
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
mutant_generation_template_mutant_generation_variant10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Construct a variant of the code with subtle modifications.
Submit only the mutated code.'''
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
mutant_generation_template_mutant_generation_variant11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Generate a slight mutant of this code by introducing minimal adjustments.
Return exclusively the mutated code.'''
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
mutant_generation_template_mutant_generation_variant12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Produce a mutant of the code by applying slight modifications.
Return only the altered code.'''
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
mutant_generation_template_mutant_generation_variant13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Create a variant of the code through small, targeted modifications.
Return solely the mutated code.'''
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
mutant_generation_template_mutant_generation_variant14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Develop a mutant of this code by implementing minor tweaks.
Return exclusively the mutated code.'''
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
