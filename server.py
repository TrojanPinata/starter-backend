### SETUP ###
# these are imported packages of code, in this case providing functionality to this webserver
import os
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

# define a new flask server instance reading a page at ./site/build/index.html
app = Flask(__name__, static_folder=os.path.join(os.getcwd(), "site", "build")) 
CORS(app)

### ENDPOINTS ###
# get image from url
@app.route('/api/get_image/<filename>', methods=['GET'])
def get_images(filename):
   return send_from_directory(filename)   # send file to frontend

# get list of images from directory structure
@app.route('/api/image_list/<directory>', methods=['GET'])
def get_image_list(directory):
   image_list = []
   for file in os.listdir(directory):  # for every image in directory
      if (file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".webp")):
         image_list.append(file) # add to list of filenames
   return jsonify(image_list)

# get 
@app.route('/api/directory_list', methods=['GET'])
def get_directory_list():
   #FIXME: implement
   return 

### LAUNCH ###
# Expression to start the server
if __name__ == '__main__':
   app.run(debug=True)