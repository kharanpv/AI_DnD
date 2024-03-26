import os
import json

class LocationObject:
    def __init__(self, name:str, data:str, image_path:str, x:int, y:int, rotation:float, scale:float):
        self.name = name
        self.data = data
        self.image_path = image_path
        self.x = x
        self.y = y
        self.rotation = rotation
        self.scale = scale

    def save(self, directory="assets"):
        # Generate file name based on the object's name attribute
        file_name = f"{self.name.replace(' ', '_').lower()}_info.lobj"
        
        # If directory is not provided, use current directory
        if not directory:
            directory = os.getcwd()
        
        # Join directory path with file name to create full file path
        file_path = os.path.join(directory, file_name)
        
        # Create dictionary with object information
        obj_info = {
            "Name": self.name,
            "Data": self.data,
            "Image Path": self.image_path,
            "Position": {"x": self.x, "y": self.y},
            "Rotation": self.rotation,
            "Scale": self.scale
        }
        
        # Write object information to the file as JSON
        with open(file_path, 'w') as file:
            json.dump(obj_info, file, indent=4)
        
        return file_path
