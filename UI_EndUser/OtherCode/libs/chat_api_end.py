### Ok, What am I doing

# We have the UI accept a different fxn in ScrollableTextEdit, so we simply pass one of the functions from here to it
# 
# The things I need to do still:
# 1. Constructor which reads API key. TODO later Maybe options to describe what should be generated?
# 2. Function which passes text input to chatgpt_api
# 3. PIL generator which builds square functions
# 4. Inserting onto canvas
# 5. save

from openai import OpenAI
import re 
import requests
import datetime

local_debug_img = True

PROMPT_AI = """
You are a generating descriptions for a 2d map.
The user will give you a description of a place. 
Put each described object in the scene in the list `objects`.
For each description in `objects`, write a 1 paragraph description of the object. Catagorized the size of the object in meters, using x and y.
Make the paragraph description be only physical. 
For each object in the `objects` list, give it a logical set of coordinates (x,y,z), as if we were looking from a top down view. Z represents height. This coordinate set is unrelated to the size.
For example, if a tree is on a hill, it would share x,y coordinates and have a larger z coordinate than the hill.
Make each pair of coordinates be based upon the description paragraphs generated. 
Before each paragraph send the message "{" on its own line.
Write the name of the object on its own line.
Respond with corresponding paragraph a line below.
After each paragraph send the message "}" on its own line.
Example:
{
Name
(coordinates as integers), (size as integer) 
Paragraph
}

Size should only be 1 integer, and wrapped in (). Coordinates should be separated by commas.
"""
#
# We aren't saving yet, TODO
#
# The cont file system is flawed, redo
#
class ChatGPTCalls():
    def __init__(self):
        self.pattern_coords = r'\(((?:.|\n)*?)\)'
        self.pattern = r'\{((?:.|\n)*?)\}'
        with open('../../chat_gpt_key.key', 'r') as file:
            CHAT_GPT_TOKEN = file.read().splitlines()

        self.client = OpenAI(
            api_key = CHAT_GPT_TOKEN[0],
            )
    # 
    # The user should only touch user_prompt. Everything else we should have set in some other way.
    #
    def text_prompt(self, user_prompt:str, prompt_ai:str=PROMPT_AI, model_used:str="gpt-4", print_fxn=print):
        stream = self.client.chat.completions.create(
            model=model_used,
            messages=[
            {"role": "system", "content": prompt_ai,
            },
            {"role": "user", "content": user_prompt,}
                ],
            stream=True,
        )
        retVal = ""
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                print_fxn(str(chunk.choices[0].delta.content), end="")
                retVal += chunk.choices[0].delta.content
        self.text = retVal
        return retVal

    def get_coords_and_text(self, text:str=None):
        if not text:
            text = self.text

        matches = re.findall(self.pattern, text)
        for match in matches:
            coords, scale_size = re.findall(self.pattern_coords, match)
            coords.replace(" ", "")
            scale_size.replace(" ", "")
        return matches
    
    def user_prompt(self, user_input:str):
        return self.get_coords_and_text(self.text_prompt(user_input))