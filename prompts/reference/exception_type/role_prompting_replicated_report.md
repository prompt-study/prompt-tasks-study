```python
exception_type_template_role_0 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Senior Software Engineer.
Which exception type should replace __HOLE__ in the following code?
Answer using the format: ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
exception_type_template_role_1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Software Developer.
Which exception type should replace __HOLE__ in the following code?
Answer using the format: ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
exception_type_template_role_2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Technical Lead.
Which exception type should replace __HOLE__ in the following code?
Answer using the format: ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
exception_type_template_role_3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Software Architect.
Which exception type should replace __HOLE__ in the following code?
Answer using the format: ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
exception_type_template_role_4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a DevOps Engineer.
Which exception type should replace __HOLE__ in the following code?
Answer using the format: ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
exception_type_template_role_5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Code Reviewer.
Which exception type should replace __HOLE__ in the following code?
Answer using the format: ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
exception_type_template_role_6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Quality Assurance Engineer.
Which exception type should replace __HOLE__ in the following code?
Answer using the format: ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
exception_type_template_role_7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Security Engineer.
Which exception type should replace __HOLE__ in the following code?
Answer using the format: ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
exception_type_template_role_8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Data Scientist.
Which exception type should replace __HOLE__ in the following code?
Answer using the format: ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
exception_type_template_role_9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a UI/UX Designer.
Which exception type should replace __HOLE__ in the following code?
Answer using the format: ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
exception_type_template_role_10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are an Algorithm Designer.
Which exception type should replace __HOLE__ in the following code?
Answer using the format: ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
exception_type_template_role_11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Technical Writer.
Which exception type should replace __HOLE__ in the following code?
Answer using the format: ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
exception_type_template_role_12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Performance Analysis Researcher.
Which exception type should replace __HOLE__ in the following code?
Answer using the format: ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
exception_type_template_role_13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Computer Science Researcher.
Which exception type should replace __HOLE__ in the following code?
Answer using the format: ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
exception_type_template_role_14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Software Engineering Professor.
Which exception type should replace __HOLE__ in the following code?
Answer using the format: ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```
