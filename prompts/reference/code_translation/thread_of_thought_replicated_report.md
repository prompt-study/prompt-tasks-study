
──────────────────────────────
Variation 0 (original):
──────────────────────────────
code_translation_template_thot = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Walk me through the code in manageable parts, summarizing how to convert it
from {source_language} to {target_language}. Then provide the translated code only.'''
    ),
    HumanMessagePromptTemplate.from_template("{code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 1:
──────────────────────────────
code_translation_template_thot_variant1 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Break down the provided code into smaller, digestible steps and explain the process of converting it from {source_language} to {target_language}. Afterwards, output only the translated code.'''
    ),
    HumanMessagePromptTemplate.from_template("Here's the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 2:
──────────────────────────────
code_translation_template_thot_variant2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Analyze the code piece by piece, describing the method to change it from {source_language} into {target_language}. Then, deliver solely the converted code.'''
    ),
    HumanMessagePromptTemplate.from_template("Code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 3:
──────────────────────────────
code_translation_template_thot_variant3 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Divide the code into understandable segments, outlining the conversion approach from {source_language} to {target_language}. Provide only the final translated code afterward.'''
    ),
    HumanMessagePromptTemplate.from_template("Submit your code here: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 4:
──────────────────────────────
code_translation_template_thot_variant4 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Examine the code step by step and summarize how to adapt it from {source_language} to {target_language}. Then, return only the code in the target language.'''
    ),
    HumanMessagePromptTemplate.from_template("Please input the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 5:
──────────────────────────────
code_translation_template_thot_variant5 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Walk through the code systematically, highlighting how to transform it from {source_language} to {target_language} in clear stages. Lastly, give just the translated code.'''
    ),
    HumanMessagePromptTemplate.from_template("Here is the code to process: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 6:
──────────────────────────────
code_translation_template_thot_variant6 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Step through the code in logical segments, detailing the conversion process from {source_language} to {target_language}. Conclude by presenting only the translated code.'''
    ),
    HumanMessagePromptTemplate.from_template("Insert your code here: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 7:
──────────────────────────────
code_translation_template_thot_variant7 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Go over the code in bite-sized portions, explaining how to convert it from {source_language} to {target_language}. Afterwards, supply only the new code.'''
    ),
    HumanMessagePromptTemplate.from_template("Provide the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 8:
──────────────────────────────
code_translation_template_thot_variant8 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Dissect the code into smaller parts and describe the technique to convert it from {source_language} into {target_language}. Then output just the translated segment.'''
    ),
    HumanMessagePromptTemplate.from_template("Kindly insert your code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 9:
──────────────────────────────
code_translation_template_thot_variant9 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Parse the code into clear sections, elucidating the process to shift it from {source_language} to {target_language}. After that, simply output the translated code.'''
    ),
    HumanMessagePromptTemplate.from_template("Drop the code here: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 10:
──────────────────────────────
code_translation_template_thot_variant10 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Segment the code into manageable sections while explaining how to convert it from {source_language} to {target_language}. Please follow with only the final translated code.'''
    ),
    HumanMessagePromptTemplate.from_template("Submit the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 11:
──────────────────────────────
code_translation_template_thot_variant11 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Detail the code in smaller fragments, outlining the method for its conversion from {source_language} to {target_language}. Then, provide just the translated version.'''
    ),
    HumanMessagePromptTemplate.from_template("Enter the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 12:
──────────────────────────────
code_translation_template_thot_variant12 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Explain the code piece by piece, summarizing the strategy to modify it from {source_language} to {target_language}. Then, share only the converted code.'''
    ),
    HumanMessagePromptTemplate.from_template("Place your code here: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 13:
──────────────────────────────
code_translation_template_thot_variant13 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Guide me through the code segment by segment, clarifying the steps to convert it from {source_language} to {target_language}. Following that, offer only the code in its translated form.'''
    ),
    HumanMessagePromptTemplate.from_template("Please provide the code: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 14:
──────────────────────────────
code_translation_template_thot_variant14 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Review the code in sequential steps and illustrate how to convert it from {source_language} into {target_language}. Then, supply solely the translated code segment.'''
    ),
    HumanMessagePromptTemplate.from_template("Present the code here: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

──────────────────────────────
Variation 15:
──────────────────────────────
code_translation_template_thot_variant15 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        '''Break the code into digestible parts, detailing the conversion process from {source_language} to {target_language} along the way. Afterwards, output only the translated code.'''
    ),
    HumanMessagePromptTemplate.from_template("Share the code snippet: {code}"),
    AIMessagePromptTemplate.from_template('prompt'),
])

