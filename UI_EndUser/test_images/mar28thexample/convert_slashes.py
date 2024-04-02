import os
import sys
import json

def convert_slashes(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # Convert forward slashes to backward slashes in the 'Image Path' field
    data['Image Path'] = data['Image Path'].replace('UI_EndUser', 'C:\\Users\\Prateek\\Desktop\\College_Stuff\\Senior_Design\\AI_DnD\\UI_EndUser')
    
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def main(folder_path):
    # Check if the specified folder path exists
    if not os.path.exists(folder_path):
        print(f"Folder does not exist: {folder_path}")
        return

    # Iterate over files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.lobj'):
            file_path = os.path.join(folder_path, file_name)
            convert_slashes(file_path)
            print(f"Converted slashes in: {file_name}")

if __name__ == "__main__":
    # Get folder path from command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script_name.py folder_path")
        sys.exit(1)

    folder_path = sys.argv[1]
    main(folder_path)
