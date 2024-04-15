# frame for the fourth and the final round is this 
#   round three frame only.
import customtkinter as ctk
from ...lib.qb import ClientQuestion
from ..._globals import _GLOBALs
from .util import set_option_active, set_option_inactive

class Quation_Frame(ctk.CTkFrame):
    options=list()
    def __init__(self, master, **kwargs):
        super().__init__(master,width=500, height=500,fg_color='white', **kwargs)
        ## for displaying the quation
        self.desplay_quations=ctk.CTkFrame(self,width=500,height=200,fg_color='white',border_color='black',border_width=0)
        qaution="who is this persion shown in the image"
        self.l_question=ctk.CTkLabel(self.desplay_quations,text=qaution,font=('Garamond',20),fg_color='white',text_color='black',width=500,height=200)
        self.l_question.pack(expand=True,padx=20,pady=20,fill=ctk.BOTH)
        text_col='black'

        self.options.append(self.createOption(self, "Abhay", 1))
        self.options.append(self.createOption(self, "Abhay", 2))
        self.options.append(self.createOption(self, "Abhay", 3))
        self.options.append(self.createOption(self, "Abhay", 4))
       
    def show(self):
        self.desplay_quations.grid(row=0,column=0,padx=100,pady=10,sticky='nsew')
        self.desplay_quations.grid_columnconfigure(0,weight=1)

        for i,option in enumerate(self.options):
            option.grid(row=i+1,column=0,padx=80,pady=5,sticky='we')
            
    def createOption(self, master, text, i):
        return ctk.CTkButton(master, width=200, height=40, text=text, border_color="#888", border_width=2,text_color="black",hover_color="#eee", fg_color="transparent", command=lambda:self.setSelected(i))
    
    def on_submit(self):
        master:Round4 = self.master
        user = _GLOBALs['user']
        user.submit_answer(master.qid, master.selectedOption)
        pass

    def setSelected(self, i):
        if self.master.isAdmin: return
        r4:Round4 = self.master
        if r4.selectedOption and r4.selectedOption != i:
            set_option_inactive(self.options[r4.selectedOption-1])
        r4.selectedOption = i
        set_option_active(self.options[i-1])

class Round4(ctk.CTkFrame):
    
    qid=None
    selectedOption=None
    isAdmin=False

    def __init__(self, master,isAdmin=False, **kwargs):
        super().__init__(master, **kwargs)
        self.isAdmin=isAdmin
        # title for the frame 
        self.page_title=ctk.CTkLabel(self,text="SPEED ROUND",fg_color="transparent",font=('Garamond', 50),text_color="blue")
        self.round_title=ctk.CTkLabel(self,text='ROUND 4',fg_color="transparent",font=('Garamond',14),text_color="black")
        # logo of the frame 
        self.logo=ctk.CTkLabel(self,text='Logo',fg_color="white",width=50,height=50,text_color="red")
        # timer for the frame
        self.timer=ctk.CTkLabel(self,text='timer',fg_color='blue',width=70,height=30,text_color='white')
    def show(self):
        self.quation_frame=Quation_Frame(self)
        self.page_title.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)
        self.round_title.grid(row=1,column=0,sticky='nwe',padx=20,pady=0)
        self.quation_frame.grid(row=2, column=0, padx=50, pady=20)
        self.quation_frame.show()
        self.logo.grid(row=0,column=0,sticky='nw',padx=20,pady=20)
        self.timer.grid(row=0,column=0,sticky='ne',padx=20,pady=20)
        self.grid_columnconfigure(0, weight=1) 
        self.pack(fill=ctk.BOTH, expand=True, padx=20, pady=20)
        
    def hide(self):
        self.pack_forget()

    def setQ(self, q:ClientQuestion):
        print("Setting Round-IV QUESTION")
        # print(q.jsons())
        self.qid = q.qid
        # for option in q.optionsT:
        self.quation_frame.l_question.configure(text=q.text)
        t_options = q.optionsT()
        for option, l_option in zip(t_options, self.quation_frame.options):
            l_option.configure(text=option)
        if self.selectedOption:
            set_option_inactive
            (self.quation_frame.options[self.selectedOption-1])#.configure(border_color="#888")
            self.selectedOption=None
