import requests
from PIL import Image
import os
from transformers import BlipProcessor, BlipForConditionalGeneration
import argparse
import json

def image_to_text(images_folder):
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to("cuda")

    # images_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..\ComfyUI\output')
    output = {}
    for image_filename in os.listdir(images_folder):
        if image_filename.endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(images_folder, image_filename)
            raw_image = Image.open(image_path).convert('RGB')

            # # conditional image captioning
            # text = "a photography of"
            # inputs = processor(raw_image, text, return_tensors="pt").to("cuda")

            # out = model.generate(**inputs)
            # print(processor.decode(out[0], skip_special_tokens=True))
            # # >>> a photography of a woman and her dog

            # unconditional image captioning
            inputs = processor(raw_image, return_tensors="pt").to("cuda")

            out = model.generate(**inputs)
            output[image_filename] = processor.decode(out[0], skip_special_tokens=True)
            print(processor.decode(out[0], skip_special_tokens=True))

    # writing output to temp.json
    output_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Custom_Scripts')
    output_file_path = os.path.join(output_folder, 'temp.json')
    with open(output_file_path, 'r') as file:
        data = json.load(file)
    data["image_caption_list"] = output
    with open(output_file_path, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    parser = argparse.ArgumentParser(description="Create text description for images.")
    parser.add_argument("images_folder", help="Path to the source folder containing image files")
    args = parser.parse_args()

    # Convert image to text and print/store output
    image_to_text(args.images_folder)

if __name__ == "__main__":
    main()