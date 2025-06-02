

### Variation 0

```python
mutant_generation_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Create a mutant version of the code by making a small change.
Provide only the mutated code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Original Code:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Now, review your mutant code. Provide feedback on your initial version and return ###FINISHED### with the final mutated code.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```

---

### Variation 1

```python
mutant_generation_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Generate an altered version of the code by introducing a minor modification.
Output solely the modified code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Here is the source code:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Now, review your variant code. Provide detailed feedback on your initial generation and return ###FINISHED### with the final mutated code.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```

---

### Variation 2

```python
mutant_generation_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Produce a mutated variant of the code by applying a small tweak.
Return only the altered version.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Provided code:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Now, review your mutant code. Provide detailed feedback on your initial generation and return ###FINISHED### with the final mutated code.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```

---

### Variation 3

```python
mutant_generation_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Develop a variant of the code by implementing a slight change.
Deliver only the revised code snippet.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Original code snippet:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Now, review your variant code. Provide detailed feedback on your initial generation and return ###FINISHED### with the final mutated code.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```

---

### Variation 4

```python
mutant_generation_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Craft a slightly altered version of the code by making a minimal change.
Only return the changed portion of the code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "The original code is:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Now, review your variant code. Provide detailed feedback on your initial generation and return ###FINISHED### with the final mutated code.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```

---

### Variation 5

```python
mutant_generation_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Formulate a variant of the code by applying a minor adjustment.
Provide exclusively the altered version.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Here is the code to be mutated:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Now, review your variant code. Provide detailed feedback on your initial generation and return ###FINISHED### with the final mutated code.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```

---

### Variation 6

```python
mutant_generation_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Construct a mutated iteration of the code by introducing a subtle change.
Output just the updated code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Review this original code:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Now, review your mutated iteration. Provide detailed feedback on your initial generation and return ###FINISHED### with the final mutated code.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```

---

### Variation 7

```python
mutant_generation_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Modify the code slightly to create a mutant version.
Return only the revised code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Original code provided:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Now, review your mutant code. Provide detailed feedback on your initial generation and return ###FINISHED### with the final mutated code.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```

---

### Variation 8

```python
mutant_generation_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Alter the code by making a minimal adjustment to form a mutant version.
Provide just the modified code snippet.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Starting code:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template('''Now, review your adjusted code. Provide detailed feedback on your initial generation and return ###FINISHED### with the final mutated code.'''),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```


### Variation 9

```python
mutant_generation_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Generate a mutated version of the code by applying a slight tweak.
Submit only the altered code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Code to modify:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Now, review your mutated version. Provide detailed feedback on your initial generation and return ###FINISHED### with the final mutated code.'''),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```

---

### Variation 10

```python
mutant_generation_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Devise a mutant rendition of the code by implementing a minor adjustment.
Output solely the changed portion.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "The following is the original code:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Now, review your mutant rendition. Provide detailed feedback on your initial generation and return ###FINISHED### with the final mutated code.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```

---

### Variation 11

```python
mutant_generation_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Construct a slightly modified version of the code with a minor tweak.
Offer only the updated code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Here is the initial code:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Now, review your mutant code. Provide detailed feedback on your initial generation and return ###FINISHED### with the final mutated code.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```

---

### Variation 12

```python
mutant_generation_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Produce a variant of the code featuring a small modification.
Return nothing but the modified code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Initial code:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Now, review your variant. Provide detailed feedback on your initial generation and return ###FINISHED### with the final mutated code.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```

---

### Variation 13

```python
mutant_generation_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Create an updated mutant of the code by executing a slight change.
Display only the altered code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Source code:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Now, review your updated mutant. Provide detailed feedback on your initial generation and return ###FINISHED### with the final mutated code.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```

---

### Variation 14

```python
mutant_generation_template_self_refine = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Generate a variant version of the code by incorporating a subtle alteration.
Supply only the revised code.'''
    ),
    HumanMessagePromptTemplate.from_template(
        "Original snippet:\n{code}"
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Now, review your variant. Provide detailed feedback on your initial generation and return ###FINISHED### with the final mutated code.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_self_refine'),
])
```

