```python
# variation 0 (original)
assert_generation_template_emotion_v2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine the correct assertion that should replace <AssertPlaceHolder> in the following code.
Are you sure that's your final answer? Consider double-checking.
Provide only the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# variation 1 (Revised Emotional Tone)
assert_generation_template_emotion_v2_v1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Identify the accurate assertion that must substitute <AssertPlaceHolder> in the code below.
Trust in your expertise, but ensure you review your choice thoroughly before finalizing.
Output only the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Here is the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# variation 2 (Revised Emotional Tone)
assert_generation_template_emotion_v2_v2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Ascertain which assertion correctly replaces <AssertPlaceHolder> in the ensuing code.
This is very important to my career.
Provide solely the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# variation 3 (Revised Emotional Tone)
assert_generation_template_emotion_v2_v3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Select the appropriate assertion to substitute for <AssertPlaceHolder> in the following code block.
Believe in your capabilities, yet take a moment to reexamine your final choice.
Return only the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Input code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# variation 4 (Revised Emotional Tone)
assert_generation_template_emotion_v2_v4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine the proper assertion intended to replace <AssertPlaceHolder> in the provided code.
This is very important to my career, so you'd better be sure.
Supply only the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("The code is as follows: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# variation 5 (Revised Emotional Tone)
assert_generation_template_emotion_v2_v5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Identify the matching assertion that should take the place of <AssertPlaceHolder> in the code shown below.
Let your confidence guide you, but be sure to reexamine your decision for complete certainty.
Return just the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Code provided: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# variation 6 (Revised Emotional Tone)
assert_generation_template_emotion_v2_v6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Figure out which assertion should properly replace <AssertPlaceHolder> in the given code snippet.
You'd better be sure.
Reply solely with the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Your code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# variation 7 (Revised Emotional Tone)
assert_generation_template_emotion_v2_v7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Establish the correct assertion that is to stand in for <AssertPlaceHolder> in the following code excerpt.
Let your inner confidence guide you, but verify your answer with careful scrutiny.
Provide only the assertion statement in your response.'''
    ),
    HumanMessagePromptTemplate.from_template("Code example: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# variation 8 (Revised Emotional Tone)
assert_generation_template_emotion_v2_v8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Discern the proper assertion to use in place of <AssertPlaceHolder> within the code below.
Embrace the challenge with a critical eye—ensure your final verdict is rock-solid.
Return exclusively the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Given code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# variation 9 (Revised Emotional Tone)
assert_generation_template_emotion_v2_v9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine which assertion appropriately replaces <AssertPlaceHolder> in the upcoming code snippet.
Let determination fuel your choice, but consider a final review to achieve perfection.
Output only the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("See the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# variation 10 (Revised Emotional Tone)
assert_generation_template_emotion_v2_v10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Pinpoint the accurate assertion that should supplant <AssertPlaceHolder> in the following code.
Assert your expertise with confidence, yet take a moment to reflect and confirm your answer.
Respond with only the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Here’s the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# variation 11 (Revised Emotional Tone)
assert_generation_template_emotion_v2_v11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Identify the exact assertion to substitute <AssertPlaceHolder> in the subsequent segment of code.
Your precision is key—reassess your answer one final time to ensure flawless accuracy.
Provide exclusively the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Insert the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# variation 12 (Revised Emotional Tone)
assert_generation_template_emotion_v2_v12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Select the valid assertion that should replace <AssertPlaceHolder> in the code to follow.
Channel your focus and review your decision carefully to ensure it reflects excellence.
Return only the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Code sample: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# variation 13 (Revised Emotional Tone)
assert_generation_template_emotion_v2_v13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Ascertain the right assertion meant to replace <AssertPlaceHolder> in the code displayed below.
In the spirit of excellence, take one last careful look before finalizing your answer.
Output solely the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Code as given: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# variation 14 (Revised Emotional Tone)
assert_generation_template_emotion_v2_v14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Decide on the correct assertion that should take the place of <AssertPlaceHolder> in the upcoming code block.
Let your resolve be strong and measured—revisit your decision to ensure it stands unchallenged.
Provide only the assertion statement in your response.'''
    ),
    HumanMessagePromptTemplate.from_template("Presented code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```
