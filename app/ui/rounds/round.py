from .util import set_option_correct, set_option_normal, set_option_selected
from ...lib.qb import ClientQuestion
from PIL import Image
import os
import customtkinter as ctk
from ..._globals import _GLOBALs
import time

class QuestionFrame(ctk.CTkFrame):

    options=None
    b_submit:ctk.CTkButton=None

    def __init__(self, master,options=None,**kwargs):
        super().__init__(master, **kwargs)
        self.option=options

    def createOption(self, master, text, i):
        return ctk.CTkButton(master, width=200, height=40, text=text, border_color="#888", border_width=2,hover_color="#eee", font=("Roboto", 18), fg_color="transparent", command=lambda:self.setSelected(i))
    
    def on_submit(self):
        r:ROUND=self.master
        if not r.selectedOption:
            return
        master:ROUND = self.master
        user = _GLOBALs['user']
        user.submit_answer(master.qid, master.selectedOption)
        self.b_submit.configure(state=ctk.DISABLED)
        r:ROUND=self.master
        r.stop_timer()
        pass

    def setSelected(self, i, flag=False):
        if self.master.isAdmin or flag: return
        r2:ROUND = self.master

        # deselect previous one
        if r2.selectedOption and r2.selectedOption != i:
            set_option_normal(self.options[r2.selectedOption-1])#.configure(border_color="#888")

        # deselect current
        if r2.selectedOption and r2.selectedOption == i:
            set_option_normal(self.options[r2.selectedOption-1])#.configure(border_color="#888")
            r2.selectedOption = None
            return
        r2.selectedOption = i
        set_option_selected(self.options[i-1])#.configure(border_color="green")

    def resetOptions(self):
        self.master.selectedOption = None
        self.master.correctOption = None
        if not bool(self.options):
            return
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
    running=False
    time_limit = 30
    l_timer:ctk.CTkLabel=None
    hasSubmit=None
    rid=None

    def setQFrame(self, f):
        self.f_question = f

    def setLTimer(self, l):
        self.l_timer=l
    
    def __init__(self,master, isAdmin,has_options=True, has_submit=True,id=None, **kwargs):
        super().__init__(master,**kwargs)
        # self.f_question = QFrame(self, options=(list() if has_options else None))
        self.isAdmin = isAdmin
        self.hasOptions = has_options
        self.hasSubmit = has_submit
        self.rid=id

    
    def limit_line_length(self, text, limit):
        words = list(text.split(" "))
        para = list()
        line = ""
        for i,word in enumerate(words):
            if i < len(words)-1:
                word+=" "
            newline = line + word
            if len(newline) > limit:
                # line = line+"\n"+word
                para.append(line)
                line = word
            else:
                line = newline
        para.append(line)
        return "\n".join(para)
    

    def setQ(self, q:ClientQuestion):
        if self.hasSubmit: self.f_question.b_submit.configure(state=ctk.NORMAL)
        self.reset_timer()
        self.start_timer()
        self.f_question.resetOptions()
        self.qid = q.qid

        q_size = 40
        q.text = self.limit_line_length(q.text, q_size)
        # if len(q.text) > q_size:
        #     parts = list()
        #     start=0
        #     end = q_size
        #     while start < len(q.text):
        #         parts.append(q.text[start:end])
        #         start += q_size
        #         end += q_size
        #     q.text = "\n".join(parts)

        self.f_question.l_question.configure(text=q.text)

        if not bool(self.f_question.option):
            return
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
        # if selected_i:self.f_question.setSelected(int(selected_i), True)
        set_option_selected(self.f_question.options[int(selected_i)-1])
        self.f_question.setCorrect(int(correct_i))

    def show(self):
        pass

    def hide(self):
        pass

    def reset_timer(self):
        self.running = False
        self.l_timer.configure(text=f"{self.time_limit}s")
        print("Timer reset")

    def start_timer(self):
        print("START TIMEr")
        if not self.running:
            self.start_time = time.time()
            self.running = True
            # self.start_button.configure(state="disabled")
            # self.stop_button.configure(state="normal")
            self.update_timer()

    def update_timer(self):
            if self.running:
                present_time = time.time()
                elapsed_time = present_time - self.start_time
                remaining_time = self.time_limit - int(elapsed_time)
    
                if remaining_time > 0:
                    self.l_timer.configure(text=f"{remaining_time}s")
                    self.l_timer.after(1000, self.update_timer)  # Update every 1 second
                else:
                    self.stop_timer()
                    self.l_timer.configure(text="TIME UP")
    
    def stop_timer(self):
        if self.running:
            self.running = False
            # self.start_button.configure(state="normal")
            if self.hasSubmit: self.f_question.b_submit.configure(state="disabled")

    def setLogo(self, imgPath):
        image = Image.open(imgPath)
        width, height = image.size
        l_width=int(self.l_logo.cget("width"))
        height = height/width*l_width
        print(f"{width}x{height}")
        image = ctk.CTkImage(image, size=(l_width,height))
        self.l_logo.configure(image=image, text="")

