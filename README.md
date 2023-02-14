
# Hidden in Plain Sight

This project is to demonstrate the use of steganography. The project can be used in two ways. Command line, or via a website.




## Authors

- [@wood-e](https://github.com/wood-e)

# Steganography functions
The main functions for this application that relate to steganography are within the `steganographyFunctions.py` file located within the root directory.

## Installation

This program requires python to be installed. 

This was tested using Python V3.10.10 on Windows 11.

To install Python by navigating to [Python For Beginners](https://learn.microsoft.com/en-us/windows/python/beginners) 

Once Python is installed open to the project directory and create a [venv environement](https://docs.python.org/3/library/venv.html)

Once that has been created you can activate the environment.

```bash
   venv\Scripts\activate
```

Now you can install the required packages with pip.
```bash
   pip install -r requirements
```
Once the requirements have been downloaded you can now run the program.

## Running the Application
### Console
To execute the console commands you must navigate to `console_application`
There is an image provided within the folder for you to use. You can however use any **PNG** file.

```bash
   cd console_application
```

There are three command line applications, the first has both functions built in to it and the second and third are split functions.

```bash
   python steganography.py
```

```bash
   python encode.py -h
   python decode.py -h
```
## Web application
The website is run by using Flask. To run the application navigate to `web_application` directory and start Flask.

```bash
   cd web_application
   Flask run
```

The output in the console will display the url for the application with 
```
 * Debug mode: off
   WARNING: This is a development server. 
   Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
   Press CTRL+C to quit
```

I've provided a png file called mydog.png which has not been modified, however you can use any png file to encode a message.