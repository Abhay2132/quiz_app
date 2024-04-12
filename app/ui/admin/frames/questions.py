import customtkinter as ctk
from .utils import rc

class QuestionsFrame(ctk.CTkFrame):
    def __init__(self, master, **kw):
        super().__init__(master=master, fg_color=rc(), **kw)
        
        self.label = ctk.CTkLabel(self, text="QUESTIONS")

    def show(self):
        self.label.place(relx=0.5, rely=0.5)
        self.grid(row=0, column=0, sticky="nswe")