```python
# Variation 0
code_translation_template_emotion_v1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Translate the following code from {source_language} to {target_language}. Provide the translated code only.
Are you sure that's your final answer? Consider double-checking.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 1
code_translation_template_emotion_v2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Please translate the code written in {source_language} into {target_language}. Return solely the translated code.
This is very important to my career.'''
    ),
    HumanMessagePromptTemplate.from_template("Insert code here: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 2
code_translation_template_emotion_v3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Your task is to convert the provided code from {source_language} into {target_language}. Only supply the resulting translated code.
Approach this task with unwavering determination; your precision will make a difference.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly input the code that requires translation: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 3
code_translation_template_emotion_v4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Translate the given code snippet from {source_language} into {target_language}. Return only the translated version of the code.
Trust in your expertise and let your skills shine—this is key to advancing my career.'''
    ),
    HumanMessagePromptTemplate.from_template("Share the code for translation: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 4
code_translation_template_emotion_v5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Please convert the following code from {source_language} to {target_language}, returning only the resulting code.
Channel your commitment to excellence in every line you translate.'''
    ),
    HumanMessagePromptTemplate.from_template("Provide the code that needs to be translated: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 5
code_translation_template_emotion_v6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Convert the following snippet from {source_language} to {target_language} and return only the translated code.
This is very important to my career, so you'd better be sure.'''
    ),
    HumanMessagePromptTemplate.from_template("Enter the code to be translated: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 6
code_translation_template_emotion_v7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Translate the code snippet below from {source_language} into {target_language} and output only the converted code.
You'd better be sure.'''
    ),
    HumanMessagePromptTemplate.from_template("Submit your code for conversion here: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 7
code_translation_template_emotion_v8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Your task is to convert this code from {source_language} into {target_language}. Provide exclusively the translated code.
Believe in your abilities and transform this challenge into an opportunity for success.'''
    ),
    HumanMessagePromptTemplate.from_template("Input the code snippet that needs translation: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 8
code_translation_template_emotion_v9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Please transform the following code from {source_language} to {target_language} and output only the translated version.
Let your commitment to quality lead you—every effort counts toward excellence.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly provide the code to be converted: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 9
code_translation_template_emotion_v10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Convert this code from {source_language} into {target_language} and output solely the translated code.
Approach this task with confidence, knowing that your expertise is invaluable.'''
    ),
    HumanMessagePromptTemplate.from_template("Please enter the code here for translation: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 10
code_translation_template_emotion_v11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Translate the code below from {source_language} into {target_language} and provide only the translated output.
Your dedication and precision in this task will make a significant impact.'''
    ),
    HumanMessagePromptTemplate.from_template("Share the code intended for translation: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 11
code_translation_template_emotion_v12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Convert the following code from {source_language} to {target_language} and return only the translated version.
Let your skill and care shine through—each line you translate builds a bridge to success.'''
    ),
    HumanMessagePromptTemplate.from_template("Type in the code you wish to translate: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 12
code_translation_template_emotion_v13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Rework the provided code from {source_language} to {target_language}, outputting solely the translated code.
Draw on your insight and determination to deliver an impeccable translation.'''
    ),
    HumanMessagePromptTemplate.from_template("Enter the code here for translation: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 13
code_translation_template_emotion_v14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Please convert the code from {source_language} into {target_language} by providing only the resulting translated code.
Draw on your strengths and let your passion for excellence be evident in every word.'''
    ),
    HumanMessagePromptTemplate.from_template("Input the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 14
code_translation_template_emotion_v15 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Translate the given code piece from {source_language} to {target_language}. Display only the translated code and nothing else.
Approach this translation with relentless determination, as it is crucial for my career advancement.'''
    ),
    HumanMessagePromptTemplate.from_template("Submit the code to be translated: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```
