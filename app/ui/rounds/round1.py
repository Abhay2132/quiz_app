import customtkinter as ctk
from ...lib.qb import ClientQuestion
from PIL import Image
from .round import ROUND,QuestionFrame
import os
from ...lib.util import setImage
from ..._globals import _GLOBALs
class Question_Frame(QuestionFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, options=None, border_width=2,border_color='white',width=700,height=400, **kwargs)
        self.configure(fg_color="#aaf", corner_radius=5)
        self.l_question=ctk.CTkLabel(self,text="Question will Appear Here",font=('Garamond',25),fg_color='transparent',text_color='black',width=500,height=200)
    def show(self):
        self.l_question.grid(row=0,column=0,sticky='nesw',padx=20,pady=20)
        
class Round1(ROUND):
    q_frame=None
    hasOptions=False
    curr_q:ClientQuestion = None
    def __init__(self, master, isAdmin=False, **kwargs):

        super().__init__(master,isAdmin=isAdmin, fg_color="#333", has_options=False, has_submit=False, **kwargs)
        

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.l_bg = ctk.CTkLabel(self, text="")#, fg_color="red")
        self.l_bg.grid(row=0, column=0, sticky="nswe", rowspan=5)
        # self.l_bg.pack(fill="both", expand=True)

        self.q_frame = Question_Frame(self)
        super().setQFrame(self.q_frame)
        self.l_round_name=ctk.CTkLabel(self,text="PRASHAN BAAN",fg_color="transparent",font=('Garamond', 50),text_color="blue")
        self.l_round_index=ctk.CTkLabel(self,text='STRAIGHT FORWARD',fg_color="transparent",font=('Garamond',18),text_color="black")
        self.l_logo=ctk.CTkLabel(self,text='Logo',fg_color="transparent", bg_color="transparent",width=100,height=100,text_color="red")
        self.l_timer=ctk.CTkButton(self, text="20s", fg_color="transparent", border_color="#888", border_width=2, corner_radius=5,font=("Roboto", 20), hover=False, width=80, height=40, text_color="#fff")
        # self.l_bg = ctk.CTkLabel(self, row=0, col)
        # self.f_question=Quation_Frame(self)
        super().setLTimer(self.l_timer)
        
        self.setQ(ClientQuestion(1,"WHO is Abay?", "1,2,3,4", ""))
     
    def show(self):
        self.grid(row=0,column=0,padx=0,pady=0,sticky='nswe')
        self.l_logo.grid(row=0,column=0,sticky='nw',padx=20,pady=20)
        self.l_timer.grid(row=0,column=0,sticky='ne',padx=20,pady=20)


        self.f_question.grid(row=2, column=0, padx=20, pady=(0,30))
        self.f_question.show()
        self.l_round_name.grid(row=0, column=0, sticky='wen', padx=20, pady=0)

        self.l_round_index.grid(row=0,column=0,sticky='nwe',padx=20,pady=(50,))
        logo_path = os.path.join(os.getcwd(), "data", "icons", "round_logo.png")
        # self.setLogo(logo_path)
        setImage(logo_path, self.l_logo)
        
        bg_path = os.path.join(os.getcwd(), "data", "images", "_round_bg.jpg")
        self.setBG(bg_path, self.l_bg)



    def setBG(self, imgPath, target:ctk.CTkLabel):
            image = Image.open(imgPath)
            width, height = image.size
            # l_width=int(target.cget("width"))
            # l_height = _GLOBALs["app:user"].winfo_width()
            # l_width = width/height*l_height
            # l_width = _GLOBALs["app:user"].winfo_height()
            print(f"bg : {width}x{height}")
            image = ctk.CTkImage(image, size=(1400,1000))
            target.configure(image=image, text="")



    def hide(self):
        self.grid_forget()

    def stop_timer(self):
        # return super().stop_timer()()
        self.running=False