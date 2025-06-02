Below are 15 complete variations of the chat prompt template. In each case only the strings in the SystemMessagePromptTemplate and HumanMessagePromptTemplate have been rephrased. Variation 0 is exactly the same as the original.

────────────────────────
Variation 0:
────────────────────────

code_question_answering_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Produce 2 examples of a 'Question' and 'Code' with label ###TRUE### if the code fully answers the question, ###FALSE### if not."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Question:
{question}

Code:
{code}

Decide ###TRUE### if the code fully answers the question, otherwise ###FALSE###. Refer to your examples."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────
Variation 1:
────────────────────────

code_question_answering_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Generate 2 illustrative pairs, each containing a 'Question' and its 'Code'. Use ###TRUE### if the code completely satisfies the question, and ###FALSE### if it does not."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Question:
{question}

Code:
{code}

Assess and decide: choose ###TRUE### if the code fully addresses the question, otherwise choose ###FALSE###. Use your examples as guidance."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────
Variation 2:
────────────────────────

code_question_answering_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Create 2 sample pairs composed of a 'Question' and a 'Code'. Label them with ###TRUE### when the code completely resolves the question, and with ###FALSE### if it falls short."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Question:
{question}

Code:
{code}

Determine whether to mark ###TRUE### if the code completely answers the question, or mark ###FALSE### if it does not. Refer to the provided examples."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────
Variation 3:
────────────────────────

code_question_answering_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Produce 2 demonstration examples, each with a 'Question' and its corresponding 'Code'. Annotate with ###TRUE### when the code is a complete solution, otherwise annotate with ###FALSE###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Question:
{question}

Code:
{code}

Decide by selecting ###TRUE### if the code fully answers the question, else select ###FALSE###. Use your examples for reference."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────
Variation 4:
────────────────────────

code_question_answering_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Draft 2 sample pairs, where each pair comprises a 'Question' and a 'Code'. Mark the pair with ###TRUE### if the code entirely responds to the question, or with ###FALSE### if it does not."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Question:
{question}

Code:
{code}

Determine: if the code completely addresses the question, label it as ###TRUE###; otherwise, label as ###FALSE###. Refer to your sample pairs."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────
Variation 5:
────────────────────────

code_question_answering_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Formulate 2 example pairs consisting of a 'Question' and a 'Code'. Tag them with ###TRUE### if the code fully answers the question, or with ###FALSE### if it does not."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Question:
{question}

Code:
{code}

Choose ###TRUE### if the code completely handles the question; otherwise, select ###FALSE###. Refer back to your examples."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────
Variation 6:
────────────────────────

code_question_answering_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Craft 2 examples, each pairing a 'Question' with its 'Code'. Use the label ###TRUE### when the code provides a full answer, and ###FALSE### when it does not."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Question:
{question}

Code:
{code}

Decide by marking ###TRUE### if the code fully resolves the written question, otherwise mark ###FALSE###. See your examples for guidance."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────
Variation 7:
────────────────────────

code_question_answering_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Assemble 2 example pairs featuring a 'Question' and its associated 'Code'. Indicate with ###TRUE### if the code completely answers the question, or with ###FALSE### if it does not."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Question:
{question}

Code:
{code}

Select ###TRUE### if the provided code fully answers the question; otherwise, choose ###FALSE###. Refer to your sample pairs for context."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────
Variation 8:
────────────────────────

code_question_answering_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Generate 2 illustrative examples that include a 'Question' and its corresponding 'Code'. Mark with ###TRUE### when the code wholly solves the question, or with ###FALSE### when it does not."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Question:
{question}

Code:
{code}

Determine whether the answer is complete by choosing ###TRUE### if the code fully addresses the question, else select ###FALSE###. Refer to your examples."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────
Variation 9:
────────────────────────

code_question_answering_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Construct 2 example sets, each consisting of a 'Question' and 'Code'. Label them with ###TRUE### if the code completely answers the question, or with ###FALSE### if it does not."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Question:
{question}

Code:
{code}

Choose ###TRUE### if the code fully meets the question's demands; otherwise, pick ###FALSE###. Refer to your provided examples."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────
Variation 10:
────────────────────────

code_question_answering_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Devise 2 example pairs with a 'Question' and its 'Code'. Use the notation ###TRUE### if the code completely answers the question and ###FALSE### if it does not."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Question:
{question}

Code:
{code}

Evaluate if the code fully addresses the question by marking ###TRUE###; if it does not, mark ###FALSE###. Use your example pairs for guidance."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────
Variation 11:
────────────────────────

code_question_answering_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Concoct 2 examples, each pairing a 'Question' with its corresponding 'Code'. Indicate with ###TRUE### when the code offers a complete answer to the question, or with ###FALSE### if it does not."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Question:
{question}

Code:
{code}

Decide: if the code fully resolves the question, annotate it as ###TRUE###; otherwise, annotate it as ###FALSE###. Refer to your previously generated examples."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────
Variation 12:
────────────────────────

code_question_answering_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Develop 2 sample pairs, each containing a 'Question' and an associated 'Code'. Designate them with ###TRUE### when the code completely meets the question, and with ###FALSE### when it doesn’t."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Question:
{question}

Code:
{code}

Decide on ###TRUE### if the code provides a full answer to the question, otherwise choose ###FALSE###. Check your sample pairs for reference."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────
Variation 13:
────────────────────────

code_question_answering_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Present 2 sample pairs that each include a 'Question' and its matching 'Code'. Tag these pairs with ###TRUE### if the code completely resolves the question, or with ###FALSE### if it does not."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Question:
{question}

Code:
{code}

Conclude by selecting ###TRUE### if the code entirely answers the question; otherwise, select ###FALSE###. Refer to your earlier examples."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────
Variation 14:
────────────────────────

code_question_answering_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Offer 2 illustrative pairs consisting of a 'Question' and its 'Code'. Label them as ###TRUE### if the code completely answers the question, and as ###FALSE### if it does not."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Question:
{question}

Code:
{code}

Decide on the appropriate label: choose ###TRUE### if the code fully addresses the question, otherwise choose ###FALSE###. Refer to your illustrative examples."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
