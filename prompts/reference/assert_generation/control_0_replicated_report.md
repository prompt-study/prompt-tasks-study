**Variation 0: Senior Software Engineer**
```python
assert_generation_template_control_0 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Find the correct assertion that should replace <AssertPlaceHolder> in the following code.
            Provide only the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template("prompt"),
])
```

