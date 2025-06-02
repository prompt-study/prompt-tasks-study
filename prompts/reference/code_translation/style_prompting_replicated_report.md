```python
# Variation 0 (Original)
code_translation_template_style = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Use a concise, instructional style:
Translate the following code from {source_language} to {target_language}.
Provide only the translated code.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 1 (Friendly, Approachable)
code_translation_template_style = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt a friendly, approachable tone:
Convert the code provided from {source_language} to {target_language}.
Return solely the translated version.'''
    ),
    HumanMessagePromptTemplate.from_template("The code is: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 2 (Efficient, Directive)
code_translation_template_style = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Use an efficient, directive style:
Rewrite the following code from {source_language} to {target_language}.
Output only the translation.'''
    ),
    HumanMessagePromptTemplate.from_template("Here is the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 3 (Precise, Analytical)
code_translation_template_style = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Utilize a precise, analytical tone:
Change the following code from {source_language} to {target_language}.
Offer just the translated output.'''
    ),
    HumanMessagePromptTemplate.from_template("Input code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 4 (Formal, Methodical)
code_translation_template_style = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''With a formal, methodical tone:
Transform the given code from {source_language} to {target_language}.
Include only the resulting translated code in your response.'''
    ),
    HumanMessagePromptTemplate.from_template("Please supply the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 5 (Didactic, Enlightening)
code_translation_template_style = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt a didactic, enlightening style:
Convert the code snippet from {source_language} to {target_language} as specified.
Provide only the resulting code.'''
    ),
    HumanMessagePromptTemplate.from_template("Present the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 6 (Straightforward, Technical)
code_translation_template_style = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Employ a straightforward, technical tone:
Translate the submitted code from {source_language} to {target_language}.
Output solely the translated code.'''
    ),
    HumanMessagePromptTemplate.from_template("Submit your code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 7 (Succinct, Professional)
code_translation_template_style = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Take on a succinct, professional approach:
Convert the following piece of code from {source_language} to {target_language}.
Return only the converted code.'''
    ),
    HumanMessagePromptTemplate.from_template("Code provided: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 8 (Terse, Unembellished)
code_translation_template_style = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Use a terse, unembellished style:
Please translate the subsequent code from {source_language} to {target_language}
and deliver only the outputted translated code.'''
    ),
    HumanMessagePromptTemplate.from_template("Attached code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 9 (Succinct, Scholarly)
code_translation_template_style = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Apply a succinct, scholarly tone:
Translate the code below from {source_language} to {target_language}.
Ensure your response contains only the translated code.'''
    ),
    HumanMessagePromptTemplate.from_template("Code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 10 (Brisk, Matter-of-Fact)
code_translation_template_style = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt a brisk, matter-of-fact tone:
Convert the below code from {source_language} to {target_language}.
Return only the final translated code.'''
    ),
    HumanMessagePromptTemplate.from_template("Input the code here: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 11 (Formal, Didactic)
code_translation_template_style = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Employ a formal, didactic style:
Rework the ensuing code from {source_language} to {target_language},
including only the translation in your output.'''
    ),
    HumanMessagePromptTemplate.from_template("Please include the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 12 (Pragmatic, Result-Oriented)
code_translation_template_style = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Use a succinct, directive tone:
Switch the following code from {source_language} to {target_language}.
Return exclusively the translated version.'''
    ),
    HumanMessagePromptTemplate.from_template("Here is the code block: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 13 (Clear, Professional)
code_translation_template_style = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt a clear, professional tone:
Modify the code below from {source_language} to {target_language}.
Provide just the modified code as your output.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly furnish the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 14 (Refined, Technical)
code_translation_template_style = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Implement a refined, technical style:
Convert the following code from {source_language} to {target_language}.
Only output the converted code.'''
    ),
    HumanMessagePromptTemplate.from_template("The code to be processed: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```
