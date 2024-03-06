# endoce data to new image that will be created
from PIL import Image
from generateData import generate_data
from tkinter import messagebox as mb

def encryption(img, data):
    size = img.size[0]
    (x,y) = (0,0)

    for pixel in generate_data(img.getdata(),data):
        img.putpixel((x,y),pixel)
        if size-1 == x:
            x = 0; y+=1
        else:
            x += 1

def main_encryption(img, text, new_image_name):

    image = Image.open(img, 'r')

    if(len(text) == 0) or (len(img) == 0) or (len(new_image_name) == 0):
        mb.showerror("You have not put value")

    new_image = image.copy()
    encryption(new_image,text)

    new_image_name += '.png'

    new_image.save(new_image_name, 'png')

