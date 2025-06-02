Below are 15 prompt template definitions. Variation 0 is exactly as originally provided. In each of the other variations only the strings inside the SystemMessagePromptTemplate and HumanMessagePromptTemplate have been rephrased (the AIMessagePromptTemplate strings remain unchanged). Note that the variable names now include a suffix to denote the variant, while keeping the original variable name intact for variation 0.

────────────────────────────────────────
Variation 0 (Original):
────────────────────────────────────────
defect_detection_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Produce 2 examples of code snippets with labels ###TRUE### if they have a defect, ###FALSE### if not."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """New code snippet:
{code}

Decide ###TRUE### if defective, or ###FALSE### if not."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 1:
────────────────────────────────────────
defect_detection_template_sg_icl_var1 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Generate two instances of code examples, marking them with ###TRUE### if they include a defect, or with ###FALSE### if they are flaw-free."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Code snippet provided below:
{code}

Select ###TRUE### when the code is defective, otherwise choose ###FALSE###."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 2:
────────────────────────────────────────
defect_detection_template_sg_icl_var2 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Create 2 sample code examples and tag them as ###TRUE### in case they contain an error, or as ###FALSE### if they don't."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Here is a new code snippet for review:
{code}

Conclude by deciding if it is ###TRUE### (contains defects) or ###FALSE###."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 3:
────────────────────────────────────────
defect_detection_template_sg_icl_var3 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Provide a pair of code snippet examples, labeling each with ###TRUE### if a defect is present or with ###FALSE### if it is absent."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Review the following code snippet:
{code}

Determine whether it should be marked as ###TRUE### (defective) or ###FALSE### (non-defective)."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 4:
────────────────────────────────────────
defect_detection_template_sg_icl_var4 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Offer 2 illustration code samples. Apply the label ###TRUE### for faulty examples and ###FALSE### otherwise."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Review this newly provided code chunk:
{code}

Assess and indicate if it's defective with ###TRUE###, otherwise ###FALSE###."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 5:
────────────────────────────────────────
defect_detection_template_sg_icl_var5 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Construct two example code snippets. Label as ###TRUE### if a defect exists, and as ###FALSE### if not."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Review the following newly submitted code snippet:
{code}

Decide if it should be flagged ###TRUE### (defective) or ###FALSE### (not defective)."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 6:
────────────────────────────────────────
defect_detection_template_sg_icl_var6 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Devise a set of 2 example snippets, tagging them with ###TRUE### for detected defects and ###FALSE### if they are error-free."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """A new code snippet is presented:
{code}

Please determine whether it contains defects by marking ###TRUE###, or if it is clean, mark ###FALSE###."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 7:
────────────────────────────────────────
defect_detection_template_sg_icl_var7 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Generate two code examples. Tag snippets with ###TRUE### when a defect is identified, and with ###FALSE### if otherwise."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """For the following code snippet:
{code}

Indicate whether it is defective by choosing ###TRUE###, or mark it as defect-free with ###FALSE###."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 8:
────────────────────────────────────────
defect_detection_template_sg_icl_var8 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Create two code sample illustrations, marking them with ###TRUE### if a defect is found, and with ###FALSE### if not."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Here is a fresh code snippet:
{code}

Decide if the snippet is flawed (###TRUE###) or free of defects (###FALSE###)."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 9:
────────────────────────────────────────
defect_detection_template_sg_icl_var9 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Develop 2 example code segments; tag them with ###TRUE### for instances with a defect, and with ###FALSE### when there is none."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Examine this new code snippet:
{code}

Choose ###TRUE### if the code is flawed, or ###FALSE### if it is clear."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 10:
────────────────────────────────────────
defect_detection_template_sg_icl_var10 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Construct two instances of code samples, marking each as ###TRUE### if it possesses defects, otherwise label as ###FALSE###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Review this new code snippet:
{code}

Determine whether the code is defective (###TRUE###) or not (###FALSE###)."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 11:
────────────────────────────────────────
defect_detection_template_sg_icl_var11 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Prepare 2 code snippet examples that are labeled with ###TRUE### if any defect exists, else mark with ###FALSE###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """New code snippet provided:
{code}

Assess and indicate if it has defects by marking ###TRUE###, or label it as ###FALSE### if clean."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 12:
────────────────────────────────────────
defect_detection_template_sg_icl_var12 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Offer two code examples. Annotate each as ###TRUE### if it includes a defect, or as ###FALSE### if it's correct."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Consider the following code snippet:
{code}

Mark it as ###TRUE### upon detecting a defect, or as ###FALSE### if no defect is found."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 13:
────────────────────────────────────────
defect_detection_template_sg_icl_var13 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Supply 2 code snippet examples; flag as ###TRUE### if a defect is present and as ###FALSE### if absent."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Incoming code snippet:
{code}
Decide on whether the code is defective (###TRUE###) or non-defective (###FALSE###)."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

────────────────────────────────────────
Variation 14:
────────────────────────────────────────
defect_detection_template_sg_icl_var14 = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Draft two code snippet examples, categorizing them as ###TRUE### for defected code, and as ###FALSE### otherwise."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Review the newly inserted code snippet below:
{code}

Determine if the snippet is flawed by selecting ###TRUE###, or not flawed by selecting ###FALSE###."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])
