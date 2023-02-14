import sys
import os
from PIL import Image
from steganographyFunctions import *

def project_name():
    print("----------------------")
    print("Hidden In Plain Sight")
    print("A tool to hide or reveal a message hidden in a file.")
    print("----------------------\n")


def get_action():
    print("This function can encode or decode a message in an image")
    print("To continue select from the following options and hit enter")
    print("1 Encode a message")
    print("2 Attempt to decode a message")
    print("To quit press any other key")
    print("What would you like to do", end=": ")
    action = input()
    os.system('cls')
    if (action == '1'):
        return 1
    elif (action == '2'):
        return 2
    else:
        return False


def get_message():
    print("Enter your message that you want to hide", end=": ")
    message = input()
    return message

# This function will check if the file is an image
def check_image(fileName):
    try:
        with Image.open(fileName) as img:
            image = isinstance(img, Image.Image)
            return image
    except FileNotFoundError as e:
        print(f"File {fileName} not found!", file=sys.stderr)

# This function will get the image from the user
def get_image(fileName=None):
    isImage = False
    # If the user has not entered a file name then we will ask them to enter one
    if not fileName:
        print("Please enter the name of image", end=": ")
        fileName = input()
    # If the user has entered a file name then we will check if it is an image
    while isImage != True:
        # If the file is not an image then we will ask the user to enter a new file name
        isImage = check_image(fileName)
        if isImage != True:
            print("Incorrect File selected"+fileName+".\nPlease enter your the name of the file", end=": ")
            fileName = input()
            os.system('cls')

    return fileName

def get_hidden_image():
    isImage = False
    print("Please enter the name of the file", end=": ")
    fileName = input()
    while isImage != True:
        isImage = check_image(fileName)
        if isImage != True:
            print("Incorrect File selected"+fileName+".\nPlease enter your the name of the file", end=": ")
            fileName = input()
            os.system('cls')

    return fileName

def find_the_message(fileName):
    image = Image.open(fileName)
    hidden_message = decoder(image)
    
    if(len(hidden_message) <= 1):
        print('No hidden message found')
        return False
    else:
        print('The hidden message is: ' + hidden_message)
        return hidden_message

def hide_the_message(message, fileName):
    print("Message to be hidden: "+ message + "\nInside this image: " + fileName)

    # Lets load the image
    image = Image.open(os.path.join(fileName))
    # now encode it

    newImg = encoder(image, message)
    
    # Save the image
    newName = 'encoded-'+fileName

    newImg.save(os.path.join(newName))

    print("Successfully saved the file")

    return newName

def confirmation():
    print("Do you want to proceed? Y/N", end=": ")
    confirmation = input()
    os.system('cls')
    if confirmation == 'Y':
        return True

    return False

