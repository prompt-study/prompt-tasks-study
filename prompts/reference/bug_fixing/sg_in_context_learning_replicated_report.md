
# Variation 0 (Original)
bug_fixing_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Produce 2 examples of 'Buggy Code' and 'Fixed Code' labeled ###fix### or ###bug###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """New code:
{code}

Provide a fixed version, using your examples as reference."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
------------------------------------------------------------
# Variation 1
bug_fixing_template_sg_icl_v1 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Generate two instances showcasing 'Defective Code' paired with 'Corrected Code', labeled as ###bug### or ###fix###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Updated code segment:
{code}

Using your earlier examples as guidelines, deliver an improved version."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
------------------------------------------------------------
# Variation 2
bug_fixing_template_sg_icl_v2 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Create a duo of examples featuring 'Erroneous Code' and its 'Repaired Code' counterparts, annotated with ###bug### or ###fix### labels."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Fresh code:
{code}

Offer a corrected iteration modeled after your prior examples."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
------------------------------------------------------------
# Variation 3
bug_fixing_template_sg_icl_v3 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Develop two sample demonstrations with 'Faulty Code' alongside 'Fixed Code', each tagged with either ###bug### or ###fix###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Present code:
{code}

Please provide a revised version referring to the examples you've generated."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
------------------------------------------------------------
# Variation 4
bug_fixing_template_sg_icl_v4 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Craft a pair of examples depicting 'Problematic Code' matched with 'Clean Code', marked respectively with ###bug### or ###fix###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Input code:
{code}

Deliver a corrected variant inspired by your sample cases."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
------------------------------------------------------------
# Variation 5
bug_fixing_template_sg_icl_v5 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Compose two illustrative cases of code errors ('Buggy Code') and their fixes ('Fixed Code'), identified by ###bug### and ###fix###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Enter new code:
{code}

Submit a refined version that aligns with your provided examples."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
------------------------------------------------------------
# Variation 6
bug_fixing_template_sg_icl_v6 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Assemble two demonstrations: one with malfunctioning code and one with its corrected version, using labels ###bug### and ###fix### respectively."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Submitted code:
{code}

Using your sample examples as guidance, provide the corrected code."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
------------------------------------------------------------
# Variation 7
bug_fixing_template_sg_icl_v7 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Draft two scenarios showcasing 'Erroneous Code' versus 'Repaired Code', with annotations ###bug### or ###fix###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Insert your code:
{code}

Generate a fixed rendition drawing from your earlier examples."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
------------------------------------------------------------
# Variation 8
bug_fixing_template_sg_icl_v8 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Outline two examples presenting 'Glitchy Code' and its improved 'Fixed Code', labeled alternatively as ###bug### or ###fix###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """New code snippet:
{code}

Based on your examples, deliver a version with fixes applied."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
------------------------------------------------------------
# Variation 9
bug_fixing_template_sg_icl_v9 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Formulate two cases featuring 'Incorrect Code' and 'Updated Code' with the labels ###bug### and ###fix###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Provided code:
{code}

Revise it to a correct version guided by your examples."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
------------------------------------------------------------
# Variation 10
bug_fixing_template_sg_icl_v10 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Generate two paired examples: one demonstrating flawed code and another showing its correction, marked with ###bug### or ###fix###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Your code:
{code}

Using your example pairs, craft a corrected version."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
------------------------------------------------------------
# Variation 11
bug_fixing_template_sg_icl_v11 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Assemble a pair of instances: one with problematic code and one with a remedied solution, identified by ###bug### or ###fix###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Code snippet:
{code}

Please output a revised version, following your example references."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
------------------------------------------------------------
# Variation 12
bug_fixing_template_sg_icl_v12 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Provide two contrasting examples of flawed code and its subsequent repair, using the tags ###bug### for issues and ###fix### for solutions."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Input new code here:
{code}

Construct a fixed version that mirrors the example pairs you've created."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
------------------------------------------------------------
# Variation 13
bug_fixing_template_sg_icl_v13 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Offer a pair of examples featuring 'Defective Code' and the corresponding 'Repaired Code', tagged with ###bug### or ###fix### as appropriate."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Supplied code:
{code}

Utilize your example cases to propose a corrected version."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
------------------------------------------------------------
# Variation 14
bug_fixing_template_sg_icl_v14 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Generate two illustrative pairs: one showing erroneous code and the other its fixed counterpart, clearly marked with ###bug### and ###fix###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Enter code snippet:
{code}

Using the provided examples as a guide, produce an updated, fixed version."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

