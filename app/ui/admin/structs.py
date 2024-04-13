import customtkinter as ctk
from ...lib.util import Obj, UI

class _SideFrame(ctk.CTkFrame, UI):
    
    activeB = None
    b_logo = None
    b_home = None
    b_live = None
    b_qb = None
    b_participants = None
    b_settings = None
    commons=None
    iconSize = (15,15)
    commons = Obj(
        anchor= "w",
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
    activeConfig = {
        "fg_color" : ("#aaf", "#111"),
        "hover_color" : ("#aaf", "#111"),
    }

    def setActiveItem(self, item):
        pass

class _MainFrame(ctk.CTkFrame,UI):
    f_home = None
    f_live = None
    f_qb = None
    f_participants = None
    f_settings = None
    activeFrame=None

    def setActiveFrame(self, frame):
        pass


class _App(ctk.CTk, UI):
    f_main:_MainFrame=None
    f_side:_SideFrame=None
    app=None
    pass