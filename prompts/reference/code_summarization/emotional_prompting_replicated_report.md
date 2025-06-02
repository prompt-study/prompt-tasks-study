Below are the revised prompt templates. Only the system‐message texts have been updated with varied, richer emotional language while leaving all other parts unchanged.

----------------------------------------------------------------
**Variation 0**
```python
code_summarization_template_emotion_v1_variation0 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Summarize the following code.
This is very important to my career.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

----------------------------------------------------------------
**Variation 1**
```python
code_summarization_template_emotion_v1_variation1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Provide a detailed summary of the code below.
This is very important to my career, so you'd better be sure.'''
    ),
    HumanMessagePromptTemplate.from_template("Presented code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

----------------------------------------------------------------
**Variation 2**
```python
code_summarization_template_emotion_v1_variation2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Please review and summarize the following code snippet.
Are you sure that's your final answer? Consider double-checking.'''
    ),
    HumanMessagePromptTemplate.from_template("The code to review is as follows: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

----------------------------------------------------------------
**Variation 3**
```python
code_summarization_template_emotion_v1_variation3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Kindly create a concise yet complete summary of the code provided below.
Your insight is pivotal to my career advancement—be both precise and expansive in your analysis.'''
    ),
    HumanMessagePromptTemplate.from_template("Review the following code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

----------------------------------------------------------------
**Variation 4**
```python
code_summarization_template_emotion_v1_variation4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Compose an in-depth summary of the enclosed code.
You'd better be sure.'''
    ),
    HumanMessagePromptTemplate.from_template("Here is the code segment: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

----------------------------------------------------------------
**Variation 5**
```python
code_summarization_template_emotion_v1_variation5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Summarize the subsequent code with precision and care.
Your feedback is a linchpin for my career—please consider every detail thoughtfully.'''
    ),
    HumanMessagePromptTemplate.from_template("The code snippet is provided: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

----------------------------------------------------------------
**Variation 6**
```python
code_summarization_template_emotion_v1_variation6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Review the provided code and craft a comprehensive summary.
Your detailed insights are instrumental to my professional success—include every important detail.'''
    ),
    HumanMessagePromptTemplate.from_template("Below is the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

----------------------------------------------------------------
**Variation 7**
```python
code_summarization_template_emotion_v1_variation7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Deliver a detailed overview of the code shown below.
Your summary is pivotal to my career growth—be meticulous and capture every nuance.'''
    ),
    HumanMessagePromptTemplate.from_template("Input code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

----------------------------------------------------------------
**Variation 8**
```python
code_summarization_template_emotion_v1_variation8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Examine the following code and produce an exhaustive summary.
Your thorough documentation is vital for my career trajectory—ensure nothing is overlooked.'''
    ),
    HumanMessagePromptTemplate.from_template("Code for review: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

----------------------------------------------------------------
**Variation 9**
```python
code_summarization_template_emotion_v1_variation9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Analyze the code below and provide a detailed summary of its functionality.
Your comprehensive evaluation is essential for my professional development—leave no stone unturned.'''
    ),
    HumanMessagePromptTemplate.from_template("Examine this code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

----------------------------------------------------------------
**Variation 10**
```python
code_summarization_template_emotion_v1_variation10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Generate a detailed summary for the code provided below.
Your insights are critical to my career journey—address every aspect with clarity and depth.'''
    ),
    HumanMessagePromptTemplate.from_template("Take a look at this code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

----------------------------------------------------------------
**Variation 11**
```python
code_summarization_template_emotion_v1_variation11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Offer a complete and detailed summary of the code snippet below.
This analysis is crucial for my career success—please cover every detail with precision.'''
    ),
    HumanMessagePromptTemplate.from_template("Review the code provided here: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

----------------------------------------------------------------
**Variation 12**
```python
code_summarization_template_emotion_v1_variation12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Provide an all-encompassing summary of the code shown below.
Your insight is vital for my career endeavors—ensure your summary is both comprehensive and insightful.'''
    ),
    HumanMessagePromptTemplate.from_template("The following code is up for review: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

----------------------------------------------------------------
**Variation 13**
```python
code_summarization_template_emotion_v1_variation13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Craft a detailed and comprehensive summary of the ensuing code snippet.
Your meticulous analysis is of utmost importance for my professional growth—be sure to cover every element.'''
    ),
    HumanMessagePromptTemplate.from_template("Consider this code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

----------------------------------------------------------------
**Variation 14**
```python
code_summarization_template_emotion_v1_variation14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Generate a thorough summary of the code presented below.
Your detailed summary is essential to my career—please ensure it captures every significant aspect.'''
    ),
    HumanMessagePromptTemplate.from_template("Here's the code for your review: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```
----------------------------------------------------------------
**Variation 7**
```python
code_summarization_template_emotion_v1_variation7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Summarize the following code.
Are you sure that’s your final answer? Believe in your abilities and strive for excellence. Your hard work will yield remarkable results.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

----------------------------------------------------------------
**Variation 8**
```python
code_summarization_template_emotion_v1_variation8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Summarize the following code.
Embrace challenges as opportunities for growth. Each obstacle you overcome brings you closer to success.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

----------------------------------------------------------------
**Variation 9**
```python
code_summarization_template_emotion_v1_variation9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Summarize the following code.
Stay focused and dedicated to your goals. Your consistent efforts will lead to outstanding achievements.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

----------------------------------------------------------------
**Variation 10**
```python
code_summarization_template_emotion_v1_variation10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Summarize the following code.
Take pride in your work and give it your best. Your commitment to excellence sets you apart.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

----------------------------------------------------------------
**Variation 11**
```python
code_summarization_template_emotion_v1_variation11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Summarize the following code.
Remember that progress is made one step at a time. Stay determined and keep moving forward.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

