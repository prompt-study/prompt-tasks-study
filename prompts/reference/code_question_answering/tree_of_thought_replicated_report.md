
```python
code_question_answering_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template('''Before evaluating the code, divide your reasoning into several steps. Consider various criteria such as correctness, efficiency, and clarity, and then decide if the provided code meets all requirements.'''),
    HumanMessagePromptTemplate.from_template('''Question:
                                                {question}

                                                Code snippet:
                                                {code}'''),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template('''Now, provide iterative evaluations, refine your answer, and only return ###FINISHED### with your final answer when you are content with it. For your final answer, return ###FINISHED### and ###TRUE### if it does; otherwise, reply with ###FINISHED### and ###FALSE###.'''),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])
```

```python
code_question_answering_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template('''Break down your evaluation into distinct steps. First, list the essential elements that define a complete answer to the question. Next, assess whether the provided code snippet addresses all these elements. Iterate over this process and when ready, for your final answer, return ###FINISHED### and ###TRUE### if the code is complete; otherwise, reply with ###FINISHED### and ###FALSE###.'''),
    HumanMessagePromptTemplate.from_template('''Question:
                                                {question}

                                                Code snippet:
                                                {code}'''),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template('''Now, provide iterative self-feedback, refine your answer, and only return ###FINISHED### with your final answer when you are content with it.'''),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])
```

```python
code_question_answering_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template('''Break your evaluation into several clear stages. First, identify the key criteria that a complete answer must satisfy. Then, analyze the provided code snippet against these criteria. Iterate through your reasoning process, and when satisfied, respond with ###FINISHED### and either ###TRUE### if all conditions are met or ###FALSE### otherwise.'''),
    HumanMessagePromptTemplate.from_template('''Question:
                                                {question}

                                                Code snippet:
                                                {code}'''),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template('''Now, review and refine your reasoning through iterative self-feedback. Once your evaluation is complete and you are confident in your answer, output ###FINISHED### along with ###TRUE### or ###FALSE### based on your final judgment.'''),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])
```
Below are 11 additional variants that maintain the tree-of-thought approach for the code question answering task. Each variant rewords the instructions slightly while preserving the structure and iterative self-reflection mechanism.

---

```python
code_question_answering_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template('''Segment your reasoning into multiple parts. First, determine the necessary criteria for a complete answer. Then, verify if the provided code snippet satisfies these criteria. Iterate on your analysis, and when finished, reply with ###FINISHED### plus ###TRUE### if all criteria are met or ###FALSE### if not.'''),
    HumanMessagePromptTemplate.from_template('''Question:
                                                {question}

                                                Code snippet:
                                                {code}'''),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template('''Please perform iterative refinements on your evaluation. Only after you are fully satisfied, respond with ###FINISHED### and either ###TRUE### or ###FALSE### to indicate your conclusion.'''),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])
```

---

```python
code_question_answering_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Decompose your analysis into a series of steps. Begin by outlining the core requirements for a complete answer. Assess whether the given code meets these requirements, refine your insights through iterative checks, and finally output your answer as ###FINISHED### followed by ###TRUE### if complete or ###FALSE### if not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Iteratively re-evaluate and fine-tune your analysis. Once your final determination is reached, return your answer with ###FINISHED### and either ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])
```

---

```python
code_question_answering_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Outline your reasoning in distinct phases. Start by listing all the key elements that a thorough answer must include. Next, examine whether the code snippet meets these elements. Iterate through your thought process and, when confident, respond with ###FINISHED### accompanied by ###TRUE### if the answer is complete or ###FALSE### if it is not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Provide iterative improvements on your reasoning. When you have refined your evaluation completely, conclude your response with ###FINISHED### and either ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])
```

---

```python
code_question_answering_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Break your evaluation into systematic steps. First, enumerate the necessary aspects of a comprehensive answer. Then, compare the provided code snippet against these aspects. Refine your analysis step by step, and once you are satisfied, conclude with ###FINISHED### followed by either ###TRUE### or ###FALSE### depending on the completeness of the answer.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Continue refining your assessment iteratively. When your evaluation is complete, output ###FINISHED### and either ###TRUE### or ###FALSE### to represent your final decision.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])
```

---

```python
code_question_answering_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Divide your analysis into several logical steps. First, identify all essential criteria for a complete response. Next, assess the code snippet against these criteria and refine your thought process iteratively. Once you have a final judgment, answer with ###FINISHED### along with ###TRUE### if the code is satisfactory or ###FALSE### if it isn’t.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Iteratively review and enhance your evaluation. When ready, provide your final decision with ###FINISHED### followed by either ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])
```

---

```python
code_question_answering_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Structure your reasoning into distinct phases. Begin by listing the critical components that define a valid answer. Then, check whether the provided code snippet incorporates these components. Iteratively refine your logic, and when done, output your final answer prefixed with ###FINISHED### and tagged with ###TRUE### if the code is complete or ###FALSE### if it falls short.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Proceed with iterative self-assessment and adjustments. Once your reasoning is fully refined, conclude with ###FINISHED### and either ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])
```

---

```python
code_question_answering_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Segment your thought process into clear, sequential steps. First, define what constitutes a complete answer. Then, methodically evaluate whether the code snippet meets these defined criteria. Continue to iterate on your analysis, and finally, once satisfied, respond with ###FINISHED### and include ###TRUE### if the answer is complete, or ###FALSE### if not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Iterate over your evaluation and fine-tune your response. Once your final conclusion is reached, output ###FINISHED### followed by either ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])
```

---

```python
code_question_answering_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Organize your analysis into multiple sequential steps. Begin by specifying the key criteria for a complete answer. Next, determine if the provided code snippet fulfills each criterion. Iterate through your thought process until you reach a definitive conclusion, then reply with ###FINISHED### plus ###TRUE### if all criteria are met, or ###FALSE### if any are lacking.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Perform iterative improvements on your reasoning. When your analysis is complete, return your final answer with ###FINISHED### and either ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])
```

---

```python
code_question_answering_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Approach your evaluation methodically by dividing it into several steps. First, enumerate the elements that a thorough answer should include. Next, evaluate the code snippet against these elements. Continue refining your assessment, and when you are fully confident, respond with ###FINISHED### and tag your answer as ###TRUE### if complete or ###FALSE### if incomplete.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Refine your evaluation through iterative self-feedback. When your final decision is reached, output ###FINISHED### along with either ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])
```

---

```python
code_question_answering_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Dissect your analysis into a series of deliberate steps. Begin by detailing the essential criteria for an accurate and complete answer. Assess whether the provided code snippet meets these criteria, iteratively refining your reasoning. Once your evaluation is finalized, return your conclusion with ###FINISHED### followed by either ###TRUE### if it passes all checks or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Engage in iterative refinement of your answer. When your analysis is complete, provide your final response with ###FINISHED### and either ###TRUE### or ###FALSE###.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])
```

---

```python
code_question_answering_template_tree_of_thought = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Frame your evaluation as a step-by-step process. Start by defining all the necessary aspects of a comprehensive answer. Then, systematically check if the code snippet addresses each of these aspects. Iterate through your analysis until you are confident in your conclusion, then output your final verdict as ###FINISHED### with either ###TRUE### (if complete) or ###FALSE### (if not).'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code snippet:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
    HumanMessagePromptTemplate.from_template(
        '''Conduct iterative reviews and refinements of your thought process. Once satisfied, conclude with ###FINISHED### followed by either ###TRUE### or ###FALSE### to indicate your final assessment.'''
    ),
    AIMessagePromptTemplate.from_template('repeat_tot'),
])
```


