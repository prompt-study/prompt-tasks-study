Below are 15 complete prompt template variations. Variation 0 is identical to the original, and Variations 1 to 14 include rephrased strings for both the system and human messages. Note that the AI message remains unchanged.

──────────────────────────── Variation 0
code_summarization_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before answering, work through your reasoning process. For example:
Incorrect reasoning: "Summarizing the code by merely rephrasing comments without understanding its functionality."
Correct reasoning: "Analyzing the code’s structure and logic to provide an accurate, concise summary."
Provide a summary of the following code.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 1
code_summarization_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before providing your answer, detail your internal thought process. For instance:
Incorrect approach: "Explaining the code by simply echoing comments without grasping its logic."
Correct approach: "Reviewing the code’s structure and flow to deliver a clear, succinct summary."
Now, please summarize the code below.'''
    ),
    HumanMessagePromptTemplate.from_template("The code is as follows: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 2
code_summarization_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you answer, walk through your mental steps. For example:
Poor process: "Just rewording comments in the code without truly understanding it."
Ideal process: "Dissecting the structure and logic of the code to create an accurate summary."
Summarize the following code snippet.'''
    ),
    HumanMessagePromptTemplate.from_template("Review this code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 3
code_summarization_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before delivering your answer, outline your reasoning method. For example:
Ineffective reasoning: "Summarizing by simply rephrasing the comments without considering functionality."
Effective reasoning: "Analyzing the code’s architecture and logic to produce a precise summary."
Please provide a summary of the following code.'''
    ),
    HumanMessagePromptTemplate.from_template("Here's the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 4
code_summarization_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Prior to answering, describe your thought process. For instance:
Faulty logic: "Summarizing by merely rephrasing comments without understanding the underlying functionality."
Correct logic: "Assessing the code’s structure and flow to construct an accurate, brief summary."
Provide a summary of the code below.'''
    ),
    HumanMessagePromptTemplate.from_template("Examine this code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 5
code_summarization_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before composing your answer, elaborate on your reasoning steps. For example:
Incorrect approach: "Just rewording the code comments without understanding their logic."
Correct approach: "Thoroughly analyzing the code’s design and behavior to form a concise summary."
Summarize the code given below.'''
    ),
    HumanMessagePromptTemplate.from_template("Code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 6
code_summarization_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before providing your answer, articulate your internal reasoning process. For instance:
Misguided reasoning: "Simply restating comments without grasping the purpose of the code."
Sound reasoning: "Evaluating the code’s structure and functionality to deliver an accurate summary."
Now, summarize the following code.'''
    ),
    HumanMessagePromptTemplate.from_template("Consider this code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 7
code_summarization_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before responding, break down your reasoning steps. For example:
Faulty reasoning: "Rewriting the comments without understanding the actual functionality."
Appropriate reasoning: "Reviewing the code’s structure and logic to craft a concise explanation."
Please provide a summary of the code below.'''
    ),
    HumanMessagePromptTemplate.from_template("The code to review: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 8
code_summarization_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before giving your answer, outline your reasoning process. For example:
Unsuitable process: "Summarizing through mere rewording of comments without comprehending functionality."
Suitable process: "Analyzing the code’s logic and structure for an accurate summary."
Kindly summarize the following code.'''
    ),
    HumanMessagePromptTemplate.from_template("Here is the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 9
code_summarization_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Prior to answering, walk through your thought process step by step. For example:
Ineffective approach: "Summarizing by simply paraphrasing comments without truly understanding the code."
Effective approach: "Reviewing the code’s design and operational flow to produce a precise summary."
Please summarize the following code fragment.'''
    ),
    HumanMessagePromptTemplate.from_template("Take a look at this code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 10
code_summarization_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before answering, detail your step-by-step reasoning. For instance:
Flawed reasoning: "Summarizing code by merely rephrasing inline comments without analyzing its behavior."
Well-founded reasoning: "Assessing the code’s design and flow to deliver a concise summary."
Provide a summary for the code below.'''
    ),
    HumanMessagePromptTemplate.from_template("Inspect this code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 11
code_summarization_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before generating your response, describe your reasoning process. For example:
Inadequate reasoning: "Summarizing code by only rewording comments and neglecting its true functionality."
Proper reasoning: "Examining the code’s structure and logical flow to articulate a succinct summary."
Summarize the code presented below.'''
    ),
    HumanMessagePromptTemplate.from_template("Here is the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 12
code_summarization_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before offering an answer, enumerate your reasoning steps. For example:
Deficient reasoning: "Merely transforming comments into different words without truly understanding the code."
Effective reasoning: "Dissecting the code’s architecture and logical flow to produce an accurate summary."
Summarize the following code block.'''
    ),
    HumanMessagePromptTemplate.from_template("Review the following code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 13
code_summarization_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Prior to providing your answer, walk through your reasoning. For instance:
Suboptimal process: "Just rephrasing comments in the code without capturing its essential functionality."
Optimal process: "Evaluating the code’s structure and logic to generate a clear, brief summary."
Summarize the subsequent code.'''
    ),
    HumanMessagePromptTemplate.from_template("Please analyze this code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 14
code_summarization_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you respond, explain your reasoning process. For example:
Poor method: "Summarizing by simply rewording comments without investigating functionality."
Better method: "Considering the code’s structure and logic to produce a precise, concise summary."
Provide a summary for the code that follows.'''
    ),
    HumanMessagePromptTemplate.from_template("See the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])