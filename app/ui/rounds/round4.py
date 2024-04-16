# frame for the fourth and the final round is this 
#   round three frame only.
import customtkinter as ctk
from ...lib.qb import ClientQuestion
from ..._globals import _GLOBALs
from .util import set_option_selected, set_option_normal, set_option_correct
from .round import ROUND, QuestionFrame

class Wrapper(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__( master, **kwargs)
        self.configure(fg_color="transparent", border_width=2)
        self.l_title=ctk.CTkLabel(self,text="USERS",font=('Roboto',16),text_color='#333',fg_color='transparent')
        self.ranktable=Rank_Table(self)
    def show(self):
        self.l_title.grid(row=0,column=0,padx=10,pady=10,sticky='nw')
        self.ranktable.grid(row=1,column=0,padx=10,pady=10,sticky='we')
        self.ranktable.show()
        
class Rank_Table(ctk.CTkFrame):
    teams=list()

    def __init__(self, master, **kwargs):
        super().__init__(master,fg_color='white', **kwargs)

        self.configure(fg_color="#eee")
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        # self.teams.append(self.createTeam(self,'anshul','1'))
        # self.teams.append(self.createTeam(self,'anshul','1'))
        # self.teams.append(self.createTeam(self,'anshul','1'))

    def createTeam(self,master, name)->ctk.CTkFrame:
        f_team=ctk.CTkFrame(master=master,fg_color='#fff', width=300,height=40,border_width=2)
        f_team.grid_propagate(False)
        f_team.columnconfigure(0,weight=1)
        l_team_nam=ctk.CTkLabel(f_team,text=name,font=('Roboto',14),text_color='#333',fg_color='transparent')
        # l_rank=ctk.CTkLabel(f_team,text=score,font=('Roboto',18),text_color='#333',fg_color='transparent')
        l_team_nam.grid(row=0,column=0,sticky='w',padx=20,pady=8)
        # l_rank.grid(row=0,column=1,sticky='e',padx=50,pady=8)
        
        return f_team

    def addTeam(self, name):
        team = self.createTeam(self, name)
        self.teams.append(team)
        team.grid(row=len(self.teams)-1,column=0,sticky='we',padx=40,pady=(5,0))

    def clearTeams(self):
        for team in self.teams:
            team.destroy()
        self.teams.clear()

    def show(self):
        for i,team in enumerate(self.teams):
            team.grid(row=i,column=0,sticky='we',padx=20,pady=8)
        
        # self.addTeam(Rank("ABhay",1))
        # self.addTeam(Rank("ABhay",1))
        # self.addTeam(Rank("ABhay",1))

class Rank():
    name=""
    score:int=0

    def __init__(self, name, score) -> None:
        self.name=name
        self.score:int=score
        pass
    pass


class Question_Frame(QuestionFrame):
    options=list()

    def __init__(self, master, **kwargs):
        
        options = list()
        super().__init__(master,options=options, width=500, height=500, **kwargs)
        self.options = options

        # super().__init__(master,width=500, height=500,fg_color='white', **kwargs)
        ## for displaying the quation
        self.desplay_quations=ctk.CTkFrame(self,width=500,height=200,fg_color='white',border_color='black',border_width=0)
        qaution="who is this persion shown in the image"
        self.l_question=ctk.CTkLabel(self.desplay_quations,text=qaution,font=('Garamond',25),fg_color='white',text_color='black',width=500,height=200)
        self.b_submit=ctk.CTkButton(self,width=100,height=40,text="SUBMIT",border_color='#888', state=ctk.DISABLED, border_width=2,hover=True,hover_color='green', command=self.on_submit)
        self.l_info=ctk.CTkLabel(self,text="- PRESS THE ENTER FIRST -",font=('Garamond',15),fg_color='transparent',text_color='black')
        
        self.options.append(self.createOption(self, "Abhay", 1))
        self.options.append(self.createOption(self, "Abhay", 2))
        self.options.append(self.createOption(self, "Abhay", 3))
        self.options.append(self.createOption(self, "Abhay", 4))

    def show(self):
        self.l_question.pack(expand=True,padx=20,pady=20,fill=ctk.BOTH)
        self.desplay_quations.grid(row=0,column=0,padx=100,pady=10,sticky='nsew')
        self.desplay_quations.grid_columnconfigure(0,weight=1)

        for i,option in enumerate(self.options):
            option.grid(row=i+1,column=0,padx=80,pady=5,sticky='we')

        # if not self.master.isAdmin:
        #     self.b_submit.grid(row=5,column=0,padx=80,pady=5,sticky='w')
        #     self.l_info.grid(row=6,column=0,padx=100,pady=5,sticky='w')
class Round4(ROUND):

    binded=False
    def __init__(self, master,isAdmin=False, **kwargs):

        super().__init__(master=master, isAdmin=isAdmin, has_submit=False,  **kwargs)
        self.f_question = Question_Frame(self)
        super().setQFrame(self.f_question)
        # super().__init__(master, **kwar   gs)
        self.grid_columnconfigure(0, weight=1) 

        self.isAdmin=isAdmin
        self.page_title=ctk.CTkLabel(self,text="SPEED ROUND",fg_color="transparent",font=('Garamond', 50),text_color="blue")
        self.round_title=ctk.CTkLabel(self,text='ROUND 4',fg_color="transparent",font=('Garamond',14),text_color="black")
        self.logo=ctk.CTkLabel(self,text='Logo',fg_color="white",width=50,height=50,text_color="red")
        self.l_timer=ctk.CTkLabel(self,text='timer',fg_color='blue',width=70,height=30,text_color='white')
        self.wrapper=Wrapper(self)

        super().setLTimer(self.l_timer)
    
    def show(self):

        if not self.binded and not self.isAdmin: 
            print("ADDED KEY BINDINGs")
            _GLOBALs.get("user") and _GLOBALs["user"].ui.bind("<Key>", self.on_key_pressed)
        self.binded=True
        self.page_title.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)
        self.round_title.grid(row=1,column=0,sticky='nwe',padx=20,pady=0)
        self.f_question.grid(row=2, column=0, padx=50, pady=20)
        self.f_question.show()
        self.logo.grid(row=0,column=0,sticky='nw',padx=20,pady=20)
        self.l_timer.grid(row=0,column=0,sticky='ne',padx=20,pady=20)
        self.pack(fill=ctk.BOTH, expand=True, padx=20, pady=20)

        # for testing
        # if True:
        #     self.wrapper.grid(row=2,column=1,padx=10,pady=10,sticky='ne')
        #     self.wrapper.show()
        #     self.adduser("ABHAY")
        #     self.clearusers()
        #     self.adduser("INDNIA")
        #     self.adduser("AAA")

        if self.isAdmin:
            self.wrapper.grid(row=2,column=1,padx=10,pady=10,sticky='ne')
            self.wrapper.show()
        
    def hide(self):
        self.pack_forget()

    def adduser(self, name):
        self.wrapper.ranktable.addTeam(name)

    def clearusers(self):
        self.wrapper.ranktable.clearTeams()
    # def set_submit_active(self):
    #     self.set_submit_active()

    def on_key_pressed(self, event):
        # print(event)
        # return
        if event.keysym=="Return" and self.running:
            print("BUZZER PRESSED")
            _GLOBALs["user"].on_buzzer_pressed(self.qid)
            self.stop_timer()


