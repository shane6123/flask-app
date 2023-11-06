# Importing Required Modules 
# from rembg import remove 
# from PIL import Image 
from flask import Flask, request, jsonify
# from flask_cors import CORS 

app = Flask(__name__)
# CORS(app)


# Defining the home page of our site
@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Remove BG API!'})



# app.run(port=5000)
if __name__ == '__main__':
    # app.run(debug=True)

# @app.route('/removebg', methods=['POST'])
# def removebg():
#     if request.method == 'POST':
#         # Store path of the image in the variable input_path 
#         input_path = './1.jpeg'

#         # Store path of the output image in the variable output_path 
#         output_path = './output1.png'
#         # Processing the image 
#         input = Image.open(input_path) 

#         # Removing the background from the given Image 
#         output = remove(input) 

#         #Saving the image in the given path 
#         output.save(output_path) 

#         return jsonify({'message': 'Image background removed successfully!'})
#     else:
#         return jsonify({'message': 'Invalid request method!'})
    


# # Store path of the image in the variable input_path 
# input_path = './1.jpeg'

# # Store path of the output image in the variable output_path 
# output_path = './output1.png'
# # Processing the image 
# input = Image.open(input_path) 

# # Removing the background from the given Image 
# output = remove(input) 

# #Saving the image in the given path 
# output.save(output_path) 
