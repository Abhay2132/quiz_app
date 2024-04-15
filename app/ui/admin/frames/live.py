import customtkinter as ctk
from random import choice
from ..structs import _App
from ....lib.struct import ADMIN
from ...rounds.round1 import Round1
from ...rounds.round2 import Round2
from ...rounds.round3 import Round3
from ...rounds.round4 import Round4

class StartFrame(ctk.CTkFrame):

    def __init__(self, master, **kw):
        super().__init__(master=master, fg_color="transparent", **kw)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.f_rounds = RoundsFrame(self)
        self.f_participants = Participants(self)

    def show(self):
        self.grid(row=0, column=0, sticky="nswe")
        self.f_rounds.show()
        self.f_participants.show()

class Rounds(ctk.CTkFrame):

    def item(self, name, description):
        frame = ctk.CTkFrame(self, border_width=2, fg_color="#fff")
        l_name = ctk.CTkLabel(frame,font=("Roboto", 17),text_color="blue", anchor="w", text=name, fg_color="transparent")
        l_desc = ctk.CTkLabel(frame,font=("Roboto", 12),height=20,text_color="#555", anchor="w", text=description, fg_color="transparent")

        frame.grid_columnconfigure(0, weight=1)
        l_name.grid(row=0, column=0, padx=10, pady=5, sticky="we")
        l_desc.grid(row=1, column=0, padx=20, pady=(0,5), sticky="we")
        return frame

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(border_width=2, fg_color="#eee")
        self.grid_columnconfigure(0, weight=1)

        self.f_m1 = self.item("Straight Forward", " • Max Points : 50      • Duration : 20s ")
        self.f_m2 = self.item("Bujho Toh Jano", " • Max Points : 50      • Duration : 30s ")
        self.f_m3 = self.item("Roll the Dice", " • Max Points : 50      • Duration : 30s ")
        self.f_m4 = self.item("Speedo Test", " • Max Points : 50      • Duration : 30s ")
        # self.f_m2 = ctk.CTkFrame(self, border_width=2)
        # self.f_m3 = ctk.CTkFrame(self, border_width=2)
        # self.f_m4 = ctk.CTkFrame(self, border_width=2)

    def show(self):
        self.grid(row=1, column=0, sticky="nswe", columnspan=2,padx=10)

        self.f_m1.grid(row=0, column=0, sticky="we", padx=10, pady=(10,0))
        self.f_m2.grid(row=1, column=0, sticky="we", padx=10, pady=(10,0))
        self.f_m3.grid(row=2, column=0, sticky="we", padx=10, pady=(10,0))
        self.f_m4.grid(row=3, column=0, sticky="we", padx=10, pady=(10,0))

class RoundsFrame(ctk.CTkFrame):
    def __init__(self, master:ctk.CTkFrame, **kwargs):
        super().__init__(master=master, **kwargs)
        self.grid_propagate(False)
        self.configure(border_width=2, border_color="#888", fg_color="#fff")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.l_title = ctk.CTkLabel(self, text="MODULES", anchor="w" )
        self.b_home = ctk.CTkButton(self, text=" < HOME" , hover_color="#eef", width=120,height=33,font=("Roboto", 15), fg_color="#fff" , text_color="#333", border_width=2, command=self.home_clicked)
        self.b_start = ctk.CTkButton(self, text="START >", hover_color="#eef", width=120,height=33,font=("Roboto", 15), fg_color="#fff", text_color="#333", border_width=2, command=self.start_clicked)

        self.f_rounds = Rounds(self)
        # self.f_modules= ctk.CTkFrame(self , border_width=2)

    def start_clicked(self):
        admin:ADMIN = ADMIN.me
        admin.start_quiz()
        lf:LiveFrame = LiveFrame.me
        lf.setActiveFrame(lf.f_play)
        pass

    def home_clicked(self):
        app:_App = _App.app
        app.f_main.setActiveFrame(app.f_main.f_home)
        app.f_side.setActiveItem(app.f_side.b_home)

    def show(self):
        self.grid(row=0, column=0, sticky="nswe", padx=(10,0), pady=10)

        self.l_title.grid(row=0, column=0, sticky="w", padx=20, columnspan=2, pady=10)
        # self.f_modules.grid(row=1, column=0, sticky="nswe", columnspan=2,padx=10)
        self.f_rounds.show()
        self.b_home.grid(row=2, column=0, sticky="w", padx=10, pady=10)
        self.b_start.grid(row=2, column=1, sticky="e", padx=10, pady=10)

        # ctk.CTkLabel(self, text="ABHAY").grid(row=0, column=0)

class Participants(ctk.CTkFrame):
    fg_color="#fff"
    participants = ["user1","user2","user3", "user4"]
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)

        self.configure(width=250, fg_color="white", border_width=2)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_propagate(False)

        self.l_title = ctk.CTkLabel(self, text="Participants", font=("Helvetica", 12))
        self.b_refresh = ctk.CTkButton(self, text="", width=30, border_width=2, fg_color="#fff", hover_color="#eee", command=self.refresh_action)

        users = ["USER1", "USER2", "USER3", "USER4"]
        self.l_users = []
        self.f_users = ctk.CTkFrame(self, fg_color="transparent")

        self.f_users.grid_columnconfigure(0, weight=1)
        self.f_users.grid_propagate(False)
        for user in users:
            # label = ctk.CTkLabel(self.f_users, text="      "+user, font=("Roboto", 12), fg_color="#eee", height=30, anchor="w")
            label = ctk.CTkButton(self.f_users, text="      "+user, font=("Helvetica", 12), border_width=2, fg_color="#eee", text_color="#333", height=35, border_color="#888", hover_color="#fff", anchor="w")
            self.l_users.append(label)
        # self.manage_button_frame = ctk.CTkFrame(self, fg_color="WHITE")
        self.b_manage = ctk.CTkButton(self, text="Manage >", width=100, command=self.manage_action)
        
    def refresh_action(self):
        print("Settings button clicked")

    def manage_action(self):
        app:_App = _App.app
        app.f_main.setActiveFrame(app.f_main.f_participants)
        app.f_side.setActiveItem(app.f_side.b_participants)

    def updateList(self):
        admin:ADMIN=ADMIN.me

        for l_user in self.l_users:
            l_user.grid_forget()
        self.l_users.clear()
        for name in admin.participants.getNames():   
            label = ctk.CTkButton(self.f_users, text="      "+name, font=("Helvetica", 12), border_width=2, fg_color="#eee", text_color="#333", height=35, border_color="#888", hover_color="#fff", anchor="w")     
            self.l_users.append(label)
        pass    

    def show(self):
        self.updateList()
        self.grid(row=0, column=1, sticky="ns", padx=10, pady=10)
        
        self.l_title.grid(column=0, row=0, sticky="w", padx=10, pady=10)
        # self.b_refresh.grid(column=1, row=0, sticky="e", padx=10, pady=10)
        for i,label in enumerate(self.l_users):
            label.grid(row=i, column=0, sticky="we", pady=(5,0))
        self.f_users.grid(row=1, column=0, columnspan=2, sticky="ns", pady=(20,10))
        self.b_manage.grid(row=2, column=0, sticky="e", pady=10, columnspan=2, padx=10)

class PlayFrame(ctk.CTkFrame):
    curr_round=None
    roundUIs=list()
    me=None
    
    # self.
    def setCurrRound(self, round):
        if self.curr_round: self.curr_round.hide()
        self.curr_round=round
        self.curr_round.show()

    def setInfo(self, name, question):
        self.f_info.configure(text=f"     {name}         {question}")

    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        PlayFrame.me = self
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.f_body = ctk.CTkFrame(self, fg_color="#eee",corner_radius=0)
        self.f_body.grid_columnconfigure(0, weight=1)
        self.f_body.grid_rowconfigure(0, weight=1)

        self.f_info = ctk.CTkLabel(self,fg_color="#fff", height=40, font=("Roboto", 15),corner_radius=5, anchor="w", text=f"     GROUP-I         Questions : 1 / 5")
        self.f_controls = ctk.CTkFrame(self, fg_color="#fff", height=40, width=0)
        
        self.b_play=ctk.CTkButton(self.f_controls, text="⏸️", width=30, height=30)
        # self.b_pre_question=ctk.CTkButton(self.f_controls, text="⏮️", width=30, height=30)
        self.b_next_question=ctk.CTkButton(self.f_controls, text="⏭️", width=30, height=30, command=self.askNext)
        self.b_right=ctk.CTkButton(self.f_controls, text="✅", width=30, height=30, command=self.mark_right)
        self.b_wrong=ctk.CTkButton(self.f_controls, text="❌", width=30, height=30, command=self.mark_wrong)

        self.roundUIs.append(Round1(self.f_body, True))
        self.roundUIs.append(Round2(self.f_body, True))
        self.roundUIs.append(Round3(self.f_body, True))
        self.roundUIs.append(Round4(self.f_body, True))

        self.curr_round=self.roundUIs[0]

    def mark_right(self):
        admin:ADMIN = ADMIN.me
        admin.currentRound.mark_right()
        pass

    def mark_wrong(self):
        # admin:ADMIN = ADMIN.me
        ADMIN.me.currentRound.mark_wrong()
        pass

    def askNext(self):
        admin:ADMIN = ADMIN.me
        admin.currentRound.askNextQ()

    def show(self):
        self.grid(row=0, column=0, sticky="nswe")
        self.f_body.grid(row=0, column=0, sticky="nswe", columnspan=5)
        self.f_info.grid(row=1, column=0, sticky="we", padx=10, )
        self.f_controls.grid(row=1, column=1, padx=(0,10), pady=10)

        self.b_play.grid(row=0, column=0, pady=5,padx=5)
        # self.b_pre_question.grid(row=0, column=1, pady=5,padx=(0,5))
        self.b_next_question.grid(row=0, column=1, pady=5,padx=(0,5))
        self.b_right.grid(row=0, column=3, pady=5, padx=(0,5))
        self.b_wrong.grid(row=0, column=4, pady=5, padx=(0,5))

        self.curr_round.show()
        pass

    def hide(self):
        pass

class LiveFrame(ctk.CTkFrame):
    me=None
    activeFrame:ctk.CTkFrame=None
    f_play:PlayFrame=None
    f_start:StartFrame=None
    def setActiveFrame(self, frame):
        if self.activeFrame: self.activeFrame.grid_forget()
        self.activeFrame=frame
        self.activeFrame.show()

    def __init__(self, master, app, **kw):
        super().__init__(master=master,fg_color="#eee", **kw)
        LiveFrame.me = self
        self.app = app
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.f_start = StartFrame(self)
        self.f_play = PlayFrame(self)
        # self.activeFrame = self.f_play
        self.activeFrame = self.f_start

    def show(self):
        self.activeFrame.show()
        self.grid(row=0, column=0, sticky="nswe")

