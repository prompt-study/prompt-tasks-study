```python
# Variation 0 (Original)
code_question_answering_template_emotion_v1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Assess whether the following code correctly answers the question.
Provide only ###TRUE### if the code fully satisfies the query or ###FALSE### if it does not.
Are you sure that's your final answer? Consider double-checking.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 1 (Revised Emotional Tone)
code_question_answering_template_emotion_v1_var1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Examine whether the code provided accurately addresses the question.
Respond exclusively with ###TRUE### if it completely meets the query, or with ###FALSE### if it does not.
Let your precision shine as you observe every nuance with unwavering clarity.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Here is the question:
{question}

And the code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 2 (Revised Emotional Tone)
code_question_answering_template_emotion_v1_var2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Evaluate if the following code satisfactorily answers the question.
Return only ###TRUE### when the code fully resolves the inquiry, or ###FALSE### if it falls short.
Channel your analytical spirit and scrutinize each nuance with careful consideration.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question details:
{question}

Accompanying code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 3 (Revised Emotional Tone)
code_question_answering_template_emotion_v1_var3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine if the code below successfully answers the question.
Output only ###TRUE### if the answer is complete; otherwise, output ###FALSE###.
This is very important to my career.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Provided code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 4 (Revised Emotional Tone)
code_question_answering_template_emotion_v1_var4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Verify whether the code shown correctly responds to the question.
Reply with only ###TRUE### if it fully matches the query, or only ###FALSE### if it does not.
This is very important to my career, so you'd better be sure.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 5 (Revised Emotional Tone)
code_question_answering_template_emotion_v1_var5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Check if the attached code effectively answers the question.
Provide solely ###TRUE### when the code completely addresses the query; otherwise, provide ###FALSE###.
You'd better be sure.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Query:
{question}

Code block:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 6 (Revised Emotional Tone)
code_question_answering_template_emotion_v1_var6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Scrutinize whether the following code answers the question in its entirety.
Answer exclusively with ###TRUE### if it fully satisfies the inquiry, or with ###FALSE### if it does not.
Trust your meticulous review to capture every essential detail.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 7 (Revised Emotional Tone)
code_question_answering_template_emotion_v1_var7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Review the code below to decide if it correctly answers the question.
If the code completely fulfills the requirements, reply with ###TRUE###; otherwise, reply with ###FALSE###.
Let your keen eye for detail and accuracy guide your evaluation.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question specifics:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 8 (Revised Emotional Tone)
code_question_answering_template_emotion_v1_var8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Judge whether the code given serves as the correct answer to the question.
Return only ###TRUE### if the response is complete, or ###FALSE### if it is not.
Allow your attention to every nuance to ensure no detail is overlooked.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code extract:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 9 (Revised Emotional Tone)
code_question_answering_template_emotion_v1_var9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Decide if the provided code properly resolves the question.
Reply with ###TRUE### when the code is entirely accurate, or with ###FALSE### if it misses the mark.
Let your evaluation be both thorough and discerning.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 10 (Revised Emotional Tone)
code_question_answering_template_emotion_v1_var10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine whether the code below sufficiently addresses the question.
Output only ###TRUE### if it meets all aspects of the query, or only ###FALSE### if it does not.
Let your response reflect an unwavering commitment to accuracy.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question prompt:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 11 (Revised Emotional Tone)
code_question_answering_template_emotion_v1_var11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Assess if the provided code completely addresses the inquiry.
Respond with only ###TRUE### if every aspect of the query is satisfied, or with ###FALSE### if it is not.
Allow your precision to be unmistakable in every detail of your evaluation.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 12 (Revised Emotional Tone)
code_question_answering_template_emotion_v1_var12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Examine the following code and determine if it correctly answers the question.
Return strictly ###TRUE### if it adequately fulfills the inquiry, or ###FALSE### if it does not.
Let your careful attention to every detail lead to a conclusive answer.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question text:
{question}

Code details:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 13 (Revised Emotional Tone)
code_question_answering_template_emotion_v1_var13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Review the given code to ascertain whether it fully responds to the question.
If the code completely satisfies the query, reply with ###TRUE###; otherwise, reply with ###FALSE###.
Ensure that every nuance is examined with unwavering diligence.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code excerpt:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 14 (Revised Emotional Tone)
code_question_answering_template_emotion_v1_var14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Evaluate the subsequent code to determine if it correctly answers the question.
Reply strictly with ###TRUE### if the response is complete, or with ###FALSE### if it is incomplete.
Let your assessment reflect the significance of every nuance.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question specifics:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```
