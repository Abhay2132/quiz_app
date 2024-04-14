from typing import Any, Tuple
import customtkinter as ctk

from PIL import Image
class Quation_Frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master,width=500, height=500, **kwargs)
        self.desplay_quations=ctk.CTkFrame(self,width=500,height=200,fg_color='white',border_color='black',border_width=2)
        qaution="who is this persion shown in the image"
        text_col='black'
        self.l_question=ctk.CTkLabel(self.desplay_quations,text=qaution,font=('Garamond',20),fg_color='white',text_color='black',width=500,height=200)
        self.l_question.pack(expand=True,padx=20,pady=20,fill=ctk.BOTH)

        
        self.b_option1 = ctk.CTkButton(self, width=200, height=40, text="ABHAY", border_color="#888", border_width=2,text_color=text_col, fg_color="transparent")
        
        self.b_option2 = ctk.CTkButton(self, width=200, height=40, text="ANshul", border_color="#888", border_width=2,text_color=text_col, fg_color="transparent")
        
        self.b_option3 = ctk.CTkButton(self, width=200, height=40, text="Super-man", border_color="#888", border_width=2,text_color=text_col, fg_color="transparent")
        
        self.b_option4 = ctk.CTkButton(self, width=200, height=40, text="Spider-man", border_color="#888", border_width=2,text_color=text_col, fg_color="transparent")
        
        self.sumit_button=ctk.CTkButton(self,width=100,height=40,text="SUMIT",border_color='#888',border_width=2,hover=True,hover_color='green')

    def show(self):
        self.desplay_quations.grid(row=0,column=0,padx=10,pady=10,sticky='nsew')
        self.desplay_quations.grid_columnconfigure(0,weight=1)
        self.b_option1.grid(row=1,column=0,padx=80,pady=5,sticky='we')
        self.b_option2.grid(row=2,column=0,padx=80,pady=5,sticky='we')
        self.b_option3.grid(row=3,column=0,padx=80,pady=5,sticky='we')
        self.b_option4.grid(row=4,column=0,padx=80,pady=5,sticky='we')
        self.sumit_button.grid(row=5,column=0,padx=80,pady=5,sticky='w')
    
class Round2(ctk.CTkFrame):
    def __init__(self, master,**kwargs):
        super().__init__(master,**kwargs)
        #adding title to the page
        self.page_title=ctk.CTkLabel(self,text="BUJHO TO JANO",fg_color="transparent",font=('Garamond', 50),text_color="blue")
        self.round_title=ctk.CTkLabel(self,text='ROUND 2',fg_color="transparent",font=('Garamond',14),text_color="black")
        # adding logo label
        self.logo=ctk.CTkLabel(self,text='Logo',fg_color="white",width=50,height=50,text_color="red")
        # adding timer label
        self.timer=ctk.CTkLabel(self,text='timer',fg_color='blue',width=70,height=30,text_color='white')
        # adding image for the quation in the frame
        # x="roundtwoimage/test.png"
        # img=ctk.CTkImage(Image.open(x),size=(50,50))
        self.image=ctk.CTkLabel(self,fg_color='white',text_color='black',width=400,height=500)#,image=img)
    def show(self):
        self.page_title.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)
        self.round_title.grid(row=1,column=0,sticky='nwe',padx=20,pady=0)
        self.logo.grid(row=0,column=0,sticky='nw',padx=20,pady=20)
        self.timer.grid(row=0,column=0,sticky='ne',padx=20,pady=20)
        self.image.grid(row=1,column=0,sticky='nw',padx=40,pady=20)
        self.quation_frame=Quation_Frame(self)
        self.quation_frame.grid(row=1,column=0,sticky='ne',padx=40,pady=20)
        self.quation_frame.show()
        self.grid_columnconfigure(0, weight=1) 
        self.pack( fill=tkinter.BOTH,expand=True, padx=20, pady=20)