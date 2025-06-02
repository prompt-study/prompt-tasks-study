Below you will find 15 prompt templates. Variation 0 is exactly the original template you provided, and variations 1–14 contain rephrased versions for the SystemMessagePromptTemplate and HumanMessagePromptTemplate strings. The AIMessagePromptTemplate strings remain unchanged.

------------------------------------------------------------
Variation 0 (original):

code_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Produce 2 examples where a programming task is described, followed by correctly generated code that solves it. "
        "Label the task description as ###task### and the generated code as ###generated###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Task:
{task_description}

Write a correct implementation to solve this task, using your examples as reference."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

------------------------------------------------------------
Variation 1:

code_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Write 2 illustrative examples where you first describe a programming challenge, then provide accurate code that solves it. "
        "Mark the challenge description with ###task### and the solution code with ###generated###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Challenge:
{task_description}

Develop a valid implementation to resolve this challenge, using the given examples as guidance."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

------------------------------------------------------------
Variation 2:

code_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Develop 2 examples where a programming problem is presented, followed by the correct code that addresses it. "
        "Use ###task### to indicate the problem description and ###generated### for the produced code."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Problem:
{task_description}

Provide a proper code solution for this problem, referring to your examples as a model."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

------------------------------------------------------------
Variation 3:

code_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Formulate 2 examples in which a programming task is explained, then show the corresponding working code that solves it. "
        "Label the explanation as ###task### and the working code as ###generated###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Task Description:
{task_description}

Write a working implementation that solves this task, using the provided examples as a reference."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

------------------------------------------------------------
Variation 4:

code_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Generate 2 examples where each starts with a description of a programming assignment followed by the exact code that solves it. "
        "Designate the assignment description with ###task### and the solution code with ###generated###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Assignment:
{task_description}

Craft a correct code implementation to address this assignment, using your examples for reference."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

------------------------------------------------------------
Variation 5:

code_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Provide 2 samples where a programming task is laid out, followed by the proper code that effectively solves it. "
        "Mark the task portion as ###task### and the solution portion as ###generated###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Task Statement:
{task_description}

Implement a correct solution to this task, drawing on your earlier examples."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

------------------------------------------------------------
Variation 6:

code_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Compose 2 examples that begin with a description of a programming task, followed by the correct code necessary to solve it. "
        "Identify the task description with ###task### and the resulting code with ###generated###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Programming Task:
{task_description}

Write a reliable implementation to solve this programming task, using the earlier examples as a guide."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

------------------------------------------------------------
Variation 7:

code_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Create 2 examples wherein you detail a programming task followed by the correct code snippet that resolves it. "
        "Use ###task### to denote the task details and ###generated### to denote the code response."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Programming Assignment:
{task_description}

Develop a correct code solution to address the assignment, based on the provided examples."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

------------------------------------------------------------
Variation 8:

code_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Prepare 2 examples where a programming task is described and immediately followed by valid code that solves it. "
        "Use the label ###task### for the description and ###generated### for the corresponding code."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Task Details:
{task_description}

Construct a functioning implementation to solve this task, referring to your examples for direction."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

------------------------------------------------------------
Variation 9:

code_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Design 2 examples where you first describe a programming task and then provide the correct and functional code that solves it. "
        "Clearly tag the task description with ###task### and the solution code with ###generated###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Task:
{task_description}

Develop a correct implementation to solve the task, using the example pair as a reference."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

------------------------------------------------------------
Variation 10:

code_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Craft 2 examples that first provide a description of a programming problem, followed by the exact code needed to solve it. "
        "Annotate the description with ###task### and the solution code with ###generated###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Problem Statement:
{task_description}

Write a correct code solution based on the provided examples."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

------------------------------------------------------------
Variation 11:

code_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Generate 2 samples where you first outline a programming task and then supply the exact code that resolves it. "
        "Label the task section as ###task### and the produced code as ###generated###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Task Overview:
{task_description}

Implement an accurate solution for this task, using the provided examples as a model."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

------------------------------------------------------------
Variation 12:

code_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Draft 2 examples that contain a programming task description along with the proper code to solve it. "
        "Mark the description with ###task### and the solution code with ###generated###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Task Description:
{task_description}

Write a correct implementation to address this task, referring to the examples provided."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

------------------------------------------------------------
Variation 13:

code_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Prepare 2 examples in which a programming task is explained and then solved with fully functional code. "
        "Indicate the task explanation with ###task### and the solution code with ###generated###."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Task Description:
{task_description}

Develop a valid coding solution based on the provided examples."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

------------------------------------------------------------
Variation 14:

code_generation_template_sg_icl = ChatPromptTemplate.from_messages([
    # Self-Generation Step
    SystemMessagePromptTemplate.from_template(
        "Construct 2 examples where you initially present a programming task and then deliver the corresponding code that solves it correctly. "
        "Use the labels ###task### for the task description and ###generated### for the code."
    ),
    AIMessagePromptTemplate.from_template("prompt"),

    # Inference Step
    HumanMessagePromptTemplate.from_template(
        """Task Brief:
{task_description}

Write an implementation that correctly solves the task, referring to the examples as guidance."""
    ),
    AIMessagePromptTemplate.from_template("prompt"),
])

------------------------------------------------------------

Each template uses the same underlying structure as your provided prompt technique, with the System and Human messages rephrased while keeping the AI messages unaltered.