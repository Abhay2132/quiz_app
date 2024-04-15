# frame for the fourth and the final round is this 
#   round three frame only.
import customtkinter as ctk

class Quation_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master,width=500, height=500,fg_color='white', **kwargs)
        ## for displaying the quation
        self.desplay_quations=ctk.CTkFrame(self,width=500,height=200,fg_color='white',border_color='black',border_width=0)
        qaution="who is this persion shown in the image"
        self.l_question=ctk.CTkLabel(self.desplay_quations,text=qaution,font=('Garamond',20),fg_color='white',text_color='black',width=500,height=200)
        self.l_question.pack(expand=True,padx=20,pady=20,fill=ctk.BOTH)
        text_col='black'

       
        self.b_option1 = ctk.CTkButton(self, width=200, height=40, text="ABHAY", border_color="#888", border_width=2,text_color=text_col, fg_color="transparent")
       
        self.b_option2 = ctk.CTkButton(self, width=200, height=40, text="ANshul", border_color="#888", border_width=2, text_color=text_col,fg_color="transparent")
       
        self.b_option3 = ctk.CTkButton(self, width=200, height=40, text="Super-man", border_color="#888", border_width=2,text_color=text_col, fg_color="transparent")
       
        self.b_option4 = ctk.CTkButton(self, width=200, height=40, text="Spider-man", border_color="#888", border_width=2, text_color=text_col,fg_color="transparent")
       
    def show(self):
        self.desplay_quations.grid(row=0,column=0,padx=100,pady=10,sticky='nsew')
        self.desplay_quations.grid_columnconfigure(0,weight=1)
        self.b_option1.grid(row=1,column=0,padx=80,pady=5,sticky='we')
        self.b_option2.grid(row=2,column=0,padx=80,pady=5,sticky='we')
        self.b_option3.grid(row=3,column=0,padx=80,pady=5,sticky='we')
        self.b_option4.grid(row=4,column=0,padx=80,pady=5,sticky='we')
    
class Round4(ctk.CTkFrame):
    def __init__(self, master,isAdmin=False, **kwargs):
        super().__init__(master, **kwargs)
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
        self.grid_forget()