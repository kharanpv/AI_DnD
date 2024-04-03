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



class PromptMaster:
    def __init__(self):
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(self.script_dir, 'chat_gpt_key.txt')

        self.img_pipeline_script = os.path.join(
            self.script_dir, "..", "ComfyUI_windows_portable", "Custom_Scripts", "create_assets.py"
        )

        self.workflow_api_folder = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "..", "ComfyUI_windows_portable", "ComfyUI", "ComfyUI-to-Python-Extension")

        with open(self.file_path, 'r') as file:
            self.CHAT_GPT_TOKEN = file.read().splitlines()

        self.client = OpenAI(api_key=self.CHAT_GPT_TOKEN[0])
        self.chat_history_path = os.path.join(self.script_dir, 'chat_history.json')

        self.chat_history = []

        self.INIT_PROMPT_AI = """
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

    def text_prompt(self, user_prompt:str, prompt_ai:str=None, model_used:str="gpt-3.5-turbo"):
        if prompt_ai is None:
            prompt_ai = self.INIT_PROMPT_AI

        stream = self.client.chat.completions.create(
            model=model_used,
            messages=[
                {"role": "system", "content": prompt_ai},
                {"role": "user", "content": user_prompt}
            ]
        )

        self.chat_history.append({"user_prompt": user_prompt, "dm_response": stream.choices[0].message.content})


    def find_prompt(self):
        last_dm_response = self.chat_history[-1]["dm_response"]
        if last_dm_response:
            index = last_dm_response.find("{\n")
            if index != -1:
                phrase_start = index + len("{\n")
                phrase_end = last_dm_response.find("\n", phrase_start)
                if phrase_end != -1:
                    prompt = last_dm_response[phrase_start:phrase_end].strip()
                    return prompt

    def queue_prompt(self):
        positive_prompt = self.find_prompt()
        if positive_prompt:
            prompt = {
                "positive_prompt": positive_prompt,
                "negative_prompt": None,
                "num_samples": 5
            }
            request_path = os.path.join(self.workflow_api_folder, "request.json") 
            with open(request_path, "w") as file:
                json.dump(prompt, file)

    def generate_response(self, USER_PROMPT):
        self.text_prompt(USER_PROMPT, self.INIT_PROMPT_AI, "gpt-3.5-turbo")
        self.queue_prompt()

    def run_workflow(self):
        try:
            subprocess.run(["python", self.img_pipeline_script], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running workflow_api.py: {e}")
            exit(1)