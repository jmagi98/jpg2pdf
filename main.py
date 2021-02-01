import os
from PIL import Image


path, dirs, files = next(os.walk("./"))
num_of_images = len(files) - 1
img_arr = []
im0 = None

for i in range(num_of_images):
    num = i+1
    filename = ""
    if (len(str(num)) == 1):
        filename = "00"+str(num)+".jpg"
    if (len(str(num)) == 2):
        filename = "0"+str(num)+".jpg"
    if (len(str(num)) == 3):
        filename = str(num)+".jpg"
    im = Image.open(r'./'+filename)
    image = im.convert('RGB')
    if i != 0:
        img_arr.append(image)
    else:
        im0 = image

im0.save(r'./output.pdf', save_all=True, append_images=img_arr)
