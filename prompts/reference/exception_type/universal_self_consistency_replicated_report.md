**Variant 0**
```python
exception_type_template_universal_self_consistency = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
    '''Determine which exception type should replace __HOLE__ in the given code. Respond with the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template('I have generated the following responses to the question above: {output_text}\n select the most consistent response based on majority consensus'),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

**Variant 1**
```python
exception_type_template_universal_self_consistency_variant1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
    '''Identify the appropriate exception type to insert in place of __HOLE__ in the following code snippet. Your answer should be formatted as ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I produced these responses for the query above: {output_text}\nPlease choose the answer that best reflects the majority consensus."),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

---

**Variant 2**
```python
exception_type_template_universal_self_consistency_variant2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
    '''Determine the correct exception type to substitute for __HOLE__ in the provided code. Answer using the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("Below are several generated responses: {output_text}\nSelect the one that best matches the majority view."),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

---

**Variant 3**
```python
exception_type_template_universal_self_consistency_variant3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
    '''Figure out which exception type should replace __HOLE__ in the code shown. Your response must follow the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have compiled the following responses: {output_text}\nPlease pick the answer that aligns with the majority consensus."),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

---

**Variant 4**
```python
exception_type_template_universal_self_consistency_variant4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
    '''Select the appropriate exception type to replace __HOLE__ in the given code. Provide your answer in the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("The following responses were generated: {output_text}\nIdentify the one that most closely reflects the majority."),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

---

**Variant 5**
```python
exception_type_template_universal_self_consistency_variant5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
    '''Ascertain which exception type should be used in place of __HOLE__ in the provided code. Ensure your answer is given in the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("The responses below have been generated: {output_text}\nPlease choose the response that best represents the majority view."),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

---

**Variant 6**
```python
exception_type_template_universal_self_consistency_variant6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
    '''Identify the exception type that should fill __HOLE__ in the following code. Provide your answer in the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I generated these responses: {output_text}\nSelect the one that best aligns with the majority opinion."),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

---

**Variant 7**
```python
exception_type_template_universal_self_consistency_variant7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
    '''Decide which exception type should be used to replace __HOLE__ in the code snippet below. Answer using the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("Here are the generated responses: {output_text}\nSelect the one that best reflects the majority consensus."),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

---

**Variant 8**
```python
exception_type_template_universal_self_consistency_variant8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
    '''Determine the proper exception type to insert in place of __HOLE__ within the provided code. Your answer should be formatted as ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("The following responses were produced: {output_text}\nPlease identify the one that corresponds with the majority consensus."),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

---

**Variant 9**
```python
exception_type_template_universal_self_consistency_variant9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
    '''Select the correct exception type to substitute for __HOLE__ in the code. Format your response as ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("Below are several generated answers: {output_text}\nPick the answer that best matches the majority consensus."),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

---

**Variant 10**
```python
exception_type_template_universal_self_consistency_variant10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
    '''Figure out which exception type should be used in the code instead of __HOLE__. Your answer must be presented in the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I have generated these responses: {output_text}\nChoose the one that best corresponds to the majority view."),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

---

**Variant 11**
```python
exception_type_template_universal_self_consistency_variant11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
    '''Determine the proper exception type to replace __HOLE__ in the provided code snippet. Respond using the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("The generated responses are as follows: {output_text}\nPlease select the one that best aligns with the majority consensus."),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

---

**Variant 12**
```python
exception_type_template_universal_self_consistency_variant12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
    '''Identify the exception type to substitute for __HOLE__ in the code below. Ensure your answer follows the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("Here are the responses I obtained: {output_text}\nSelect the one that reflects the majority consensus."),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

---

**Variant 13**
```python
exception_type_template_universal_self_consistency_variant13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
    '''Ascertain the appropriate exception type to fill __HOLE__ in the given code snippet. Respond in the following format: ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("The responses below were generated: {output_text}\nPlease choose the one that best represents the consensus."),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

---

**Variant 14**
```python
exception_type_template_universal_self_consistency_variant14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
    '''Decide on the exception type that should replace __HOLE__ in the code provided. Your answer should strictly follow the format ###ExceptionType###.'''
    ),
    HumanMessagePromptTemplate.from_template("Code:\n{code}"),
    AIMessagePromptTemplate.from_template('self_consistency_multi_prompt'),
    HumanMessagePromptTemplate.from_template("I generated the following answers: {output_text}\nIdentify the one that is most consistent with the majority consensus."),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

