````python
# Variation 0: Senior Software Engineer
clone_detection_template_control_0 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Are the two code snippets clones of each other? Answer ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```
