
────────────────────────────────────────────
**Variation 0**
```python
exception_type_template_analogical = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We’ll determine the correct exception type for a missing placeholder.
First, create a small code example where an exception might occur.
Explain how you'd identify the correct exception type for it.
Then, I'll give you the actual code snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Please provide your self-generated code and your reasoning steps."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Now, here's the real code:
{code}

Which exception type should replace __HOLE__?
Answer in the format ###ExceptionType###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────────────────────
**Variation 1**
```python
exception_type_template_analogical_variant1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We are going to decide the proper exception type for a missing part.
Begin by writing a brief code snippet where an error might be triggered.
Describe the method you would use to determine the correct exception type.
Afterwards, I will provide the actual code segment.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly share the code you generated along with the explanation of your thought process."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Here is the genuine code:
{code}

What exception type should take the place of __HOLE__?
Reply using the format ###ExceptionType###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────────────────────
**Variation 2**
```python
exception_type_template_analogical_variant2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We will select the appropriate exception type for a placeholder that is missing.
Start by crafting a concise code sample in which an exception may arise.
Outline your strategy for pinpointing the right exception type.
Then, I will supply you with the actual code snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Please submit your created code along with a detailed explanation of your reasoning."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Below is the actual code:
{code}

Which exception type should substitute __HOLE__?
Answer using the format ###ExceptionType###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────────────────────
**Variation 3**
```python
exception_type_template_analogical_variant3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We are going to determine the fitting exception type for a missing element.
First, draft a short piece of code that might raise an exception.
Detail how you would determine the correct exception type.
Subsequently, I will provide the actual code snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Please present your self-written code along with the steps of your reasoning."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Here is the true code:
{code}

Which exception type should replace __HOLE__?
Respond in the format ###ExceptionType###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────────────────────
**Variation 4**
```python
exception_type_template_analogical_variant4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We will now choose the appropriate exception type for a missing placeholder.
Begin by providing a brief code example where an error could occur.
Explain how you would go about identifying the correct exception type.
After that, I will share the actual code snippet with you.'''
    ),
    HumanMessagePromptTemplate.from_template("Share your generated code along with an explanation of the reasoning behind your choice."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''The actual code is below:
{code}

Which exception type is the suitable replacement for __HOLE__?
Provide your answer using the format ###ExceptionType###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────────────────────
**Variation 5**
```python
exception_type_template_analogical_variant5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We'll determine the proper exception type for a placeholder that's missing.
Start with a simple code sample where an exception might be thrown.
Describe how you would identify the appropriate exception type.
Then, I will present you with the actual code snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Please provide the code you created along with the reasoning you followed."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Below is the real code:
{code}

Which exception type should be used instead of __HOLE__?
Answer in the following format: ###ExceptionType###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────────────────────
**Variation 6**
```python
exception_type_template_analogical_variant6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Our task is to choose the correct exception type for a missing placeholder.
Please begin by writing a brief code snippet where an exception could potentially occur.
Include in your explanation how you would determine the exact exception type.
Afterwards, I will offer the actual code snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Provide your self-created code and elaborate on the reasoning behind it."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Here is the verified code:
{code}

Which exception type should take the place of __HOLE__?
Your answer should follow the format ###ExceptionType###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────────────────────
**Variation 7**
```python
exception_type_template_analogical_variant7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We are going to determine which exception type fits a missing placeholder.
Start by producing a short example of code that might trigger an exception.
Clarify the process you would use to detect the proper exception type.
Later, I will provide you with the genuine code snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly present your generated code and articulate your reasoning steps."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Below is the authentic code:
{code}

Which exception type should be inserted in place of __HOLE__?
Respond following the format ###ExceptionType###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────────────────────
**Variation 8**
```python
exception_type_template_analogical_variant8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We will decide the proper exception type for a missing placeholder.
First, write a short code sample that could result in an exception.
Detail the approach you would take to determine the correct exception type.
Afterwards, I will give you the actual code snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Please share the code you drafted along with your step-by-step reasoning."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''This is the actual code:
{code}

Which exception type correctly replaces __HOLE__?
Answer using this format: ###ExceptionType###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────────────────────
**Variation 9**
```python
exception_type_template_analogical_variant9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We are set to identify the suitable exception type for a missing placeholder.
Start by composing a brief code example in which an exception might occur.
Explain the method you would utilize to determine the proper exception type.
Afterwards, I will share the actual code snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Submit your self-generated code along with an explanation of your reasoning process."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Here is the actual code:
{code}

Which exception type should replace __HOLE__?
Provide your answer in the format ###ExceptionType###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────────────────────
**Variation 10**
```python
exception_type_template_analogical_variant10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Let's determine the appropriate exception type for a missing placeholder.
Begin by drafting a short snippet of code where an exception may occur.
Describe how you would decide on the correct exception type.
Following that, I will provide you with the actual code snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Please present your crafted code along with a detailed explanation of your thought process."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Below is the actual code:
{code}

What exception type should replace __HOLE__?
Respond using the format ###ExceptionType###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────────────────────
**Variation 11**
```python
exception_type_template_analogical_variant11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We will select the proper exception type for a placeholder that is missing.
First, construct a brief code snippet that might raise an exception.
Discuss your approach for determining the correct exception type.
Then, I will provide the genuine code snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly provide the code you developed along with your reasoning steps."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Here is the actual code:
{code}

Which exception type is the right substitution for __HOLE__?
Answer in the format ###ExceptionType###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────────────────────
**Variation 12**
```python
exception_type_template_analogical_variant12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Our objective is to find the correct exception type for a missing placeholder.
Start by writing a succinct code example that might lead to an exception.
Explain the process you would follow to identify the appropriate exception type.
After that, I will show you the actual code snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Provide your generated code accompanied by an explanation of your logic."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Presenting the real code below:
{code}

Which exception type should be used to substitute __HOLE__?
Answer with the format ###ExceptionType###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────────────────────
**Variation 13**
```python
exception_type_template_analogical_variant13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We will identify which exception type correctly fills a missing placeholder.
First, generate a brief code sample that could trigger an exception.
Describe how you would determine the suitable exception type.
Then, I will provide you with the actual code snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Share your self-created code and detail the reasoning steps you used."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Below is the actual code:
{code}

Which exception type should be inserted in place of __HOLE__?
Please answer in the format ###ExceptionType###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────────────────────
**Variation 14**
```python
exception_type_template_analogical_variant14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We're going to determine the correct exception type for a missing placeholder.
Begin by writing a short example of code where an exception may happen.
Explain your method for finding the correct exception type.
Once done, I will provide the actual code snippet for further review.'''
    ),
    HumanMessagePromptTemplate.from_template("Please supply your written code along with a clear explanation of your reasoning process."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Here is the actual code:
{code}

Which exception type should replace __HOLE__?
Answer using the following format: ###ExceptionType###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```
