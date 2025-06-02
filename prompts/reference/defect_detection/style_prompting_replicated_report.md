Below are the updated templates. Only the system‐prompt strings were changed where the tone or style was redundant. The human and AI parts remain unchanged.

────────────────────────────
**Variation 0 (Original – unchanged)**
```python
defect_detection_template_style_v0 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Use a professional, concise style to answer:
Is there a defect in the code?
Reply with ###TRUE### or ###FALSE### only.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

────────────────────────────
**Variation 1 (Modified tone)**
```python
defect_detection_template_style_v1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt a friendly and conversational tone:
Evaluate the given code for any defects.
Return only ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template("Examine this code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

────────────────────────────
**Variation 2 (Modified tone)**
```python
defect_detection_template_style_v2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''In an analytical and objective tone, determine if the provided code contains a defect.
Answer solely with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template("Analyze the following code sample: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

────────────────────────────
**Variation 3 (Modified tone)**
```python
defect_detection_template_style_v3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt an incisive and critical tone:
Does this code exhibit any flaws?
Your reply should be just ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template("Review the code below: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

────────────────────────────
**Variation 4 (Modified tone)**
```python
defect_detection_template_style_v4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Offer a meticulous and formal assessment:
Identify whether the code has a defect.
Only reply with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template("Take a look at this code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

────────────────────────────
**Variation 5 (Modified tone)**
```python
defect_detection_template_style_v5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt an authoritative and measured tone:
Check if there is a defect in the code provided.
Respond solely with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template("Here is the code to inspect: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

────────────────────────────
**Variation 6 (Modified tone)**
```python
defect_detection_template_style_v6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Respond in a direct and objective tone:
Is any fault present in the code?
Reply exclusively with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template("Inspect the following code segment: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

────────────────────────────
**Variation 7 (Modified tone)**
```python
defect_detection_template_style_v7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Answer in an unembellished and factual manner:
Does the code contain any flaws?
Answer with one of these: ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template("Consider this segment of code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

────────────────────────────
**Variation 8 (Modified tone)**
```python
defect_detection_template_style_v8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Respond in a straightforward and no-frills manner:
Assess the code for defects.
Use only ###TRUE### or ###FALSE### in the reply.'''
    ),
    HumanMessagePromptTemplate.from_template("Here is the code snippet for evaluation: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

────────────────────────────
**Variation 9 (Modified tone)**
```python
defect_detection_template_style_v9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Deliver a succinct, expert-level evaluation:
Is the code flawed?
Reply strictly with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template("Evaluate this code portion: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

────────────────────────────
**Variation 10 (Modified tone)**
```python
defect_detection_template_style_v10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Respond in a sharp and authoritative manner:
Does the given code exhibit any issues?
Your reply should be either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template("Code to be checked: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

────────────────────────────
**Variation 11 (Modified tone)**
```python
defect_detection_template_style_v11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Employ a clear and scholarly tone:
Determine if the code is defective.
Only respond with either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template("Examine this code block: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

────────────────────────────
**Variation 12 (Modified tone)**
```python
defect_detection_template_style_v12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''In an impartial and succinct style, determine if there is a flaw present in the provided code.
Answer exclusively with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template("Review the following code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

────────────────────────────
**Variation 13 (Modified tone)**
```python
defect_detection_template_style_v13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Answer in a measured and precise manner:
Does the examined code have any defects?
Your answer must be only ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template("Study this code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

────────────────────────────
**Variation 14 (Modified tone)**
```python
defect_detection_template_style_v14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Reply with a direct and critical assessment:
Is there an error in the code?
Reply only with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template("Inspect the code sample: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```
