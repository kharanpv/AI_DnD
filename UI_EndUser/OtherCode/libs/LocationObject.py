import os
import json
import random
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
        if self.name:
            file_name = f"{self.name.replace(' ', '_').lower()}_info.lobj"
        else:
             # Format the date and time as a string
            timestamp_string = str(random.randint(0, 20000000))
            file_name = timestamp_string + ".lobj"
        
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
        with open(file_path, 'w+') as file:
            json.dump(obj_info, file, indent=4)
        
        return file_path


    @classmethod
    def load(cls, file_path):
        with open(file_path, 'r') as file:
            obj_info = json.load(file)
        
        name = obj_info.get("Name")
        data = obj_info.get("Data")
        image_path = obj_info.get("Image Path")
        print("DEBUG: ABS PATH = ", image_path)
        position = obj_info.get("Position", {})
        x = position.get("x", 0)
        y = position.get("y", 0)
        rotation = obj_info.get("Rotation", 0.0)
        scale = obj_info.get("Scale", 1.0)
        
        return cls(name, data, image_path, x, y, rotation, scale)