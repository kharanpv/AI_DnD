import os
from PIL import Image

def count_transparent_pixels(image_path):
    image = Image.open(image_path)
    transparent_pixels = 0

    # Check if the image is a PNG file
    if image.mode in ('RGBA', 'LA') or (image.mode == 'P' and 'transparency' in image.info):
        pixel_data = image.convert('RGBA').getdata()

        for pixel in pixel_data:
            if pixel[3] == 0:  # Check if the pixel is transparent
                transparent_pixels += 1

    return transparent_pixels

def find_image_with_most_transparent_pixels(image_folder_path):
    max_transparent_pixels = 0
    image_with_most_transparent_pixels = None

    for filename in os.listdir(image_folder_path):
        if filename.endswith('.png'):
            image_path = os.path.join(image_folder_path, filename)
            transparent_pixels = count_transparent_pixels(image_path)

            if transparent_pixels > max_transparent_pixels:
                max_transparent_pixels = transparent_pixels
                image_with_most_transparent_pixels = filename

    return image_with_most_transparent_pixels

if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print('Usage: python script.py image_folder_path')
        sys.exit(1)

    image_folder_path = sys.argv[1]
    image_with_most_transparent_pixels = find_image_with_most_transparent_pixels(image_folder_path)

    if image_with_most_transparent_pixels:
        with open(os.path.dirname(os.path.abspath(__file__)) + "\\temp.txt", 'r') as file:
            first_line = file.readline().rstrip('\n')
            new_string = first_line.replace(' ', '_')
            new_string += image_with_most_transparent_pixels[image_with_most_transparent_pixels.rfind('.'):]
        image_path = os.path.join(image_folder_path, image_with_most_transparent_pixels)
        os.rename(image_path, os.path.join(image_folder_path, new_string))
        print(f'The image with the most transparent pixels is: {image_with_most_transparent_pixels}')
        with open(os.path.dirname(os.path.abspath(__file__)) + "\\temp.txt", 'a') as file:
            file.write(f'\n\n{os.path.join(image_folder_path, new_string)}')
    else:
        print('No PNG images found in the specified folder.')
