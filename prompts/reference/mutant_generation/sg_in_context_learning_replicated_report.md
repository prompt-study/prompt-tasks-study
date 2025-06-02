Below are 15 full prompt‐template definitions. In each one the strings inside SystemMessagePromptTemplate and HumanMessagePromptTemplate have been reworded (while the two AIMessagePromptTemplates remain exactly the same). Variation 0 is simply the original template you provided.

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Variation 0 (Original)
mutant_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Produce 2 examples of code 'Original' and 'Mutant' labeled ###mutant### or ###original###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Original code:
{code}

Generate a mutant version, using your examples as reference."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Variation 1
mutant_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Create two code samples—one as 'Original' and another as 'Mutant'—using the markers ###original### and ###mutant### respectively."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Here is the original code:
{code}

Using the provided examples as guidance, produce a mutated version."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Variation 2
mutant_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Construct a pair of code examples labeled 'Original' and 'Mutant'—with ###original### for the original one and ###mutant### for the mutant."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Original snippet:
{code}

Please formulate a mutant variant by drawing on your sample cases."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Variation 3
mutant_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Provide two code illustrations, one denoted as 'Original' and the other as 'Mutant', marked with ###original### and ###mutant### accordingly."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """The provided code is:
{code}

Develop a mutant version, using your earlier examples as a reference."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Variation 4
mutant_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Offer two coding examples—label one 'Original' and the other 'Mutant'—using the tags ###original### and ###mutant### respectively."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Here is the submitted code:
{code}

Kindly generate a mutant version using your provided examples as a basis."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Variation 5
mutant_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Generate a duo of code examples labeled 'Original' and 'Mutant', denoting them with ###original### and ###mutant###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Original code block:
{code}

Now, produce a mutant variant inspired by the example pair."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Variation 6
mutant_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Deliver two code instances categorized as 'Original' and 'Mutant' with indicators ###original### and ###mutant### respectively."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """The original snippet is as follows:
{code}

Generate a mutant version by referring back to your earlier examples."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Variation 7
mutant_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Create two examples of code: one marked 'Original' and one marked 'Mutant'. Use ###original### for the original and ###mutant### for the mutant."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Given the original code:
{code}

Please produce a mutant version, keeping your prior examples in mind."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Variation 8
mutant_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Develop a pair of code samples where one is 'Original' and the other is 'Mutant', marked clearly with ###original### and ###mutant###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Below is the original code:
{code}

Using your reference examples, create a mutant adaptation."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Variation 9
mutant_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Compose two code examples: one flagged as 'Original' and one as 'Mutant'. Use the tags ###original### and ###mutant### to denote them."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Starting with the original code:
{code}

Construct a mutant version based on your example pair."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Variation 10
mutant_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Generate a dual set of code illustrations labeled as 'Original' and 'Mutant' by using the markers ###original### and ###mutant###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Original code extract:
{code}

Please produce a mutant version that reflects the style of your provided examples."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Variation 11
mutant_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Present a pair of code samples—one 'Original' and one 'Mutant'—using the labels ###original### and ###mutant###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """The provided code is:
{code}

Generate a corresponding mutant version using your earlier examples as a guide."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Variation 12
mutant_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Offer two code instances: one entitled 'Original' and the other 'Mutant'; label them using ###original### and ###mutant###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Here is the original code snippet:
{code}

Now, please craft a mutant variant by referring to your example models."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Variation 13
mutant_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Produce a set of two code samples, one marked as 'Original' and the other as 'Mutant', using the designations ###original### and ###mutant###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Original code provided:
{code}

Now generate a mutant version utilizing the previously shown examples."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Variation 14
mutant_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Craft two sample codes: one identified as 'Original' and the other as 'Mutant', with the tags ###original### and ###mutant### to differentiate them."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Below is the original code:
{code}

Using your reference examples, create an appropriate mutant version."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

Each variation preserves the prompt technique while rewording only the specified template strings.