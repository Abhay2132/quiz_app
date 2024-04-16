import customtkinter as ctk
from ...lib.qb import ClientQuestion
import os
from PIL import Image
# from ...lib.struct import USER
from ..._globals import _GLOBALs
from .util import set_option_normal, set_option_selected, set_option_correct
from .round import ROUND, QuestionFrame

class Question_Frame(QuestionFrame):

    options = None
    def __init__(self, master, **kwargs):
        options = list()
        super().__init__(master,options=options, width=500, height=500, **kwargs)
        self.options = options

        self.desplay_quations=ctk.CTkFrame(self,width=500,height=200,fg_color='white',border_color='black',border_width=2)
        self.l_question=ctk.CTkLabel(self.desplay_quations,text="",font=('Garamond',20),fg_color='white',text_color='black',width=500,height=200)
        self.l_question.pack(expand=True,padx=20,pady=20,fill=ctk.BOTH)
        self.b_submit=ctk.CTkButton(self,width=100,height=40,text="SUBMIT",border_color='#888',border_width=2,hover=True,hover_color='green', command=self.on_submit)
        
        options.append(self.createOption(self, "Abhay", 1))
        options.append(self.createOption(self, "Abhay", 2))
        options.append(self.createOption(self, "Abhay", 3))
        options.append(self.createOption(self, "Abhay", 4))

    def show(self):
        self.grid(row=1,column=0,sticky='ne',padx=40,pady=20)
        self.desplay_quations.grid(row=0,column=0,padx=10,pady=10,sticky='nsew')
        self.desplay_quations.grid_columnconfigure(0,weight=1)
        
        for i,option in enumerate(self.options):
            option.grid(row=i+1,column=0,padx=80,pady=5,sticky='we')
            
        if not self.master.isAdmin:
            self.b_submit.grid(row=5,column=0,padx=80,pady=5,sticky='w')
        
class Round2(ROUND):

    def __init__(self, master,isAdmin=False,**kwargs):

        super().__init__(master=master, isAdmin=isAdmin, **kwargs)
        self.q_frame = Question_Frame(self)
        super().setQFrame(self.q_frame)
        
        self.isAdmin=isAdmin
        Round2.me=self
        self.page_title=ctk.CTkLabel(self,text="BUJHO TO JANO",fg_color="transparent",font=('Garamond', 50),text_color="blue")
        self.round_title=ctk.CTkLabel(self,text='ROUND 2',fg_color="transparent",font=('Garamond',14),text_color="black")
        self.logo=ctk.CTkLabel(self,text='Logo',fg_color="white",width=50,height=50,text_color="red")
        self.l_timer=ctk.CTkLabel(self,text='timer',fg_color='blue',width=70,height=30,text_color='white')
        self.image=ctk.CTkLabel(self,fg_color='white',text_color='black',width=400,height=500, text="")#,image=img)

    def show(self):
        self.page_title.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)
        self.round_title.grid(row=1,column=0,sticky='nwe',padx=20,pady=0)
        self.logo.grid(row=0,column=0,sticky='nw',padx=20,pady=20)
        self.l_timer.grid(row=0,column=0,sticky='ne',padx=20,pady=20)
        self.image.grid(row=1,column=0,sticky='nw',padx=40,pady=20)
        self.f_question.show()
        self.grid_columnconfigure(0, weight=1) 
        self.pack( fill=ctk.BOTH,expand=True, padx=20, pady=20)
        # self.show_answer(2,3)

        # self.start_timer()

    def hide(self):
        self.pack_forget()

def test():
    app = ctk.CTk()
    r2 = Round2(app)
    r2.show()
    app.mainloop()
    pass


if __name__=="__main__":
    test()