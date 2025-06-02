```python
# Variation 0: Senior Software Engineer
code_question_answering_template_role_c_0 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Senior Software Engineer.
Evaluate whether the provided code is an accurate and complete response to the question.
Provide only ###TRUE### if the code fully satisfies the query or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 1: Software Developer
code_question_answering_template_role_c_1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Software Developer.
Evaluate whether the provided code is an accurate and complete response to the question.
Provide only ###TRUE### if the code fully satisfies the query or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 2: Technical Lead
code_question_answering_template_role_c_2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Technical Lead.
Evaluate whether the provided code is an accurate and complete response to the question.
Provide only ###TRUE### if the code fully satisfies the query or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 3: Software Architect
code_question_answering_template_role_c_3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Software Architect.
Evaluate whether the provided code is an accurate and complete response to the question.
Provide only ###TRUE### if the code fully satisfies the query or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 4: DevOps Engineer
code_question_answering_template_role_c_4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a DevOps Engineer.
Evaluate whether the provided code is an accurate and complete response to the question.
Provide only ###TRUE### if the code fully satisfies the query or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 5: Code Reviewer
code_question_answering_template_role_c_5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Code Reviewer.
Evaluate whether the provided code is an accurate and complete response to the question.
Provide only ###TRUE### if the code fully satisfies the query or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 6: Quality Assurance Engineer
code_question_answering_template_role_c_6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Quality Assurance Engineer.
Evaluate whether the provided code is an accurate and complete response to the question.
Provide only ###TRUE### if the code fully satisfies the query or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 7: Security Engineer
code_question_answering_template_role_c_7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Security Engineer.
Evaluate whether the provided code is an accurate and complete response to the question.
Provide only ###TRUE### if the code fully satisfies the query or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 8: Data Scientist
code_question_answering_template_role_c_8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Data Scientist.
Evaluate whether the provided code is an accurate and complete response to the question.
Provide only ###TRUE### if the code fully satisfies the query or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 9: UI/UX Designer
code_question_answering_template_role_c_9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a UI/UX Designer.
Evaluate whether the provided code is an accurate and complete response to the question.
Provide only ###TRUE### if the code fully satisfies the query or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 10: Algorithm Designer
code_question_answering_template_role_c_10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are an Algorithm Designer.
Evaluate whether the provided code is an accurate and complete response to the question.
Provide only ###TRUE### if the code fully satisfies the query or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 11: Technical Writer
code_question_answering_template_role_c_11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Technical Writer.
Evaluate whether the provided code is an accurate and complete response to the question.
Provide only ###TRUE### if the code fully satisfies the query or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 12: Performance Analysis Researcher
code_question_answering_template_role_c_12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Performance Analysis Researcher.
Evaluate whether the provided code is an accurate and complete response to the question.
Provide only ###TRUE### if the code fully satisfies the query or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 13: Computer Science Researcher
code_question_answering_template_role_c_13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Computer Science Researcher.
Evaluate whether the provided code is an accurate and complete response to the question.
Provide only ###TRUE### if the code fully satisfies the query or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 14: Software Engineering Professor
code_question_answering_template_role_c_14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are a Software Engineering Professor.
Evaluate whether the provided code is an accurate and complete response to the question.
Provide only ###TRUE### if the code fully satisfies the query or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```
