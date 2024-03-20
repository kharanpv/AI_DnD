from PIL import Image, ImageDraw, ImageFont
import random


def generate_image(word, size=300, border_size=10, font_size=None, seed=1, font_path=None):
    # Set the random seed based on the input word
    if seed is not None:
        random.seed(hash(word))

    # Generate a random color for both text and border
    text_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    border_color = text_color

    # Create a white square image with a border
    img_size = size + 2 * border_size
    image = Image.new("RGB", (img_size, img_size), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Find the largest font size that fits the text within the box
    if font_size is None:
        font_size = 1
    
    font = ImageFont.load_default() if font_path is None else ImageFont.truetype(font_path, font_size)

    text_width = draw.textlength(text=word, font=font)
    text_height = 1
    while text_width < size - 2 * border_size and text_height < size - 2 * border_size:
        font_size += 1
        font = ImageFont.load_default(size=font_size) if font_path is None else ImageFont.truetype(font_path, font_size)
        text_width = font.getmask(word).getbbox()[2]
        text_height = font.getmask(word).getbbox()[3]


    # Calculate the position to center the text
    x_position = (img_size - text_width) // 2
    y_position = (img_size - text_height) // 2

    # Draw the border
    draw.rectangle([(0, 0), (img_size - 1, img_size - 1)], outline=border_color, width=border_size)

    # Draw the text
    draw.text((x_position, y_position), word, font=font, fill=text_color)

    return image

generate_image("burned chicken pen")