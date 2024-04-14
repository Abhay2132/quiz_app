from typing import Tuple
import customtkinter as ctk
import tkinter
class Quation_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master,border_width=2,border_color='white',width=700,height=400, **kwargs)
        qaution="who is prime minister of India"
        self.quation_label=ctk.CTkLabel(self,text=qaution,font=('Garamond',20),fg_color='white',text_color='black',width=500,height=200)
    def show(self):
        self.quation_label.grid(row=0,column=0,sticky='nesw',padx=20,pady=20)
        
class Round1(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.page_title=ctk.CTkLabel(self,text="STRAIGHT FORWARD",fg_color="transparent",font=('Garamond', 50),text_color="blue")
        self.round_title=ctk.CTkLabel(self,text='ROUND 1',fg_color="transparent",font=('Garamond',14),text_color="black")
        self.logo=ctk.CTkLabel(self,text='Logo',fg_color="white",width=50,height=50,text_color="red")
        self.quation_frame=Quation_Frame(self)
    def show(self):
        self.grid(row=0,column=0,padx=20,pady=20,sticky='nswe')

        self.page_title.grid(row=0, column=0, sticky='nsew', padx=20, pady=0)
        self.round_title.grid(row=1,column=0,sticky='nwe',padx=20,pady=0)
        self.quation_frame.grid(row=2, column=0, padx=20, pady=20)
        self.logo.grid(row=0,column=0,sticky='nw',padx=20,pady=20)
        self.quation_frame.show()
