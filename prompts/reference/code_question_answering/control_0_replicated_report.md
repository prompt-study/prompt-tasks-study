```python
code_question_answering_template_control_0 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Evaluate whether the provided code is an accurate and complete response to the question.
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

