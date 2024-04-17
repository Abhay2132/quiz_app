from random import choice
import customtkinter as ctk
from PIL import Image

cc = list([str(i) for i in range(0,10)]) + ['a','b','c', 'd', 'e', 'f']
rc = lambda : ("#"+"".join([choice(cc) for i in range(0,6)]))


def setImage(imgPath, target:ctk.CTkLabel):
        image = Image.open(imgPath)
        width, height = image.size
        l_width=int(target.cget("width"))
        height = height/width*l_width
        print(f"{width}x{height}")
        image = ctk.CTkImage(image, size=(l_width,height))
        target.configure(image=image, text="")