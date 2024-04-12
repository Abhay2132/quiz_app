import customtkinter as ctk
from .frames.home import HomeFrame
from .frames.live import LiveFrame
from .frames.questions import QuestionsFrame
from .frames.participants import ParticipantsFrame
from .frames.settings import SettingsFrame
from PIL import Image
import os

from tktooltip import ToolTip
from CTkToolTip import *

ctk.set_appearance_mode("light")

class Obj(dict):
    def set(self, **kwargs):
        for key in kwargs:
            # self.__data[key] = kwargs[key]
            super().__setitem__(key, kwargs[key])
        return self
    
    def copy(self):
        return Obj(**self)

class SidePanel(ctk.CTkFrame):

    # children
    b_logo = None
    activeB = None
    b_home = None
    b_live = None
    b_questions = None
    b_participants = None
    b_settings = None

    # common property used by chldrens
    commons = Obj(
        anchor= "w",
        # height= 0,
        width=150,
        corner_radius= 5,
        fg_color= "transparent",
        hover_color= ("#bbb", "#333"),
        border_spacing=8,
        # text_color=("gray10", "gray90"),
        font=("calibri", 13),
        border_width = 0,
        text_color=("#333", "#eee")
    )

    # configure / style for action item
    activeConfig = {
        "fg_color" : ("#aaf", "#111"),
        "hover_color" : ("#aaf", "#111"),
    }

    # icon size of panel items
    iconSize = (15,15)

    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.configure(fg_color=("#ddd", "#444"), width=400)

        self.b_logo = ctk.CTkButton(self, text="LOGO", **self.commons.copy().set(fg_color="red", height=self.commons["width"]))
        self.b_home = self.button("HOME",self.click_home, ("home_dark.png", "home_light.png"))
        self.b_live = self.button("LIVE",self.click_live, ("live_dark.png", "live_light.png"))
        self.b_questions = self.button("QUESTIONS",self.click_questions, ("database_dark.png", "database_light.png"))
        self.b_participants = self.button("PARTICIPANTS",self.click_participants, ("users_dark.png", "users_light.png"))
        self.b_settings = self.button("SETTINGS",self.click_settings, ("settings_dark.png", "settings_light.png"))

        self.setActiveItem(self.b_home)

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
        app.mainPanel.setActiveFrame(app.mainPanel.homeFrame)
        self.setActiveItem(self.b_home)

    def click_live(self):
        app.mainPanel.setActiveFrame(app.mainPanel.liveFrame)
        self.setActiveItem(self.b_live)

    def click_questions(self):
        app.mainPanel.setActiveFrame(app.mainPanel.questionsFrame)
        self.setActiveItem(self.b_questions)

    def click_participants(self):
        app.mainPanel.setActiveFrame(app.mainPanel.participantsFrame)
        self.setActiveItem(self.b_participants)

    def click_settings(self):
        app.mainPanel.setActiveFrame(app.mainPanel.settingsFrame)
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
        self.b_questions.pack(side=ctk.BOTTOM,fill=ctk.X, **commons)

        self.grid(row=0, column=0, stick="nsw")

class MainPanel(ctk.CTkFrame):
    homeFrame = None
    liveFrame = None
    questionsFrame = None
    participantsFrame = None
    settingsFrame = None

    def setActiveFrame(self, frame):
        app.mainPanel.activeFrame.grid_forget()
        app.mainPanel.activeFrame = frame
        app.mainPanel.activeFrame.show()

    def __init__(self, master, **kwargs):
        super().__init__(master=master, fg_color="green", **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.homeFrame = HomeFrame(self)
        self.liveFrame = LiveFrame(self)
        self.questionsFrame = QuestionsFrame(self)
        self.participantsFrame = ParticipantsFrame(self)
        self.settingsFrame = SettingsFrame(self)

        self.activeFrame = self.homeFrame

    def show(self):
        self.activeFrame.show()
        self.grid(row=0, column=1, stick="nswe")

class App(ctk.CTk):
    HEIGHT = 400
    WIDTH = 800
    side_panel_width = 300

    def __init__(self):
        super().__init__()
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # self.topBar = TopBar(self)
        self.sidePanel = SidePanel(self, width=self.side_panel_width)
        self.mainPanel = MainPanel(self)

    def show(self):
        # self.topBar.show()
        self.sidePanel.show()
        self.mainPanel.show()
        self.mainloop()

app = None

def start():
    global app
    app = App()
    app.show()

if __name__ == "__main__":
    start()