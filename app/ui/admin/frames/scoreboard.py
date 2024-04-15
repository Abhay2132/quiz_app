import customtkinter as ctk

class Rank():
    name=""
    score:int=0

    def __init__(self, name, score) -> None:
        self.name=name
        self.score:int=score
        pass
    pass


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
        f_team=ctk.CTkFrame(master=master,fg_color='transparent',width=400,height=100,border_width=2)
        f_team.columnconfigure(0,weight=1)
        l_team_nam=ctk.CTkLabel(f_team,text=name,font=('Roboto',30),text_color='blue',fg_color='transparent')
        l_rank=ctk.CTkLabel(f_team,text=score,font=('Roboto',30),text_color='blue',fg_color='transparent')
        l_team_nam.grid(row=0,column=0,sticky='w',padx=10,pady=8)
        l_rank.grid(row=0,column=1,sticky='e',padx=50,pady=8)
        
        return f_team

    def updateTeams(self, ranks: tuple):
        print("updating teams")
        for child in self.teams:
            child.grid_forget()
        self.teams = list([self.createTeam(self, rank.name, rank.score) for rank in ranks ])
        for i,team in enumerate(self.teams):
            team.grid(row=i,column=0,sticky='we',padx=20,pady=8)

    def show(self):
        for i,team in enumerate(self.teams):
            team.grid(row=i,column=0,sticky='we',padx=20,pady=8)

        self.grid(row=1,column=0,sticky='nsew',padx=10,pady=10)

        self.updateTeams([
            Rank("ABC", 1),
            Rank("ABD", 2),
            Rank("ABF", 3),
        ])
        # self.f_team1.grid(row=0,column=0,sticky='nsew',padx=20,pady=8)
    
class ScoreBoard(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master,fg_color='white', **kwargs)
        self.page_title=ctk.CTkLabel(self,text='Final Rank',font=('Roboto',56),text_color='blue',fg_color='transparent')
        self.rowconfigure(2,weight=1)
        self.columnconfigure(0,weight=1)
        self.ranktable=Rank_Table(self)

    def show(self):
        self.ranktable.show()
        self.grid(row=0,column=0,sticky='nsew',padx=10,pady=10)
        self.page_title.grid(row=0,column=0,sticky='nw',padx=20,pady=20)

if __name__ == "__main__":
    app = ctk.CTk()

    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(0, weight=1)
    sb=ScoreBoard(app)
    sb.show()

    app.mainloop()
