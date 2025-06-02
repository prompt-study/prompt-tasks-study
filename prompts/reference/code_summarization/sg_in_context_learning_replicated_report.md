Below are 15 versions of the prompt template. Variation 0 is exactly the original you provided, and Variations 1–14 use rephrased strings for the System and Human messages. Note that the AI messages remain unchanged.

────────────────────────────────────────
Variation 0
────────────────────────────────────────
code_summarization_template_sg_icl = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Produce 2 examples of 'code' and 'summary' labeled ###summary###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Code:
{code}

Summarize it in one sentence, using your examples as reference."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 1
────────────────────────────────────────
code_summarization_template_sg_icl = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Provide two illustrations with labels 'code' and 'summary' marked as ###summary###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Here is the code snippet: {code}

Write a one-sentence summary, referring to your illustrations as guidance."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 2
────────────────────────────────────────
code_summarization_template_sg_icl = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Create a pair of examples, one for 'code' and another for 'summary', tagged with ###summary###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Presented code: {code}

Offer a concise, one-sentence description, using provided examples as a model."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 3
────────────────────────────────────────
code_summarization_template_sg_icl = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Generate two examples, one labeled 'code' and the other 'summary', all marked with ###summary###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Given the following code: {code}

Formulate a brief summary in one sentence, inspired by your examples."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 4
────────────────────────────────────────
code_summarization_template_sg_icl = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Draft two sample entries: one for 'code' and one for 'summary', demarcated with ###summary###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Code snippet: {code}

Summarize the code in one sentence, considering the sample entries provided."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 5
────────────────────────────────────────
code_summarization_template_sg_icl = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Output two sample cases: one classed as 'code' and another as 'summary', both tagged with ###summary###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Code provided: {code}

Craft a one-sentence summary based on the sample cases."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 6
────────────────────────────────────────
code_summarization_template_sg_icl = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Assembly two instance examples with labels 'code' and 'summary', annotated with ###summary###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Input code: {code}

Deliver a one-sentence overview, referencing your provided instances."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 7
────────────────────────────────────────
code_summarization_template_sg_icl = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Offer two distinct examples, labeled 'code' and 'summary', identifiable with ###summary###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Here is the code: {code}

Compose a succinct one-sentence summary modeled on the examples above."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 8
────────────────────────────────────────
code_summarization_template_sg_icl = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Present two example pairs, one marked as 'code' and the other as 'summary', denoted by ###summary###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """See the code: {code}

Provide a concise one-sentence summary that aligns with your examples."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 9
────────────────────────────────────────
code_summarization_template_sg_icl = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Deliver a duo of examples, one for 'code' and one for 'summary', all identified with ###summary### markers."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Your code: {code}

Summarize it briefly in a single sentence, mirroring the structure of your examples."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 10
────────────────────────────────────────
code_summarization_template_sg_icl = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Construct two sample outputs: one for 'code' and another for 'summary', both indicated with ###summary###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """The code is as follows: {code}

Generate a one-sentence summary, using your examples as a reference point."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 11
────────────────────────────────────────
code_summarization_template_sg_icl = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Develop two illustrative examples: one tagged as 'code' and the other as 'summary', highlighted by ###summary###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Code snippet: {code}

Offer a one-sentence summary, referring back to the illustrative examples."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 12
────────────────────────────────────────
code_summarization_template_sg_icl = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Compose two demonstration examples, one labeled 'code' and the other 'summary', marked with ###summary###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Provided code: {code}

Write a single-sentence summary, using the demonstration examples as inspiration."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 13
────────────────────────────────────────
code_summarization_template_sg_icl = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Formulate two example entries: one for 'code' and one for 'summary', designated with ###summary###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Code block: {code}

Summarize in one sentence, drawing from your provided entries for guidance."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 14
────────────────────────────────────────
code_summarization_template_sg_icl = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Offer a pair of illustrative examples, featuring one 'code' and one 'summary', each marked with ###summary###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Inserted code: {code}

Create a concise one-sentence summary, guided by your illustrative examples."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
