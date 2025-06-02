Below are 15 variations of the original prompt template. Variation 0 is unchanged from the original, and variations 1–14 rephrase the strings within the SystemMessagePromptTemplate and HumanMessagePromptTemplate while keeping the AIMessagePromptTemplate intact.

──────────────────────────── Variation 0 ────────────────────────────
clone_detection_template_contrastive_cot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before answering, work through your reasoning process. For example:
Incorrect reasoning: "Concluding that the snippets are clones based solely on similar formatting."
Correct reasoning: "Comparing both the structural and logical aspects of the snippets to determine functional similarity."
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

──────────────────────────── Variation 1 ────────────────────────────
clone_detection_template_contrastive_cot_variant1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you answer, please detail your reasoning. For instance:
Incorrect logic: "Assuming the snippets are clones merely because their formatting appears similar."
Correct logic: "Examining both the code structure and the logical operations to verify functional similarity."
Decide if these two code snippets are clones.
Respond with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''First Code Snippet:
{code_snippet1}

Second Code Snippet:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 2 ────────────────────────────
clone_detection_template_contrastive_cot_variant2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Prior to answering, describe your reasoning process. For example:
A mistaken approach: "Concluding clones based solely on identical formatting."
A proper approach: "Analyzing both the arrangement and the logic of the snippets to assess their functionality."
Determine if the two code snippets are clones.
Provide your answer as either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Piece 1:
{code_snippet1}

Code Piece 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 3 ────────────────────────────
clone_detection_template_contrastive_cot_variant3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Work out your thought process step by step before responding. For example:
Flawed reasoning: "Determining clones solely from similar visual layout."
Sound reasoning: "Comparing the architecture and logic of the snippets to determine if they function identically."
Decide whether the two code snippets are clones.
Answer with either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Snippet One:
{code_snippet1}

Snippet Two:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 4 ────────────────────────────
clone_detection_template_contrastive_cot_variant4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before giving your answer, explain your reasoning process. For instance:
An erroneous method: "Inferring that snippets are clones based only on similar formatting."
A correct method: "Examining both the structural design and the underlying logic to decide functionality."
Assess if the two code snippets are clones.
Respond with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Block A:
{code_snippet1}

Code Block B:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 5 ────────────────────────────
clone_detection_template_contrastive_cot_variant5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before responding, outline your reasoning path. For example:
Incorrect approach: "Labeling snippets as clones merely due to similar visual styling."
Correct approach: "Comparing both the design structure and functionality of the snippets."
Decide if these provided code snippets are clones.
Answer using ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Snippet 1:
{code_snippet1}

Code Snippet 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 6 ────────────────────────────
clone_detection_template_contrastive_cot_variant6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Think through your reasoning before you answer. For instance:
A wrong assumption might be: "Matching similar formatting implies clones."
A well-founded assumption: "Evaluating both the code’s structure and its operational logic to detect similarity."
Determine whether the two code snippets are clones.
Conclude with either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''First snippet:
{code_snippet1}

Second snippet:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 7 ────────────────────────────
clone_detection_template_contrastive_cot_variant7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you respond, please explain your sequence of reasoning. For example:
An incorrect process: "Assuming clone status solely based on similar formatting."
A correct process: "Inspecting both the logical structure and the coding design to verify clone similarity."
Decide if these code snippets are clones.
Answer with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Snippet Alpha:
{code_snippet1}

Snippet Beta:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 8 ────────────────────────────
clone_detection_template_contrastive_cot_variant8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Elaborate on your chain-of-thought before finalizing your answer. For example:
Avoid the mistake of viewing only superficial formatting as proof of clones. Instead, compare the underlying logic and design.
Decide if the two code snippets are clones.
Respond with either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''View Code:
{code_snippet1}

and

{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 9 ────────────────────────────
clone_detection_template_contrastive_cot_variant9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Prior to finalizing your answer, outline your reasoning. For example:
One might wrongly conclude clones based solely on similar layout, while the correct approach requires analyzing both structure and logic.
Determine if the code snippets are clones.
Answer with either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code sample one:
{code_snippet1}

Code sample two:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 10 ────────────────────────────
clone_detection_template_contrastive_cot_variant10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Work through your reasoning in detail before responding. For example:
A misstep would be: "Assuming clones from identical appearances alone."
A proper analysis involves comparing both the design and the logical flow.
Decide whether the provided snippets are clones.
Answer with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Segment 1:
{code_snippet1}

Segment 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 11 ────────────────────────────
clone_detection_template_contrastive_cot_variant11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before issuing an answer, carefully describe your thought process. For example:
A flawed deduction might be: "Similar formatting automatically means clones."
The proper process involves comparing both the structural and functional elements of the code.
Determine if these snippets are clones.
Respond with ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Block 1:
{code_snippet1}

Block 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 12 ────────────────────────────
clone_detection_template_contrastive_cot_variant12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Before you answer, break down your reasoning step by step. For instance:
An error would be to judge clones solely on formatting similarity. Correct reasoning evaluates both the code’s structure and logic.
Determine whether the two code snippets are clones.
Answer with either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Program Piece 1:
{code_snippet1}

Program Piece 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 13 ────────────────────────────
clone_detection_template_contrastive_cot_variant13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Step through your logical reasoning before answering the query. For example:
One might mistakenly assume clone status based on similar formatting. Instead, analyze both the code's structure and its logic.
Decide whether the snippets are clones.
Answer with either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Snippet Part 1:
{code_snippet1}

Snippet Part 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────── Variation 14 ────────────────────────────
clone_detection_template_contrastive_cot_variant14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Detail your reasoning process methodically before giving your final answer. For example:
Avoid the error of assuming clones based on superficial similarities; instead, compare both the structural framework and the logical basis of the snippets.
Determine if these two snippets are clones.
Provide your answer as either ###TRUE### or ###FALSE###.'''
    ),
    HumanMessagePromptTemplate.from_template(
        '''Code Example 1:
{code_snippet1}

Code Example 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])