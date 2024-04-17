import os
from PIL import Image
import customtkinter as ctk

def set_option_selected(l_option):
    # l_option.configure(border_color="#4169E1", )
    l_option.configure(fg_color="#4169E1", text_color="#fff", hover_color="#4169E1")

def set_option_normal(l_option):
    # l_option.configure(border_color="#888")
    l_option.configure(fg_color="transparent", text_color="#000", hover_color="#eee")

def set_option_correct(l_option):
    # l_option.configure(border_color="green")
    l_option.configure(fg_color="#00A36C", hover_color="#00A36C", text_color="#fff")
    # l_option.configure("")

def createLogo(self, imgPath):
    image = Image.open(imgPath)
    width, height = image.size
    l_width=int(self.icon.cget("width"))
    height = height/width*l_width
    print(f"{width}x{height}")
    image = ctk.CTkImage(image, size=(l_width,height))
    self.icon.configure(image=image, text="")