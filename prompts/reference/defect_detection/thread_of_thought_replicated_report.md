```python

────────────────────────────────────────
Variation 0:
────────────────────────────────────────
defect_detection_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Walk me through the code in manageable parts, step by step, summarizing and analyzing as we go.
Finally, state if there's a defect (###TRUE###) or not (###FALSE###).'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python

────────────────────────────────────────
Variation 1:
────────────────────────────────────────
defect_detection_template_thot_v1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Please explain the code by breaking it into small, manageable segments, offering summaries and analysis at each step.
Conclude by indicating whether a defect is present using (###TRUE###) or absent using (###FALSE###).'''
    ),
    HumanMessagePromptTemplate.from_template("Please provide the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

```

```python
────────────────────────────────────────
Variation 2:
────────────────────────────────────────
defect_detection_template_thot_v2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Guide me through the code piece by piece with clear, sequential explanations and analysis.
At the end, clarify whether you detect a defect (###TRUE###) or no defect (###FALSE###).'''
    ),
    HumanMessagePromptTemplate.from_template("Submit your code here: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
────────────────────────────────────────
Variation 3:
────────────────────────────────────────
defect_detection_template_thot_v3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Break down the code into digestible segments and provide stepwise explanations along with summaries.
Finally, mention if a defect is detected (###TRUE###) or not (###FALSE###).'''
    ),
    HumanMessagePromptTemplate.from_template("Include the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
────────────────────────────────────────
Variation 4:
────────────────────────────────────────
defect_detection_template_thot_v4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Analyze the provided code in ordered segments, delivering concise summaries and commentary as you progress.
End by stating if there is a defect (###TRUE###) or if the code passes without issues (###FALSE###).'''
    ),
    HumanMessagePromptTemplate.from_template("Enter your code sample: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
────────────────────────────────────────
Variation 5:
────────────────────────────────────────
defect_detection_template_thot_v5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Walk through the code in logical, incremental steps, offering recaps and evaluations for each segment.
Conclude by specifying if a defect exists (###TRUE###) or is absent (###FALSE###).'''
    ),
    HumanMessagePromptTemplate.from_template("Input the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
────────────────────────────────────────
Variation 6:
────────────────────────────────────────
defect_detection_template_thot_v6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Step through the code methodically, dissecting it into manageable chunks while providing summaries and insights at every stage.
Ultimately, indicate whether a defect is found (###TRUE###) or not (###FALSE###).'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly enter your code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
────────────────────────────────────────
Variation 7:
────────────────────────────────────────
defect_detection_template_thot_v7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Systematically review the code by splitting it into clear, sequential parts while delivering both analysis and summaries.
Finally, report if a defect is present (###TRUE###) or absent (###FALSE###).'''
    ),
    HumanMessagePromptTemplate.from_template("Supply the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
────────────────────────────────────────
Variation 8:
────────────────────────────────────────
defect_detection_template_thot_v8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Offer a detailed walkthrough of the code by inspecting it in step-by-step segments, complete with summary and commentary for each section.
End by declaring whether a defect exists (###TRUE###) or does not (###FALSE###).'''
    ),
    HumanMessagePromptTemplate.from_template("Paste your code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
────────────────────────────────────────
Variation 9:
────────────────────────────────────────
defect_detection_template_thot_v9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Provide a step-by-step breakdown of the code, ensuring that every part is explained and summarized with precise analysis.
Conclude with a declaration of whether a defect is found (###TRUE###) or not (###FALSE###).'''
    ),
    HumanMessagePromptTemplate.from_template("Present your code in the designated field: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
────────────────────────────────────────
Variation 10:
────────────────────────────────────────
defect_detection_template_thot_v10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Detail your analysis of the code by parsing it into sequential segments, adding brief summaries and evaluations throughout.
At the end, mention if there’s a defect (###TRUE###) or not (###FALSE###).'''
    ),
    HumanMessagePromptTemplate.from_template("Show the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
────────────────────────────────────────
Variation 11:
────────────────────────────────────────
defect_detection_template_thot_v11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Examine the code thoroughly in incremental segments, providing clear summaries and evaluations at each step.
Finally, indicate if you find a defect (###TRUE###) or if none is present (###FALSE###).'''
    ),
    HumanMessagePromptTemplate.from_template("Insert the code for analysis: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
────────────────────────────────────────
Variation 12:
────────────────────────────────────────
defect_detection_template_thot_v12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Navigate through the code step by step, breaking it into manageable sections and offering concise summaries and insights as you proceed.
At the conclusion, state whether a defect exists (###TRUE###) or is absent (###FALSE###).'''
    ),
    HumanMessagePromptTemplate.from_template("Compose your code snippet here: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
────────────────────────────────────────
Variation 13:
────────────────────────────────────────
defect_detection_template_thot_v13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Step through the code sequentially, elaborating on each segment with clear summaries and thoughtful analysis.
Conclude by specifying if a defect is present (###TRUE###) or not (###FALSE###).'''
    ),
    HumanMessagePromptTemplate.from_template("Deliver the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
────────────────────────────────────────
Variation 14:
────────────────────────────────────────
defect_detection_template_thot_v14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Guide through the code in clear, sequential parts, offering succinct summaries and an analytical viewpoint at every stage.
Finish by stating clearly if a defect is present (###TRUE###) or if none exist (###FALSE###).'''
    ),
    HumanMessagePromptTemplate.from_template("Submit the source code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```


Each of these variants maintains the intended task structure while only modifying the language in the system and human messages.
