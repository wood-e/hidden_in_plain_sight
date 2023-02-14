
import numpy as np  

msg = "This message is what I want to hide"
if type(msg) == str:  
    result = ''.join([format(ord(i), "08b") for i in msg])  
elif type(msg) == bytes or type(msg) == np.ndarray:  
    result = [format(i, "08b") for i in msg]  
elif type(msg) == int or type(msg) == np.uint8:  
    result = format(msg, "08b")  
else:  
    print("Input type not supported")

print(result)