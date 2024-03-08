from PIL import Image, ImageDraw, ImageFont
import random

def generate_image(word, size=300, border_size=10, font_size=30, seed=1, font_path=None):
    # Set the random seed based on the input word
    if seed is not None:
        random.seed(hash(word))

    # Generate a random color for both text and border
    text_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    border_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Create a white square image with a border
    img_size = size + 2 * border_size
    image = Image.new("RGB", (img_size, img_size), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Load a font (you can customize the font_path or use the default font)
    if font_path is None:
        font = ImageFont.load_default()
    else:
        font = ImageFont.truetype(font_path, font_size)

    # Calculate the position to center the text
    text_width, text_height = draw.textsize(word, font)
    x_position = (img_size - text_width) // 2
    y_position = (img_size - text_height) // 2

    # Draw the border
    draw.rectangle([(0, 0), (img_size - 1, img_size - 1)], outline=border_color, width=border_size)

    # Draw the text
    draw.text((x_position, y_position), word, font=font, fill=text_color)

    return image

# Example usage:
word_to_display = "Hello"
generated_image = generate_image(word_to_display, seed=1)

# Save the generated image
generated_image.save("generated_image.png")
