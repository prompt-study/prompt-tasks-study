```python
# Variation 0
clone_detection_template_emotion_v2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Are the two code snippets clones of each other? Answer with TRUE or FALSE only, using the format: ###TRUE### or ###FALSE###.
Are you sure that's your final answer? Consider double-checking.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 1
clone_detection_template_emotion_v2_variation1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine if these two code fragments are exact copies. Provide your answer solely as TRUE or FALSE using the format: ###TRUE### or ###FALSE###.
Embrace the challenge and let your expertise guide you to a precise answer.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''For analysis, please review the following code fragments:
{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 2
clone_detection_template_emotion_v2_variation2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Assess whether these two code segments are duplicates. Respond only with TRUE or FALSE in the format: ###TRUE### or ###FALSE###.
Trust in your critical eye and respond with clarity—your decision matters.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Consider the two code blocks provided below:
{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 3
clone_detection_template_emotion_v2_variation3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Evaluate if the provided code blocks are clones of one another. Your answer must be exclusively TRUE or FALSE, formatted as: ###TRUE### or ###FALSE###.
Rely on your sharp judgment and deliver your answer with conviction.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Review the following two code sections:
{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 4
clone_detection_template_emotion_v2_variation4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Examine whether these two portions of code are essentially clones. Answer only with TRUE or FALSE using the format: ###TRUE### or ###FALSE###.
Let your attention to detail shine through; your analysis will pave the way to success.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Please inspect the two code pieces below:
{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 5
clone_detection_template_emotion_v2_variation5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Look over the two code snippets and decide if they are clones of each other. Respond strictly with TRUE or FALSE using the exact format: ###TRUE### or ###FALSE###.
This is very important to my career.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Analyze the following code examples:
{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 6
clone_detection_template_emotion_v2_variation6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Decide whether these two sections of code are duplicates. Your response should be either TRUE or FALSE, formatted exactly as: ###TRUE### or ###FALSE###.
This is very important to my career, so you'd better be sure.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Inspect the two code samples provided:
{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 7
clone_detection_template_emotion_v2_variation7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine if the code excerpts provided are exact clones. Answer exclusively with TRUE or FALSE using this format: ###TRUE### or ###FALSE###.
You'd better be sure.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Examine the following code excerpts:
{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 8
clone_detection_template_emotion_v2_variation8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Verify whether the two code excerpts are duplicates. Your answer must be solely TRUE or FALSE in the format: ###TRUE### or ###FALSE###.
Bring your full analytical strength to this task; your answer is a stepping stone to excellence.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Below are two code segments for your review:
{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 9
clone_detection_template_emotion_v2_variation9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Ascertain if these two provided code excerpts are identical clones. Answer solely with TRUE or FALSE using the format: ###TRUE### or ###FALSE###.
Use your discernment to deliver a clear answer—your expertise is your strength.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Please review the following code examples:
{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 10
clone_detection_template_emotion_v2_variation10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Check if the two code samples are clones. Your response should be strictly TRUE or FALSE, formatted as: ###TRUE### or ###FALSE###.
Engage your meticulous mind and respond confidently—your evaluation is invaluable.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Consider the code pieces provided below:
{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 11
clone_detection_template_emotion_v2_variation11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Confirm whether these code snippets are clones of each other. Answer solely with TRUE or FALSE using the format: ###TRUE### or ###FALSE###.
Rely on your insight and commit to a precise answer—this review is a testament to your skill.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Review the following two snippets of code:
{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 12
clone_detection_template_emotion_v2_variation12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Review whether the two code segments are exact clones. Respond only with TRUE or FALSE in the format: ###TRUE### or ###FALSE###.
Draw on your focused determination and deliver your response with unwavering accuracy.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Here are the code segments for your comparison:
{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 13
clone_detection_template_emotion_v2_variation13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Judge if the following code snippets are mere clones of one another. Your reply must be exclusively TRUE or FALSE, using the format: ###TRUE### or ###FALSE###.
Let your analytical skills shine—provide your answer with both clarity and conviction.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Provided below are two code portions:
{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 14
clone_detection_template_emotion_v2_variation14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine if the two provided code segments are exact copies. Your answer should be only TRUE or FALSE using the specified format: ###TRUE### or ###FALSE###.
Trust your expertise and answer decisively; your judgment is crucial for this evaluation.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''See the two code examples below:
{code_snippet1}

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```
