# This function will convert the data passed into binary format
# Example: Hidden
# Binary: ['01001000', '01101001', '01100100', '01100100', '01100101', '01101110']
def convert_to_binary(data):
    new_data = []
    for i in data:
        # Convert the data to binary and append it to the list
        new_data.append(format(ord(i), '08b'))
    return new_data

# This function modifies the pixel of the image and places the binary 
def modify_Pixel(pixel, message):
    # Get the binary of the message
    dataList = convert_to_binary(message)
    # Get the length of the converted message
    dataLen = len(dataList)
    # Get the iterator of the image
    imgData = iter(pixel)
    # Create a list to store the modified pixels
    modified_pixels = []

    # Loop through the message
    for i in range(dataLen):
        pixel = []
        # Get 3 pixels at a time
        for j in range(3):
            pixel += imgData.__next__()[:3]

        for j in range(8):
            # If the message is 0, then we need to change the last bit to 0
            if dataList[i][j] == '0' and pixel[j] % 2 != 0:
                pixel[j] -= 1
            # If the message is 1, then we need to change the last bit to 1
            elif dataList[i][j] == '1' and pixel[j] % 2 == 0:
                pixel[j] -= 1
        
        # If the message is over, then we need to change the last pixel
        if i == dataLen - 1:
            if pixel[-1] % 2 == 0:
                pixel[-1] -= 1
        else:
            # If the message is not over, then we need to change the last pixel
            if pixel[-1] % 2 != 0:
                pixel[-1] -= 1
        # Convert the pixel back to a tuple
        pixel = tuple(pixel)
        # Append the modified pixel to the list
        modified_pixels.extend([pixel[:3], pixel[3:6], pixel[6:9]])

    return modified_pixels

# This function will encode the message into the image
def encoder(image, data):
    # Get the size of an image
    w = image.size[0]
    # Set the starting point of X and Y of an image
    (x, y) = (0, 0)
    # Iterate over each pixel from the modify_pixel function using the data from the Image
    # getdata() returns a sequence of values representing the color of each
    # https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.getdata
    for pixel in modify_Pixel(image.getdata(), data):
        # Each pixel returned is placed within x, y
        image.putpixel((x, y), pixel)
        # If the X is the width of the image then set X to 0 and increment Y by 1
        # This allows us to move around the image pixel by pixel
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1
    # Return the modified pixel
    return image

# This function will decode the message from the image
def decoder(image):
    # Get the iterator of the image
    image_data = iter(image.getdata())
    data = ''

    while (True):
        # Get 3 pixels at a time
        pixels = []
        for i in range(3):
            pixels += image_data.__next__()[:3]
        
        binary_str = ''
        # Get up to the 8th pixel
        for i in pixels[:8]:
            # If the pixel is even then add a 0 to the binary string
            if i % 2 == 0:
                binary_str += '0'
            # If the pixel is odd then add a 1 to the binary string
            else:
                binary_str += '1'
        # Convert the binary to ASCII
        data += chr(int(binary_str, 2))
        # If the last pixel is odd then stop and return the data
        if pixels[-1] % 2 != 0:
            return data