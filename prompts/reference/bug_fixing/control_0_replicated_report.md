```python
# Variation 0: Senior Software Engineer
bug_fixing_template_control_0 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Fix the bug in the code. Provide only the corrected code.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```
