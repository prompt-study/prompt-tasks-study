Below are 15 variations of the prompt template. Variation 0 is exactly the original, and variations 1–14 contain reworded versions of the strings in the SystemMessagePromptTemplate and HumanMessagePromptTemplate. The AIMessagePromptTemplate remains unchanged in each case.

--------------------------------------------------

Variation 0:
code_translation_template_rar_v2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Translate the following code from {source_language} to {target_language}. Provide the translated code only.
Reword the request with more detail, then give the translation.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------

Variation 1:
code_translation_template_rar_v2_variant1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Please convert the code provided from {source_language} to {target_language}. Output only the final converted code.
Begin by expressing the request in more detailed terms, then present the translation.'''
    ),
    HumanMessagePromptTemplate.from_template("Code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------

Variation 2:
code_translation_template_rar_v2_variant2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Reformat the following program by translating it from {source_language} to {target_language}. Return solely the translated version.
Start with an expanded explanation of the request, then supply the conversion.'''
    ),
    HumanMessagePromptTemplate.from_template("Please find the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------

Variation 3:
code_translation_template_rar_v2_variant3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Transform the provided code from {source_language} to {target_language}. Deliver only the final translated code.
First, restate the instruction with additional details, then include the translation.'''
    ),
    HumanMessagePromptTemplate.from_template("The code to translate is: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------

Variation 4:
code_translation_template_rar_v2_variant4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Please translate this code from {source_language} into {target_language}. Only output the translated code.
Begin by rephrasing the instructions with further explanation, then provide the conversion.'''
    ),
    HumanMessagePromptTemplate.from_template("Submitted code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------

Variation 5:
code_translation_template_rar_v2_variant5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Convert the following source code from {source_language} to {target_language} and supply only the final result.
First, elaborate on the request with more detailed wording, then present the translated code.'''
    ),
    HumanMessagePromptTemplate.from_template("Here is the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------

Variation 6:
code_translation_template_rar_v2_variant6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Translate the code snippet from {source_language} to {target_language}. Ensure that only the final converted code is output.
Initially, enhance the request by rewording it with added details, and then show the translation.'''
    ),
    HumanMessagePromptTemplate.from_template("Code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------

Variation 7:
code_translation_template_rar_v2_variant7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Please convert the provided code from {source_language} to {target_language}. Return solely the final translation.
Start by rephrasing the direction in a more descriptive manner, then display the converted code.'''
    ),
    HumanMessagePromptTemplate.from_template("Initial code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------

Variation 8:
code_translation_template_rar_v2_variant8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Take the code below and convert it from {source_language} to {target_language}. Output only the translated version.
First, comprehensively reword the request, then provide the translation.'''
    ),
    HumanMessagePromptTemplate.from_template("Code provided: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------

Variation 9:
code_translation_template_rar_v2_variant9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Translate this coding snippet from {source_language} to {target_language} and return just the translation.
Begin by elaborating on the original request with further detail, and then deliver the converted code.'''
    ),
    HumanMessagePromptTemplate.from_template("Input code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------

Variation 10:
code_translation_template_rar_v2_variant10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Convert the following program code from {source_language} to {target_language} and provide only the converted output.
Initially, rephrase the task with added explanation, then proceed with the translation.'''
    ),
    HumanMessagePromptTemplate.from_template("The code is as follows: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------

Variation 11:
code_translation_template_rar_v2_variant11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Transform this piece of code from {source_language} to {target_language}. Only the final translated version should be presented.
First, restate the directive with supplemental details, then supply the conversion.'''
    ),
    HumanMessagePromptTemplate.from_template("Please review the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------

Variation 12:
code_translation_template_rar_v2_variant12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Please convert the specified code from {source_language} into {target_language}. Return solely the final translated code.
Begin with an expanded rendition of the request, then display the translation.'''
    ),
    HumanMessagePromptTemplate.from_template("Here is the snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------

Variation 13:
code_translation_template_rar_v2_variant13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Take the following code and translate it from {source_language} to {target_language}. Provide only the final translated code.
First, offer a more detailed rewording of this request, then furnish the translation.'''
    ),
    HumanMessagePromptTemplate.from_template("Code sample: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------

Variation 14:
code_translation_template_rar_v2_variant14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Recast the provided code from {source_language} into {target_language}. Output only the final result.
Initially, rephrase the task with a more comprehensive explanation, then provide the translation.'''
    ),
    HumanMessagePromptTemplate.from_template("Presented code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

--------------------------------------------------

Variation 15:
code_translation_template_rar_v2_variant15 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Convert the code below from {source_language} to {target_language}. Return only the translated code.
Begin by restating the instruction in greater detail, followed by the conversion.'''
    ),
    HumanMessagePromptTemplate.from_template("Snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])
