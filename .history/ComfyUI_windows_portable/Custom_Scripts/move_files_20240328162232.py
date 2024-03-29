import os
import shutil
import argparse
import json

def move_images(destination_folder):
    # Ensure destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Read the last line from temp.txt
    with open(os.path.dirname(os.path.abspath(__file__)) + "/temp.json", 'r') as file:
        data = json.load(file)

        # Move images specified in "images_to_move" list
        if "images_to_move" in data:
            for image_path in data["images_to_move"]:
                # Extract file name from the image path
                file_name = os.path.basename(image_path)

                # separate the extension from the file name
                file_name_text, extension = file_name.rsplit('.', 1)
                # split the file name text into its constituent words
                words = file_name_text.split('_')
                # remove words that have 'pixel' in them
                filtered_words = [word for word in words if 'pixel' not in word]
                # merge back to get file_name
                file_name = '_'.join(filtered_words) + '.' + extension

                # Construct destination path
                destination_path = os.path.join(destination_folder, file_name)
                # Move the image to the destination folder
                shutil.move(image_path, destination_path)
                print(f"Moved {file_name} to {destination_folder}")
    
    os.remove(os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp.json"))

def main():
    parser = argparse.ArgumentParser(description="Move image files from source to destination.")
    parser.add_argument("ui_images_path", help="Path to the destination folder for UI images")

    args = parser.parse_args()

    # Move images from source to destination
    move_images(args.ui_images_path)

if __name__ == "__main__":
    main()
