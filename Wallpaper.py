from PIL import Image, ImageDraw, ImageFont
import textwrap


def get_wallpaper(quote):
    # image_width
    image = Image.new('RGB', (800, 400), color=(0, 0, 0))
    font = ImageFont.truetype("Arial.ttf", 40)
    text1 = quote
    text_color = (200, 200, 200)
    text_start_height = 100
    draw_text_on_image(image, text1, font, text_color, text_start_height)
    image.save('created_image.png')

    
def draw_text_on_image(image, text, font, text_color, text_start_height):
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    y_text = text_start_height
    lines = textwrap.wrap(text, width=40)
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 2, y_text),line, font=font, fill=text_color)
        y_text += line_height

