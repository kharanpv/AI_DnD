import "./libs/token_lib"
import pdf_lib
import re
pdf_path = "./DnD_5E_CharacterSheet_FormFillable.py"

characterSheetJson = pdf_lib.pdf_to_json(pdf_path)

prompt = "I want a bard who is an elf and 3rd level. I want him to use a harp."

# Questions
q_getLevel = "What level does the player state they want? Answer with only a number. If they didn't provide a level, answer with `0`."
q_getClass = "What class should the player pick from the following options?"
q_getSubClassIF = "Does the class and level the player selected require a subclass? Answer `YES` or `NO` (if the level is not provided, answer NO)."
q_getSubClass = "Does the player specify a subclass?"
q_getSubClass_unspecified = "What subclass would the player like based upon the initial question?"
q_getRace = "What race should the player pick from the following? Answer with only the "
q_getLevel = "What level does the player state they want? Answer with only a number. If they didn't provide a level, answer with `0`."

q_getAdditionalConstraints = "Are there any other criteria the player provides?"
# Commented out due to no being most easy to test
# Below attempts to use the LLM to prompt itself. That can get weird, so we don't do that (yet)
#q_getAdditionalQuestions
token_lib.setup_ai("ChatGPT")

token_lib.PROMPT_FXN(prompt)

o_level = token_lib.PROMPT_FXN(q_getLevel)

level = re.findall(r'\b\d+\b', q_getLevel)

if len(values) != 1:
    raise ValueError

o_class = token_lib.PROMPT_FXN(q_getClass)
o_subclass = token_lib.PROMPT_FXN(q_getSubClass)
o_race = token_lib.PROMPT_FXN(q_getRace)

# Now we want to push this back into the pdf. 




