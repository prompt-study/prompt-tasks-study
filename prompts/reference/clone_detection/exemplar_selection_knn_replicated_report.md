```python
clone_detection_template_clone_detection_variant0 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine if the two code snippets are clones.
Answer with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code Snippet 1:
    {input1_1}

    Code Snippet 2:
    {input2_1}

    Output:
    {output_1}


    Code Snippet 1:
    {input1_2}

    Code Snippet 2:
    {input2_2}

    Output:
    {output_2}


    Code Snippet 1:
    {input1_3}

    Code Snippet 2:
    {input2_3}

    Output:
    {output_3}


    Code Snippet 1:
    {input1_4}

    Code Snippet 2:
    {input2_4}

    Output:
    {output_4}


    Code Snippet 1:
    {input1_5}

    Code Snippet 2:
    {input2_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Snippet 1:
        {code_snippet1}

        Code Snippet 2:
        {code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
clone_detection_template_clone_detection_variant1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Evaluate whether the two code snippets are identical clones.
Respond exclusively with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code Snippet 1:
    {input1_1}

    Code Snippet 2:
    {input2_1}

    Output:
    {output_1}


    Code Snippet 1:
    {input1_2}

    Code Snippet 2:
    {input2_2}

    Output:
    {output_2}


    Code Snippet 1:
    {input1_3}

    Code Snippet 2:
    {input2_3}

    Output:
    {output_3}


    Code Snippet 1:
    {input1_4}

    Code Snippet 2:
    {input2_4}

    Output:
    {output_4}


    Code Snippet 1:
    {input1_5}

    Code Snippet 2:
    {input2_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Snippet 1:
        {code_snippet1}

        Code Snippet 2:
        {code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
clone_detection_template_clone_detection_variant2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Assess if the provided code snippets are clones.
Answer only with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code Snippet 1:
    {input1_1}

    Code Snippet 2:
    {input2_1}

    Output:
    {output_1}


    Code Snippet 1:
    {input1_2}

    Code Snippet 2:
    {input2_2}

    Output:
    {output_2}


    Code Snippet 1:
    {input1_3}

    Code Snippet 2:
    {input2_3}

    Output:
    {output_3}


    Code Snippet 1:
    {input1_4}

    Code Snippet 2:
    {input2_4}

    Output:
    {output_4}


    Code Snippet 1:
    {input1_5}

    Code Snippet 2:
    {input2_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Snippet 1:
        {code_snippet1}

        Code Snippet 2:
        {code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
clone_detection_template_clone_detection_variant3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Check if the following two code samples are clones.
Return your answer as ###TRUE### if they match, or ###FALSE### if they do not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code Snippet 1:
    {input1_1}

    Code Snippet 2:
    {input2_1}

    Output:
    {output_1}


    Code Snippet 1:
    {input1_2}

    Code Snippet 2:
    {input2_2}

    Output:
    {output_2}


    Code Snippet 1:
    {input1_3}

    Code Snippet 2:
    {input2_3}

    Output:
    {output_3}


    Code Snippet 1:
    {input1_4}

    Code Snippet 2:
    {input2_4}

    Output:
    {output_4}


    Code Snippet 1:
    {input1_5}

    Code Snippet 2:
    {input2_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Snippet 1:
        {code_snippet1}

        Code Snippet 2:
        {code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
clone_detection_template_clone_detection_variant4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Decide if the two code snippets are clones.
Answer with only ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code Snippet 1:
    {input1_1}

    Code Snippet 2:
    {input2_1}

    Output:
    {output_1}


    Code Snippet 1:
    {input1_2}

    Code Snippet 2:
    {input2_2}

    Output:
    {output_2}


    Code Snippet 1:
    {input1_3}

    Code Snippet 2:
    {input2_3}

    Output:
    {output_3}


    Code Snippet 1:
    {input1_4}

    Code Snippet 2:
    {input2_4}

    Output:
    {output_4}


    Code Snippet 1:
    {input1_5}

    Code Snippet 2:
    {input2_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Snippet 1:
        {code_snippet1}

        Code Snippet 2:
        {code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
clone_detection_template_clone_detection_variant5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine if these two code snippets are identical clones.
Provide your answer solely as ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code Snippet 1:
    {input1_1}

    Code Snippet 2:
    {input2_1}

    Output:
    {output_1}


    Code Snippet 1:
    {input1_2}

    Code Snippet 2:
    {input2_2}

    Output:
    {output_2}


    Code Snippet 1:
    {input1_3}

    Code Snippet 2:
    {input2_3}

    Output:
    {output_3}


    Code Snippet 1:
    {input1_4}

    Code Snippet 2:
    {input2_4}

    Output:
    {output_4}


    Code Snippet 1:
    {input1_5}

    Code Snippet 2:
    {input2_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Snippet 1:
        {code_snippet1}

        Code Snippet 2:
        {code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
clone_detection_template_clone_detection_variant6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Examine whether the two code segments are clones.
Reply with ###TRUE### if they are clones, or ###FALSE### if they are not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code Snippet 1:
    {input1_1}

    Code Snippet 2:
    {input2_1}

    Output:
    {output_1}


    Code Snippet 1:
    {input1_2}

    Code Snippet 2:
    {input2_2}

    Output:
    {output_2}


    Code Snippet 1:
    {input1_3}

    Code Snippet 2:
    {input2_3}

    Output:
    {output_3}


    Code Snippet 1:
    {input1_4}

    Code Snippet 2:
    {input2_4}

    Output:
    {output_4}


    Code Snippet 1:
    {input1_5}

    Code Snippet 2:
    {input2_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Snippet 1:
        {code_snippet1}

        Code Snippet 2:
        {code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
clone_detection_template_clone_detection_variant7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Verify if the pair of code snippets are clones.
Your answer must be either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code Snippet 1:
    {input1_1}

    Code Snippet 2:
    {input2_1}

    Output:
    {output_1}


    Code Snippet 1:
    {input1_2}

    Code Snippet 2:
    {input2_2}

    Output:
    {output_2}


    Code Snippet 1:
    {input1_3}

    Code Snippet 2:
    {input2_3}

    Output:
    {output_3}


    Code Snippet 1:
    {input1_4}

    Code Snippet 2:
    {input2_4}

    Output:
    {output_4}


    Code Snippet 1:
    {input1_5}

    Code Snippet 2:
    {input2_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Snippet 1:
        {code_snippet1}

        Code Snippet 2:
        {code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
clone_detection_template_clone_detection_variant8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Investigate if the two given code snippets are clones.
Answer with just ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code Snippet 1:
    {input1_1}

    Code Snippet 2:
    {input2_1}

    Output:
    {output_1}


    Code Snippet 1:
    {input1_2}

    Code Snippet 2:
    {input2_2}

    Output:
    {output_2}


    Code Snippet 1:
    {input1_3}

    Code Snippet 2:
    {input2_3}

    Output:
    {output_3}


    Code Snippet 1:
    {input1_4}

    Code Snippet 2:
    {input2_4}

    Output:
    {output_4}


    Code Snippet 1:
    {input1_5}

    Code Snippet 2:
    {input2_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Snippet 1:
        {code_snippet1}

        Code Snippet 2:
        {code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
clone_detection_template_clone_detection_variant9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Check whether the two provided code snippets are clones.
Respond with either ###TRUE### or ###FALSE### only.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code Snippet 1:
    {input1_1}

    Code Snippet 2:
    {input2_1}

    Output:
    {output_1}


    Code Snippet 1:
    {input1_2}

    Code Snippet 2:
    {input2_2}

    Output:
    {output_2}


    Code Snippet 1:
    {input1_3}

    Code Snippet 2:
    {input2_3}

    Output:
    {output_3}


    Code Snippet 1:
    {input1_4}

    Code Snippet 2:
    {input2_4}

    Output:
    {output_4}


    Code Snippet 1:
    {input1_5}

    Code Snippet 2:
    {input2_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Snippet 1:
        {code_snippet1}

        Code Snippet 2:
        {code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
clone_detection_template_clone_detection_variant10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Assess the similarity of the two code snippets to determine if they are clones.
Answer solely with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code Snippet 1:
    {input1_1}

    Code Snippet 2:
    {input2_1}

    Output:
    {output_1}


    Code Snippet 1:
    {input1_2}

    Code Snippet 2:
    {input2_2}

    Output:
    {output_2}


    Code Snippet 1:
    {input1_3}

    Code Snippet 2:
    {input2_3}

    Output:
    {output_3}


    Code Snippet 1:
    {input1_4}

    Code Snippet 2:
    {input2_4}

    Output:
    {output_4}


    Code Snippet 1:
    {input1_5}

    Code Snippet 2:
    {input2_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Snippet 1:
        {code_snippet1}

        Code Snippet 2:
        {code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
clone_detection_template_clone_detection_variant11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine if the two code examples are clones.
Provide your answer using only ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code Snippet 1:
    {input1_1}

    Code Snippet 2:
    {input2_1}

    Output:
    {output_1}


    Code Snippet 1:
    {input1_2}

    Code Snippet 2:
    {input2_2}

    Output:
    {output_2}


    Code Snippet 1:
    {input1_3}

    Code Snippet 2:
    {input2_3}

    Output:
    {output_3}


    Code Snippet 1:
    {input1_4}

    Code Snippet 2:
    {input2_4}

    Output:
    {output_4}


    Code Snippet 1:
    {input1_5}

    Code Snippet 2:
    {input2_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Snippet 1:
        {code_snippet1}

        Code Snippet 2:
        {code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
clone_detection_template_clone_detection_variant12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Evaluate whether the given code snippets are clones.
Your answer should be either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code Snippet 1:
    {input1_1}

    Code Snippet 2:
    {input2_1}

    Output:
    {output_1}


    Code Snippet 1:
    {input1_2}

    Code Snippet 2:
    {input2_2}

    Output:
    {output_2}


    Code Snippet 1:
    {input1_3}

    Code Snippet 2:
    {input2_3}

    Output:
    {output_3}


    Code Snippet 1:
    {input1_4}

    Code Snippet 2:
    {input2_4}

    Output:
    {output_4}


    Code Snippet 1:
    {input1_5}

    Code Snippet 2:
    {input2_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Snippet 1:
        {code_snippet1}

        Code Snippet 2:
        {code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
clone_detection_template_clone_detection_variant13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Analyze the two code snippets to see if they are clones.
Answer only with ###TRUE### if they are, or ###FALSE### otherwise.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code Snippet 1:
    {input1_1}

    Code Snippet 2:
    {input2_1}

    Output:
    {output_1}


    Code Snippet 1:
    {input1_2}

    Code Snippet 2:
    {input2_2}

    Output:
    {output_2}


    Code Snippet 1:
    {input1_3}

    Code Snippet 2:
    {input2_3}

    Output:
    {output_3}


    Code Snippet 1:
    {input1_4}

    Code Snippet 2:
    {input2_4}

    Output:
    {output_4}


    Code Snippet 1:
    {input1_5}

    Code Snippet 2:
    {input2_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Snippet 1:
        {code_snippet1}

        Code Snippet 2:
        {code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
clone_detection_template_clone_detection_variant14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Decide whether the two code snippets are clones.
Return your response as ###TRUE### if they are, or ###FALSE### if they are not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Code Snippet 1:
    {input1_1}

    Code Snippet 2:
    {input2_1}

    Output:
    {output_1}


    Code Snippet 1:
    {input1_2}

    Code Snippet 2:
    {input2_2}

    Output:
    {output_2}


    Code Snippet 1:
    {input1_3}

    Code Snippet 2:
    {input2_3}

    Output:
    {output_3}


    Code Snippet 1:
    {input1_4}

    Code Snippet 2:
    {input2_4}

    Output:
    {output_4}


    Code Snippet 1:
    {input1_5}

    Code Snippet 2:
    {input2_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Snippet 1:
        {code_snippet1}

        Code Snippet 2:
        {code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```
