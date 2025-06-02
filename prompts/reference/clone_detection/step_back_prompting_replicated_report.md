clone_detection_template_step_back_0 = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''First, please discuss the key criteria or facts you consider
when determining if two code snippets are clones.'''
    ),
    HumanMessagePromptTemplate.from_template("Please explain those general criteria."),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Now, apply these criteria to determine if these two snippets are clones.
Answer ###TRUE### or ###FALSE### only.

Snippet 1:
{code_snippet1}

Snippet 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

clone_detection_template_step_back_1 = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''Initially, please describe the essential factors or evidence you consider important when assessing whether two code fragments are identical.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly outline these overarching criteria."),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Next, use these guidelines to evaluate if the provided code snippets are clones.
Respond with either ###TRUE### or ###FALSE### exclusively.

Snippet 1:
{code_snippet1}

Snippet 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

clone_detection_template_step_back_2 = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''To start, please outline the primary principles or facts you rely on when judging if two code snippets are clones.'''
    ),
    HumanMessagePromptTemplate.from_template("Explain these general principles in detail, please."),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Now, based on those principles, decide if the two snippets presented are indeed clones.
Answer strictly with ###TRUE### or ###FALSE###.

Snippet 1:
{code_snippet1}

Snippet 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

clone_detection_template_step_back_3 = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''First, elaborate on the key factors or details you typically consider when evaluating if two blocks of code are duplicates.'''
    ),
    HumanMessagePromptTemplate.from_template("Please provide an explanation of these core factors."),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Then, apply these factors to the following code snippets to determine if they are clones.
Respond exclusively with either ###TRUE### or ###FALSE###.

Snippet 1:
{code_snippet1}

Snippet 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

clone_detection_template_step_back_4 = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''Begin by detailing the significant criteria or pieces of information you use when identifying cloned code segments.'''
    ),
    HumanMessagePromptTemplate.from_template("Could you explain these significant criteria?"),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Subsequently, utilize these criteria to assess whether the following code snippets are clones.
Answer solely with ###TRUE### or ###FALSE###.

Snippet 1:
{code_snippet1}

Snippet 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

clone_detection_template_step_back_5 = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''Start by describing the most important indicators or facts you consider when evaluating if two pieces of code are clones.'''
    ),
    HumanMessagePromptTemplate.from_template("Please clarify these key indicators."),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Afterwards, apply these indicators to analyze the following snippets and determine if they are clones.
Respond only with either ###TRUE### or ###FALSE###.

Snippet 1:
{code_snippet1}

Snippet 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

clone_detection_template_step_back_6 = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''Initially, detail the main criteria or facts you consider when deciding if two code segments are essentially clones.'''
    ),
    HumanMessagePromptTemplate.from_template("I would appreciate if you explain these main criteria."),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Now, leveraging these criteria, evaluate if these two code segments constitute a clone pair.
Answer only with ###TRUE### or ###FALSE###.

Snippet 1:
{code_snippet1}

Snippet 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

clone_detection_template_step_back_7 = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''Please start by discussing the fundamental criteria or notable facts you refer to when determining if two code snippets are clones.'''
    ),
    HumanMessagePromptTemplate.from_template("Share an explanation of these fundamental criteria, please."),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Then, based on the outlined criteria, determine whether these two code snippets are clones.
Answer solely with either ###TRUE### or ###FALSE###.

Snippet 1:
{code_snippet1}

Snippet 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

clone_detection_template_step_back_8 = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''First, identify the core principles or specific details you find crucial in assessing whether two code snippets are duplicates.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly elucidate these core principles."),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Next, use these principles to evaluate if the following snippets are clones.
Provide your response exclusively as ###TRUE### or ###FALSE###.

Snippet 1:
{code_snippet1}

Snippet 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

clone_detection_template_step_back_9 = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''To begin with, please elaborate on the critical criteria or pieces of understanding that inform your judgment on whether two code fragments are clones.'''
    ),
    HumanMessagePromptTemplate.from_template("Please articulate these overarching criteria."),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Subsequently, employ these insights to judge if the two code samples are clones.
Answer only with ###TRUE### or ###FALSE###.

Snippet 1:
{code_snippet1}

Snippet 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

clone_detection_template_step_back_10 = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''First off, please detail the primary indicators or facts you consider when judging if two code snippets are duplicates.'''
    ),
    HumanMessagePromptTemplate.from_template("Could you please elaborate on these primary indicators?"),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Then, apply these indicators to evaluate the code snippets provided and decide if they are clones.
Answer only with either ###TRUE### or ###FALSE###.

Snippet 1:
{code_snippet1}

Snippet 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

clone_detection_template_step_back_11 = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''As a starting point, please discuss the main principles or notable facts you use in discerning if two pieces of code are equivalent clones.'''
    ),
    HumanMessagePromptTemplate.from_template("Please explain these main principles in detail."),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''After that, make use of these principles to assess if the provided snippets are clones.
Respond strictly with ###TRUE### or ###FALSE###.

Snippet 1:
{code_snippet1}

Snippet 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

clone_detection_template_step_back_12 = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''To start with, please talk through the essential criteria or evidence you rely on when determining if two code blocks are identical clones.'''
    ),
    HumanMessagePromptTemplate.from_template("Please expound on these essential criteria."),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Now, using these criteria, decide whether these two snippets are clones.
Answer only with either ###TRUE### or ###FALSE###.

Snippet 1:
{code_snippet1}

Snippet 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

clone_detection_template_step_back_13 = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''Begin by outlining the major guidelines or facts that influence your decision when checking if two code snippets are clones.'''
    ),
    HumanMessagePromptTemplate.from_template("Could you clarify these major guidelines?"),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Subsequently, apply these guidelines to decide if the given code snippets are clones.
Your response should be confined to ###TRUE### or ###FALSE###.

Snippet 1:
{code_snippet1}

Snippet 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])

clone_detection_template_step_back_14 = ChatPromptTemplate.from_messages([
    # Phase One: Outline General Principles
    SystemMessagePromptTemplate.from_template(
        '''Firstly, please share the key elements or facts you consider significant when evaluating if two code fragments are clones.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly describe these key elements."),
    AIMessagePromptTemplate.from_template('prompt'),

    # Phase Two: Apply Principles to Specific Task
    HumanMessagePromptTemplate.from_template(
        '''Then, utilize these elements to assess whether the following snippets are clones.
Respond exclusively with ###TRUE### or ###FALSE###.

Snippet 1:
{code_snippet1}

Snippet 2:
{code_snippet2}'''
    ),
    AIMessagePromptTemplate.from_template('prompt'),
])