
import customtkinter as ctk
import tkinter
class Rank_Table(ctk.CTkFrame):
    teams=list()

    def __init__(self, master, **kwargs):
        super().__init__(master,fg_color='white', **kwargs)
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.teams.append(self.createTeam(self,'anshul','1'))
        self.teams.append(self.createTeam(self,'anshul','1'))
        self.teams.append(self.createTeam(self,'anshul','1'))

    def createTeam(self,master, name, score)->ctk.CTkFrame:
        f_team=ctk.CTkFrame(master=master,fg_color='transparent', width=500,height=40,border_width=2)
        f_team.grid_propagate(False)
        f_team.columnconfigure(0,weight=1)
        l_team_nam=ctk.CTkLabel(f_team,text=name,font=('Roboto',20),text_color='#333',fg_color='transparent')
        l_rank=ctk.CTkLabel(f_team,text=score,font=('Roboto',18),text_color='#333',fg_color='transparent')
        l_team_nam.grid(row=0,column=0,sticky='w',padx=20,pady=8)
        l_rank.grid(row=0,column=1,sticky='e',padx=50,pady=8)
        
        return f_team

    def updateTeams(self, ranks: tuple):
        print("updating teams")
        for child in self.teams:
            child.grid_forget()
        self.teams = list([self.createTeam(self, rank.name, rank.score) for rank in ranks ])
        for i,team in enumerate(self.teams):
            team.grid(row=i,column=0,sticky='we',padx=40,pady=(5,0))

    def show(self):
        for i,team in enumerate(self.teams):
            team.grid(row=i,column=0,sticky='we',padx=20,pady=8)
        self.updateTeams([
            Rank("ABC", 1),
            Rank("ABD", 2),
            Rank("ABF", 3),
        ])

class Rank():
    name=""
    score:int=0

    def __init__(self, name, score) -> None:
        self.name=name
        self.score:int=score
        pass
    pass

class Score(ctk.CTkFrame):

    scores=list()
    def __init__(self, master, **kwargs):
        super().__init__(master=master, fg_color='white',**kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.main_frame = ctk.CTkFrame(self, border_width=2,fg_color='transparent')
        self.round_text = ctk.CTkLabel(self.main_frame, text="Round I",font=("Arival",40), text_color="#333", )
        self.finish = ctk.CTkLabel(self.main_frame, text="Finished",font=("Arival",25), text_color="#666", )
        self.score_text = ctk.CTkLabel(self.main_frame, text="Score: ",font=("Arival",25), text_color="#333", )
        self.next_button = ctk.CTkButton(self.main_frame, text="      Next ROUND ⏩      ", fg_color="#4169E1", command=self.next_action, font=("Roboto", 16), height=40)
        
        self.ranktable=Rank_Table(self.main_frame)

    def show(self):
        self.main_frame.grid(row=0,column=0,padx=0,pady=20)
        self.round_text.grid(row=1, column=0, columnspan=3, padx=20, pady=(10,0), sticky="we")
        self.finish.grid(row=2, column=0, padx=10, sticky="we", pady=0)
        self.score_text.grid(row=3, column=0, padx=30, sticky="w", pady=20)
        self.ranktable.show()
        self.ranktable.grid(row=4,column=0,sticky='nsew',padx=10,pady=10)
        self.next_button.grid(row=5,column=0,padx=(0,50),pady=10, sticky="e")
        self.pack(expand=True,fill=tkinter.BOTH,padx=30,pady=30,)

    def next_action(self):
        print("next")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # self.geometry("800x600")
        # self.grid_columnconfigure(0, weight=``)
        self.title("Question FRAME")
        self.scoring =  Score(self)

    def show(self):
        self.scoring.show()
        self.mainloop()

if __name__ == "__main__":
    app = App()
    app.show()
