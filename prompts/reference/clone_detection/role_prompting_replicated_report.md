```python
# Variation 0: Senior Software Engineer
clone_detection_template_role_0 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Senior Software Engineer.
Are the two code snippets clones of each other? Answer ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 1: Software Developer
clone_detection_template_role_1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Software Developer.
Are the two code snippets clones of each other? Answer ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 2: Technical Lead
clone_detection_template_role_2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Technical Lead.
Are the two code snippets clones of each other? Answer ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 3: Software Architect
clone_detection_template_role_3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Software Architect.
Are the two code snippets clones of each other? Answer ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 4: DevOps Engineer
clone_detection_template_role_4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a DevOps Engineer.
Are the two code snippets clones of each other? Answer ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 5: Code Reviewer
clone_detection_template_role_5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Code Reviewer.
Are the two code snippets clones of each other? Answer ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 6: Quality Assurance Engineer
clone_detection_template_role_6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Quality Assurance Engineer.
Are the two code snippets clones of each other? Answer ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 7: Security Engineer
clone_detection_template_role_7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Security Engineer.
Are the two code snippets clones of each other? Answer ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 8: Data Scientist
clone_detection_template_role_8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Data Scientist.
Are the two code snippets clones of each other? Answer ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 9: UI/UX Designer
clone_detection_template_role_9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a UI/UX Designer.
Are the two code snippets clones of each other? Answer ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 10: Algorithm Designer
clone_detection_template_role_10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are an Algorithm Designer.
Are the two code snippets clones of each other? Answer ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 11: Technical Writer
clone_detection_template_role_11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Technical Writer.
Are the two code snippets clones of each other? Answer ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 12: Performance Analysis Researcher
clone_detection_template_role_12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Performance Analysis Researcher.
Are the two code snippets clones of each other? Answer ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 13: Computer Science Researcher
clone_detection_template_role_13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Computer Science Researcher.
Are the two code snippets clones of each other? Answer ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 14: Software Engineering Professor
clone_detection_template_role_14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Software Engineering Professor.
Are the two code snippets clones of each other? Answer ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```
