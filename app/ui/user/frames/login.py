import customtkinter as ctk
from ....lib.struct import USER

# Entry and Login Panel (Enhanced)
class Form(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, fg_color='transparent',border_color="white",border_width=2, **kwargs)

        # for the icon 
        self.icon=ctk.CTkLabel(self,fg_color="blue",width=500,height=300,text="icon goes here")
        

        # Create user ID label with better styling (optional)
        self.userid = ctk.CTkLabel(self, text="UserID:",
                                   font=('Helvetica', 18, 'bold'),
                                   text_color='#DAA520')

        # Create entry field with improved styling (optional)
        self.e_userid = ctk.CTkEntry(self,
                                     placeholder_text="Enter the ID...",
                                     font=('Helvetica', 14),
                                     text_color='black',
                                     width=200)

        # Create login button with better styling (optional)
        self.submit_b = ctk.CTkButton(self, text='Login',
                                      fg_color="blue",
                                      hover_color="lightblue",
                                      command=self.click_submit
                                      )

    def click_submit(self):

        name = str(self.e_userid.get()).strip()
        if len(name) < 3:
            return print("ERROR : USERNAME SHOULD BE GREATER THAN 3 LETTERS")
        user:USER = USER.me
        user.setName(name)
        user.client.connect()
        # user.ui.mainpanel.setActiveFrame(user.ui.mainpanel.f_screensaver)
    
    def show(self):
        """Organize elements using grid for precise layout"""
        self.icon.grid(row=0, column=0, padx=20, pady=10, sticky='we')
        self.userid.grid(row=1, column=0, padx=20, pady=10, )#sticky='we')
        self.e_userid.grid(row=2, column=0, padx=20, pady=10, )#sticky='we')
        self.submit_b.grid(row=3, column=0, padx=20, pady=15, )#sticky='we')
        self.after(500, lambda : self.e_userid.focus())


# Main Login Frame (Enhanced)
class LoginFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, fg_color='transparent',border_color="white",border_width=3, **kwargs)

        # Create title using customtkinter label and styling (optional)
        self.title_page = ctk.CTkLabel(
            self, text="Login", fg_color='transparent',
            font=('Garamond', 50), text_color='#00FF00',
            )
    def show(self):
        # Create an instance of the Entery class (enhanced)
        self.entry = Form(self)

        # Place elements using grid for layout control
        self.title_page.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)
        self.entry.grid(row=1, column=0, padx=20, pady=20)
        self.entry.show()

        # Configure LoginFrame's grid for centering
        self.grid_columnconfigure(0, weight=1)  # Make the single column flexible

        # Use `pack` for optional padding and window filling
        # self.pack(fill=ctk.BOTH, expand=True, padx=20, pady=20)
        self.grid(row=0, column=0, sticky="nswe", padx=20, pady=20)

