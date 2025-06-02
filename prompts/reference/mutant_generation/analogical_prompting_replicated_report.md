```python
# variation 0:
mutant_generation_template_analogical = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We'll generate a mutant of some code.
First, create a small code snippet and show how you produce a mutant by making small changes.
Then, I'll give you the real code.'''
    ),
    HumanMessagePromptTemplate.from_template("Provide your snippet and the mutated version now."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Now, here's the real code:
{code}

Generate a mutant by making small changes. Provide only the mutated code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# variation 1:
mutant_generation_template_analogical_variation_1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''In this exercise, you'll craft a variant of some code.
Start by writing a brief code snippet and demonstrate how slight modifications can yield a mutant.
Afterwards, I'll provide you with the actual code.'''
    ),
    HumanMessagePromptTemplate.from_template("Share your snippet along with the modified version."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Below is the actual code:
{code}

Apply minor modifications to create a mutant. Respond with only the altered code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# variation 2:
mutant_generation_template_analogical_variation_2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We are about to produce a mutant of code.
Begin by generating a short code segment and explain how subtle tweaks lead to a mutant.
Later, I'll supply the actual code.'''
    ),
    HumanMessagePromptTemplate.from_template("Please provide your code snippet and its mutated version now."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Here is the actual code:
{code}

Create a mutant by making slight adjustments. Only show the changed code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# variation 3:
mutant_generation_template_analogical_variation_3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Your task is to develop a variant of a piece of code.
Initially, draft a small snippet and illustrate how to derive a mutant by lightly tweaking it.
Once done, I will supply you with the real code.'''
    ),
    HumanMessagePromptTemplate.from_template("Submit your code example along with the modified mutant."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''The real code is as follows:
{code}

Generate a mutant version by applying minor modifications. Present only the resulting mutant.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# variation 4:
mutant_generation_template_analogical_variation_4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We will generate a code mutant.
First, produce a brief code snippet and show how minor edits yield a mutant version.
Subsequently, I will send the actual code.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly provide your code snippet together with its mutant variant."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Here is the real code:
{code}

With small adjustments, generate a mutant and return only the altered code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# variation 5:
mutant_generation_template_analogical_variation_5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''In this prompt, you are to create a mutant version of code.
Start by writing a simple snippet and clarifying how minor changes can produce a mutant.
I will then supply the real code.'''
    ),
    HumanMessagePromptTemplate.from_template("Could you share your snippet and its mutant version?"),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''The actual code appears here:
{code}

Make a mutant by introducing subtle changes and present just the mutated code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# variation 6:
mutant_generation_template_analogical_variation_6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Your objective is to construct a mutated version of code.
Begin with a short snippet and detail how you would produce a mutant by slightly altering it.
Afterwards, I'll provide the definitive code.'''
    ),
    HumanMessagePromptTemplate.from_template("Please share your code snippet along with its mutated counterpart."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Below is the definitive code:
{code}

Create a mutant using minor modifications and provide only the modified code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# variation 7:
mutant_generation_template_analogical_variation_7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We'll be generating a variant of a given code.
Initially, write a brief code snippet and illustrate how small modifications yield a mutant.
After that, I'll share the actual code.'''
    ),
    HumanMessagePromptTemplate.from_template("Submit your snippet along with the resulting mutated code."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Now, here is the actual code:
{code}

Generate a mutant version with slight tweaks and return just the mutated version.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# variation 8:
mutant_generation_template_analogical_variation_8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''For this task, produce a mutant code version.
Begin with a concise snippet and demonstrate how minor modifications create a mutant.
Then, I'll supply the original code.'''
    ),
    HumanMessagePromptTemplate.from_template("Provide your code example and its mutated version."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Here is the original code:
{code}

Apply subtle changes to create a mutant. Only output the mutated code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# variation 9:
mutant_generation_template_analogical_variation_9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''You are set to produce a mutated form of code.
Start by writing a compact code snippet and exhibiting how minimal adjustments produce a mutant.
Then, I will give you the real code.'''
    ),
    HumanMessagePromptTemplate.from_template("Please offer your snippet together with the altered version."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Below is the real code:
{code}

Make a mutant by introducing slight modifications and provide only the resultant code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# variation 10:
mutant_generation_template_analogical_variation_10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''In this challenge, you will generate a code mutant.
First, come up with a brief code snippet and show how to derive a mutant via small tweaks.
I will then supply the true code.'''
    ),
    HumanMessagePromptTemplate.from_template("Share your snippet and the corresponding mutant version."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''This is the true code:
{code}

Create a mutant by applying minor edits and return solely the mutant code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# variation 11:
mutant_generation_template_analogical_variation_11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''This exercise involves creating a mutant code.
Initially, produce a short snippet and illustrate the process of forming a mutant through slight modifications.
Then, you'll receive the actual code.'''
    ),
    HumanMessagePromptTemplate.from_template("Provide your code snippet along with its mutated form."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Here is the actual code:
{code}

Generate a mutant by making subtle changes and include only the altered code in your reply.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# variation 12:
mutant_generation_template_analogical_variation_12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We are tasked with crafting a mutant code.
Start by writing a concise snippet and explain how minor adjustments yield a mutant variant.
Once done, I will present you with the real code.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly supply your snippet and its corresponding mutant version."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Below is the real code:
{code}

Using modest changes, generate a mutant and respond with only the mutated code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# variation 13:
mutant_generation_template_analogical_variation_13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Your mission is to develop a mutant code.
First, create a small snippet and detail how slight modifications transform it into a mutant.
Afterward, I'll send you the actual code.'''
    ),
    HumanMessagePromptTemplate.from_template("Please provide your snippet along with the modified mutant."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Here is the actual code:
{code}

Make a mutant using minor adjustments and provide only the altered code snippet.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# variation 14:
mutant_generation_template_analogical_variation_14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We will create a mutant version of some code.
Start with a short code example and clarify how minor edits result in a mutant version.
Then, I'll give you the actual code to work with.'''
    ),
    HumanMessagePromptTemplate.from_template("Submit your code snippet together with the mutant you derive."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Below is the actual code:
{code}

Generate a mutant by employing slight modifications and present only the mutated code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```
