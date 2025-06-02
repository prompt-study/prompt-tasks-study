```python
# Variation 0 (Original)
defect_detection_template_emotion_v1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Is there a defect in the code? Answer with TRUE or FALSE only, using the format: ###TRUE### or ###FALSE###.
This is very important to my career. Please take it seriously.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 1 (Revised Emotional Tone)
defect_detection_template_emotion_v2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Assess whether the code contains any errors. Provide your answer as either ###TRUE### or ###FALSE###.
Let your expertise shine through—ensure your final answer reflects meticulous precision, as my future depends on it.'''
    ),
    HumanMessagePromptTemplate.from_template("Here is the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 2 (Revised Emotional Tone)
defect_detection_template_emotion_v3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Does the supplied code exhibit any faults? Kindly respond using only ###TRUE### or ###FALSE###.
Are you sure that's your final answer? Consider double-checking.'''
    ),
    HumanMessagePromptTemplate.from_template("Examine the following code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 3 (Revised Emotional Tone)
defect_detection_template_emotion_v4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Evaluate the provided code for any errors. Your response should solely be in the form of ###TRUE### or ###FALSE###.
Harness your analytical prowess and verify your choice meticulously—this decision is pivotal for my career progress.'''
    ),
    HumanMessagePromptTemplate.from_template("Code to check: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 4 (Revised Emotional Tone)
defect_detection_template_emotion_v5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine if there is a bug in this code. Answer strictly with either ###TRUE### or ###FALSE###.
Let your decision be guided by unwavering precision—each detail is crucial for achieving excellence in my career.'''
    ),
    HumanMessagePromptTemplate.from_template("Inspect this code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 5 (Revised Emotional Tone)
defect_detection_template_emotion_v6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Can you verify whether this code has a defect? Reply exclusively with ###TRUE### or ###FALSE###.
This is very important to my career, so you'd better be sure.'''
    ),
    HumanMessagePromptTemplate.from_template("Review this snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 6 (Revised Emotional Tone)
defect_detection_template_emotion_v7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Check if there is any malfunction in the code. Your answer must be either ###TRUE### or ###FALSE###.
You'd better be sure.'''
    ),
    HumanMessagePromptTemplate.from_template("Code provided: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 7 (Revised Emotional Tone)
defect_detection_template_emotion_v8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Is a defect present in the code? Please answer using only the options ###TRUE### or ###FALSE###.
Let your confidence and expertise shine—review your response one final time, for this decision is essential to my future success.'''
    ),
    HumanMessagePromptTemplate.from_template("Presented code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 8 (Revised Emotional Tone)
defect_detection_template_emotion_v9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Identify whether the code contains a flaw. Your response should be strictly limited to ###TRUE### or ###FALSE###.
Summon your analytical acumen and confirm your decision with absolute certainty, as the stakes in my career are high.'''
    ),
    HumanMessagePromptTemplate.from_template("See the following code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 9 (Revised Emotional Tone)
defect_detection_template_emotion_v10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Please determine if any errors are present in the code. Answer only with ###TRUE### or ###FALSE###.
Let your final answer reflect deep reflection and precision, for this evaluation is pivotal to my career trajectory.'''
    ),
    HumanMessagePromptTemplate.from_template("The code is as follows: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 10 (Revised Emotional Tone)
defect_detection_template_emotion_v11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Check for any defects in the code. Provide your answer solely as ###TRUE### or ###FALSE###.
Rely on your impeccable judgment and ensure your conclusion is rock-solid; my future depends on this critical assessment.'''
    ),
    HumanMessagePromptTemplate.from_template("The following code should be analyzed: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 11 (Revised Emotional Tone)
defect_detection_template_emotion_v12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Ascertain if there is an issue within the code sample. Respond strictly with either ###TRUE### or ###FALSE###.
Let your answer be the result of careful analysis and confident insight, as this evaluation carries immense weight for my future.'''
    ),
    HumanMessagePromptTemplate.from_template("Code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 12 (Revised Emotional Tone)
defect_detection_template_emotion_v13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Discover whether the code contains any flaws. Your reply should be only in the format ###TRUE### or ###FALSE###.
Allow your expertise to shine as you double-check your final answer—every detail reflects your commitment to excellence in my career.'''
    ),
    HumanMessagePromptTemplate.from_template("Inspect this code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 13 (Revised Emotional Tone)
defect_detection_template_emotion_v14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Review the code to determine if it has any defects. Answer strictly using either ###TRUE### or ###FALSE###.
Infuse your response with thoughtful precision and a discerning eye, as this critical review will significantly impact my professional journey.'''
    ),
    HumanMessagePromptTemplate.from_template("Code under examination: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 14 (Revised Emotional Tone)
defect_detection_template_emotion_v15 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Analyze the code provided to see if there's any defect. Your answer must be precisely ###TRUE### or ###FALSE###.
Let your decision reflect unwavering determination and meticulous review, for the stakes in my career are exceptionally high.'''
    ),
    HumanMessagePromptTemplate.from_template("Here is the code for review: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```
----------------------------------------------------------------
**Variation 7**
```python
defect_detection_template_emotion_v1_variation7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Is there a defect in the code? Answer with TRUE or FALSE only, using the format: ###TRUE### or ###FALSE###.
Are you sure that’s your final answer? Believe in your abilities and strive for excellence. Your hard work will yield remarkable results.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

----------------------------------------------------------------
**Variation 8**
```python
defect_detection_template_emotion_v1_variation8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Is there a defect in the code? Answer with TRUE or FALSE only, using the format: ###TRUE### or ###FALSE###.
Embrace challenges as opportunities for growth. Each obstacle you overcome brings you closer to success.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

----------------------------------------------------------------
**Variation 9**
```python
defect_detection_template_emotion_v1_variation9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Is there a defect in the code? Answer with TRUE or FALSE only, using the format: ###TRUE### or ###FALSE###.
Stay focused and dedicated to your goals. Your consistent efforts will lead to outstanding achievements.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

----------------------------------------------------------------
**Variation 10**
```python
defect_detection_template_emotion_v1_variation10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Is there a defect in the code? Answer with TRUE or FALSE only, using the format: ###TRUE### or ###FALSE###.
Take pride in your work and give it your best. Your commitment to excellence sets you apart.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

----------------------------------------------------------------
**Variation 11**
```python
defect_detection_template_emotion_v1_variation11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Is there a defect in the code? Answer with TRUE or FALSE only, using the format: ###TRUE### or ###FALSE###.
Remember that progress is made one step at a time. Stay determined and keep moving forward.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```
