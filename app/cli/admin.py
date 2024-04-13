from ..lib.sockets import ServerSocket, ClientSocket, EventEmitter
from .util import askMCQ, cls, goBack
import sys
from .settings import addr, MCQ_1, cwd
import os
import csv
from ..lib.rounds import Round1
import json
from ..lib.admin import ADMIN
from ..lib.util import Participant, Participants, createPayload
from ..lib.qb import QuestionBank, Question
from ..lib.rounds import Round

class Admin(ADMIN, EventEmitter):
    
    participants = Participants()
    qBank:QuestionBank=QuestionBank(os.path.join(cwd, "..", "lib", "sample_data"))
    server = None
    currentRoundIndex=0
    rounds = list()
    currentRound = None
    
    def __init__(self) -> None:
        self.server = ServerSocket(addr=addr)
        self.server.on("new-connection", self.addParticipant)
        self.server.on("data", self.handleDataEvent)
        self.rounds.append(Round1(self, self.qBank.round1))

        self.currentRound = self.rounds[0]
        # self.qBank.load()
    
    def askQ(self, clientID:Participant.clientID, question: Question):
        options = list(filter(bool, question.options.split(",")))
        payload = createPayload("askQ", question.forParticipant())
        self.server.sendTo(payload, clientID)
        # ans = askMCQ(question.text, question.options, lambda:print(""))
        cls()
        print("ROUND -", self.currentRoundIndex+1)
        print("\n Q.)", question.text)
        for i,o in enumerate(question.options):
            print(f"{i}. {o}")


    def addParticipant(self, args):
        """append a new `Participant` and Attach it events """
        clientID = args[0]
        clientSocket = self.server.clients.get(clientID).fileobj
        participant = Participant(clientSocket,clientID, )
        # self.participants.append(participant)
        self.participants.add(participant)
        pass

    def handleDataEvent(self, args):
        # self.server.on("data", )
        data = args[0]
        clientID = data["clientID"]
        data = data['data']
        if not data:
            return
        data = json.loads(data)#.decode("utf-8"))
        
        # handle data actions
        action = data["action"]
        data = data["data"]
        
        if action=="setname":
            if self.participants.find(clientID):
                participant = self.participants.get(clientID)
                participant.name = data

    def getParticipants(self) -> tuple:
        return tuple(self.participants.getNames())
    
    def viewQuestions(self):
        print("qid , text , options , answer , imgPath")
        for q in self.qBank.round1:
            print(f"{q.qid}. '{q.text}' '{q.options}' '{q.answer}' '{q.imgPath}'")

    def printParticipants(self):
        participants = self.getParticipants()
        print(f"\tParticipants ({len(participants)})")
        for i,participant in enumerate(participants):
            print(f"{i+1}). {participant}")

    def viewParticipants(self):
        ans = askMCQ("", ("REFRESH", "GO BACK",) , self.printParticipants)
        if ans == 1:
            self.dashboard()
        elif ans == 0:
            self.viewParticipants()
        
    def startQuiz(self):
        for i,round in enumerate(self.rounds):
            self.currentRoundIndex = i
            self.currentRound:Round = round
            # round.init()
            self.currentRound.start()
            # round

    def dashboard(self):
        cls()
        self.server.start()
        # self.attachListeners()

        options = ("Start QUIZ", "VIEW PARTICIPANTS", "View Questions", "ExiT")
        ans = askMCQ("\tADMIN PANEL",options)

        if ans == 0:
            self.startQuiz()
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

def main():
    admin = Admin()
    admin.start()

if __name__ == "__main__":
    main()