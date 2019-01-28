import os, sys
from PIL import Image

binary_str = ''
for idx,frame in enumerate(sorted(os.listdir('./frames'))):
    if idx == 144:
        break
    try:
        result = "./frames/" + frame
        img = Image.open(result)
        # Convert image to white and black
        img = img.convert('1')
        pix = img.load()

        if pix[0, 0] == 0:
            binary_str += '1'
        else:
            binary_str += '0'
    except Exception as e:
        print(e)

print("Binary: {}\n".format(binary_str))
n = int('0b'+binary_str, 2)
flag = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

# We add the missing '}' ;)
print("Flag: {}".format(flag+"}"))
