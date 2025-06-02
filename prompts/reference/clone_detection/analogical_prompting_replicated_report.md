```python
# Variation 0:
clone_detection_template_analogical = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine if two code snippets are clones.
First, invent a small pair of code snippets that are similar or identical.
Show how you'd check whether they're clones.
Then, I’ll give you the real pair.'''
    ),
    HumanMessagePromptTemplate.from_template("Go ahead and generate your example now."),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Real snippets:
Code Snippet 1:
{code_snippet1}

Code Snippet 2:
{code_snippet2}

Are these clones?
Provide ###TRUE### or ###FALSE### only.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 1:
clone_detection_template_analogical_v1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Apply a method to evaluate whether two code segments are clones.
Begin by crafting a pair of brief code examples that are either very similar or identical.
Demonstrate the clone verification process with these examples.
Later, I will supply the actual pair.'''
    ),
    HumanMessagePromptTemplate.from_template("Please produce your example now."),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Actual code segments:
Code Snippet 1:
{code_snippet1}

Code Snippet 2:
{code_snippet2}

Do these represent clones?
Respond only with ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 2:
clone_detection_template_analogical_v2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Utilize an example-based approach to decide if two pieces of code are clones.
Start by inventing a concise pair of code examples that are nearly or exactly alike.
Illustrate your method for assessing clone similarity using these examples.
Subsequently, I will present you with the actual pair.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly generate your sample now."),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Provided code segments:
Code Snippet 1:
{code_snippet1}

Code Snippet 2:
{code_snippet2}

Are these two clones?
Answer with only ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 3:
clone_detection_template_analogical_v3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Use an example-based method to check if two code fragments are clones.
First, create a brief pair of code snippets with high similarity or identity.
Walk through how you would verify them as clones.
After that, I will provide the actual code pair.'''
    ),
    HumanMessagePromptTemplate.from_template("Now, please generate your example."),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Here are the actual snippets:
Code Snippet 1:
{code_snippet1}

Code Snippet 2:
{code_snippet2}

Can you confirm if they are clones?
Answer only with ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 4:
clone_detection_template_analogical_v4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Apply a method to decide whether two code examples are clones.
Initially, devise a pair of short code snippets that are nearly identical or very similar.
Describe how you would determine their clone status.
Then, I will share the real pair with you.'''
    ),
    HumanMessagePromptTemplate.from_template("Please create your example now."),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''The actual code snippets are:
Code Snippet 1:
{code_snippet1}

Code Snippet 2:
{code_snippet2}

Are these clones?
Reply only with ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 5:
clone_detection_template_analogical_v5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Use a method to determine if two code blocks are clones.
Start off by constructing a small pair of code samples that are almost or completely alike.
Explain how you would check their clone relationship.
Later, I will provide the genuine pair.'''
    ),
    HumanMessagePromptTemplate.from_template("Go ahead and produce your example now."),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''The actual snippets provided are:
Code Snippet 1:
{code_snippet1}

Code Snippet 2:
{code_snippet2}

Do these represent clones?
Respond exclusively with ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 6:
clone_detection_template_analogical_v6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Apply a method to assess whether two code excerpts are clones.
Begin by generating a brief pair of code examples that share identical or highly similar features.
Illustrate how you would determine if they are clones.
Subsequently, I will supply you with the actual pair.'''
    ),
    HumanMessagePromptTemplate.from_template("Please generate your sample now."),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Here are the real code excerpts:
Code Snippet 1:
{code_snippet1}

Code Snippet 2:
{code_snippet2}

Are these clones?
Answer with only ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 7:
clone_detection_template_analogical_v7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Apply a method to decide if two pieces of code are clones.
First, design a simple pair of code snippets that are either identical or very similar.
Walk through the steps you would use to verify if they are clones.
Afterwards, I will send you the actual pair.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly produce your example now."),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Actual snippets provided:
Code Snippet 1:
{code_snippet1}

Code Snippet 2:
{code_snippet2}

Are these code clones?
Provide only ###TRUE### or ###FALSE### as your answer.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 8:
clone_detection_template_analogical_v8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Use an approach to figure out if two code snippets are clones.
Begin by coming up with a concise pair of code examples that resemble each other closely.
Outline your process for determining their clone status.
Then, I will present the actual pair for evaluation.'''
    ),
    HumanMessagePromptTemplate.from_template("Now, please generate your sample."),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''The provided code snippets are:
Code Snippet 1:
{code_snippet1}

Code Snippet 2:
{code_snippet2}

Are these clones?
Respond solely with ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 9:
clone_detection_template_analogical_v9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Leverage a method to determine whether two snippets of code are clones.
First, write a pair of short code examples that are either the same or very similar.
Show the method you would use to check if they are clones.
Later on, I’ll provide the actual code pair.'''
    ),
    HumanMessagePromptTemplate.from_template("Please go ahead and generate your example now."),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Given real code snippets:
Code Snippet 1:
{code_snippet1}

Code Snippet 2:
{code_snippet2}

Do they qualify as clones?
Answer strictly with ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 10:
clone_detection_template_analogical_v10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Invoke a method to examine if two provided code instances are clones.
To start, construct a pair of brief code segments that are nearly or exactly alike.
Detail how you would inspect them for clone characteristics.
Subsequently, I will offer the real pair for assessment.'''
    ),
    HumanMessagePromptTemplate.from_template("Generate your example, please."),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Here are the actual code segments:
Code Snippet 1:
{code_snippet1}

Code Snippet 2:
{code_snippet2}

Are these clones?
Answer using only ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 11:
clone_detection_template_analogical_v11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Engage a method to verify if two code samples are clones.
Initially, come up with a short pair of code examples that are very similar or identical.
Explain how you would test their clone status.
Afterwards, I will provide you with the actual code pair.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly create your example now."),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''The actual code samples are as follows:
Code Snippet 1:
{code_snippet1}

Code Snippet 2:
{code_snippet2}

Are these clones?
Respond only with ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 12:
clone_detection_template_analogical_v12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Apply a method to assess whether two given code fragments are clones.
Start by drafting a pair of short code snippets that mirror each other in similarity.
Describe the method you would use to check for cloning.
Next, I will present the real pair for your evaluation.'''
    ),
    HumanMessagePromptTemplate.from_template("Please produce your example now."),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Real code fragments:
Code Snippet 1:
{code_snippet1}

Code Snippet 2:
{code_snippet2}

Are these clones?
Reply solely with ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 13:
clone_detection_template_analogical_v13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Use a method to figure out if two code blocks are clones.
Begin by devising a compact pair of code snippets that are either very similar or identical.
Illustrate how you would check for a clone relationship using these samples.
Then, I will hand you the actual code pair.'''
    ),
    HumanMessagePromptTemplate.from_template("Now, generate your example, please."),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Actual code blocks:
Code Snippet 1:
{code_snippet1}

Code Snippet 2:
{code_snippet2}

Can you determine if they are clones?
Answer exclusively with ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```

```python
# Variation 14:
clone_detection_template_analogical_v14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Leverage a method to decide whether two coding examples are clones.
Start by formulating a brief pair of code snippets that are nearly identical or very alike.
Demonstrate your strategy for checking if they are indeed clones.
Afterwards, I will provide the actual set for evaluation.'''
    ),
    HumanMessagePromptTemplate.from_template("Please go ahead and produce your example now."),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Here are the real code examples:
Code Snippet 1:
{code_snippet1}

Code Snippet 2:
{code_snippet2}

Do these qualify as clones?
Reply only with either ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('prompt')
])
```
