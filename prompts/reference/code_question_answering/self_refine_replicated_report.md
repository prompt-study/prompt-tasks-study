

### Variation 0

```python
code_question_answering_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine if the provided code adequately answers the question.
Return ###TRUE### if the code completely meets the question's requirements; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
        {question}

        Code snippet:
        {code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Now, review your initial response and refine your answer.
        Only return ###FINISHED### with your final answer when you are fully satisfied.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```

---

### Variation 1

```python
code_question_answering_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Assess whether the provided code snippet fully answers the question.
Return ###TRUE### if all requirements are met; otherwise, reply with ###FALSE###.
Then, reflect on your answer and iteratively refine it by offering self-feedback until your response is final.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Now, based on your initial response, iteratively provide feedback and update your answer.
Only return ###FINISHED### with your final refined answer when ready.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```

---

### Variation 2

```python
code_question_answering_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Decide if the provided code snippet completely addresses the question.
Return ###TRUE### if it satisfies all requirements; otherwise, reply with ###FALSE###.
After your initial evaluation, iteratively provide self-feedback and update your answer until no further improvements are possible.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Now, reexamine your answer and iteratively incorporate feedback.
Only return ###FINISHED### with your final answer when it is fully refined.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```

---

### Variation 3

```python
code_question_answering_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Evaluate if the provided code snippet fully answers the question.
Return ###TRUE### if it meets every requirement; otherwise, reply with ###FALSE###.
Then, engage in iterative self-review and refine your answer by incorporating your own feedback until it is polished.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Now, iteratively review your evaluation, provide self-feedback, and refine your response.
Only return ###FINISHED### with your final answer when you are completely satisfied.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```

---

### Variation 4

```python
code_question_answering_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine whether the provided code snippet completely answers the question.
Return ###TRUE### if the code meets all requirements; otherwise, reply with ###FALSE###.
After your initial answer, iteratively self-assess and refine your response based on your feedback until it is final.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Now, iteratively review your answer, provide detailed self-feedback, and update your response.
Only return ###FINISHED### with your final answer when no further improvements are needed.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```

---

### Variation 5

```python
code_question_answering_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Review the provided code snippet and decide if it fully answers the question.
Return ###TRUE### if it completely satisfies the requirements; otherwise, reply with ###FALSE###.
Then, iteratively refine your answer through self-feedback until you have reached a final response.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Now, provide iterative self-feedback and refine your answer.
Only return ###FINISHED### with your final answer when it is perfect.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```

---

### Variation 6

```python
code_question_answering_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine if the provided code snippet adequately answers the question.
Return ###TRUE### if the code fully meets the requirements; otherwise, reply with ###FALSE###.
After your initial response, iteratively self-assess and refine your answer until you reach a final conclusion.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Now, evaluate your answer with iterative self-feedback and refine your response.
Only return ###FINISHED### with your final answer when you are fully satisfied.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```

---

### Variation 7

```python
code_question_answering_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Assess whether the provided code snippet completely answers the question.
Return ###TRUE### if it fulfills all criteria; otherwise, reply with ###FALSE###.
Then, engage in iterative self-review and improve your answer based on your feedback until it is final.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Now, provide iterative self-feedback, refine your answer, and only return ###FINISHED### with your final answer when ready.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```

---

### Variation 8

```python
code_question_answering_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Decide if the provided code snippet fully addresses the question.
Return ###TRUE### if it meets every requirement; otherwise, reply with ###FALSE###.
After your initial answer, iteratively incorporate self-feedback and update your response until it is final.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Now, reexamine your response, iteratively refine it with self-feedback, and only return ###FINISHED### with your final answer when complete.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```

---

### Variation 9

```python
code_question_answering_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Evaluate if the provided code snippet is a complete answer to the question.
Return ###TRUE### if it satisfies all requirements; otherwise, reply with ###FALSE###.
Then, iteratively provide self-feedback and refine your answer until it reaches finality.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Now, iteratively review and improve your answer with self-feedback.
Only return ###FINISHED### with your final answer when you are satisfied.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```

---

### Variation 10

```python
code_question_answering_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine whether the provided code snippet fully answers the question.
Return ###TRUE### if all criteria are met; otherwise, reply with ###FALSE###.
After your initial response, iteratively refine your answer through self-feedback until it is complete.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Now, provide iterative self-feedback and refine your response.
Only return ###FINISHED### with your final answer when it is fully refined.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```

---

### Variation 11

```python
code_question_answering_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Assess if the provided code snippet adequately answers the question.
Return ###TRUE### if the code meets all requirements; otherwise, reply with ###FALSE###.
Then, iteratively self-assess your response and refine your answer until you have a final, accurate conclusion.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Now, iterate on your answer with self-feedback and only return ###FINISHED### with your final answer when no further improvements are possible.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```

---

### Variation 12

```python
code_question_answering_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Decide if the provided code snippet completely answers the question.
Return ###TRUE### if it fully satisfies the requirements; otherwise, reply with ###FALSE###.
Then, engage in iterative self-review, providing feedback and refining your answer until it is final.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Now, provide iterative self-feedback, refine your answer, and only return ###FINISHED### with your final answer when you are content with it.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```

---

### Variation 13

```python
code_question_answering_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Evaluate whether the provided code snippet fully answers the question.
Return ###TRUE### if it meets every requirement; otherwise, reply with ###FALSE###.
Then, iteratively assess your answer, offer self-feedback, and refine your response until you reach a final answer.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Now, review your response iteratively with self-feedback and only return ###FINISHED### with your final answer when it is complete.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```

---

### Variation 14

```python
code_question_answering_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine if the provided code snippet completely answers the question.
Return ###TRUE### if it fully meets the requirements; otherwise, reply with ###FALSE###.
After your initial response, iteratively self-assess your answer, provide feedback, and refine it until you achieve a final, accurate response.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Now, iteratively review your answer, provide self-feedback, and only return ###FINISHED### with your final answer when you are completely satisfied.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```
