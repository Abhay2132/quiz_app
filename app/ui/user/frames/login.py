import customtkinter as ctk
from ....lib.struct import USER
from PIL import Image
import os

# Entry and Login Panel (Enhanced)
class Form(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, fg_color='transparent',border_color="white",border_width=2, **kwargs)


        self.icon=ctk.CTkLabel(self, fg_color="transparent",width=500,height=300,text="icon goes here")
        self.userid = ctk.CTkLabel(self, text="UserID:",font=('Helvetica', 18, 'bold'),text_color='#DAA520')
        self.e_userid = ctk.CTkEntry(self,placeholder_text="Enter the ID...",font=('Helvetica', 14),width=200)
        self.submit_b = ctk.CTkButton(self, text='Login',fg_color="blue",hover_color="lightblue",command=self.click_submit)
        self.l_info=ctk.CTkLabel(self, text="", anchor="w", fg_color="transparent", font=("Roboto", 13))

    def click_submit(self):

        name = str(self.e_userid.get()).strip()
        if len(name) < 3:
            return print("ERROR : USERNAME SHOULD BE GREATER THAN 3 LETTERS")
        user:USER = USER.me
        user.setName(name)
        user.login()
        # user.ui.mainpanel.setActiveFrame(user.ui.mainpanel.f_screensaver)
    
    def show(self):
        """Organize elements using grid for precise layout"""
        self.icon.grid(row=0, column=0, padx=20, pady=10, sticky='we')
        self.userid.grid(row=1, column=0, padx=20, pady=10, )#sticky='we')
        self.e_userid.grid(row=2, column=0, padx=20, pady=10, )#sticky='we')
        self.submit_b.grid(row=3, column=0, padx=20, pady=(15,0), )#sticky='we')
        self.l_info.grid(row=4, column=0, padx=50, pady=(10,15), sticky="we")
        self.after(400, lambda : self.e_userid.focus())

        # img=None
        logo_path = os.path.join(os.getcwd(), "data", "icons", "login_logo.jpg")
        self.setImage(logo_path)
        # if os.path.exists(logo_path) and os.path.isfile(logo_path):
        #     img = ctk.CTkImage(Image.open(logo_path))

    def setImage(self, imgPath):
        image = Image.open(imgPath)
        width, height = image.size
        l_width=int(self.icon.cget("width"))
        height = height/width*l_width
        print(f"{width}x{height}")
        image = ctk.CTkImage(image, size=(l_width,height))
        self.icon.configure(image=image, text="")

# Main Login Frame (Enhanced)
class LoginFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, fg_color='transparent',border_color="white",border_width=3, **kwargs)

        # Create title using customtkinter label and styling (optional)
        self.title_page = ctk.CTkLabel(
            self, text="Login", fg_color='transparent',
            font=('Garamond', 50), text_color='#00FF00',
            )
        self.f_form = Form(self)

    def show(self):
        # Create an instance of the Entery class (enhanced)

        # Place elements using grid for layout control
        self.title_page.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)
        self.f_form.grid(row=1, column=0, padx=20, pady=20)
        self.f_form.show()

        # Configure LoginFrame's grid for centering
        self.grid_columnconfigure(0, weight=1)  # Make the single column flexible

        # Use `pack` for optional padding and window filling
        # self.pack(fill=ctk.BOTH, expand=True, padx=20, pady=20)
        self.grid(row=0, column=0, sticky="nswe", padx=20, pady=20)

    def hide(self):
        self.grid_forget()

