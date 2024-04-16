import customtkinter as ctk
from ...lib.qb import ClientQuestion

from .round import ROUND,QuestionFrame

class Question_Frame(QuestionFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, options=None, border_width=2,border_color='white',width=700,height=400, **kwargs)
        self.l_question=ctk.CTkLabel(self,text="Question will Appear Here",font=('Garamond',20),fg_color='white',text_color='black',width=500,height=200)
    def show(self):
        self.l_question.grid(row=0,column=0,sticky='nesw',padx=20,pady=20)
        
class Round1(ROUND):
    q_frame=None
    hasOptions=False
    curr_q:ClientQuestion = None
    def __init__(self, master, isAdmin=False, **kwargs):

        super().__init__(master,isAdmin=isAdmin, has_options=False, has_submit=False, **kwargs)
        
        self.q_frame = Question_Frame(self)
        super().setQFrame(self.q_frame)

        self.grid_columnconfigure(0, weight=1)
        self.l_round_name=ctk.CTkLabel(self,text="STRAIGHT FORWARD",fg_color="transparent",font=('Garamond', 50),text_color="blue")
        self.l_round_index=ctk.CTkLabel(self,text='ROUND 1',fg_color="transparent",font=('Garamond',14),text_color="black")
        self.l_logo=ctk.CTkLabel(self,text='Logo',fg_color="white",width=50,height=50,text_color="red")
        self.l_timer=ctk.CTkButton(self, text="20s", fg_color="transparent", border_color="#888", border_width=2, corner_radius=5,font=("Roboto", 20), hover=False, width=80, height=40, text_color="#333")
        # self.f_question=Quation_Frame(self)
        
    def show(self):
        self.grid(row=0,column=0,padx=20,pady=20,sticky='nswe')
        self.l_round_name.grid(row=0, column=0, sticky='wen', padx=20, pady=0)
        self.l_round_index.grid(row=1,column=0,sticky='nwe',padx=20,pady=0)
        self.l_logo.grid(row=0,column=0,sticky='nw',padx=20,pady=20)
        self.l_timer.grid(row=0,column=0,sticky='ne',padx=20,pady=20)

        self.f_question.grid(row=2, column=0, padx=20, pady=20)
        self.f_question.show()

    def hide(self):
        self.grid_forget()

    def stop_timer(self):
        # return super().stop_timer()()
        self.running=False