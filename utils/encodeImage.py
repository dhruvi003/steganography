from tkinter import *
from encryption import main_encryption

def encode_image():
    root = Tk()
    encode_ig = Toplevel(root)
    encode_ig.title("Encode an Image")
    encode_ig.geometry('600x200')
    encode_ig.resizable(0,0)
    encode_ig.config(bg = 'black')

    label1 = Label(encode_ig, text = "Encode an Image", font=('Comic Sans MS',15), bg='AntiqueWhite')
    label1.place(x=220, rely=0)
    Label(encode_ig, text='Enter the path to the image(with extension):', font=("Times New Roman", 13),
          bg='AntiqueWhite').place(x=10, y=50)
    Label(encode_ig, text='Enter the data to be encoded:', font=("Times New Roman", 13), bg='AntiqueWhite').place(
        x=10, y=90)
    Label(encode_ig, text='Enter the output file name (without extension):', font=("Times New Roman", 13),
          bg='AntiqueWhite').place(x=10, y=130)

    img_path = Entry(encode_ig, width=35)
    img_path.place(x=350,y=50)

    text_to_be_encoded = Entry(encode_ig, width=35)
    text_to_be_encoded.place(x=350, y=90)

    after_save_path = Entry(encode_ig, width=35)
    after_save_path.place(x=350, y=130)

    Button(encode_ig, text='Encode the Image', font=('Helvetica', 12), bg='PaleTurquoise', command=lambda:main_encryption(img_path.get(), text_to_be_encoded.get(), after_save_path.get())).place(x=220, y=175)
