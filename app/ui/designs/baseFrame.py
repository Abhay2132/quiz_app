import customtkinter as ctk

class FrameName(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        """attach children and configure grid"""
        super().__init__(master, **kwargs)

        self.label = ctk.CTkLabel(master=self, text="THIS LABEL IS CHILD OF THIS FRAME", anchor="center")

    def show(self):
        """render children and current frame"""

        self.label.place(relx=0.5, rely=0.5, anchor="center")
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