import subprocess
import os

# Get the current script's directory
script_directory = os.path.dirname(os.path.realpath(__file__))

# Specify the relative paths to the scripts
workflow_api_script = os.path.join(
    script_directory, "..", "ComfyUI", "ComfyUI-to-Python-Extension", "workflow_api.py"
)

images_folder_path = os.path.join(
    script_directory, "..", "ComfyUI", "output"
)

image_to_text_script = os.path.join(
    script_directory, "..", "blip-image-captioning-base", "image_to_text.py"
)

# Run the image generation script
try:
    subprocess.run(["python", workflow_api_script], check=True)
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
    subprocess.run(["python", image_to_text_script], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running image_to_text.py: {e}")
    exit(1)