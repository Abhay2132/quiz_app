import customtkinter as ctk
from .frames.home import HomeFrame
from .frames.live import LiveFrame
from .frames.qb import QBFrame
from .frames.participants import ParticipantsFrame
from .frames.settings import SettingsFrame
from PIL import Image
import os
from tktooltip import ToolTip
from CTkToolTip import *
from ...lib.util import Obj
from .structs import _App, _SideFrame, _MainFrame

ctk.set_appearance_mode("light")


class SidePanel(_SideFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.configure(fg_color=("#fff", "#444"), width=400)
        self.parent = master

        self.b_logo = ctk.CTkButton(self, text="LOGO", **self.commons.copy().set(fg_color="red", height=self.commons["width"]))
        self.b_home = self.button("HOME",self.click_home, ("home_dark.png", "home_light.png"))
        self.b_live = self.button("LIVE",self.click_live, ("live_dark.png", "live_light.png"))
        self.b_qb = self.button("QUESTIONS",self.click_questions, ("database_dark.png", "database_light.png"))
        self.b_participants = self.button("PARTICIPANTS",self.click_participants, ("users_dark.png", "users_light.png"))
        self.b_settings = self.button("SETTINGS",self.click_settings, ("settings_dark.png", "settings_light.png"))

        # self.setActiveItem(self.b_home)

    def button(self, text, cmd,icons:tuple):
        light, dark = icons
        img = ctk.CTkImage(
            light_image=Image.open(os.path.join(os.path.dirname(__file__), "icons", light)),
            dark_image=Image.open(os.path.join(os.path.dirname(__file__),"icons", dark)),
            size=self.iconSize
        )
        btn =  ctk.CTkButton(
            self,
            text=f"  {text}     ", 
            image=img,
            command=cmd,
            **self.commons
        )
        CTkToolTip(btn, message=text, delay=0.1, corner_radius=5)    
        return btn
    
    def click_home(self):
        app = App.me
        app.f_main.setActiveFrame(app.f_main.f_home)
        self.setActiveItem(self.b_home)

    def click_live(self):
        app = App.me
        app.f_main.setActiveFrame(app.f_main.f_live)
        self.setActiveItem(self.b_live)

    def click_questions(self):
        app = App.me
        app.f_main.setActiveFrame(app.f_main.f_qb)
        self.setActiveItem(self.b_qb)

    def click_participants(self):
        app = App.me
        app.f_main.setActiveFrame(app.f_main.f_participants)
        self.setActiveItem(self.b_participants)

    def click_settings(self):
        app = App.me
        app.f_main.setActiveFrame(app.f_main.f_settings)
        self.setActiveItem(self.b_settings)

    def setActiveItem(self, item):
        if self.activeB:
            self.activeB.configure(**self.commons)
        self.activeB = item
        self.activeB.configure(**self.activeConfig)

    def show(self):
        commons = Obj(
            padx=5,
            pady=2
        )
        self.b_logo.pack(fill=ctk.X, **commons.copy().set(pady=8))
        self.b_home.pack(fill=ctk.X, **commons)
        self.b_live.pack(fill=ctk.X, **commons)
        self.b_participants.pack(fill=ctk.X, **commons)
        self.b_settings.pack(fill=ctk.X, side=ctk.BOTTOM, **commons)
        self.b_qb.pack(side=ctk.BOTTOM,fill=ctk.X, **commons)

        self.grid(row=0, column=0, stick="nsw")

class MainPanel(_MainFrame):

    def setActiveFrame(self, frame):
        if self.activeFrame:self.activeFrame.grid_forget()
        self.activeFrame = frame
        self.activeFrame.show()

    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.parent = master

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.configure(fg_color="#dfdfdf")
        self.f_home = HomeFrame(self,app=master)
        self.f_live = LiveFrame(self,app=master)
        self.f_qb = QBFrame(self,)
        self.f_participants = ParticipantsFrame(self,)
        self.f_settings = SettingsFrame(self,)

    def show(self):
        self.activeFrame.show()
        self.grid(row=0, column=1, stick="nswe")

class App(ctk.CTk):
    f_main:MainPanel=None
    f_side:SidePanel=None
    f_side_width = 300
    # app:_App= None
    me=None

    def __init__(self):
        super().__init__()
        App.me = self
        self.geometry("800x600")
        self.after(10, lambda:self.state("zoomed"))
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # self.topBar = TopBar(self)
        self.f_side = SidePanel(self, width=self.f_side_width, fg_color="#fff")
        self.f_main = MainPanel(self)
        
        self.f_side.setActiveItem(self.f_side.b_home)
        self.f_main.setActiveFrame(self.f_main.f_home)

        _App.app=self

    def show(self):
        # self.topBar.show()
        self.f_side.show()
        self.f_main.show()
        self.mainloop()

app = None

def start():
    global app
    app = App()
    app.show()

if __name__ == "__main__":
    start()