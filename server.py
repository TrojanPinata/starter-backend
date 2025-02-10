### SETUP ###
import os
from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS

project_name = "site"

# define a new flask server instance reading a page at ./site/build/index.html
app = Flask(__name__, static_folder=os.path.join(os.getcwd(), project_name, "build")) 
CORS(app, resources={r"/api/*": {"origins": "*"}})
image_dir = os.path.join(os.getcwd(), "images") # directory all image subfolders will be located in

### ENDPOINTS ###
# get image from url
@app.route('/api/get_image/<path:filename>', methods=['GET'])
def get_images(filename):
   target_dir = os.path.abspath(os.path.join(image_dir, filename))

   if not target_dir.startswith(image_dir):
      return jsonify({"error": "Access Denied"}), 403

   return send_from_directory(image_dir, filename)   # send file to frontend

# get list of images from directory structure
@app.route('/api/image_list/<path:directory>', methods=['GET'])
def get_image_list(directory):
   target_dir = os.path.abspath(os.path.join(image_dir, directory))

   if not target_dir.startswith(image_dir) or not os.path.isdir(target_dir):  # ensure target directory exists and is on current path
      return jsonify({"error": "Access Denied"}), 403 # else, deny it

   image_list = []
   for file in os.listdir(target_dir):  # for every image in directory
      if file.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif', '.svg', '.apng', '.avif')):  # make sure each file is a image
         image_list.append(file) # add to list of filenames
   return jsonify(image_list)

# get all directories 
@app.route('/api/directory_list', methods=['GET'])
def get_directory_list():
   directory_list = []
   for root, dirs, files in os.walk(image_dir):
      rel_path = os.path.relpath(root, image_dir)
      directory_list.append(rel_path if rel_path != "." else "/")
   return jsonify(directory_list)

### LAUNCH ###
# send index.html when queried
@app.route("/")
def serve_react():
   return send_from_directory(app.static_folder, "index.html")

# send static css/js/whatever if queried
@app.route("/static/<path:path>")
def serve_static(path):
   return send_from_directory(os.path.join(app.static_folder, "static"), path)

# send css/js/whatever if queried
@app.route("/<path:path>")
def serve_assets(path):
   return send_from_directory(app.static_folder, path)

# minor error handling
@app.errorhandler(404)
def not_found(e):
   return send_from_directory(app.static_folder, "index.html") # 404? send back index.html

# Expression to start the server
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, ssl_context=None)