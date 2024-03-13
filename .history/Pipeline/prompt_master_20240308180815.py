from openai import OpenAI
import re 
import requests
import datetime
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'chat_gpt_key.txt')

with open(file_path, 'r') as file:
    # Read a single line from the file
    CHAT_GPT_TOKEN = file.read().splitlines()

client = OpenAI(
    api_key = CHAT_GPT_TOKEN[0],
    )

USER_PROMPT: str
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
# The user should only touch user_prompt. Everything else we should have set in some other way.
# Realistically we need to reincorporate this and everything in this file back into token_lib.py
# If I had time to clean, I would, but I hate cleaning.
#
def text_prompt(user_prompt:str=USER_PROMPT, prompt_ai:str=PROMPT_AI, model_used:str="gpt-4"):
    stream = client.chat.completions.create(
        model=model_used,
        messages=[
        {"role": "system", "content": prompt_ai,
        },
        {"role": "user", "content": user_prompt,}
            ],
        stream=True,
    )
    retVal = ""
    with open("chat_history.txt", "w") as file:
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                file.write(chunk.choices[0].delta.content)
                retVal += chunk.choices[0].delta.content
    
    return retVal

def generate_response():
    USER_PROMPT = input("What are we generating?")
    print("What would you like to generate?")
    text_prompt(USER_PROMPT, PROMPT_AI, "gpt-4")