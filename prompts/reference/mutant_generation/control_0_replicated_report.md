

**Variation 0: Senior Software Engineer**
```python
mutant_generation_template_control_0 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Generate a mutant of the code by making small changes. Provide the mutated code only.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```


