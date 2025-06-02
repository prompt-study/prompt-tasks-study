
```python
─────────────────────────────
Variation 0:
─────────────────────────────
assert_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before answering, work through your reasoning process. For example:
Incorrect reasoning: "Creating an assertion based on an incomplete understanding of the expected behavior."
Correct reasoning: "Carefully analyzing the code to generate an assertion that fully captures the intended condition."
Determine the correct assertion that should replace <AssertPlaceHolder> in the following code.
Provide only the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python

─────────────────────────────
Variation 1:
─────────────────────────────
assert_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Prior to delivering your answer, step through your reasoning. For instance:
Flawed thought: "Formulating an assertion based on an insufficient understanding of what's required."
Sound thought: "Examining the code in detail to devise an assertion that accurately reflects the intended logic."
Identify the appropriate assertion that should substitute <AssertPlaceHolder> in the provided code.
Return only the assertion.'''
    ),
    HumanMessagePromptTemplate.from_template("Submit the following code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python

─────────────────────────────
Variation 2:
─────────────────────────────
assert_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you respond, please detail your reasoning process. For example:
Incorrect logic: "Generating an assertion without fully comprehending the desired behavior."
Correct logic: "Thoroughly inspecting the code to craft an assertion that meets the specified condition."
Find the correct assertion to be inserted in place of <AssertPlaceHolder> within the code below.
Output solely the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Here is the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python

─────────────────────────────
Variation 3:
─────────────────────────────
assert_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Start by outlining your thought process before answering. For instance:
Wrong approach: "Designing an assertion while misinterpreting the expected functionality."
Accurate approach: "Scrutinizing the code carefully to construct an assertion that perfectly matches the required behavior."
Identify the assertion that should take the place of <AssertPlaceHolder> in the code that follows.
Only provide the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Code sample: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python

─────────────────────────────
Variation 4:
─────────────────────────────
assert_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Please articulate your reasoning steps prior to answering. For instance:
Misguided reasoning: "Constructing an assertion based on a partial grasp of the intended output."
Correct reasoning: "Analyzing the code thoroughly to generate an assertion that captures the full requirement."
Determine the suitable assertion to replace <AssertPlaceHolder> in the snippet below.
Offer only the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Present the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python

─────────────────────────────
Variation 5:
─────────────────────────────
assert_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Explain your reasoning process first before answering. As an example:
Faulty reasoning: "Forming an assertion with an incomplete understanding of the desired outcome."
Proper reasoning: "Examining the code in-depth to create an assertion that satisfies the complete condition."
Identify the correct assertion to substitute <AssertPlaceHolder> in the code sample that follows.
Respond with only the assertion.'''
    ),
    HumanMessagePromptTemplate.from_template("The code is provided here: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python

─────────────────────────────
Variation 6:
─────────────────────────────
assert_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you give your final answer, please detail your reasoning steps. For example:
Incorrect pathway: "Developing an assertion without a full appreciation of the expected behavior."
Correct pathway: "Analyzing the code carefully to produce an assertion aligning with the intended conditions."
Locate the appropriate assertion to stand in place of <AssertPlaceHolder> in the subsequent code.
Return just the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Examine this code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python

─────────────────────────────
Variation 7:
─────────────────────────────
assert_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Work through your logical reasoning prior to answering. Consider the following:
Poor reasoning: "Sketching an assertion from an incomplete perspective of the expected result."
Good reasoning: "Investigating the code in detail to generate an assertion that meets the intended specification."
Find the assertion that should replace <AssertPlaceHolder> in the code below.
Provide only the assertion as your answer.'''
    ),
    HumanMessagePromptTemplate.from_template("The following code is provided: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python

─────────────────────────────
Variation 8:
─────────────────────────────
assert_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Proceed by elaborating your thought process before answering. For instance:
Faulty approach: "Creating an assertion based on a limited understanding of what is required."
Correct approach: "Carefully reviewing the code to determine an assertion that fully adheres to the intended condition."
Figure out the assertion that should be inserted in place of <AssertPlaceHolder> in the ensuing code.
Only include the assertion statement in your response.'''
    ),
    HumanMessagePromptTemplate.from_template("Here is the code segment: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python

─────────────────────────────
Variation 9:
─────────────────────────────
assert_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before providing your answer, describe your reasoning approach. For example:
Suboptimal reasoning: "Devising an assertion without a complete view of the expected behavior."
Optimal reasoning: "Closely examining the code to infer an assertion that encapsulates the correct condition."
Identify the assertion to replace <AssertPlaceHolder> in the code below.
Reply solely with the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Supply the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python

─────────────────────────────
Variation 10:
─────────────────────────────
assert_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Articulate your reasoning before you answer. For example:
Flawed logic: "Crafting an assertion with only a partial understanding of the target behavior."
Refined logic: "Reviewing the code meticulously to produce an assertion that adheres to the intended outcome."
Decide on the correct assertion to substitute for <AssertPlaceHolder> in the following code.
Respond with just the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Code input: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python

─────────────────────────────
Variation 11:
─────────────────────────────
assert_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Elaborate your reasoning process before providing your answer. For example:
Inadequate reasoning: "Building an assertion without completely grasping the expected function."
Proper reasoning: "Studying the code thoroughly to derive an assertion that precisely fits the intended rule."
Determine the appropriate assertion to replace <AssertPlaceHolder> in the code below.
Supply only the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Input the code as follows: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python

─────────────────────────────
Variation 12:
─────────────────────────────
assert_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Please outline your reasoning before answering. For example:
Insufficient reasoning: "Forming an assertion that misinterprets the expected behavior."
Accurate reasoning: "Inspecting the code in sufficient detail to formulate an assertion that exactly meets the required condition."
Discover the assertion that should substitute <AssertPlaceHolder> in the code provided.
Offer only the assertion statement as your response.'''
    ),
    HumanMessagePromptTemplate.from_template("The code is: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python

─────────────────────────────
Variation 13:
─────────────────────────────
assert_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Detail your thought process prior to giving an answer. For instance:
Erroneous reasoning: "Proposing an assertion based on a misunderstanding of the required outcome."
Correct method: "Carefully examining the code to generate an assertion that fully satisfies the criteria."
Identify the correct assertion to replace <AssertPlaceHolder> in the following code snippet.
Return solely the assertion statement.'''
    ),
    HumanMessagePromptTemplate.from_template("Share the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python

─────────────────────────────
Variation 14:
─────────────────────────────
assert_generation_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before sharing your answer, please explain your reasoning. For example:
Misguided approach: "Suggesting an assertion without a full analysis of what is expected."
Accurate approach: "Reviewing the code thoroughly to design an assertion that captures the entire intended behavior."
Determine the precise assertion to be used in place of <AssertPlaceHolder> within the code below.
Provide only the assertion statement as your answer.'''
    ),
    HumanMessagePromptTemplate.from_template("Here is the code to analyze: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
