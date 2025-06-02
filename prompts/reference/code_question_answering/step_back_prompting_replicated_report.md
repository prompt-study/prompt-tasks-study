```python
code_question_answering_template_step_back_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before evaluating the code, step back and consider: What constitutes a complete code answer to a question? Now, determine if the provided code adequately answers the question.
Return ###TRUE### if it fully meets the requirements; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_step_back_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Step back and reflect: What are the essential elements that make a code answer complete? Then, assess whether the provided code snippet fully addresses the question.
Return ###TRUE### if it does; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_step_back_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Consider the general criteria for a complete code answer. Now, evaluate if the provided code snippet fully answers the question.
Return ###TRUE### if it meets all requirements; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_step_back_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Step back: Reflect on the key factors that define a correct and complete code answer. Then, determine if the provided code snippet answers the question adequately.
Return ###TRUE### if all criteria are met; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_step_back_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before delving into the specifics, step back and ask: What makes a code answer complete? Now, assess if the provided code snippet fully satisfies the question.
Return ###TRUE### if it does; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_step_back_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Reflect on the general principles of complete code answers. Now, determine whether the provided code snippet adequately addresses the question.
Return ###TRUE### if the code meets all requirements; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_step_back_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Step back and consider: What are the critical elements of a complete answer when evaluating code? With that in mind, determine if the provided code snippet fully answers the question.
Return ###TRUE### if it does; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_step_back_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before evaluating the code, step back and think: What criteria ensure that a code snippet completely answers a question? Then, decide if the provided code snippet meets those criteria.
Return ###TRUE### if yes; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_step_back_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Step back and reflect on the high-level requirements for a complete code answer. Now, evaluate whether the provided code snippet adequately addresses the question.
Return ###TRUE### if the code is complete; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_step_back_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Take a step back: What are the general factors that determine if a code answer is complete? Then, review the provided code snippet to decide if it fully meets the question's requirements.
Return ###TRUE### if it does; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_step_back_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Reflect on the overall standards for a complete and correct code answer. Now, determine if the provided code snippet meets these standards and fully answers the question.
Return ###TRUE### if it does; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_step_back_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before assessing the code, step back and consider: What does it mean for code to completely answer a question? With that perspective, evaluate if the provided code snippet is sufficient.
Return ###TRUE### if it is; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_step_back_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Step back and think: What are the key high-level requirements for a code snippet to fully answer a question? Now, assess the provided code snippet against those requirements.
Return ###TRUE### if it is complete; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_step_back_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before evaluating, take a step back: What broad criteria define a fully complete code answer? Then, determine whether the provided code snippet satisfies the question.
Return ###TRUE### if it does; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_step_back_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Reflect broadly: What are the essential high-level criteria that make a code answer complete? Now, using that understanding, decide if the provided code snippet fully addresses the question.
Return ###TRUE### if it meets all criteria; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```