import customtkinter as ctk
from .frames.screen_saver import ScreenSaver
from .frames.login import LoginFrame
from ..rounds.round1 import Round1
from ..rounds.round2 import Round2
from ..rounds.round3 import Round3
from ..rounds.round4 import Round4

ctk.set_appearance_mode('light')

class MainPanel(ctk.CTkFrame):
    f_login=None
    def setActiveFrame(self,frame):
        app = App.me
        app.mainpanel.activeframe.grid_forget()
        app.mainpanel.activeframe=frame
        app.mainpanel.activeframe.show()
        
    def __init__(self,master,**kwargs):
        
        super().__init__(master=master,fg_color="transparent",border_color="black",border_width=2,**kwargs)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.f_login=LoginFrame(self)
        self.f_round1=Round1(self)
        self.f_round2=Round2(self)
        self.f_round3=Round3(self)
        self.f_round4=Round4(self)
        self.f_screensaver=ScreenSaver(self)
        self.activeframe=self.f_login
        
    def show(self):
        self.activeframe.show()
        self.pack(fill=ctk.BOTH, expand=True,padx=20,pady=20)  # Fills and expands to center


class App(ctk.CTk):
    hight,width=400,800
    me =None
    app = None
    activeRound=None

    def __init__(self, app=None, **kwargs):
        super().__init__(fg_color=None, **kwargs)
        App.me = self
        self.app = app
        # self.geometry(f'{self.width}x{self.hight}')
        self.geometry("800x600")
        self.after(10, lambda:self.state("zoomed"))

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.mainpanel=MainPanel(self)

    def show(self):
        self.mainpanel.show()
        self.mainloop()

def main():
    app=App()
    app.show()

if __name__ == "__main__":
    main()