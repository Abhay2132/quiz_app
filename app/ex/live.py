import customtkinter as ctk

class List(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        """attach children and configure grid"""
        super().__init__(master,  **kwargs)
        self.p1 = ctk.CTkButton(master=self, text="participants 1" ,fg_color="#333" , command=self.onclick)
        self.p2 = ctk.CTkButton(master=self, text="participants 3" ,fg_color="#433"  , command=lambda : print("CLICKED PARTICIPANT 3"))
        self.p3 = ctk.CTkButton(master=self, text="participants 2" ,fg_color="#566933"  , command=lambda : print("CLICKED PARTICIPANT 2"))
        self.grid_columnconfigure(0, weight=1)

    def onclick (self, n=1):
        print(f"CLICKED PARTICIPANT {n}")
    
    def show(self):

        self.grid(row=1, column=0,sticky="nswe")
        self.p1.grid(row=0,column=0,sticky="we", padx=10 , pady=5)
        self.p2.grid(row=1,column=0,sticky="we", padx=10 , pady=5)
        self.p3.grid(row=2,column=0,sticky="we", padx=10 , pady=5)


class FrameName(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        """attach children and configure grid"""
        super().__init__(master, fg_color="white",  **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # self.label = ctk.CTkLabel(master=self, text="THIS LABEL IS CHILD OF THIS FRAME", anchor="center")
        self.topbar = ctk.CTkLabel(master=self,text="Participants", fg_color="red")
        # self.list = ctk.CTkLabel(master=self, text="PARTCIPANT", fg_color="green")
        self.list = List(master=self, fg_color="green")
        self.footer = ctk.CTkLabel(master=self, text="Footer", fg_color="blue")

    def show(self):
        """render children and current frame"""

        # self.label.place(relx=0.5, rely=0.5, anchor="center")
        self.topbar.grid(row=0, column=0, sticky="we")
        self.list.show()
        self.footer.grid(row=2, column=0,sticky="we")

        self.grid(row=0, column=0,padx=10, pady=10, sticky="nswe")
        # implement your own logic
        pass

if __name__ == "__main__":
    window = ctk.CTk()
    window.geometry("800x600")

    frame = FrameName(window)
    # frame = FrameName(window, border_width=10, border_color="#333")
    frame.show()

    window.grid_columnconfigure(0,weight=1)
    window.grid_rowconfigure(0,weight=1)
    window.mainloop()