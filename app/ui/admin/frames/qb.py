import customtkinter as ctk
from .utils import rc
from tkinter import filedialog
import os
from PIL import Image
# import csv
from ....lib.util import copy_file
from ....lib.struct import ADMIN

class ListItem(ctk.CTkFrame):
    
    id:int=None
    def __init__(self, master, id, name="", **kwargs):
        super().__init__(master, **kwargs)
        self.configure(height=60)
        self.grid_columnconfigure(0, weight=1)
        # self.grid_propagate(False)
        # transparent
        self.configure(fg_color="#eee")
        self.name=name

        commons = {
            "border_width":2,
            "border_color":"#888",
            "fg_color":"#fff",
            "width":100,
            "text_color":"#333",
            "hover_color":"#ccf"
        }
        self.id = id
        self.l_name = ctk.CTkLabel(self,text=name, fg_color="transparent",font=('sans', 15))
        self.l_desc = ctk.CTkLabel(self, text="questions:0", fg_color="transparent", anchor="s", font=('sans', 12), height=15, text_color="#444")
        self.b_manage = ctk.CTkButton(self, text="MANAGE", command=self.click_manage, **commons)
        self.b_upload = ctk.CTkButton(self, text="UPLOAD", command=self.upload_csv, **commons)
        self.b_add = ctk.CTkButton(self, text="ADD",command=self.click_add, **commons)

    def upload_csv(self):
        """
        Opens a file dialog and displays the selected CSV file path.
        Restricts selection to CSV files only.
        """
        file_path = filedialog.askopenfilename(
            title="Select CSV File",
            filetypes=[("CSV Files", "*.csv")]  # Only allow CSV files
        )
        if file_path:
            # Process the selected CSV file here
            admin:ADMIN = ADMIN.me
            copy_file(file_path, admin.qBank.qdir, f"r{self.id}.csv")
            admin.qBank.load()
            qb=QBFrame.me
            qb.selectedRound=self.id
            qb.setActiveFrame(qb.f_manage)
            pass

    def click_manage(self):
        qb = QBFrame.me
        qb.selectedRound=self.id
        qb.setActiveFrame(qb.f_manage)
        qb.f_manage.setTitle("   MANAGE "+self.name+" ")

    def click_add(self):
        qb = QBFrame.me
        qb.selectedRound=self.id
        qb.setActiveFrame(qb.f_add)
        qb.addSource = qb.f_rounds

    def update_questions_count(self):
        admin:ADMIN=ADMIN.me
        count= 0
        if self.id==1:
            count= len(admin.qBank.round1)
        if self.id==2:
            count= len(admin.qBank.round2)
        if self.id==3:
            count= len(admin.qBank.round3)
        if self.id==4:
            count= len(admin.qBank.round4)
        self.l_desc.configure(text="Question:"+str(count))

    def show(self, r,c):

        self.l_name.grid(row=0, column=0, sticky="w", padx=20, pady=(5,0))
        self.l_desc.grid(row=1, column=0, sticky="w", padx=30, pady=(0,10))
        self.b_manage.grid(row=0, column=1, rowspan=2, padx=(0,10))
        self.b_upload.grid(row=0, column=2, rowspan=2, padx=(0,10))
        self.b_add.grid(row=0, column=3, rowspan=2, padx=(0,10))

        # self.grid(row=r, column=c, sticky="we", padx=5, pady=5)
        self.pack(side=ctk.TOP, fill=ctk.X, padx=(0,10), pady=(5,0))
        self.update_questions_count()

class List(ctk.CTkFrame):
    items = list()
    def __init__(self, master, **kwargs):
        """attach children and configure grid"""
        super().__init__(master,  **kwargs)
        self.items.append(ListItem(self,id=1, name="ROUND-I", fg_color='transparent', border_width=2))
        self.items.append(ListItem(self,id=2, name="ROUND-II", fg_color='transparent', border_width=2))
        self.items.append(ListItem(self,id=3, name="ROUND-III", fg_color='transparent', border_width=2))
        self.items.append(ListItem(self,id=4, name="ROUND-IV", fg_color='transparent', border_width=2))

        self.grid_columnconfigure(0, weight=1)
    
    def show(self):

        self.grid(row=1, column=0,sticky="nswe", padx=20)
        for r,item in enumerate(self.items):
            item.show(r=r, c=0)

class RoundsFrame(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        """attach children and configure grid"""
        super().__init__(master, fg_color="white",  **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.topbar = ctk.CTkLabel(master=self,text="ROUNDS", anchor="w")
        self.list = List(master=self, fg_color="transparent")

    def show(self):
        """render children and current frame"""
        self.topbar.grid(row=0, column=0, sticky="we", padx=20, pady=10)

        self.list.show()
        self.grid(row=0, column=0,padx=10, pady=10, sticky="nswe")

class AddQuestion(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        # self = ctk.CTkFrame(self)
        self.configure(border_width=2, fg_color="#fff")
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.l_title = ctk.CTkLabel(self, text="Add Question",  padx=5, font=("Roboto", 15))

        self.f_body = ctk.CTkScrollableFrame(self)
        self.l_question = ctk.CTkLabel(self.f_body, text="Question*", padx=5, fg_color="transparent", font=("Roboto", 14))
        self.e_question = ctk.CTkTextbox(self.f_body, width=600, height=150)  # Adjust width and height of Question entry box
        self.l_options = ctk.CTkLabel(self.f_body, text="Options:", font=("Roboto", 14))
        self.e_option1 = ctk.CTkEntry(self.f_body,width=200, height=35, placeholder_text="Option-1")
        self.e_option2 = ctk.CTkEntry(self.f_body,width=200, height=35, placeholder_text="Option-2")
        self.e_option3 = ctk.CTkEntry(self.f_body,width=200, height=35, placeholder_text="Option-3")
        self.e_option4 = ctk.CTkEntry(self.f_body,width=200, height=35, placeholder_text="Option-4")
        self.l_image = ctk.CTkLabel(self.f_body, text="Image:")
        self.l_image_logo = ctk.CTkLabel(self.f_body, width=100, height=100,text="Image \nPreview", fg_color="#fff", corner_radius=5)
        self.l_image_detail = ctk.CTkLabel(self.f_body, text="No Image Selected")
        self.b_upload = ctk.CTkButton(self.f_body, text="Click to Upload",command=self.upload)#, image=self.upload_logo_photo)

        self.f_footer = ctk.CTkFrame(self, width=800, height=50, fg_color="transparent")
        self.f_footer.grid_columnconfigure(0, weight=1)
        self.b_back = ctk.CTkButton(self.f_footer, text="Back", height=30,width=80,command=self.back_action)
        self.b_save = ctk.CTkButton(self.f_footer, text="Save", height=30,width=80,command=self.save_action)

    def show(self):
        # self.pack(side=ctk.CTkLEFT, fill=ctk.CTkBOTH, expand=True, padx=15, pady=15)
        self.grid(row=0, column=0, sticky="nswe", padx=10, pady=5)
        self.l_title.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.f_body.grid(row=1, column=0, sticky="nswe", padx=10, pady=5)
        self.l_question.grid(row=0, column=0, sticky="w", pady=10, padx=(80,10))
        self.e_question.grid(row=1, column=0,  padx=(100,10), pady=5, sticky="w")
        self.l_options.grid(row=2, column=0, padx=80, pady=5, sticky="w")
        self.e_option1.grid(row=3, column=0, sticky="w", padx=(100,10), pady=5)
        self.e_option2.grid(row=3, column=0, sticky="w", padx=(310,0),pady=5)
        self.e_option3.grid(row=4, column=0, sticky="w", padx=(100,10), pady=5)
        self.e_option4.grid(row=4, column=0, sticky="w", padx=(310,0), pady=5)

        self.l_image.grid(row=5, column=0, padx=(80,10), pady=(10,5), sticky="w")
        self.l_image_logo.grid(row=6,padx=(120,0),pady=10, sticky="w")
        self.l_image_detail.grid(row=7, column=0, padx=(110,0), sticky="w")
        self.b_upload.grid(row=10,padx=(100,0) ,pady=10, sticky="w")

        self.f_footer.grid(row=2, sticky="we")
        # self.b_back.pack(side=ctk.RIGHT, padx=10, pady=5)
        # self.b_save.pack(side=ctk.RIGHT, padx=10, pady=5)
        self.b_back.grid(row=0, column=0, sticky="e", padx=(0,120), pady=5)
        self.b_save.grid(row=0, column=0, sticky="e", padx=30, pady=5)
        return

    def upload(self):
        filename = filedialog.askopenfilename(title="Select Image", filetypes=(("Image files", "*.jpg *.jpeg *.png *.gif"), ("All files", "*.*")))
        if filename:
            file = os.path.basename(filename)
            self.setImage(filename)
            self.l_image_detail.configure(text="  "+file)

    def setImage(self, imgPath):
        image = Image.open(imgPath)
        width, height = image.size
        width = width/height*100
        image = ctk.CTkImage(image, size=(width, 100))
        self.l_image_logo.configure(image=image, text="")
        
    def save_action(self):
        print("save")

    def back_action(self):
        qb = QBFrame.me
        qb.setActiveFrame(qb.addSource)

class ManageQuestion(ctk.CTkFrame):
    searchVar:ctk.StringVar = None
    search_types = ("Question", "ID", "Options")
    search_type:str = None
    rows = list()
    questions:tuple=("What is TKINTEr", "What is python", "WHO IS ABHAY", "WHAT COMEs after 77")

    def load_questions(self):
        admin:ADMIN=ADMIN.me
        qb:QBFrame = QBFrame.me
        id = qb.selectedRound
        if int(id) == 1:
            questions = admin.qBank.round1
        if int(id) == 2:
            questions = admin.qBank.round2
        if int(id) == 3:
            questions = admin.qBank.round3
        if int(id) == 4:
            questions = admin.qBank.round4

        for row in self.rows:
            row.destroy()
        
        self.rows.clear()
        for q in questions:
            self.rows.append(self.createRow(self.f_questions, 0, q.qid, q.text,q.options,q.imgPath, "E"))
    
    def setTitle(self, title):
        self.l_title.configure(text=title)
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)

        self.configure(fg_color="#eee")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.searchVar = ctk.StringVar()
        # self.searchVar.set("")
        self.l_title = ctk.CTkLabel(self, text="Manage Question", fg_color="transparent")

        self.f_body=ctk.CTkFrame(self, fg_color="#fff", width=1000)
        self.f_body.grid_propagate(False)
        self.f_body.grid_columnconfigure(0, weight=1)
        self.f_body.grid_rowconfigure(2, weight=1)

        self.f_form = ctk.CTkFrame(self.f_body, fg_color="transparent", height=50)
        self.f_form.grid_columnconfigure(1, weight=1)

        self.l_filter = ctk.CTkLabel(self.f_form, text="Filter", )
        self.s_type = ctk.CTkComboBox(self.f_form,values=self.search_types, width=120)
        self.e_search = ctk.CTkEntry(self.f_form, placeholder_text="Search Questions",textvariable=self.searchVar, width=50  )
        self.b_search = ctk.CTkButton(self.f_form, text="🔍 Search ", width=10,  command=self.searching)
        self.b_add = ctk.CTkButton(self.f_form, text="+ Add ", width=10,  command=self.add_question)

        self.f_header=self.createRow(self.f_body, 0, "id", "Questions","Options", "IMAGE", "EDIT")
        self.f_header.configure(fg_color="transparent", corner_radius=5, border_width=2)

        self.f_questions = ctk.CTkScrollableFrame(self.f_body, fg_color="transparent",)# border_width=2, border_color="#888")
        self.f_questions.grid_columnconfigure(0,weight=1)
        for i,q in enumerate(self.questions):
            self.rows.append(self.createRow(self.f_questions, 0, i+1, q, "1,2,3,4", "N", "E"))
    
        self.f_footer = ctk.CTkFrame(self.f_body, width=800, height=400,  fg_color="transparent")
        self.b_discard = ctk.CTkButton(self.f_footer, text="Discard",  width=80, command=self.discard_action, height=35,)
        self.b_save = ctk.CTkButton(self.f_footer, text="Save", width=80, command=self.save_action, height=35)

    def createRow(self, master, select:bool, id:str, question:str, options:str, img:bool, edit:bool):
        f_header = ctk.CTkFrame(master,corner_radius=0, fg_color="transparent")
        checkbox_var = ctk.IntVar()
        c_selectall = ctk.CTkCheckBox(f_header, variable=checkbox_var, text="", checkbox_height=20, checkbox_width=20, border_width=2, width=24, )
        l_id = ctk.CTkLabel(f_header, text=id, anchor="w", width=40)
        l_question = ctk.CTkLabel(f_header, text=question, anchor="w", width=400)
        l_options = ctk.CTkLabel(f_header, text=options, anchor="w", width=200)

        l_img = ctk.CTkLabel(f_header, text=img, anchor="w", width=50)
        l_edit = ctk.CTkLabel(f_header, text=edit, anchor="w", )
        l_del = ctk.CTkLabel(f_header, text="DELETE", anchor="w", )
        
        
        c_selectall.grid(row=0, column=0, pady=5,padx=(10,0))
        l_id.grid(row=0, column=1,)
        l_question.grid(row=0, column=2, sticky="we",padx=10)
        l_options.grid(row=0, column=3, sticky="we")
        l_img.grid(row=0, column=4,padx=(10,0))
        l_edit.grid(row=0, column=5,padx=(10,0))
        l_del.grid(row=0, column=6,padx=10)

        return f_header
        pass

    def show(self):
        self.load_questions()
        self.grid(row=0, column=0, sticky="nswe",pady=10)

        self.l_title.grid(row=0, column=0,pady=(10,0), sticky="w", padx=20)
        
        self.f_body.grid(row=1, column=0, padx=10, pady=10, sticky="ns",)

        self.f_form.grid(row=0, column=0, sticky="we")
        self.l_filter.grid(row=0, column=0, sticky="w",padx=13)
        self.s_type.grid(row=1, column=0, sticky="w", padx=(10,0))
        self.e_search.grid(row=1, column=1, sticky="we", padx=10)
        self.b_search.grid(row=1, column=2, sticky="w")
        self.b_add.grid(row=1, column=3, sticky="w", padx=10)

        self.f_header.grid(row=1, column=0, sticky="we", pady=(5,0), padx=(8,15))
        
        self.f_questions.grid(row=2, column=0, sticky="nswe")
        for i,row in enumerate(self.rows):
            row.grid(row=i, column=0, sticky="we")
        
        self.f_footer.grid(row=3, column=0, sticky="we", pady=0, padx=10,)
        self.b_save.pack(side=ctk.RIGHT, padx=10, pady=5)
        self.b_discard.pack(side=ctk.RIGHT, padx=10, pady=5)

    def update_search_type(self, choice):
        self.search_type = self.search_types[choice]

    def save_questions(self):
        pass

    def save_action(self):
        self.save_questions()
        qb = QBFrame.me
        qb.setActiveFrame(qb.f_rounds)

    def discard_action(self):
        qb = QBFrame.me
        qb.setActiveFrame(qb.f_rounds)

    def searching(self):
        print("searching")

    def add_question(self):
        print("click add question")

class QBFrame(ctk.CTkFrame):
    me=None
    activeFrame:ctk.CTkFrame = None
    selectedRound = None
    addSource=None

    def setActiveFrame(self, frame):
        if self.activeFrame: self.activeFrame.grid_forget()
        self.activeFrame = frame
        self.activeFrame.show()

    def __init__(self, master, **kwargs):
        """attach children and configure grid"""
        super().__init__(master, fg_color="white",  **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.f_rounds = RoundsFrame(self)
        self.f_add = AddQuestion(self)
        self.f_manage = ManageQuestion(self)

        self.activeFrame=self.f_rounds
        QBFrame.me = self

    def show(self):
        """render children and current frame"""
        # self.f_rounds.show()
        # self.setActiveFrame(self.f_rounds)
        self.f_rounds.show()
        self.grid(row=0, column=0,padx=10, pady=10, sticky="nswe")
