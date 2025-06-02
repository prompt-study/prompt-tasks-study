Below are the revised **code summarization** prompt templates. In each variation all explicit references to analogical techniques have been removed while preserving the overall structure and instructions.

────────────────────────────
**Variation 0**
```python
code_summarization_template_analogical = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We'll summarize code.
First, invent a brief code snippet. Show how you'd produce a concise summary for it.
Then I'll give you the real code to summarize.'''
    ),
    HumanMessagePromptTemplate.from_template("Please provide your example code and your summary of it."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Now, here's the real code:
{code}

Summarize it. Provide only the summary.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────
**Variation 1**
```python
code_summarization_template_analogical = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We are going to create a summary for some code.
Begin by crafting a short example snippet and a corresponding brief summary.
After that, I will provide the actual code for you to summarize.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly submit your sample code along with its summary."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Here's the actual code:
{code}

Kindly provide only the summary.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────
**Variation 2**
```python
code_summarization_template_analogical = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Our aim is to summarize code.
Begin by generating a simple code snippet with a succinct explanation.
Then I'll present the genuine code for you to summarize.'''
    ),
    HumanMessagePromptTemplate.from_template("Could you share your sample code along with its brief explanation?"),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Below is the actual code:
{code}

Offer only its concise summary.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────
**Variation 3**
```python
code_summarization_template_analogical = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We are summarizing code.
First, create a quick code snippet paired with a short summary.
Next, I will give you the true code that needs summarizing.'''
    ),
    HumanMessagePromptTemplate.from_template("Please send over your example code along with its concise summary."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Now, this is the real code:
{code}

Respond with just the summary.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────
**Variation 4**
```python
code_summarization_template_analogical = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Let's summarize code.
Start by inventing a small code snippet and providing a crisp summary.
Later, I will supply you with the actual code that needs summarizing.'''
    ),
    HumanMessagePromptTemplate.from_template("Please submit your example code along with its accompanying summary."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Presenting the real code now:
{code}

Share only the summary.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────
**Variation 5**
```python
code_summarization_template_analogical = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We'll approach code summarization.
Begin by formulating a brief code snippet together with a neat, concise summary.
Subsequently, I will introduce the actual code for summarization.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly provide your sample code along with its summary."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Here is the actual code:
{code}

Only include the summary.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────
**Variation 6**
```python
code_summarization_template_analogical = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Proceed by summarizing code.
Start by composing a short example code along with a succinct summary.
Afterwards, I will provide you with the actual code to summarize.'''
    ),
    HumanMessagePromptTemplate.from_template("Share your sample code along with its brief summary."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Below is the actual code:
{code}

Provide solely the summary.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────
**Variation 7**
```python
code_summarization_template_analogical = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We are summarizing code.
Initially, devise a small code snippet and craft a brief explanation.
Then, I will supply you with the actual code to summarize.'''
    ),
    HumanMessagePromptTemplate.from_template("Please share your example code along with its summary."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''This is the real code:
{code}

Return only the summary.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────
**Variation 8**
```python
code_summarization_template_analogical = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''In this task, we'll summarize code.
First, please create a concise example snippet along with its summary.
Later, I will furnish you with the actual code to summarize.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly provide your example code and its concise summary."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Now, here is the actual code:
{code}

Summarize it with just the summary.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────
**Variation 9**
```python
code_summarization_template_analogical = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We're going to perform code summarization.
Start by drafting a brief code sample along with a short description.
After that, I will deliver the real code for you to summarize.'''
    ),
    HumanMessagePromptTemplate.from_template("Please submit your example code along with its succinct summary."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Here's the actual code:
{code}

Supply only the summary.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────
**Variation 10**
```python
code_summarization_template_analogical = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Let's do code summarization.
First, generate a short snippet of code accompanied by a clear, concise summary.
Then, I will provide the actual code that requires summarizing.'''
    ),
    HumanMessagePromptTemplate.from_template("Share your sample code and a quick summary of it."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Now presenting the actual code:
{code}

Just provide the summary.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────
**Variation 11**
```python
code_summarization_template_analogical = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We will summarize code.
Begin by writing a small code snippet along with a compact summary.
Following that, I will give you the actual code to be summarized.'''
    ),
    HumanMessagePromptTemplate.from_template("Could you please share your sample code along with a brief summary?"),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Below is the real code:
{code}

Reply with only the summary.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────
**Variation 12**
```python
code_summarization_template_analogical = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''The task is to summarize code.
Please start by crafting a short snippet of code with its brief summary.
Then, I will send you the real code that needs summarization.'''
    ),
    HumanMessagePromptTemplate.from_template("Submit your example code along with its summary."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Here’s the actual code:
{code}

Provide just the summary.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────
**Variation 13**
```python
code_summarization_template_analogical = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''We'll be summarizing code.
First, create a succinct code example accompanied by a brief summary.
Later, I will present the real code that needs to be summarized.'''
    ),
    HumanMessagePromptTemplate.from_template("Please provide your sample code and its concise summary."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Here is the actual code:
{code}

Offer only the summary.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

────────────────────────────
**Variation 14**
```python
code_summarization_template_analogical = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Our goal is to summarize code.
Start by formulating a short code snippet paired with a clear, concise summary.
After that, I'll offer the genuine code for summarization.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly share your sample code along with its summary."),
    AIMessagePromptTemplate.from_template('prompt'),

    HumanMessagePromptTemplate.from_template(
        '''Now, here's the actual code:
{code}

Include only the summary.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```
