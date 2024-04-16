from .util import set_option_correct, set_option_normal, set_option_selected
from ...lib.qb import ClientQuestion
from PIL import Image
import os
import customtkinter as ctk
from ..._globals import _GLOBALs

class QuestionFrame(ctk.CTkFrame):

    options=None

    def __init__(self, master,options=None, **kwargs):
        super().__init__(master, **kwargs)
        self.option=options

    def createOption(self, master, text, i):
        return ctk.CTkButton(master, width=200, height=40, text=text, border_color="#888", border_width=2,text_color="black",hover_color="#eee", fg_color="transparent", command=lambda:self.setSelected(i))
    
    def on_submit(self):
        master:ROUND = self.master
        user = _GLOBALs['user']
        user.submit_answer(master.qid, master.selectedOption)
        pass

    def setSelected(self, i, flag=False):
        if self.master.isAdmin or flag: return
        r2:ROUND = self.master
        if r2.selectedOption and r2.selectedOption != i:
            set_option_normal(self.options[r2.selectedOption-1])#.configure(border_color="#888")
        r2.selectedOption = i
        set_option_selected(self.options[i-1])#.configure(border_color="green")

    def resetOptions(self):
        self.master.selectedOption = None
        self.master.correctOption = None
        for option in self.options:
            set_option_normal(option)

    def setCorrect(self, i):
        r2:ROUND = self.master
        if r2.correctOption and r2.correctOption != i:
            set_option_normal(self.options[r2.correctOption-1])
        r2.correctOption = i
        set_option_correct(self.options[i-1])

class ROUND(ctk.CTkFrame):
    correctOption:int=None
    selectedOption:int=None
    isAdmin=False
    qid=None
    me=None
    f_question:QuestionFrame=None
    hasOptions=True

    def setQFrame(self, f):
        self.f_question = f

    def __init__(self,master, isAdmin,has_options, **kwargs):
        super().__init__(master,**kwargs)
        # self.f_question = QFrame(self, options=(list() if has_options else None))
        self.isAdmin = isAdmin
        self.hasOptions = has_options

    def setQ(self, q:ClientQuestion):
        self.f_question.resetOptions()
        self.qid = q.qid

        self.f_question.l_question.configure(text=q.text)
        t_options = q.optionsT()
        for option, l_option in zip(t_options, self.f_question.options):
            l_option.configure(text=option)

        if q.imgPath:
            img_path = q.get_img_path()
            if os.path.exists(img_path) and os.path.isfile(img_path):
                self.setImage(img_path)
        else:
            print(f"IMAGE NOT FOUND : '{q.imgPath}' , '{q.get_img_path()}'")

        if self.selectedOption:
            set_option_normal(self.f_question.options[self.selectedOption-1])#.configure(border_color="#888")
            self.selectedOption=None

    def setImage(self, imgPath):
        image = Image.open(imgPath)
        width, height = image.size
        l_width=int(self.image.cget("width"))
        height = height/width*l_width
        print(f"{width}x{height}")
        image = ctk.CTkImage(image, size=(l_width,height))
        self.image.configure(image=image, text="")

    def show_answer(self, correct_i, selected_i=None):
        self.f_question.setCorrect(int(correct_i))
        # if selected_i:self.f_question.setSelected(int(selected_i), True)
        set_option_selected(self.f_question.options[int(selected_i)-1])

    def show(self):
        pass

    def hide(self):
        pass