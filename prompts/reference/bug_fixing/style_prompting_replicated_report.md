```python
# Variation 0: Senior Software Engineer
bug_fixing_template_style_v0 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt a direct, solution-focused style:
Fix the bug in the code and provide only the corrected version.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 1: Software Developer (Analytical, Methodical)
bug_fixing_template_style_v1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Apply an analytical, methodical tone:
Locate and correct the error in the provided code snippet, returning only the revised code.'''
    ),
    HumanMessagePromptTemplate.from_template("Submit the code here: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 2: Technical Lead (Reflective, Diagnostic)
bug_fixing_template_style_v2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Maintain a reflective, diagnostic approach:
Identify the bug in the code and deliver the fixed code alone.'''
    ),
    HumanMessagePromptTemplate.from_template("Please supply your code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 3: Software Architect (Action-First, Solution-Driven)
bug_fixing_template_style_v3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Embrace an action-first, solution-driven tone:
Correct the error in the code and output just the updated version.'''
    ),
    HumanMessagePromptTemplate.from_template("Input your code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 4: DevOps Engineer (No-Nonsense, Outcome-Oriented)
bug_fixing_template_style_v4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Utilize a no-nonsense, outcome-oriented style:
Resolve the bug in the code and return only the corrected version.'''
    ),
    HumanMessagePromptTemplate.from_template("Enter the code to be fixed: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 5: Code Reviewer (Clear-Cut, Detail-Oriented)
bug_fixing_template_style_v5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt a clear-cut, detail-oriented strategy:
Detect the bug within the code and provide the adjusted version only.'''
    ),
    HumanMessagePromptTemplate.from_template("Provide the code snippet for debugging: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 6: Quality Assurance Engineer (Pragmatic, Performance-Focused)
bug_fixing_template_style_v6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Apply a pragmatic, performance-focused style:
Pinpoint the error in the code and output solely the corrected version.'''
    ),
    HumanMessagePromptTemplate.from_template("Insert your code for review: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 7: Security Engineer (Succinct, Efficiency-Driven)
bug_fixing_template_style_v7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt a succinct, efficiency-driven approach:
Troubleshoot the bug in the code and supply just the fixed version.'''
    ),
    HumanMessagePromptTemplate.from_template("Share the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 8: Data Scientist (Transparent, Outcome-Centric)
bug_fixing_template_style_v8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Exhibit a transparent, outcome-centric tone:
Identify the defect in the code and produce only the revised version.'''
    ),
    HumanMessagePromptTemplate.from_template("Present the code segment: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 9: UI/UX Designer (Sharp, Analytical)
bug_fixing_template_style_v9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Embrace a sharp, analytical tone:
Spot the bug in the provided code and return only the refined version.'''
    ),
    HumanMessagePromptTemplate.from_template("Please paste your code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 10: Algorithm Designer (Brisk, Performance-Driven)
bug_fixing_template_style_v10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Employ a brisk, performance-driven approach:
Uncover and correct the fault in the code, offering solely the improved version.'''
    ),
    HumanMessagePromptTemplate.from_template("Submit the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 11: Technical Writer (Measured, Fact-Based)
bug_fixing_template_style_v11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt a measured, fact-based tone:
Locate the error in the code and only produce the rectified version.'''
    ),
    HumanMessagePromptTemplate.from_template("Insert your code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 12: Performance Analysis Researcher (Impartial, Technical)
bug_fixing_template_style_v12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Maintain an impartial, technical tone:
Fix the bug in the code and output exclusively the amended version.'''
    ),
    HumanMessagePromptTemplate.from_template("Provide your code block: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 13: Computer Science Researcher (Concise, Logic-Based)
bug_fixing_template_style_v13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Adopt a concise, logic-based approach:
Identify and correct the bug in the code, returning simply the fixed version.'''
    ),
    HumanMessagePromptTemplate.from_template("Enter the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```

```python
# Variation 14: Software Engineering Professor (Decisive, Corrective)
bug_fixing_template_style_v14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Embrace a decisive, corrective tone:
Address the bug in the code and yield only the corrected code.'''
    ),
    HumanMessagePromptTemplate.from_template("Share your code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
```
