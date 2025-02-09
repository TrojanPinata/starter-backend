# Starting Files for Web Design
This is a repository for getting beginner web developers familiar with endpoints and sending requests to a backend. This guide assumes the reader has never used Python before or installed Node/built a page before.  I believe it is easier to learn something when attempting to make something you are interested in rather than taking baby steps and doing prompted work.

So far this repository ahs the following endpoints:
- `/api/get_image` - takes in a filepath and returns a image
- `/api/image_list` - takes in a directory and returns a list of all found images in provided directory
- `/api/directory_list` - returns a list of all found directories
- `/api/get_version` - returns the version of the backend

More endpoints wil probably be added in the future, but the first version of this site was made to display images and not much else.

## To Run
To run the flask server which will host your backend, you need to have python, pip, and some necessary packages installed. [A good guide to do this is here](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/). If you believe you already have python and pip installed, try these commands to check everything is ready for the next steps: 
```
python --version     # this checks that python is installed. you should get a version number (e.g. 3.11.0)
pip --version        # same thing, just make sure the output is not a error
```
Once those are working, preform the following to start the backend.
```
python -m venv server      # make virtual environment ('server' can be changed to any name)
source server/bin/activate # start virtual environment
pip install flask          # to install flask server

python server.py           # run page stored in ./site/build/index.html
```

## Short Guide on Starting and Building ReactJS Page
I am writing this short guide and some example files in ReactJS, as that is what I am most familiar with, but any framework will work with this as long as it is Node based and produces a index.html file in a build directory. The goal with this is simply to demonstrate a very basic version of what I hope a user can accomplish with this repository.

Before anything, make sure to install Node.js.
```

```
