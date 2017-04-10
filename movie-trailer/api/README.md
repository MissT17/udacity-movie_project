# website_project

This program allows to dynamically create/generate a webpage with the list of user's favourite movies. The list of movies is created directly on the fly from the user inputs (titles of the movies). The links to the movie trailers, the short description of the films as well as the poster images are then imported from [youtube] (https://www.youtube.com/) and from a movie database, [omdb] (http://www.omdbapi.com/). By hovering the movie images the user can read the description of each movie and watch the video trailers by clicking on corresponding film poster images. 

# Directory Structure

In the github *website_project/api* repository you will find the following files:
  1. media.py - the file contains all the information related to the `class Movie()`
  2. hidden.py - this file contains the key information related to the developer youtube API account. Please read the **__Installation__** section below to find out how to insert your KEY in the file and run the program.   
  3. youtube_video_api.py - contains the function that allows to do the search of the corresponding video trailers on youtube via the API.
  4. test_api.py - the core file of the API integration, it allows to dynamically construct the queries that are used to retrieve the data  from Youtube and OMDB (the title of the films, their short descriptions, the poster images and the youtube video trailers.
  5. fresh_tomatoes.py - contains all the HTML, CSS, JS, PYTHON code that allows to design, generate and create the .html file in the *templates* folder
  6. server.py - contains the methods related to *flask*. Flask is used to create a server environment allowing to receive the user request in terms of the films that he/she would like to display on the page, run this information through the program and return the html page to the browser.
  7. templates folder contains a user_input.html file that display the form that the users fill in with the titles of their favourite movies.
  8. README.md - contains a short "How To" which I hope you are enjoying right now.

# Installation

1. Download the files from the github repository. It's important that *all* the files are saved within the same folder on your computer.
2. Open hidden.py in any text editor and insert your Youtube API Key into the follwoing field `os.environ['API_KEY'] = ' YOUR KEY GOES HERE'`. Save the file.  
3. Open the Terminal on your machine (if you use Mac: go to Applications > iTerm, on Windows machines it corresponds to...)
4. In the terminal navigate to the folder that contains the downloaded documents and open the server.py file: `python server.py`
   The terminal will provide you with the adress that you need to insert into the browser to start the program.
   ```
     Running on **http://127.0.0.1:5000/** (Press CTRL+C to quit)
   * Restarting with stat
   * Debugger is active!
   * Debugger PIN: 129-045-349
   ```
   At this point you should see a form in the browser.

# Requirements
1. Please make sure that a 2.7 version of Python is installed on your machine (as the code is adapted to this version of Python). In order to check if you have the necessary Python version installed:
  1. Open the terminal on your computer (if you use Mac: go to Applications > iTerm, on Windows machines it corresponds to...) 
  2. Type `python` or `python --v` in the command line, which should provide you with something similar to: 
  ```
  Python 2.7.5 (default, Jun 17 2014, 18:11:42)
  [GCC 4.8.2 20140120 (Red Hat 4.8.2-16)] on linux2
  Type “help”, “copyright”, “credits” or “license” for more information.
  ``` 
If there is no Python installed, please install it on your machine. You can find the necessary links for download here:
[Python](https://wiki.python.org/moin/BeginnersGuide/Download)
2. Please check if you also have Flask installed on the machine. If that is not the case, please follow the following guidelines [here] (https://pypi.python.org/pypi/Flask/0.12).
3. You will also need to open a developer youtube API account. Please follow a quick guide here: (https://youtu.be/Im69kzhpR3I) 
4. You would also need to know what the IP adress of your machine is. To quickly find out this information, you can visit the following website: (http://whatismyipaddress.com/) or just type *My IP* in Google and it will provide with a set of numbers. 

# Expected Outcome

Once the form appears in the browser, fill in the corresponding fields with the titles of your favourite movies. (Please make sure the spelling is correct), then click **__Submit__** On click a new page will open up with your favourite movies displayed. By clicking on the poster images, you will activate the video trailer which will be displayed in the center of the page. The video will start automatically once you click on the poster and the player window opens. The video will stop automatically and the player will be closed, if you click outside the video window or close the player. On hovering the images, a short description of the movie will be displayed over the poster. 

# License

The *fresh_tomatoes.py* code was provided by Udacity in its course, the rest of the files were created by the owner of this repository on the basis of the introductory course to Python class given by Udacity. All poster images and descriptions are provided by OMDB and the trailers are taken from youtube.


