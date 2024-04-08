from PIL import Image, ImageDraw
import os
import argparse

def remove_background(image_folder_path, tolerance=30):
    # Get the directory of the current script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Make the path absolute by joining with the current working directory
    image_folder_path = os.path.abspath(os.path.join(script_directory, image_folder_path))

    # If folder does not exist throw error
    if not os.path.exists(image_folder_path):
        raise FileNotFoundError(f"The specified output folder '{image_folder_path}' does not exist.")
    
    # Iterate through all PNG files in the input folder
    for filename in os.listdir(image_folder_path):
        if filename.endswith(".png"):
            image_path = os.path.join(image_folder_path, filename)
        
        # Open the image
        original_image = Image.open(image_path)

        # convert image to RGBA if not already
        if original_image.mode != 'RGBA':
            original_image = original_image.convert('RGBA')
        
        # Get the size of the image
        width, height = original_image.size

        # Define the flood-fill starting points
        start_points = [(0, 0), (width-1, 0), (0, height-1), (width-1, height-1)]

        for start_point in start_points:
            # Perform flood-fill starting from the current point
            ImageDraw.floodfill(original_image, start_point, (0, 0, 0, 0), thresh=tolerance)

        # Save the result (overwriting the original image)
        original_image.save(image_path)

def main():
    parser = argparse.ArgumentParser(description="Remove background from images using flood-fill.")
    parser.add_argument("image_folder_path", help="Path to the folder containing images.")
    # parser.add_argument("--tolerance", type=int, default=30, help="Tolerance for flood-fill (default: 30).")
    parser.add_argument("--tolerance", type=int, default=40, help="Tolerance for flood-fill (default: 40).")
    args = parser.parse_args()

    remove_background(args.image_folder_path, args.tolerance)

if __name__ == "__main__":
    main()