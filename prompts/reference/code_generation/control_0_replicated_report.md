```python
code_generation_template_control_0 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Generate code for the following task. Provide only the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Task Description:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

