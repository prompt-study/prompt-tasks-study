```python
# Variation 0
assert_generation_template_style = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Use a succinct, instructive style:
Determine the correct assertion that should replace <AssertPlaceHolder> in the following code.
Provide only the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 1 (Modified Tone)
assert_generation_template_style_1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt a formal and authoritative tone:
Identify the appropriate assertion that should substitute <AssertPlaceHolder> within the code provided.
Return solely the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Insert the code snippet here: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 2 (Modified Tone)
assert_generation_template_style_2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Embrace an analytical and precise tone:
Find the proper assertion to replace <AssertPlaceHolder> in the code snippet below.
Only output the assertion; omit any extra text.'''
    ),
    HumanMessagePromptTemplate.from_template("Review this code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 3 (Modified Tone)
assert_generation_template_style_3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt an innovative and insightful tone:
Identify the proper assertion that fills the role of <AssertPlaceHolder> in the provided code.
Submit just the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Consider the following code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 4 (Modified Tone)
assert_generation_template_style_4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt a calm and methodical tone:
Ascertain the correct assertion to use in place of <AssertPlaceHolder> in the given code.
Respond with only the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 5 (Modified Tone)
assert_generation_template_style_5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt a lighthearted yet precise style:
Decide which assertion should replace <AssertPlaceHolder> in the code snippet.
Reply solely with the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Here is the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 6 (Modified Tone)
assert_generation_template_style_6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt an assertive and pragmatic tone:
Figure out the accurate assertion that needs to substitute <AssertPlaceHolder> in the code.
Provide only the assertion statement in your answer.'''
    ),
    HumanMessagePromptTemplate.from_template("Analyze this code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 7 (Modified Tone)
assert_generation_template_style_7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt an energetic and confident tone:
Find the appropriate assertion to substitute for <AssertPlaceHolder> in the code provided.
Return just the assertion statement without extra commentary.'''
    ),
    HumanMessagePromptTemplate.from_template("Examine the following code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 8 (Modified Tone)
assert_generation_template_style_8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt a reflective and measured tone:
Identify the assertion that should replace <AssertPlaceHolder> in the subsequent code.
Include only the assertion statement in your response.'''
    ),
    HumanMessagePromptTemplate.from_template("Review this test code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 9 (Modified Tone)
assert_generation_template_style_9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt a creative and methodical tone:
Determine the assertion that correctly fills <AssertPlaceHolder> in the given code.
Supply only the assertion statement in your reply.'''
    ),
    HumanMessagePromptTemplate.from_template("Take a look at the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 10 (Modified Tone)
assert_generation_template_style_10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt an assertive and results-driven tone:
Pinpoint the correct assertion to replace <AssertPlaceHolder> in this piece of code.
Return solely the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 11 (Modified Tone)
assert_generation_template_style_11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt a thoughtful and systematic tone:
Identify the accurate assertion to substitute for <AssertPlaceHolder> within the code below.
Include only the assertion statement in your answer.'''
    ),
    HumanMessagePromptTemplate.from_template("Present the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 12 (Modified Tone)
assert_generation_template_style_12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt a reflective and succinct tone:
Figure out the proper assertion that should replace <AssertPlaceHolder> in the code that follows.
Reply with only the single assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Inspect this code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 13 (Modified Tone)
assert_generation_template_style_13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt an engaging and thoughtful tone:
Detect the appropriate assertion capable of substituting for <AssertPlaceHolder> in the sample code provided.
Ensure your reply is limited solely to the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Observe the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 14 (Modified Tone)
assert_generation_template_style_14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt a confident and straightforward tone:
Determine which assertion correctly replaces <AssertPlaceHolder> in the given code example.
Offer only the assertion statement in your response.'''
    ),
    HumanMessagePromptTemplate.from_template("Access the following code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```
