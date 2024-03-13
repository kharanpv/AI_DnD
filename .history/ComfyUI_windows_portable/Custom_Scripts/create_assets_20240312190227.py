import subprocess
import os
import argparse
from shlex import quote

parser = argparse.ArgumentParser(description="Run the image pipeline")
parser.add_argument("positive_prompt", type=str, help="The positive prompt to use")
args = parser.parse_args()

# Get the current script's directory
script_directory = os.path.dirname(os.path.realpath(__file__))

# Relative path to the Stable Diffusion execution script
workflow_api_script = os.path.join(
    script_directory, "..", "ComfyUI", "ComfyUI-to-Python-Extension", "workflow_api.py"
)

# Relative path to the image folders
images_folder_path = os.path.join(
    script_directory, "..", "ComfyUI", "output"
)

ui_images_path = os.path.join(
    script_directory, r"..\..", "UI_EndUser", "test_images"
)

# Relative path to the image captioning script
image_to_text_script = os.path.join(
    script_directory, "..", "blip-image-captioning-base", "image_to_text.py"
)

# Relative path to the TinyLlama execution script
tinyLlama_script = os.path.join(
    script_directory, "..", "TinyLlama1.0", "run_Llama.py"
)

# Run the image generation script
try:
    subprocess.run(["python", workflow_api_script, quote(args.positive_prompt)], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running workflow_api.py: {e}")
    exit(1)

# Run the remove background script
try:
    subprocess.run(["python", "remove_background.py", images_folder_path], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running remove_background.py: {e}")
    exit(1)

# Run the image to text script
try:
    subprocess.run(["python", image_to_text_script, images_folder_path], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running image_to_text.py: {e}")
    exit(1)


# Run the image check script
try:
    subprocess.run(["python", "image_check.py", images_folder_path], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running image_check.py: {e}")
    exit(1)


# # Run the TinyLlama script
# try:
#     subprocess.run(["python", tinyLlama_script], check=True)
# except subprocess.CalledProcessError as e:
#     print(f"Error running run_Llama.py: {e}")
#     exit(1)

# Run the script to move images to the test_images folder
try:
    subprocess.run(["python", "move_files.py", ui_images_path], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running move_files.py: {e}")
    exit(1)

