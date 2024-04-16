# frame for the fourth and the final round is this 
#   round three frame only.
import customtkinter as ctk
from ...lib.qb import ClientQuestion
from ..._globals import _GLOBALs
from .util import set_option_selected, set_option_normal, set_option_correct
from .round import ROUND, QuestionFrame

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
        self.l_question=ctk.CTkLabel(self.desplay_quations,text=qaution,font=('Garamond',20),fg_color='white',text_color='black',width=500,height=200)

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

class Round4(ROUND):

    binded=False
    def __init__(self, master,isAdmin=False, **kwargs):

        super().__init__(master=master, isAdmin=isAdmin, has_submit=False, **kwargs)
        self.f_question = Question_Frame(self)
        super().setQFrame(self.f_question)
        # super().__init__(master, **kwar   gs)

        self.isAdmin=isAdmin
        self.page_title=ctk.CTkLabel(self,text="SPEED ROUND",fg_color="transparent",font=('Garamond', 50),text_color="blue")
        self.round_title=ctk.CTkLabel(self,text='ROUND 4',fg_color="transparent",font=('Garamond',14),text_color="black")
        self.logo=ctk.CTkLabel(self,text='Logo',fg_color="white",width=50,height=50,text_color="red")
        self.l_timer=ctk.CTkLabel(self,text='timer',fg_color='blue',width=70,height=30,text_color='white')

        super().setLTimer(self.l_timer)
    
    def show(self):

        if not self.binded and not self.isAdmin: _GLOBALs["user"].ui.bind("<Key>", self.on_key_pressed)
        self.binded=True
        self.page_title.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)
        self.round_title.grid(row=1,column=0,sticky='nwe',padx=20,pady=0)
        self.f_question.grid(row=2, column=0, padx=50, pady=20)
        self.f_question.show()
        self.logo.grid(row=0,column=0,sticky='nw',padx=20,pady=20)
        self.l_timer.grid(row=0,column=0,sticky='ne',padx=20,pady=20)
        self.grid_columnconfigure(0, weight=1) 
        self.pack(fill=ctk.BOTH, expand=True, padx=20, pady=20)

        # self.show_answer(1)
        self.start_timer()
        
    def hide(self):
        self.pack_forget()

    def on_key_pressed(self, event):
        # print(event)
        # return
        if event.keysym=="Return":
            print("BUZZER PRESSED")
            _GLOBALs["user"].on_buzzer_pressed(self.qid)


