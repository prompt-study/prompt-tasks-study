
```python
code_question_answering_template_code_question_answering_variant0 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Assess whether the following code correctly answers the question.
Provide only ###TRUE### if the code fully satisfies the query or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Question:
    {input1_1}

    Code:
    {input2_1}

    Output:
    {output_1}


    Question:
    {input1_2}

    Code:
    {input2_2}

    Output:
    {output_2}


    Question:
    {input1_3}

    Code:
    {input2_3}

    Output:
    {output_3}


    Question:
    {input1_4}

    Code:
    {input2_4}

    Output:
    {output_4}


    Question:
    {input1_5}

    Code:
    {input2_5}

    Output:
    {output_5}
    '''
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
code_question_answering_template_code_question_answering_variant1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine if the provided code adequately answers the question.
Return ###TRUE### if the code completely meets the question's requirements; otherwise, reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Question:
    {input1_1}

    Code:
    {input2_1}

    Output:
    {output_1}


    Question:
    {input1_2}

    Code:
    {input2_2}

    Output:
    {output_2}


    Question:
    {input1_3}

    Code:
    {input2_3}

    Output:
    {output_3}


    Question:
    {input1_4}

    Code:
    {input2_4}

    Output:
    {output_4}


    Question:
    {input1_5}

    Code:
    {input2_5}

    Output:
    {output_5}
    '''
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
code_question_answering_template_code_question_answering_variant2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Evaluate if the code correctly addresses the question.
Respond solely with ###TRUE### if it fully satisfies the inquiry, or ###FALSE### if it falls short.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Question:
    {input1_1}

    Code:
    {input2_1}

    Output:
    {output_1}


    Question:
    {input1_2}

    Code:
    {input2_2}

    Output:
    {output_2}


    Question:
    {input1_3}

    Code:
    {input2_3}

    Output:
    {output_3}


    Question:
    {input1_4}

    Code:
    {input2_4}

    Output:
    {output_4}


    Question:
    {input1_5}

    Code:
    {input2_5}

    Output:
    {output_5}
    '''
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
code_question_answering_template_code_question_answering_variant3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Examine whether the code meets the demands of the question.
Reply with ###TRUE### if it fully answers the query, and ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Question:
    {input1_1}

    Code:
    {input2_1}

    Output:
    {output_1}


    Question:
    {input1_2}

    Code:
    {input2_2}

    Output:
    {output_2}


    Question:
    {input1_3}

    Code:
    {input2_3}

    Output:
    {output_3}


    Question:
    {input1_4}

    Code:
    {input2_4}

    Output:
    {output_4}


    Question:
    {input1_5}

    Code:
    {input2_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Please consider the following question:
{question}

Code provided:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_code_question_answering_variant4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Judge if the given code properly answers the question.
Answer exclusively with ###TRUE### if the code is sufficient, or ###FALSE### if it is not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Question:
    {input1_1}

    Code:
    {input2_1}

    Output:
    {output_1}


    Question:
    {input1_2}

    Code:
    {input2_2}

    Output:
    {output_2}


    Question:
    {input1_3}

    Code:
    {input2_3}

    Output:
    {output_3}


    Question:
    {input1_4}

    Code:
    {input2_4}

    Output:
    {output_4}


    Question:
    {input1_5}

    Code:
    {input2_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Presented code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_code_question_answering_variant5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Assess if the code provides a complete answer to the question.
Your response should be either ###TRUE### if it does, or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Question:
    {input1_1}

    Code:
    {input2_1}

    Output:
    {output_1}


    Question:
    {input1_2}

    Code:
    {input2_2}

    Output:
    {output_2}


    Question:
    {input1_3}

    Code:
    {input2_3}

    Output:
    {output_3}


    Question:
    {input1_4}

    Code:
    {input2_4}

    Output:
    {output_4}


    Question:
    {input1_5}

    Code:
    {input2_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''The question is as follows:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_code_question_answering_variant6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine if the code supplied answers the question appropriately.
Provide only ###TRUE### if it fully satisfies the question, otherwise respond with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Question:
    {input1_1}

    Code:
    {input2_1}

    Output:
    {output_1}


    Question:
    {input1_2}

    Code:
    {input2_2}

    Output:
    {output_2}


    Question:
    {input1_3}

    Code:
    {input2_3}

    Output:
    {output_3}


    Question:
    {input1_4}

    Code:
    {input2_4}

    Output:
    {output_4}


    Question:
    {input1_5}

    Code:
    {input2_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Review the following question:
{question}

And the corresponding code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_code_question_answering_variant7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Verify whether the code effectively addresses the question.
Reply with only ###TRUE### if the code meets the query, or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Question:
    {input1_1}

    Code:
    {input2_1}

    Output:
    {output_1}


    Question:
    {input1_2}

    Code:
    {input2_2}

    Output:
    {output_2}


    Question:
    {input1_3}

    Code:
    {input2_3}

    Output:
    {output_3}


    Question:
    {input1_4}

    Code:
    {input2_4}

    Output:
    {output_4}


    Question:
    {input1_5}

    Code:
    {input2_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Accompanying code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_code_question_answering_variant8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Review the code to see if it adequately answers the question.
Return solely ###TRUE### if the answer is complete, or ###FALSE### if it is incomplete.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Question:
    {input1_1}

    Code:
    {input2_1}

    Output:
    {output_1}


    Question:
    {input1_2}

    Code:
    {input2_2}

    Output:
    {output_2}


    Question:
    {input1_3}

    Code:
    {input2_3}

    Output:
    {output_3}


    Question:
    {input1_4}

    Code:
    {input2_4}

    Output:
    {output_4}


    Question:
    {input1_5}

    Code:
    {input2_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Consider the question below:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_code_question_answering_variant9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Examine the code to determine if it answers the question properly.
Answer exclusively with ###TRUE### if the query is fully met, or with ###FALSE### otherwise.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Question:
    {input1_1}

    Code:
    {input2_1}

    Output:
    {output_1}


    Question:
    {input1_2}

    Code:
    {input2_2}

    Output:
    {output_2}


    Question:
    {input1_3}

    Code:
    {input2_3}

    Output:
    {output_3}


    Question:
    {input1_4}

    Code:
    {input2_4}

    Output:
    {output_4}


    Question:
    {input1_5}

    Code:
    {input2_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Here is the query:
{question}

Associated code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_code_question_answering_variant10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Check whether the code successfully answers the question.
Reply only with ###TRUE### if it is fully correct, otherwise respond with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Question:
    {input1_1}

    Code:
    {input2_1}

    Output:
    {output_1}


    Question:
    {input1_2}

    Code:
    {input2_2}

    Output:
    {output_2}


    Question:
    {input1_3}

    Code:
    {input2_3}

    Output:
    {output_3}


    Question:
    {input1_4}

    Code:
    {input2_4}

    Output:
    {output_4}


    Question:
    {input1_5}

    Code:
    {input2_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question:
{question}

Code sample:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_code_question_answering_variant11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Evaluate the provided code to see if it answers the question satisfactorily.
Provide only ###TRUE### if the code meets the criteria, or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Question:
    {input1_1}

    Code:
    {input2_1}

    Output:
    {output_1}


    Question:
    {input1_2}

    Code:
    {input2_2}

    Output:
    {output_2}


    Question:
    {input1_3}

    Code:
    {input2_3}

    Output:
    {output_3}


    Question:
    {input1_4}

    Code:
    {input2_4}

    Output:
    {output_4}


    Question:
    {input1_5}

    Code:
    {input2_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Examine this question:
{question}

With the following code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_code_question_answering_variant12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Determine if the code presented is an adequate response to the question.
Answer only with ###TRUE### if it completely addresses the query, or ###FALSE### if not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Question:
    {input1_1}

    Code:
    {input2_1}

    Output:
    {output_1}


    Question:
    {input1_2}

    Code:
    {input2_2}

    Output:
    {output_2}


    Question:
    {input1_3}

    Code:
    {input2_3}

    Output:
    {output_3}


    Question:
    {input1_4}

    Code:
    {input2_4}

    Output:
    {output_4}


    Question:
    {input1_5}

    Code:
    {input2_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Question to answer:
{question}

Code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_code_question_answering_variant13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Assess if the code fulfills the requirements of the question.
Respond with ###TRUE### if it completely satisfies the question, or ###FALSE### if it does not.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Question:
    {input1_1}

    Code:
    {input2_1}

    Output:
    {output_1}


    Question:
    {input1_2}

    Code:
    {input2_2}

    Output:
    {output_2}


    Question:
    {input1_3}

    Code:
    {input2_3}

    Output:
    {output_3}


    Question:
    {input1_4}

    Code:
    {input2_4}

    Output:
    {output_4}


    Question:
    {input1_5}

    Code:
    {input2_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''The question is:
{question}

Code provided:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
code_question_answering_template_code_question_answering_variant14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Review whether the code properly answers the question.
Reply solely with ###TRUE### if it fully meets the question’s needs, otherwise reply with ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''
    Examples

    Question:
    {input1_1}

    Code:
    {input2_1}

    Output:
    {output_1}


    Question:
    {input1_2}

    Code:
    {input2_2}

    Output:
    {output_2}


    Question:
    {input1_3}

    Code:
    {input2_3}

    Output:
    {output_3}


    Question:
    {input1_4}

    Code:
    {input2_4}

    Output:
    {output_4}


    Question:
    {input1_5}

    Code:
    {input2_5}

    Output:
    {output_5}
    '''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Please answer the following question:
{question}

Review this code:
{code}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])
```
