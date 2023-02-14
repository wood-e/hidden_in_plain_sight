#Week 4
## Getting a move on
This week I needed to get a move on with my PCP, I've fallen behind and promised that I would have a working version to test out this week and provide a video with it working.

Here is my video of my tool working 

This week I needed to implement the handling of images, I'm already using Pillow, a pythong library, but I still needed to learn how to actually use it. Some quick googling and I found a tutorial on how to use Pillow.

I've created the function to handle the following

- User inputs the message they want hidden
- User enters the name of the image to be used 
-- This checks to see if the file exists
-- This checks to see if the file is an image

- System will then ask for confirmation to hide the message in the file
- User will type y/n  to continue or not


Once each criteria is met, it will then try and encrypt the file using Pillow to modify the image.

using [image.save()](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save)



Citation

Image Processing With the python Pillow Library. Real Python, https://realpython.com/image-processing-with-the-python-pillow-library/
ImageTK Module, Pillow, https://pillow.readthedocs.io/en/stable/reference/ImageTk.html