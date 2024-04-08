import os
import argparse
import subprocess
import json
import re

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("image_folder_path", help="Path to the image folder")
args = parser.parse_args()

# Get the path of the current script
script_path = os.path.dirname(os.path.abspath(__file__))

# Open the text file "temp.txt" in the same folder
file_path = os.path.join(script_path, "temp.json")
image_caption_list = {}
data = None
with open(file_path, "r") as file:
    data = json.load(file)
    positive_prompt = data.get("positive_prompt", None)
    image_caption_list = data.get("image_caption_list", {})

# Select the first line
# first_line = list(image_caption_list.values())[0].strip().split()

# Get the 100 most common words in the English language
common_words = ["the", "be", "to", "of", "and", "a", "in", "that", "have", "I", "it", "for", "not", "on",
                "with", "he", "as", "you", "do", "at", "this", "but", "his", "by", "from", "they", "we",
                "say", "her", "she", "or", "an", "will", "my", "one", "all", "would", "there", "their", 
                "what", "so", "up", "out", "if", "about", "who", "get", "which", "go", "me", "when", 
                "make", "can", "like", "time", "no", "just", "him", "know", "take", "people", "into", 
                "year", "your", "good", "some", "could", "them", "see", "other", "than", "then", "now", 
                "look", "only", "come", "its", "over", "think", "also", "back", "after", "use", "two", 
                "how", "our", "work", "first", "well", "way", "even", "new", "want", "because", "any", 
                "these", "give", "day", "most", "us", "single"]

# Check if any match is found
max_matches = 0
best_image = None

# if lines[1].strip() == "":
#     start_line = 2
# else:
#     start_line = 3

for filename, caption in image_caption_list.items():
    words = caption.strip().split()
    matches = sum(word.lower() in positive_prompt for word in words if word.lower() not in common_words)
    if matches > max_matches:
        max_matches = matches
        best_image = caption.strip()
        best_image_name = filename

    if matches >= 1:
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
        with open(file_path, 'w') as json_file:
            # Get the file path of the best_image_index-th file
            file_list = os.listdir(args.image_folder_path)
            image_extensions = [".jpg", ".jpeg", ".png", ".gif"]  # Add more extensions if needed
            image_files = [file for file in file_list if any(file.lower().endswith(ext) for ext in image_extensions)]
            
            if best_image_name:
                # image_file = next((file for file in image_files if file.lower() == best_image_name.lower()), None)
                
                # for legal file naming conventions
                file_name_pattern = r'[^\w.\s-]|[\n\t]'
                new_name = '_'.join(re.sub(file_name_pattern, '', word) for word in words if word.lower() not in common_words)
                new_name = os.path.join(args.image_folder_path, new_name + os.path.splitext(filename)[1])
                
                # Check if the new name already exists
                if os.path.exists(new_name):
                    suffix = 1
                    while True:
                        suffix += 1
                        new_name_with_suffix = f"{new_name}_{suffix}"
                        if not os.path.exists(new_name_with_suffix):
                            new_name = new_name_with_suffix
                            break
                        else:
                            continue
                
                os.rename(os.path.join(args.image_folder_path, filename), new_name)
                if "images_to_move" in data:
                    data["images_to_move"].append(os.path.join(args.image_folder_path, os.path.basename(new_name)))
                else:
                    data["images_to_move"] = [os.path.join(args.image_folder_path, os.path.basename(new_name))]

                json_file.seek(0)
                json.dump(data, json_file, indent=4)
                json_file.truncate()
                
                if filename == best_image_name:
                    print(f"Best image with {max_matches} matches: {best_image_name} - {best_image}.")
                else:
                    print(f"Image with {matches} matches: {filename} - {caption.strip()}.")

if not best_image:
    print("No matches found for any image")

# Run choose_with_least_bg.py script if no matches found
if not best_image:
    script_path = os.path.join(script_path, "choose_with_least_bg.py")
    subprocess.run(["python", script_path, args.image_folder_path])
