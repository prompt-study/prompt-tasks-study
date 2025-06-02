
code_generation_template_step_back = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''Please explain the general strategy for generating code from a task description
(e.g., plan structure, decide on data structures, etc.).'''
    ),
    HumanMessagePromptTemplate.from_template("Describe that strategy."),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Now generate code for the following task, applying your approach.
Provide only the code.

Task Description:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

code_generation_template_step_back = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''Provide an overview of your method for converting a task description into code
(for example, by mapping out the structure and selecting appropriate data structures).'''
    ),
    HumanMessagePromptTemplate.from_template("Please detail your methodology."),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Now, using your method, create code for the task described below.
Return only the code.

Task Description:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

code_generation_template_step_back = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''Outline your overall approach for transforming a task description into code,
such as how you organize the program and select data handling structures.'''
    ),
    HumanMessagePromptTemplate.from_template("Explain your overall approach."),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Apply this approach to generate code for the following task.
Output solely the code.

Task Description:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

code_generation_template_step_back = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''Describe your general plan for turning a task description into functioning code,
including aspects like outlining the program’s design and choosing data structures.'''
    ),
    HumanMessagePromptTemplate.from_template("Share your plan in detail."),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Using your plan, produce code for the task outlined below.
Only include the final code.

Task Description:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

code_generation_template_step_back = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''Summarize the key concepts you use to derive code from a task description,
covering elements like structural planning and data structure selection.'''
    ),
    HumanMessagePromptTemplate.from_template("Articulate your key concepts."),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Now, leveraging your explained concepts, generate the corresponding code for the task below.
Provide only the code snippet.

Task Description:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

code_generation_template_step_back = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''Explain the primary strategy you follow to develop code from a task description,
including considerations like program layout and appropriate data structures.'''
    ),
    HumanMessagePromptTemplate.from_template("Clarify your primary strategy."),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Using the outlined strategy, write the code for the following task.
Return only the code output.

Task Description:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

code_generation_template_step_back = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''Detail the method you use for generating code from a given task description,
touching on how you design the structure and decide on data storage methods.'''
    ),
    HumanMessagePromptTemplate.from_template("Detail your method."),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Then, apply your method to write code for the task specified below.
Please include only the code in your response.

Task Description:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

code_generation_template_step_back = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''Present the overall approach you take to convert a task description into code,
including planning the structure and selecting the appropriate data types.'''
    ),
    HumanMessagePromptTemplate.from_template("Outline your overall approach."),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Now, put your approach into action by generating code for the task detailed below.
Respond with just the code.

Task Description:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

code_generation_template_step_back = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''Elucidate your overall technique for deriving code from a provided task description,
touching on design blueprint and the choice of data structures, for example.'''
    ),
    HumanMessagePromptTemplate.from_template("Expound on your overall technique."),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Now, using your detailed technique, produce the code corresponding to the task below.
Return only the code.

Task Description:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

code_generation_template_step_back = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''Clarify the systematic approach you use to generate code from a task description,
for instance by planning the program’s framework and selecting data structures.'''
    ),
    HumanMessagePromptTemplate.from_template("Please clarify your systematic approach."),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Apply this systematic approach to create code for the task outlined below.
Include only the code in your answer.

Task Description:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

code_generation_template_step_back = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''Describe the process you follow to convert a task description into code,
covering aspects like structural planning and the selection of data organization methods.'''
    ),
    HumanMessagePromptTemplate.from_template("Describe your process in detail."),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Using the process described above, generate the appropriate code for the task below.
Return nothing but the code.

Task Description:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

code_generation_template_step_back = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''Summarize the methodology you adopt to produce code from a given task description,
including how you plan the code's organization and pick data structures.'''
    ),
    HumanMessagePromptTemplate.from_template("Summarize your methodology."),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Now, with your methodology in mind, generate code for the task described below.
Provide only the code response.

Task Description:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

code_generation_template_step_back = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''Explain the approach you typically use to turn a task description into executable code,
highlighting your planning of the overall structure and data management techniques.'''
    ),
    HumanMessagePromptTemplate.from_template("Explain your approach."),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Now, using your explained approach, write code for the task provided below.
Return exclusively the code.

Task Description:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

code_generation_template_step_back = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''Lay out the overall strategy you use for deriving code from a task description,
which might include planning the layout of the code and choosing fitting data structures.'''
    ),
    HumanMessagePromptTemplate.from_template("Lay out your overall strategy."),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Using the stated strategy, craft code for the task described below.
Please provide only the code.

Task Description:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

code_generation_template_step_back = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''Provide a detailed explanation of your approach to generating code from a task description,
including steps like organizing the code’s structure and determining suitable data structures.'''
    ),
    HumanMessagePromptTemplate.from_template("Detail your approach."),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Now, utilizing your detailed approach, generate code for the task presented below.
Return only the code in your response.

Task Description:
{task_description}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

