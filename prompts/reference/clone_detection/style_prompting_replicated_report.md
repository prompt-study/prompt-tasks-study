```python
# variation 0 (Original)
clone_detection_template_style_variation_0 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Maintain a clear, methodical style.
Determine if the two code snippets are clones.
Answer with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Snippet 1:
{code_snippet1}

Code Snippet 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# variation 1 (Modified Tone)
clone_detection_template_style_variation_1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt a casual and reflective tone.
Assess whether the two code samples are identical clones.
Respond exclusively with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''First Code Snippet:
{code_snippet1}

Second Code Snippet:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# variation 2 (Modified Tone)
clone_detection_template_style_variation_2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt a rigorous and scholarly tone.
Judge if the two provided code sections are clones.
Please answer with either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Snippet A:
{code_snippet1}

Code Snippet B:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# variation 3 (Modified Tone)
clone_detection_template_style_variation_3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt an assertive and confident style.
Analyze if these two code blocks are clones.
Reply solely using ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Snippet 1:
{code_snippet1}

Snippet 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# variation 4 (Modified Tone)
clone_detection_template_style_variation_4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt a concise and factual tone.
Evaluate whether the following two code segments are clones.
Your answer should be limited to ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''First snippet:
{code_snippet1}

Second snippet:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# variation 5 (Modified Tone)
clone_detection_template_style_variation_5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt a minimalist and succinct tone.
Decide if the presented code snippets constitute clones.
Answer only with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Section 1 - Code:
{code_snippet1}

Section 2 - Code:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# variation 6 (Modified Tone)
clone_detection_template_style_variation_6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt an analytical and no-nonsense style.
Verify if the two code examples are essentially clones.
Please reply with just ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Example 1:
{code_snippet1}

Code Example 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# variation 7 (Modified Tone)
clone_detection_template_style_variation_7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt a reflective and thoughtful tone.
Determine whether these code examples are clones.
Provide your answer exclusively as ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Example Snippet 1:
{code_snippet1}

Example Snippet 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# variation 8 (Modified Tone)
clone_detection_template_style_variation_8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Employ a brisk and decisive style.
Investigate whether the paired code fragments are clones.
Respond only with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Fragment 1:
{code_snippet1}

Fragment 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# variation 9 (Modified Tone)
clone_detection_template_style_variation_9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt an enthusiastic and energetic tone.
Analyze if the two segments of code are clones.
Your reply must be solely ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Segment One (Code):
{code_snippet1}

Segment Two (Code):
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# variation 10 (Modified Tone)
clone_detection_template_style_variation_10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt a straightforward yet candid tone.
Check if the presented pair of code snippets are clones.
Answer strictly with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Part 1:
{code_snippet1}

Code Part 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# variation 11 (Modified Tone)
clone_detection_template_style_variation_11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Use a measured and reflective tone.
Determine if the two code pieces are effectively clones.
Reply only with either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Programming Snippet 1:
{code_snippet1}

Programming Snippet 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# variation 12 (Modified Tone)
clone_detection_template_style_variation_12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Embrace an inquisitive and perceptive tone.
Evaluate whether the provided code samples are clones.
Your answer should be either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Block 1 of Code:
{code_snippet1}

Block 2 of Code:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# variation 13 (Modified Tone)
clone_detection_template_style_variation_13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Take on an innovative and insightful tone.
Verify if the given code extracts are clones.
Respond using only ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Extract 1:
{code_snippet1}

Extract 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# variation 14 (Modified Tone)
clone_detection_template_style_variation_14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt a reflective and balanced tone.
Examine if these two code excerpts are clones.
Answer solely with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Excerpt One:
{code_snippet1}

Code Excerpt Two:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```
