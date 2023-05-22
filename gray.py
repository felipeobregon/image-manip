from PIL import Image

def to_grayscale(path):
    # load images
    image = Image.open(path)

    # convert to gray scale
    grayscale_image = image.convert("L")

