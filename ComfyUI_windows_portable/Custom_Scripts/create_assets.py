import subprocess
import os
import json

# Get the current script's directory
script_directory = os.path.dirname(os.path.realpath(__file__))

# Relative path to the Stable Diffusion execution script
workflow_api_script = os.path.join(
    script_directory, "..", "ComfyUI", "ComfyUI-to-Python-Extension", "workflow_api.py"
)

workflow_api_directory = os.path.join(
    script_directory, "..", "ComfyUI", "ComfyUI-to-Python-Extension"
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

# read the positive prompt from the temp.json file
# with open(os.path.join(workflow_api_directory, 'request.json'), 'r') as json_file:
#     data = json.load(json_file)
#     positive_prompt = data.get("positive_prompt")

def check_if_exists():
    positive_prompt = [word.lower() for word in positive_prompt.split()]
    max_count = 0
    max_match_img_name = ''

    # Filter out only the image files
    image_files = [f.lower() for f in os.listdir(ui_images_path) if f.lower().endswith('.png')]

    for image in image_files:
        image_words = image.replace('.png', '').split('_')
        # Count the number of similar words between image name and positive prompt
        similar_words_count = sum(1 for word in positive_prompt if word in image_words)

        # Update max_count and max_image_name if needed
        if similar_words_count > max_count:
            max_count = similar_words_count
            max_image_name = image
        
        return max_count

# Run the image generation script
try:
    subprocess.run(["python", workflow_api_script], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running workflow_api.py: {e}")
    exit(1)

# Run the remove background script
try:
    subprocess.run(["python", script_directory + "\\remove_background.py", images_folder_path], check=True)
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
    subprocess.run(["python", script_directory + "\\image_check.py", images_folder_path], check=True)
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
    subprocess.run(["python", script_directory + "\\move_files.py", ui_images_path], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running move_files.py: {e}")
    exit(1)

