```python
# Variation 0:
code_translation_template_analogical = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''For code translation, first invent a small example of translating code (e.g., from Python to Java).
Show your reasoning for how you convert the syntax.
Then, I'll give you the real code to translate.'''
    ),
    HumanMessagePromptTemplate.from_template("Give me your self-generated translation example and the solution."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Now translate the real code from {source_language} to {target_language}.
Code:
{code}

Provide only the translated code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 1:
code_translation_template_analogical_v1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''For converting code from one language to another, begin by creating a brief illustration of code translation (for instance, converting Python to Java).
Explain your thought process for adjusting the syntax.
After that, I will supply the actual code to be translated.'''
    ),
    HumanMessagePromptTemplate.from_template("Present your generated translation example along with its answer."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Proceed to convert the actual code from {source_language} into {target_language}.
Code:
{code}

Return only the translated code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 2:
code_translation_template_analogical_v2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Perform code conversion by first crafting a concise example of code translation (e.g., converting Python to Java).
Detail your reasoning behind adapting the syntax.
Then, I will present you with the real code to translate.'''
    ),
    HumanMessagePromptTemplate.from_template("Please share your drafted translation example along with its corresponding solution."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Translate the actual code provided from {source_language} to {target_language}.
Code:
{code}

Offer only the final translated code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 3:
code_translation_template_analogical_v3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''For translating code, begin by designing a simple demonstration of code translation (for instance, converting Python to Java).
Clarify your method for modifying the syntax.
Then, I will deliver the actual code that needs to be transformed.'''
    ),
    HumanMessagePromptTemplate.from_template("Could you present your self-devised translation illustration along with the solution?"),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Now convert the actual code snippet from {source_language} to {target_language}.
Code:
{code}

Submit just the translated code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 4:
code_translation_template_analogical_v4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''For guiding your code conversion, begin by forming a brief example of how you translate code (e.g., converting Python into Java).
Elaborate on your reasoning behind changing the syntax.
Afterward, I will share the actual code for translation.'''
    ),
    HumanMessagePromptTemplate.from_template("Offer your self-generated translation example and its complete solution."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Convert the following code from {source_language} to {target_language}.
Code:
{code}

Provide only the translated version of the code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 5:
code_translation_template_analogical_v5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''For code conversion tasks, start by inventing a minimal example of a code translation (for example, from Python to Java).
Describe the logic behind the syntax modification.
Later, I will provide you with the actual code that you need to translate.'''
    ),
    HumanMessagePromptTemplate.from_template("Share your crafted translation example along with the explained solution."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Now transform the supplied code from {source_language} to {target_language}.
Code:
{code}

Respond with only the translated code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 6:
code_translation_template_analogical_v6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''To assist with code translation, initially generate a short example of code translation (such as converting Python into Java).
Discuss, step by step, how you adjust the syntax.
Subsequently, I will present the actual code that must be translated.'''
    ),
    HumanMessagePromptTemplate.from_template("Show me your invented translation example and the solution process."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Convert the provided code from {source_language} to {target_language}.
Code:
{code}

Return solely the translated code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 7:
code_translation_template_analogical_v7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''For converting code between languages, first come up with a concise demonstration of code translation (for example, Python to Java).
Explain your step-by-step modifications of the syntax.
Afterwards, I will give you the real code to convert.'''
    ),
    HumanMessagePromptTemplate.from_template("Please provide your self-created translation illustration along with the resulting solution."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Translate the given code from {source_language} to {target_language}.
Code:
{code}

Include only the translated code in your output.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 8:
code_translation_template_analogical_v8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Apply a practical approach to code conversion.
To start, create a brief demonstration of a code translation scenario (like converting Python syntax to Java).
Outline your thought process regarding the syntax changes.
Then, I will share the actual code that needs translation.'''
    ),
    HumanMessagePromptTemplate.from_template("Submit your example translation along with its complete solution."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Now convert the actual code from {source_language} to {target_language}.
Code:
{code}

Show only the translated output.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 9:
code_translation_template_analogical_v9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Employ a strategy for code translation.
Initially, create a small sample of code translation (for example, translating from Python to Java).
Illustrate your reasoning for modifying the syntax.
Then, I will supply the actual code to be converted.'''
    ),
    HumanMessagePromptTemplate.from_template("Deliver your self-formulated translation example along with the solution."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Transform the provided code from {source_language} to {target_language}.
Code:
{code}

Return only the final translated code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 10:
code_translation_template_analogical_v10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''To tackle code translation challenges, start by devising a miniature illustration of code translation (e.g., converting Python to Java).
Discuss the logic behind your syntax changes.
Afterwards, I'll provide you with the actual code to translate.'''
    ),
    HumanMessagePromptTemplate.from_template("Offer your constructed translation example and its solution."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Translate the actual code from {source_language} to {target_language}.
Code:
{code}

Only include the translated code in your answer.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 11:
code_translation_template_analogical_v11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Leverage a method to translate code.
Begin by constructing a brief sample of code translation (for instance, converting Python into Java).
Detail your reasoning for the syntactic conversion.
Then, I will supply you with the actual code to be translated.'''
    ),
    HumanMessagePromptTemplate.from_template("Present your creative translation sample along with the outcome."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Proceed to convert the code from {source_language} to {target_language}.
Code:
{code}

Share only the final translated code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 12:
code_translation_template_analogical_v12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Utilize a method for code conversion.
Start off by crafting a brief code translation example (e.g., translating from Python to Java).
Explain your reasoning and the steps taken to modify the syntax.
Then, I'll provide you with the actual code to convert.'''
    ),
    HumanMessagePromptTemplate.from_template("Show your created translation example along with the complete solution."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Convert the following code from {source_language} to {target_language}.
Code:
{code}

Return solely the translated version.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 13:
code_translation_template_analogical_v13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt a facilitative approach to code translation.
First, invent a concise demonstration of code translation (for example, from Python to Java).
Detail your process for adapting the syntax.
Once done, I will present the actual code for conversion.'''
    ),
    HumanMessagePromptTemplate.from_template("Share your independently devised translation example with its solution."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Translate the provided code from {source_language} to {target_language}.
Code:
{code}

Ensure that you return only the translated code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 14:
code_translation_template_analogical_v14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''For code translation, begin by producing a small illustrative example of a code conversion (such as translating Python to Java).
Walk through your reasoning for modifying the syntax.
Afterward, I will provide you with the actual code to translate.'''
    ),
    HumanMessagePromptTemplate.from_template("Please submit your self-generated translation example along with the detailed solution."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Now, translate the actual code from {source_language} to {target_language}.
Code:
{code}

Output solely the translated code.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```
