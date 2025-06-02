```python
code_question_answering_template_universal_self_consistency = ChatPromptTemplate.from_messages([
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
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template(
        '''I have generated the following responses to the question above: {output_text}
Select the most consistent response based on majority consensus.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_universal_self_consistency = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Evaluate whether the provided code snippet fully answers the question.
Return ###TRUE### if all requirements are met; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Below are several generated responses: {output_text}
Please select the response that most consistently satisfies the evaluation criteria.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_universal_self_consistency = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Assess if the provided code snippet completely answers the question.
Return ###TRUE### if the code fulfills every requirement; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template(
        '''I have produced multiple responses for the input above: {output_text}
Choose the response that is most consistent with the majority consensus.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_universal_self_consistency = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine whether the given code snippet fully answers the question.
Return ###TRUE### if it completely meets the requirements; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template(
        '''The following responses have been generated: {output_text}
Select the one that most consistently reflects the correct evaluation.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_universal_self_consistency = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Review the provided code and decide if it fully answers the question.
Return ###TRUE### if the code satisfies all the requirements; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template(
        '''I have collected multiple responses for the question above: {output_text}
Please pick the response that most consistently meets the evaluation criteria.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_universal_self_consistency = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Decide if the provided code snippet fully meets the question's requirements.
Return ###TRUE### if it does; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Multiple responses have been generated: {output_text}
Select the response that best aligns with the majority consensus.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_universal_self_consistency = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine if the given code snippet is a complete answer to the question.
Return ###TRUE### if the code fully satisfies the requirements; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template(
        '''I have the following responses for the above question: {output_text}
Select the most consistent response based on majority consensus.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```


```python
code_question_answering_template_universal_self_consistency = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Review whether the provided code snippet fully resolves the question.
Return ###TRUE### if it completely meets the requirements; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template(
        '''The following responses were generated: {output_text}
Choose the response that best represents the majority view.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_universal_self_consistency = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Assess if the provided code snippet is a complete answer to the question.
Return ###TRUE### if it satisfies all specified criteria; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template(
        '''I have generated several responses: {output_text}
Please select the response that is most consistent with the consensus.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_universal_self_consistency = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine if the given code snippet completely answers the question.
Return ###TRUE### if every requirement is fulfilled; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Generated responses:
{output_text}
Select the response that most accurately reflects a complete answer.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_universal_self_consistency = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Examine the provided code snippet and determine if it fully addresses the question.
Return ###TRUE### if it meets all the criteria; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Below are the responses generated: {output_text}
Choose the one that best aligns with the majority consensus.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_universal_self_consistency = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Verify if the provided code snippet completely answers the question.
Return ###TRUE### if the answer is complete; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template(
        '''I have collected the following responses: {output_text}
Select the most consistent response based on the majority view.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_universal_self_consistency = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Decide if the provided code snippet fully meets the question's requirements.
Return ###TRUE### if it does; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Multiple responses have been generated: {output_text}
Select the response that most consistently reflects a complete answer.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_universal_self_consistency = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Evaluate whether the provided code snippet fully answers the question.
Return ###TRUE### if it completely meets the requirements; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template(
        '''The following responses were produced: {output_text}
Pick the response that best aligns with the majority consensus.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_universal_self_consistency = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Assess whether the provided code snippet fully satisfies the question's requirements.
Return ###TRUE### if it meets all the criteria; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template(
        '''The following responses were generated: {output_text}
Please select the response that best represents the majority consensus.'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```
