# Starting Files for Web Design
This is a repository for getting beginner web developers familiar with endpoints and sending requests to a backend. This guide assumes the reader has never used Python before or installed Node/built a page before.  I believe it is easier to learn something when attempting to make something you are interested in rather than taking baby steps and doing prompted work.

So far this repository ahs the following endpoints:
- `/api/get_image` - takes in a filepath and returns a image
- `/api/image_list` - takes in a directory and returns a list of all found images in provided directory
- `/api/directory_list` - returns a list of all found directories
- `/api/get_version` - returns the version of the backend

More endpoints wil probably be added in the future, but the first version of this site was made to display images and not much else.

I also should make clear, this site is not made for external deployment, and is only for development and learning purposes. The endpoints are not secured and there is no SSL other than what your browser provides. Do not open this to the greater internet, only use this as a educational tool for learning how to write Javascript and develop a practical website.

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

Optionally, for a really quick start to see what this project is all about, my original build directory is stored with a few test images to show off how image loading works.


## Short Guide on Starting and Building ReactJS Page
I am writing this short guide and some example files in ReactJS, as that is what I am most familiar with, but any framework will work with this as long as it is Node based and produces a index.html file in a build directory. The goal with this is simply to demonstrate a very basic version of what I hope a user can accomplish with this repository.

Before anything, make sure to install Node.js. This will allow you to use a number of different frameworks and packages that will be essential for web development. Then [follow this guide](https://create-react-app.dev/docs/getting-started/). It feels kind of cheap, but this guide makes it really easy to bootstrap a project quickly and efficiently. You can either use that, or build off of my example by editing my files. Regardless, under the `site` folder (or whatever you called your project), run `npm install` to install the core node/react packages. From here, you can change anything you want, then compile by running `npm run build`. If making a new project, open server.py and change `project_name` to the name of your new project folder.
