from openai import OpenAI
import re 
import requests
import datetime

with open('../../chat_gpt_key.key', 'r') as file:
    # Read a single line from the file
    CHAT_GPT_TOKEN = file.read().splitlines()

client = OpenAI(
    api_key = CHAT_GPT_TOKEN[0],
    )


USER_PROMPT = "I want a hill with a tree and a well on top. I want a dragon statue surrounding it."
PROMPT_AI = """
You are a generating descriptions for a 2d map.
The user will give you a description of a place.
Put each described object in the scene in the list `objects`.
For each description in `objects`, write a 1 paragraph description of the object. Catagorized the size of the object in meters, using x and y.
Make the paragraph description be only physical. 
For each object in the `objects` list, give it a logical set of coordinates (x,y,z), as if we were looking from a top down view. Z represents height. This coordinate set is unrelated to the size.
For example, if a tree is on a hill, it would share x,y coordinates and have a larger z coordinate than the hill.
Make each pair of coordinates be based upon the description paragraphs generated. 
Before each paragraph send the message "(" on its own line.
Write the name of the object on its own line.
Respond with corresponding paragraph a line below.
After each paragraph send the message ")" on its own line.
Example:
{
Name
Paragraph
}
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
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")
            retVal += chunk.choices[0].delta.content
    
    print()
    return retVal

# The user should not touch this function. The only function the user should touch is text_prompt.
valid_sizes =  ['256x256', '512x512', '1024x1024', '1024x1792', '1792x1024']
def image_prompt_url(text_prompt:str, gen_model:str="dall-e-3", gen_size:str='256x256', gen_quality="standard"):
    response = client.images.generate(
    model=gen_model,
    prompt=text_prompt,
    size='1024x1024',
    quality="standard",
    n=1,
    )
    return response.data[0].url 







output = text_prompt()


save_path = "./assets/"

pattern = r'\(((?:.|\n)*?)\)'
matches = re.findall(pattern, output)
print(matches)


for match in matches:
    now = datetime.datetime.now()
    url = image_prompt_url(text_prompt=match)
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        with open(str(now) +".png", 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded successfully and saved at: {save_path}")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")






