from openai import OpenAI
import os
import json
import subprocess

script_dir = None
file_path = None
img_pipeline_script = None
workflow_api_folder = None
CHAT_GPT_TOKEN = None
client = None
chat_history_path = None

INIT_PROMPT_AI = """
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
# this all needs to be rewritten as a class
# as setup is called every time instead of simply once
# 

def setup():
    global script_dir, file_path, img_pipeline_script, workflow_api_folder, CHAT_GPT_TOKEN, client
    global chat_history_path, INIT_PROMPT_AI
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'chat_gpt_key.txt')

    img_pipeline_script = os.path.join(
        script_dir, "..", "ComfyUI_windows_portable", "Custom_Scripts", "create_assets.py"
    )

    workflow_api_folder = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), "..", "ComfyUI_windows_portable", "ComfyUI", "ComfyUI-to-Python-Extension")

    with open(file_path, 'r') as file:
        # Read a single line from the file
        CHAT_GPT_TOKEN = file.read().splitlines()

    client = OpenAI(api_key=CHAT_GPT_TOKEN[0],)

    chat_history_path = os.path.join(script_dir, 'chat_history.json')

    USER_PROMPT: str = None
    INIT_PROMPT_AI = """
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
def text_prompt(user_prompt:str, prompt_ai:str=INIT_PROMPT_AI, model_used:str="gpt-3.5-turbo"):
    global script_dir, file_path, img_pipeline_script, workflow_api_folder, CHAT_GPT_TOKEN, client
    global chat_history_path, INIT_PROMPT_AI

    stream = client.chat.completions.create(
        model=model_used,
        messages=[
        {"role": "system", "content": prompt_ai,
         },
        {"role": "user", "content": user_prompt,
         }
         ],
        # stream=True,
    )
    # retVal = ""
    
    # Ensure file exists and initialize with empty JSON object if it doesn't
    if not os.path.exists(chat_history_path):
        with open(chat_history_path, 'w') as file:
            json.dump([], file)

    # Read existing chat history or initialize as empty list
    with open(chat_history_path, 'r') as file:
        try:
            chat_history = json.load(file)
        except json.decoder.JSONDecodeError:
            chat_history = []

    chat_history.append({"user_prompt": user_prompt, "dm_response": stream.choices[0].message.content})

    # Write updated chat history back to file
    with open(chat_history_path, 'w') as file:
        json.dump(chat_history, file)

        # retVal += stream.choices[0].delta.content
    # return retVal

def find_prompt():
    global script_dir, file_path, img_pipeline_script, workflow_api_folder, CHAT_GPT_TOKEN, client
    global chat_history_path, INIT_PROMPT_AI

    with open(chat_history_path, 'r') as file:
        chat_history = json.load(file)
        last_dm_response = chat_history[-1]["dm_response"]
        if last_dm_response:
            # Find the index of "{\n" and extract the phrase after it
            index = last_dm_response.find("{\n")
            if index != -1:
                phrase_start = index + len("{\n")
                phrase_end = last_dm_response.find("\n", phrase_start)
                if phrase_end != -1:
                    prompt = last_dm_response[phrase_start:phrase_end].strip()
                    return prompt

def queue_prompt():
    global script_dir, file_path, img_pipeline_script, workflow_api_folder, CHAT_GPT_TOKEN, client
    global chat_history_path, INIT_PROMPT_AI

    positive_prompt = find_prompt()
    if positive_prompt:
        prompt = {
            "positive_prompt": positive_prompt,
            "negative_prompt": None,
            "num_samples": 5
        }
        request_path = os.path.join(workflow_api_folder, "request.json") 
        with open(request_path, "w") as file:
            json.dump(prompt, file)
    # Here I add method to output


def generate_response(USER_PROMPT):
    global script_dir, file_path, img_pipeline_script, workflow_api_folder, CHAT_GPT_TOKEN, client
    global chat_history_path, INIT_PROMPT_AI

    setup()
    text_prompt(USER_PROMPT, INIT_PROMPT_AI, "gpt-3.5-turbo")
    queue_prompt()

def run_workflow():
    global img_pipeline_script

    try:
        subprocess.run(["python", img_pipeline_script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running workflow_api.py: {e}")
        exit(1)

# def generate_response():
#     global script_dir, file_path, img_pipeline_script, workflow_api_folder, CHAT_GPT_TOKEN, client
#     global chat_history_path, INIT_PROMPT_AI

#     setup()
#     USER_PROMPT = input("What are we generating? ")
#     text_prompt(USER_PROMPT, INIT_PROMPT_AI, "gpt-4")
#     queue_prompt()
#     try:
#         subprocess.run(["python", img_pipeline_script], check=True)
#     except subprocess.CalledProcessError as e:
#         print(f"Error running workflow_api.py: {e}")
#         exit(1)

# generate_response()