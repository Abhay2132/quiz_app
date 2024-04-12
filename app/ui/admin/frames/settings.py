import customtkinter as ctk
from .utils import rc

class SettingsFrame(ctk.CTkFrame):
    def __init__(self, master, **kw):
        super().__init__(master=master, fg_color=rc(), **kw)
        
        self.label = ctk.CTkLabel(self, text="SETTINGS")

    def show(self):
        self.label.place(relx=0.5, rely=0.5)
        self.grid(row=0, column=0, sticky="nswe")