Below are 15 complete prompt templates. Variation 0 is exactly the original, and Variations 1–14 include rephrased strings for the SystemMessagePromptTemplate and HumanMessagePromptTemplate. Note that the AIMessagePromptTemplate strings remain unchanged.

────────────────────────────────────────
Variation 0:
────────────────────────────────────────
code_translation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Produce 2 code translation pairs, each in 'Language A' and 'Language B' with a label ###translation a -> b### or ###translation b -> a###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """New code in {source_language}:
{code}

Translate to {target_language}."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 1:
────────────────────────────────────────
code_translation_template_sg_icl_variation_1 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Generate two pairs of code translations in 'Language A' and 'Language B'. Each pair should be marked with either ###translation a -> b### or ###translation b -> a###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Here is the code written in {source_language}:
{code}

Please convert it to {target_language}."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 2:
────────────────────────────────────────
code_translation_template_sg_icl_variation_2 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Create 2 sets of code translation pairs for 'Language A' and 'Language B'. Tag each pair as either ###translation a -> b### or ###translation b -> a###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Given the code in {source_language}:
{code}

Please translate it into {target_language}."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 3:
────────────────────────────────────────
code_translation_template_sg_icl_variation_3 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Craft two translation pairs for code—one in 'Language A' and one in 'Language B'. Use the tags ###translation a -> b### or ###translation b -> a### accordingly."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """A new snippet in {source_language} is provided:
{code}

Convert it into {target_language}."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 4:
────────────────────────────────────────
code_translation_template_sg_icl_variation_4 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Assemble two pairs of code translations for 'Language A' and 'Language B'. Clearly label them with either ###translation a -> b### or ###translation b -> a### to indicate the conversion direction."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """The following code is written in {source_language}:
{code}

Translate it into {target_language}."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 5:
────────────────────────────────────────
code_translation_template_sg_icl_variation_5 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Prepare 2 code translation pairs in 'Language A' and 'Language B', marking each pair with a label of either ###translation a -> b### or ###translation b -> a###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Presented below is code in {source_language}:
{code}

Please produce its translation in {target_language}."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 6:
────────────────────────────────────────
code_translation_template_sg_icl_variation_6 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Develop two pairs of code translations for the languages 'Language A' and 'Language B'. Each pair should be designated with either ###translation a -> b### or ###translation b -> a###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """We have received code in {source_language}:
{code}

Provide the corresponding translation into {target_language}."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 7:
────────────────────────────────────────
code_translation_template_sg_icl_variation_7 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Construct two sets of code translation pairs—one in 'Language A' and one in 'Language B'. Ensure you label them as ###translation a -> b### or ###translation b -> a###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """A fresh code sample in {source_language} is presented:
{code}

Convert it to {target_language}."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 8:
────────────────────────────────────────
code_translation_template_sg_icl_variation_8 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Create a duo of code translation sets: one for 'Language A' and another for 'Language B'. Label each with either ###translation a -> b### or ###translation b -> a###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """The new code snippet is in {source_language}:
{code}

Translate this snippet to {target_language}."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 9:
────────────────────────────────────────
code_translation_template_sg_icl_variation_9 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Develop 2 distinct pairs of code translations, one in 'Language A' and one in 'Language B'. Each should be tagged with either ###translation a -> b### or ###translation b -> a###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Below is a segment of code in {source_language}:
{code}

Please translate it into {target_language}."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 10:
────────────────────────────────────────
code_translation_template_sg_icl_variation_10 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Formulate two code translation pairs: one for 'Language A' and one for 'Language B'. Use the labels ###translation a -> b### or ###translation b -> a### appropriately."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Provided is new code from {source_language}:
{code}

Translate it to {target_language}."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 11:
────────────────────────────────────────
code_translation_template_sg_icl_variation_11 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Compose 2 code conversion pairs for 'Language A' and 'Language B'. Label each conversion with either ###translation a -> b### or ###translation b -> a### to indicate the direction."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Here is updated code written in {source_language}:
{code}

Convert it into {target_language}."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 12:
────────────────────────────────────────
code_translation_template_sg_icl_variation_12 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Outline two paired code translations: one in 'Language A' and another in 'Language B'. Mark them using either ###translation a -> b### or ###translation b -> a###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """New code in {source_language} has been provided:
{code}

Please render it into {target_language}."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 13:
────────────────────────────────────────
code_translation_template_sg_icl_variation_13 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Design two code translation pairs, each featuring code in 'Language A' and 'Language B'. Use the labels ###translation a -> b### or ###translation b -> a### to indicate the conversion."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """The code sample provided is in {source_language}:
{code}

Translate it into {target_language}."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 14:
────────────────────────────────────────
code_translation_template_sg_icl_variation_14 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Generate two sets of code translations, one for 'Language A' and another for 'Language B'. Clearly mark each with either ###translation a -> b### or ###translation b -> a###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """See this code snippet in {source_language}:
{code}

Translate it into {target_language}."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])