Here are 15 variations of the bug‐fixing prompt template. Variation 0 is exactly as you provided, and variations 1–14 contain rephrased strings in the SystemMessagePromptTemplate and HumanMessagePromptTemplate (while leaving the AIMessagePromptTemplate unchanged):


```python
----------------------------------------------------------------
Variation 0:
----------------------------------------------------------------
bug_fixing_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before answering, work through your reasoning process. For example:
Incorrect reasoning: "Fixing the bug by making arbitrary changes without identifying the root cause."
Correct reasoning: "Analyzing the code to pinpoint the underlying issue and applying a precise fix that preserves intended functionality."
Fix the bug in the code and provide only the corrected version.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

```

```python
----------------------------------------------------------------
Variation 1:
----------------------------------------------------------------
bug_fixing_template_contrastive_cot_var1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''When responding, first outline your thought process. For instance:
Flawed approach: "Making random tweaks without finding the actual error."
Proper method: "Carefully inspect the code to locate the true bug and implement a targeted fix, ensuring the intended behavior remains intact."
Then, fix the bug in the code and return only the updated version.'''
    ),
    HumanMessagePromptTemplate.from_template("Please provide the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

```

```python
----------------------------------------------------------------
Variation 2:
----------------------------------------------------------------
bug_fixing_template_contrastive_cot_var2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before giving your final answer, display your reasoning process. As an illustration:
An incorrect approach might be: "Changing code arbitrarily without diagnosing the core problem."
A correct approach is: "Reviewing the code to locate the defect and then applying an exact remedy that preserves the intended functionality."
Return only the modified code with the bug fixed.'''
    ),
    HumanMessagePromptTemplate.from_template("Insert your code here: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

```

```python
----------------------------------------------------------------
Variation 3:
----------------------------------------------------------------
bug_fixing_template_contrastive_cot_var3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Prior to answering, walk through your logical steps. For example:
Wrong approach: "Applying random modifications without understanding the error's origin."
Ideal approach: "Systematically analyzing the code to detect the bug's source and implementing an exact correction that respects the original design."
Provide only the corrected version of the code.'''
    ),
    HumanMessagePromptTemplate.from_template("Submit the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

```

```python
----------------------------------------------------------------
Variation 4:
----------------------------------------------------------------
bug_fixing_template_contrastive_cot_var4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Explain your reasoning method before presenting your answer. For instance:
A flawed logic could be: "Arbitrarily modifying the code without pinpointing the issue."
In contrast, a proper reasoning is: "Examining the code to identify the exact problem and then applying a well-targeted correction that maintains proper functionality."
Your answer should include only the fixed code.'''
    ),
    HumanMessagePromptTemplate.from_template("Enter the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

```

```python
----------------------------------------------------------------
Variation 5:
----------------------------------------------------------------
bug_fixing_template_contrastive_cot_var5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you supply your answer, detail your thought process. For example:
An incorrect strategy might be: "Modifying the code in random ways without addressing the fundamental bug."
The correct procedure is: "Investigate the code thoroughly to identify the bug and apply a deliberate fix that maintains the expected behavior."
Submit only the fixed code.'''
    ),
    HumanMessagePromptTemplate.from_template("Provide your code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

```

```python
----------------------------------------------------------------
Variation 6:
----------------------------------------------------------------
bug_fixing_template_contrastive_cot_var6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Outline your thought process before presenting your final result. For instance:
A flawed reasoning example is: "Adjusting code arbitrarily rather than diagnosing the real error."
In contrast, the proper approach is: "Scrutinize the code to uncover the bug and implement a targeted correction that retains the intended functionality."
Return only the corrected code.'''
    ),
    HumanMessagePromptTemplate.from_template("Supply the code segment: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

```

```python
----------------------------------------------------------------
Variation 7:
----------------------------------------------------------------
bug_fixing_template_contrastive_cot_var7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before answering, provide details of your reasoning steps. For example:
An incorrect method would be: "Fixing the bug by making random changes without understanding its cause."
A preferred method is: "Review the code carefully to identify the underlying issue and then apply a precise correction that preserves the original behavior."
Reply with only the corrected code.'''
    ),
    HumanMessagePromptTemplate.from_template("Share the code module: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

```

```python
----------------------------------------------------------------
Variation 8:
----------------------------------------------------------------
bug_fixing_template_contrastive_cot_var8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before giving an answer, quickly summarize your problem-solving process. For example:
An ineffective approach might be: "Altering the code haphazardly without pinpointing the error."
The effective route is: "Evaluating the code to uncover the bug and then applying an accurate fix that preserves its intended purpose."
Ensure that your response contains solely the fixed code.'''
    ),
    HumanMessagePromptTemplate.from_template("Input the code sample: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

```

```python
----------------------------------------------------------------
Variation 9:
----------------------------------------------------------------
bug_fixing_template_contrastive_cot_var9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Elucidate your reasoning process before delivering your answer. For example:
A misstep would be: "Attempting to fix the bug by randomly adjusting the code while ignoring the true error."
A more effective approach is: "Systematically examining the code to locate the bug and then providing a precise fix that respects the intended functionality."
Only include the updated code in your response.'''
    ),
    HumanMessagePromptTemplate.from_template("Paste your code snippet here: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

```

```python
----------------------------------------------------------------
Variation 10:
----------------------------------------------------------------
bug_fixing_template_contrastive_cot_var10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Prior to providing your final answer, articulate your chain-of-thought process. For instance:
A mistaken approach might be: "Modifying the code without first detecting the true error."
The correct method is: "Thoroughly analyzing the code to identify the error and then implementing a focused fix that maintains the expected functionality."
Include only the corrected code in your answer.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly enter the code block: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

```

```python
----------------------------------------------------------------
Variation 11:
----------------------------------------------------------------
bug_fixing_template_contrastive_cot_var11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Detail your reasoning process before you provide your answer. For example:
An incorrect method might be: "Changing code arbitrarily without properly analyzing the bug."
A proper approach is: "Investigate and review the code to detect the precise issue and then apply an accurate correction that preserves functionality."
Return only the fixed code.'''
    ),
    HumanMessagePromptTemplate.from_template("Include the code you wish to fix: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

```

```python
----------------------------------------------------------------
Variation 12:
----------------------------------------------------------------
bug_fixing_template_contrastive_cot_var12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you finalize your answer, walk through your reasoning steps. For example:
A flawed strategy might be: "Randomly altering the code without determining the exact error."
The correct practice is: "Examine the code to isolate the bug and then produce a targeted fix that maintains the intended behavior."
Respond with only the corrected code.'''
    ),
    HumanMessagePromptTemplate.from_template("Type in the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

```

```python
----------------------------------------------------------------
Variation 13:
----------------------------------------------------------------
bug_fixing_template_contrastive_cot_var13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Prior to your answer, share the logical steps of your reasoning. For example:
An inadequate approach might be: "Trying to fix the bug by making unsystematic edits without understanding the cause."
The correct method is: "Meticulously review the code to identify the issue and then execute an accurate fix that preserves the desired functionality."
Return only the updated code.'''
    ),
    HumanMessagePromptTemplate.from_template("Present the code fragment: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

```

```python
----------------------------------------------------------------
Variation 14:
----------------------------------------------------------------
bug_fixing_template_contrastive_cot_var14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before answering, present your reasoning process. For example:
An incorrect strategy may be: "Making non-specific code changes without properly diagnosing the problem."
Instead, analyze the code to locate the fault and then apply a considered fix that retains the intended functionality.
Supply only the corrected code as your answer.'''
    ),
    HumanMessagePromptTemplate.from_template("Attach the relevant code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

Each variation maintains the intended task and prompt technique while presenting the instruction strings differently in the System and Human parts.

```
