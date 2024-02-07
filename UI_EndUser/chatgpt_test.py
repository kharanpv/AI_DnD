from openai import OpenAI

with open('../../chat_gpt_key.key', 'r') as file:
    # Read a single line from the file
    CHAT_GPT_TOKEN = file.read().splitlines()

client = OpenAI(
    api_key = CHAT_GPT_TOKEN[0],
    )


USER_PROMPT = "I want a hill with a tree and a well on top."
PROMPT_AI = """
You are a generating descriptions for a 2d map.
The user will give you a description of a place.
Put each described object in the scene in the list `objects`.
For each description in `objects`, write a 1 paragraph description of the object. Catagorized the size of the object in meters, using x and y.
Make the paragraph description be only physical. 
For each object in the `objects` list, give it a logical set of coordinates (x,y,z), as if we were looking from a top down view. Z represents height. This coordinate set is unrelated to the size.
For example, if a tree is on a hill, it would share x,y coordinates and have a larger z coordinate than the hill.
Make each pair of coordinates be based upon the description paragraphs generated. 
Respond with the paragraphs.
"""


def prompt(user_prompt:str=USER_PROMPT, prompt_ai:str=PROMPT_AI, model_used:str="gpt-4"):
    stream = client.chat.completions.create(
        model=model_used,
        messages=[
        {"role": "system", "content": prompt_ai,
        },
        {"role": "user", "content": user_prompt,}
            ],
        stream=True,
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")

prompt()