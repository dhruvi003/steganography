from tkinter import *
import tkinter.filedialog
from tkinter import messagebox
from utils import encodeImage as encode_imagae
from utils import decodeImage as decode_image

root = Tk()
root.title('Image Stegeanography Project')
root.geometry('600x500')
root.resizable(0,0)

root.config(bg='sienna3')
# label = Label(root, text = "Welcome!", fg = 'black')
# label.pack()

label1 = Label(root, text = 'Welcome to my App', font=('Comic sans MS',30), bg='NavajoWhite',wraplength=400)
label1.place(x=40, y=10)

button_encode = Button(root, text='Encode', width=25, font=('Times New Roman',15), bg='SteelBlue', command=encode_imagae)
button_encode.place(x=40, y=80)

button_decode = Button(root, text='Decode', width=25, font=('Times New Roman', 15),bg='SteelBlue', command=decode_image)
button_decode.place(x=40, y=130)

root.update()
root.mainloop()