```python
# Variation 0: Senior Software Engineer
code_translation_template_control_0 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Translate this code from {source_language} to {target_language}. Provide only the translated code.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```
