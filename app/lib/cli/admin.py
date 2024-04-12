from ..sockets import ServerSocket
from .util import askMCQ, cls, goBack
import sys
from .settings import addr
import os
import csv

def main():
    admin = Admin()
    admin.start()

class Admin():
    
    participants = dict()
    server = None
    def __init__(self) -> None:
        self.server = ServerSocket(addr=addr)
        self.server.on("new-connection", self.addParticipant)
        pass
    
    def addParticipant(self, args):
        pass

    def attachListeners(self):
        pass

    def getParticipants(self) -> tuple:
        return tuple(self.server.clients.keys())
    
    def printParticipants(self):
        participants = self.getParticipants()
        print(f"\tParticipants ({len(participants)})")
        for i,participant in enumerate(participants):
            print(f"{i+1}). {participant}")

    def viewQuestions(self):
        csvPath = os.path.join(__file__, "..","..", "sample_data", "MCQs.csv")
        with open(csvPath, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)

    def viewParticipants(self):
        ans = askMCQ("", ("REFRESH", "GO BACK",) , self.printParticipants)
        if ans == 1:
            self.dashboard()
        elif ans == 0:
            self.viewParticipants()
        
    def startQuiz(self):
        pass

    def dashboard(self):
        cls()
        self.server.start()
        self.attachListeners()

        options = ("Start QUIZ", "VIEW PARTICIPANTS", "View Questions", "ExiT")
        ans = askMCQ("\tADMIN PANEL",options)

        if ans == 0:
            pass
        elif ans == 1:
            self.viewParticipants()
        elif ans == 2:
            askMCQ("",("GO BACK",),self.viewQuestions)
            self.dashboard()
        elif ans == 3:
            sys.exit()
        pass

    def start(self):
        options = ("Start Server", "Exit")
        ans = askMCQ("\t Admin Panel", options)
        if ans == 0:
            self.dashboard()
        if ans == 1:
            sys.exit()

if __name__ == "__main__":
    main()