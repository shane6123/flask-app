from flask import Flask, request, send_file, jsonify
import rembg
import io
from PIL import Image

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        
        file = request.files['image']
        
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        
        image_data = file.read()
        
        # Remove background using rembg library
        output_data = rembg.remove(image_data)
        
        # Create a PIL Image from the output data
        output_image = Image.open(io.BytesIO(output_data))
        
        # Save the output image (optional)
        # output_image.save('output.png')
        
        # Send the image as a response
        output_buffer = io.BytesIO()
        output_image.save(output_buffer, format='PNG')
        output_buffer.seek(0)
        
        return send_file(output_buffer, mimetype='image/png'), 200
    
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# if __name__ == '__main__':
#     app.run(debug=True)
