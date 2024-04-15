import customtkinter as ctk
from ...lib.qb import ClientQuestion
import os
from PIL import Image
# from ...lib.struct import USER
from ..._globals import _GLOBALs
from .util import set_option_inactive, set_option_active

class Question_Frame(ctk.CTkFrame):

    options=list()
    def __init__(self, master, **kwargs):
        super().__init__(master,width=500, height=500, **kwargs)
        self.desplay_quations=ctk.CTkFrame(self,width=500,height=200,fg_color='white',border_color='black',border_width=2)
        # text_col='black'
        self.l_question=ctk.CTkLabel(self.desplay_quations,text="",font=('Garamond',20),fg_color='white',text_color='black',width=500,height=200)
        self.l_question.pack(expand=True,padx=20,pady=20,fill=ctk.BOTH)
        self.b_submit=ctk.CTkButton(self,width=100,height=40,text="SUBMIT",border_color='#888',border_width=2,hover=True,hover_color='green', command=self.on_submit)
        
        self.options.append(self.createOption(self, "Abhay", 1))
        self.options.append(self.createOption(self, "Abhay", 2))
        self.options.append(self.createOption(self, "Abhay", 3))
        self.options.append(self.createOption(self, "Abhay", 4))

    def createOption(self, master, text, i):
        return ctk.CTkButton(master, width=200, height=40, text=text, border_color="#888", border_width=2,text_color="black",hover_color="#eee", fg_color="transparent", command=lambda:self.setSelected(i))
    
    def on_submit(self):
        master:Round2 = self.master
        user = _GLOBALs['user']
        user.submit_answer(master.qid, master.selectedOption)
        pass

    def setSelected(self, i):
        if self.master.isAdmin: return
        r2:Round2 = self.master
        if r2.selectedOption and r2.selectedOption != i:
            set_option_inactive(self.options[r2.selectedOption-1])#.configure(border_color="#888")
        r2.selectedOption = i
        set_option_active(self.options[i-1])#.configure(border_color="green")

    def show(self):
        self.grid(row=1,column=0,sticky='ne',padx=40,pady=20)
        self.desplay_quations.grid(row=0,column=0,padx=10,pady=10,sticky='nsew')
        self.desplay_quations.grid_columnconfigure(0,weight=1)
        
        for i,option in enumerate(self.options):
            option.grid(row=i+1,column=0,padx=80,pady=5,sticky='we')
            
        if not self.master.isAdmin:
            self.b_submit.grid(row=5,column=0,padx=80,pady=5,sticky='w')
    
class Round2(ctk.CTkFrame):

    selectedOption:int=None
    isAdmin=False
    qid=None
    me=None

    def __init__(self, master,isAdmin=False,**kwargs):
        super().__init__(master,**kwargs)
        self.isAdmin=isAdmin
        Round2.me=self
        self.page_title=ctk.CTkLabel(self,text="BUJHO TO JANO",fg_color="transparent",font=('Garamond', 50),text_color="blue")
        self.round_title=ctk.CTkLabel(self,text='ROUND 2',fg_color="transparent",font=('Garamond',14),text_color="black")
        self.logo=ctk.CTkLabel(self,text='Logo',fg_color="white",width=50,height=50,text_color="red")
        self.timer=ctk.CTkLabel(self,text='timer',fg_color='blue',width=70,height=30,text_color='white')
        self.image=ctk.CTkLabel(self,fg_color='white',text_color='black',width=400,height=500, text="")#,image=img)
        self.quation_frame=Question_Frame(self)

    def show(self):
        self.page_title.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)
        self.round_title.grid(row=1,column=0,sticky='nwe',padx=20,pady=0)
        self.logo.grid(row=0,column=0,sticky='nw',padx=20,pady=20)
        self.timer.grid(row=0,column=0,sticky='ne',padx=20,pady=20)
        self.image.grid(row=1,column=0,sticky='nw',padx=40,pady=20)
        self.quation_frame.show()
        self.grid_columnconfigure(0, weight=1) 
        self.pack( fill=ctk.BOTH,expand=True, padx=20, pady=20)

    def hide(self):
        self.pack_forget()

    def setQ(self, q:ClientQuestion):
        print("Setting Round-II QUESTION")

        # print(q.jsons())

        self.qid = q.qid
        # for option in q.optionsT:
        self.quation_frame.l_question.configure(text=q.text)
        t_options = q.optionsT()
        for option, l_option in zip(t_options, self.quation_frame.options):
            l_option.configure(text=option)
        # self.quation_frame.b_option1.configure(text=t_options[0])
        # self.quation_frame.b_option2.configure(text=t_options[1])
        # self.quation_frasme.b_option3.configure(text=t_options[2])
        # self.quation_frame.b_option4.configure(text=t_options[3])

        if q.imgPath:
            img_path = q.get_img_path()
            if os.path.exists(img_path) and os.path.isfile(img_path):
                self.setImage(img_path)
        else:
            print(f"IMAGE NOT FOUND : '{q.imgPath}' , '{q.get_img_path()}'")

        if self.selectedOption:
            set_option_inactive(self.quation_frame.options[self.selectedOption-1])#.configure(border_color="#888")
            self.selectedOption=None

    def setImage(self, imgPath):
        image = Image.open(imgPath)
        width, height = image.size
        l_width=int(self.image.cget("width"))
        height = height/width*l_width
        print(f"{width}x{height}")
        image = ctk.CTkImage(image, size=(l_width,height))
        self.image.configure(image=image, text="")

def test():
    app = ctk.CTk()
    r2 = Round2(app)
    r2.show()
    app.mainloop()
    pass


if __name__=="__main__":
    test()