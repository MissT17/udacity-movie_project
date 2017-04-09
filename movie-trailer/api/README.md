# website_project

This program allows to dynamically create a webpage with the list of movies that were stored beforehand. Each movie is represented by a poster image with its title, its short description and allows the user to watch a trailer of a video by clicking on an image. 

# Directory Structure

In the github *website_project* repository you will find four files:
  1. media.py - the file contains the information related to the `class Movie()`
  2. entertainment_center.py - this files contains the list of all the movies displayed on the webpage
  3. fresh_tomatoes.py - contains all the HTML, CSS, JS, PYTHON code that allows to design the webpage, request the information from the entertainment_center.py file, display its contents and open it in the browser
  4. README.md - contains a short "How To" which I hope you are enjoying right now.

# Installation

1. Download the files from the github repository. It's important that *all* the files are saved within the same folder on your computer.
2. Open the Terminal on your machine.
3. Navigate to the folder that contains the downloaded files.
4. Run the entertainment_center.py file.

# Requirements
Please make sure that a 2.7 version of Python is installed on your machine (as the code is adapted to this version of Python). In order to check if you have the necessary Python version installed:
  1. Open the terminal on your computer
  2. Run `python` or `python --v` in the command line, which should provide you with something similar to: 
  
> Python 2.7.5 (default, Jun 17 2014, 18:11:42)

> [GCC 4.8.2 20140120 (Red Hat 4.8.2-16)] on linux2

> Type “help”, “copyright”, “credits” or “license” for more information.

If there is no Python installed, please install it on your machine. You can find the necessary links for download here:
[Python](http://www....com)

# Expected Outcome

On running the *entertainment_center.py* file, a new tab will open in your browser and a webpage with the posters of my favourite movies will be displayed. By clicking on the poster images, you will activate the video trailer which will be displayed in the center of the page. The video will start automatically once you click on the poster and the player window opens. The video will stop automatically and the player will be closed, if you click outside the video window or close the player. On hovering the images, a short description of the movie will be displayed over the poster. 

# License

The *fresh_tomatoes.py* code was provided by Udacity in its course, the rest of the files were created by the owner of this repository on the basis of the introductory course to Python class given by Udacity. All poster images were taken from Wikipedia, just like the short descriptions od the films.


