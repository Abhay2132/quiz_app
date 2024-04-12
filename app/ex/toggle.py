import customtkinter as ctk

window = ctk.CTk()

window.geometry("800x600")
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)

list = ctk.CTkScrollableFrame(window, height=300, width=500)
# list.pack_propagate(False)
list.grid_columnconfigure(0, weight=1)
list.grid(row=0, column=0)


def toggle(item1):
    if item1.winfo_height() == 50:
        item1.configure(height=80)
    else:
        item1.configure(height=80)


class Item(ctk.CTkFrame):
    titleLabel = None
    bodyLabel = None
    opened = False
    def __init__(self, master,title="", body="", **kwargs):
        super().__init__(master=master, **kwargs)
        self.configure(fg_color="red")
        self.grid_columnconfigure(0, weight=1)
        self.titleLabel = ctk.CTkLabel(self, text=title, fg_color="green", height=40)
        self.bodyLabel = ctk.CTkLabel(self, text=body, fg_color="red")

        self.b_toggle = ctk.CTkButton(self, text="Toggle", fg_color="transparent", border_width=1, corner_radius=5, command=self.toggle)

    def toggle(self):
        if self.opened:
            self.bodyLabel.grid_forget()
            self.opened = False
        else:
            self.bodyLabel.grid(row=1, column=0, columnspan=2)
            self.opened = True

        pass
        
    def show(self, r=0,c=0):
        self.b_toggle.grid(row=0, column=1)
        self.grid(row=r, column=c, sticky="we")

Item(list, "Title", body="BODY").show()

window.mainloop()