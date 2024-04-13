import customtkinter as ctk
# from .utils import rc``

# class HomeFrame(cctk.CTkFrame):
#     def __init__(self, master, **kw):
#         super().__init__(master=master, fg_color=rc(), **kw)
#         self.label = cctk.CTkLabel(self, text="HOME")

#     def show(self):
#         self.label.place(relx=0.5, rely=0.5)
#         self.grid(row=0, column=0, sticky="nswe")

from ....lib.util import UI
from ..structs import _App

class HomeFrame(ctk.CTkFrame, UI):
    app=None
    def __init__(self, master,app:_App, **kwargs):
        super().__init__(master=master, **kwargs)
        self.app = app
        
        self.configure(fg_color="#fff",height=500, width=600)
        self.l_logo = ctk.CTkLabel(self, height=300, width=300,fg_color="#aaa", text="")#, image=self.logo_photo, borderwidth=0)
        self.l_title = ctk.CTkLabel(self, text="- Parashan Baan -", font=("sans", 20))
        self.b_start = ctk.CTkButton(self,height=40, width=200,text="Start", command=self.start_action,fg_color="green", font=("sans", 15))# bg="#007bff", fg="white", width=29, relief=ctk.FLAT)
        self.b_settings = ctk.CTkButton(self, height=40, width=200, text="⚙️ Settings", command=self.settings_action, fg_color="blue", font=("sans", 15))# bg="#28a745", fg="white", width=29, relief=ctk.FLAT)
    
    def start_action(self):
        self.app.f_main.setActiveFrame(self.app.f_main.f_live)
        self.app.f_side.setActiveItem(self.app.f_side.b_live)

    def settings_action(self):
        self.app.f_main.setActiveFrame(self.app.f_main.f_settings)
        self.app.f_side.setActiveItem(self.app.f_side.b_settings)

    def show(self):
        self.grid(row=0, column=0)
        self.l_logo.grid(row=0, column=0, padx=100, pady=(100, 10))
        self.l_title.grid(row=1, pady=(10, 50))
        self.b_start.grid(row=2, column=0,pady=10)
        self.b_settings.grid(row=3, column=0, pady=(0, 40))