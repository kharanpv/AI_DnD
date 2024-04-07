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
import re, os, json
import requests
import subprocess
local_debug_img = True

from OtherCode.libs.UI import ImageOnCanvas, ViewWindow

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
(set of coordinates), (size as integer) 
Paragraph
}

Size should only be 1 integer, and wrapped in (). Coordinates should be separated by commas.
"""

script_dir = None
file_path = None
img_pipeline_script = None
workflow_api_folder = None
CHAT_GPT_TOKEN = None
client = None
chat_history_path = None

script_dir = script_dir = os.path.dirname(os.path.abspath(__file__))
script_dir = os.path.join(script_dir, '..', 'Pipeline')


img_pipeline_script = os.path.join(
script_dir, "..", "ComfyUI_windows_portable", "Custom_Scripts", "create_assets.py"
)

class PromptMaster:
    def __init__(self, parent_widget:ViewWindow.ViewWindow=None):
        
        self.img_pipeline_script = os.path.join(
        script_dir, "..", "ComfyUI_windows_portable", "Custom_Scripts", "create_assets.py"
        )


        self.pattern_coords = r'\(((?:.|\n)*?)\)'
        self.pattern = r'\{((?:.|\n)*?)\}'
        self.parent_widget = parent_widget

        self.file_path = os.path.join(script_dir, 'chat_gpt_key.txt')

        self.workflow_api_folder = os.path.join(os.path.dirname(
            script_dir), "ComfyUI_windows_portable", "ComfyUI", "ComfyUI-to-Python-Extension")

        with open(self.file_path, 'r') as file:
            self.CHAT_GPT_TOKEN = file.read().splitlines()

        self.client = OpenAI(api_key=self.CHAT_GPT_TOKEN[0])
        self.chat_history_path = os.path.join(script_dir, 'chat_history.json')

        self.chat_history = []
        
        self.x = 0
        self.y = 0
        self.z = 0

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

        # Ensure file exists and initialize with empty JSON object if it doesn't
        if not os.path.exists(self.chat_history_path):
            with open(self.chat_history_path, 'w') as file:
                json.dump([], file)

        # Read existing chat history or initialize as empty list
        with open(self.chat_history_path, 'r') as file:
            try:
                chat_history = json.load(file)
            except json.decoder.JSONDecodeError:
                chat_history = []

        chat_history.append({"user_prompt": user_prompt, "dm_response": retVal})

        
        positive_prompt = retVal
        if positive_prompt:
            prompt = {
                "positive_prompt": positive_prompt,
                "negative_prompt": None,
                "num_samples": 5
            }
            request_path = os.path.join(self.workflow_api_folder, "request.json") 
            with open(request_path, "w+") as file:
                json.dump(prompt, file)

        # Write updated chat history back to file
        with open(self.chat_history_path, 'w') as file:
            json.dump(chat_history, file)

        self.images_for_self()
        return retVal

    def get_coords_and_text(self, text:str=None):
        if not text:
            text = self.text

        matches = re.findall(self.pattern, text)
        for match in matches:
            coords, scale_size = re.findall(self.pattern_coords, match, re.DOTALL)
            coords.replace(" ", "")
            scale_size.replace(" ", "")
        return matches
    
    def get_names(self, text:str=None):
        if text is None:
            text = self.text
        print(text)
        retVal = re.findall(r"^(.+)$", text)
        print(retVal, id(retVal))
        return retVal

    def get_xyz(self, text:str=None):
        if text is None:
            text = self.text
        matches = re.findall(r"\((.*?)\)", text)
        print(matches)
        if matches:
            text = matches[0].replace("(","").replace(")","").replace(" ","")
            text = text.split(',')
            self.x = text[0]
            self.y = text[1]
            return text
        else:
            return []

    def user_prompt(self, user_input:str):
        return self.get_coords_and_text(self.text_prompt(user_input))

    # TODO after Jiang meeting
    def generate_lobj(self):
        pass

    def images_for_self(self):
        for a_match in self.get_coords_and_text():
            x,y,z = self.get_xyz(text=a_match)
            #name = self.get_names(text=a_match)
            name = a_match.split('\n')[1]
            print(f"Name:{name}")
            #current_image = PlaceHolder_img.generate_image(name)
            #image_path = f"assets/{name}{random.randint(0,255)}.png"
            #current_image.save(image_path)
            build_images(a_Prompt=self)
        return True

    def get_pipeline_path(self):
        return self.img_pipeline_script

def build_images(a_Prompt:PromptMaster):
    img_pipeline_script = a_Prompt.img_pipeline_script

    try:
        process_handle = subprocess.Popen(["python", img_pipeline_script])
        process_handle.communicate()
        print("Finished generating!")
    except subprocess.CalledProcessError as e:
        print(f"Error running workflow_api.py: {e}")
        exit(1)

