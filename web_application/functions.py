import os
from PIL import Image
from datetime import datetime
from steganographyFunctions import *

def check_image(fileName):
    try:
        f = open(fileName, 'r')
        with Image.open(fileName) as img:
            image = isinstance(img, Image.Image)
            return image
    except FileNotFoundError as e:
        return False

def get_image(fileName):
    isImage = False
    if not fileName:
        fileName = input()
    
    while isImage != True:
        isImage = check_image(fileName)
        if isImage != True:
            fileName = input()
            os.system('cls')

    return fileName


def get_hidden_image():
    isImage = False
    fileName = input()
    while isImage != True:
        isImage = check_image(fileName)
        if isImage != True:
            fileName = input()
            os.system('cls')

    return fileName

def find_the_message(fileName):
    image = Image.open(fileName)
    hidden_message = decoder(image)
    
    if(len(hidden_message) <= 1):
        return False
    else:
        return hidden_message

def hide_the_message(message, fileName, filePath):
    # Lets load the image
    image = Image.open(os.path.join(filePath))
    # now encode it

    newImg = encoder(image, message)
    
    # Save the image
    newName = 'encoded-'+datetime.now().strftime("%H%M%S")+'.'+fileName
    newImg.save(os.path.join('processed',newName))

    return newName