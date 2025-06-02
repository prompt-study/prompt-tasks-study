
**Variant 1**  
```python
code_question_answering_template_analogical_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine if the provided code adequately answers the question. Before evaluating, recall one or two analogous instances where you assessed code answers, and briefly explain the criteria that define a complete answer. Then, return ###TRUE### if the code fully meets the question’s requirements; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''First, recall an analogous example of code evaluation. Summarize the key factors that confirmed a complete answer.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Now, evaluate the following:
Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

---

**Variant 2**  
```python
code_question_answering_template_analogical_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Evaluate whether the given code snippet fully answers the question. Start by reflecting on similar evaluation cases and the standards used to judge completeness. Then, return ###TRUE### if the code meets all requirements; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Recall one or more past examples of evaluating code answers. Briefly describe the reasoning process and key criteria you used.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Proceed with:
Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

---

**Variant 3**  
```python
code_question_answering_template_analogical_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Your task is to assess if the provided code snippet correctly answers the question. First, recall similar situations where you evaluated code, and outline the reasoning steps involved. Then, return ###TRUE### if the code fully satisfies the question; otherwise, return ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Recall an analogous evaluation scenario and describe the factors that indicated a complete answer.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Now, review the following:
Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

---

**Variant 4**  
```python
code_question_answering_template_analogical_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Assess whether the provided code fully answers the question. Begin by recalling similar cases and detailing the criteria used to judge a correct answer. Then, return ###TRUE### if the code is completely adequate; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Before proceeding, recall one analogous example and summarize the reasoning and criteria applied in that evaluation.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Now, consider:
Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

---

**Variant 5**  
```python
code_question_answering_template_analogical_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine whether the provided code snippet completely answers the question. First, recall similar evaluation examples from your experience and outline the essential criteria for completeness. Then, return ###TRUE### if the code meets every requirement; otherwise, return ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Recall a similar code evaluation example and briefly explain the key factors that defined a complete answer.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Now, evaluate:
Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

---

**Variant 6**  
```python
code_question_answering_template_analogical_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Examine whether the provided code snippet fully addresses the question. Start by recalling analogous instances and describing the decision process used to determine a correct answer. Then, return ###TRUE### if the code is fully compliant; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Recall one or two analogous evaluations and outline the reasoning steps and criteria that ensured the answer was complete.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Proceed with the evaluation:
Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

---

**Variant 7**  
```python
code_question_answering_template_analogical_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Judge if the provided code snippet adequately answers the question. First, recall similar evaluation tasks and summarize the criteria you used to determine a complete answer. Then, return ###TRUE### if the code meets the requirements; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Recall an analogous code evaluation case and briefly describe the key criteria that were critical for a correct assessment.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Now, evaluate the following:
Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

---

**Variant 8**  
```python
code_question_answering_template_analogical_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine if the provided code snippet is a complete answer to the question. Begin by reflecting on similar evaluation scenarios and the factors that ensured an answer was complete. Then, return ###TRUE### if the code fully meets the question's requirements; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Recall one or more past analogous evaluations and summarize the key reasoning and standards applied.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Now, review:
Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

---

**Variant 9**  
```python
code_question_answering_template_analogical_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Decide if the provided code snippet completely answers the question. Start by recalling similar cases where you evaluated code answers and outline the key reasoning. Then, return ###TRUE### if the code is fully adequate; otherwise, return ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Recall a similar evaluation example and briefly note the critical factors used to judge completeness.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Proceed with:
Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

---

**Variant 10**  
```python
code_question_answering_template_analogical_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Review the provided code snippet to determine if it fully answers the question. First, recall analogous evaluation instances and describe the standards you used to assess completeness. Then, return ###TRUE### if the code meets all criteria; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Before assessing the current input, recall and briefly explain a similar code evaluation scenario along with its key decision criteria.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Now, evaluate:
Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

---

**Variant 11**  
```python
code_question_answering_template_analogical_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine whether the provided code snippet fully answers the question. First, recall a few analogous evaluation cases and outline the essential reasoning steps. Then, return ###TRUE### if the code completely meets the requirements; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Recall an analogous example of code evaluation and summarize the critical factors that indicated a complete answer.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Now, review the following:
Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

---

**Variant 12**  
```python
code_question_answering_template_analogical_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Analyze if the provided code snippet completely answers the question. Begin by recalling similar evaluation examples and describing the key criteria used in those cases. Then, return ###TRUE### if the code fully complies; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Reflect on one or more analogous code evaluations and briefly outline the reasoning and standards applied to ensure completeness.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Proceed with:
Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

---

**Variant 13**  
```python
code_question_answering_template_analogical_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Decide whether the provided code snippet is a complete and correct answer to the question. Start by recalling similar cases and summarizing the criteria that determined a complete answer. Then, return ###TRUE### if the code meets the requirements fully; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Recall a similar code evaluation and briefly describe the reasoning and criteria that ensured the answer was complete.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Now, evaluate:
Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

---

**Variant 14**  
```python
code_question_answering_template_analogical_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Evaluate if the provided code snippet fully addresses the question. First, recall analogous evaluation examples and explain the criteria you used to judge a complete answer. Then, return ###TRUE### if the code is entirely adequate; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Recall one analogous example of code evaluation and summarize the key factors that led to a correct assessment.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Now, consider:
Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

---

**Variant 15**  
```python
code_question_answering_template_analogical_prompting = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Review the provided code snippet and determine if it completely answers the question. Start by recalling similar examples of code evaluations and outlining the key criteria used in those cases. Then, return ###TRUE### if the code fully meets the requirements; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Recall one or two analogous cases where code was evaluated. Briefly describe the evaluation process and the standards that confirmed a complete answer.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Now, evaluate the following:
Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

