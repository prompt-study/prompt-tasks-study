```python
# Variation 0: Senior Software Engineer
defect_detection_template_control_0 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Is there a defect in the code? Answer with ###TRUE### or ###FALSE### only.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```
