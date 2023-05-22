from flask import Flask, request, Response
from flask_cors import CORS
from PIL import Image
import io

app = Flask(__name__)
CORS(app)

# route that receives an image and returns a grayscale version of it
@app.route('/', methods=['POST'])
def grayscale():
    image_data = request.files['image']

    image = Image.open(image_data)
    grayscale_image = image.convert("L")

    # Create a buffer to hold the image bytes
    image_buffer = io.BytesIO()

    # Save the grayscale image to the buffer
    grayscale_image.save(image_buffer, format='JPEG')

    # Retrieve the image bytes from the buffer
    grayscale_bytes = image_buffer.getvalue()

    # Create response with grayscale image bytes and content type
    response = Response(grayscale_bytes, mimetype='image/jpeg')

    return response

if __name__ == '__main__':
    app.run()
