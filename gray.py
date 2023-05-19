from PIL import Image

def to_grayscale(path):
    # load images
    image = Image.open(path)

    # convert to gray scale
    grayscale_image = image.convert("L")

    #save
    grayscale_image.save(f'grayscale_{path}')
