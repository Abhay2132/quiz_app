import customtkinter as ctk
from .utils import rc

class ListItem(ctk.CTkFrame):
    
    def __init__(self, master, name="", **kwargs):
        super().__init__(master, **kwargs)
        self.configure(height=60)
        self.grid_columnconfigure(0, weight=1)
        # self.grid_propagate(False)
        # transparent
        self.configure(fg_color="#eee")

        commons = {
            "border_width":2,
            "border_color":"#888",
            "fg_color":"#fff",
            "width":100,
            "text_color":"#333",
            "hover_color":"#ccf"
        }

        self.l_name = ctk.CTkLabel(self,text=name, fg_color="transparent",font=('sans', 15))
        self.l_desc = ctk.CTkLabel(self, text="questions:0", fg_color="transparent", anchor="s", font=('sans', 12), height=15, text_color="#444")
        self.b_manage = ctk.CTkButton(self, text="MANAGE", **commons)
        self.b_upload = ctk.CTkButton(self, text="UPLOAD", **commons)
        self.b_add = ctk.CTkButton(self, text="ADD", **commons)

    def show(self, r,c):

        self.l_name.grid(row=0, column=0, sticky="w", padx=20, pady=(5,0))
        self.l_desc.grid(row=1, column=0, sticky="w", padx=30, pady=(0,10))
        self.b_manage.grid(row=0, column=1, rowspan=2, padx=(0,10))
        self.b_upload.grid(row=0, column=2, rowspan=2, padx=(0,10))
        self.b_add.grid(row=0, column=3, rowspan=2, padx=(0,10))

        # self.grid(row=r, column=c, sticky="we", padx=5, pady=5)
        self.pack(side=ctk.TOP, fill=ctk.X, padx=(0,10), pady=(5,0))

class List(ctk.CTkFrame):
    items = list()
    def __init__(self, master, **kwargs):
        """attach children and configure grid"""
        super().__init__(master,  **kwargs)
        self.items.append(ListItem(self, name="ROUND-I", fg_color='transparent', border_width=2))
        self.items.append(ListItem(self, name="ROUND-II", fg_color='transparent', border_width=2))
        self.items.append(ListItem(self, name="ROUND-III", fg_color='transparent', border_width=2))
        self.items.append(ListItem(self, name="ROUND-IV", fg_color='transparent', border_width=2))

        self.grid_columnconfigure(0, weight=1)
    
    def show(self):

        self.grid(row=1, column=0,sticky="nswe", padx=20)
        for r,item in enumerate(self.items):
            item.show(r=r, c=0)

class QBFrame(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        """attach children and configure grid"""
        super().__init__(master, fg_color="white",  **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.topbar = ctk.CTkLabel(master=self,text="Participants", anchor="w")
        self.list = List(master=self, fg_color="transparent")

    def show(self):
        """render children and current frame"""
        self.topbar.grid(row=0, column=0, sticky="we", padx=20, pady=10)

        self.list.show()
        self.grid(row=0, column=0,padx=10, pady=10, sticky="nswe")
