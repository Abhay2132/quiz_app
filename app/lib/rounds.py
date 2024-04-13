"""
Round Manager classes to operate rounds
Actions :-
1.) Send Start signal to clients
2.) PLAY / PAUSE (signal from admin)

Admin Signals :-
1.) Signal to play , pause , stop, goto next round and pre round
"""
from .sockets import ServerSocket
import csv
import random
from .admin import ADMIN
from .qb import QuestionBank
from .util import Participants,Participant

class Round():
    admin:ADMIN=None
    __questions = tuple()
    num_q = 5
    currentParticipant:int=0
    currentQuestion:int=0

    def loadQ():
        pass

    def start():
        pass
    
    def askQ():
        pass

    def onend():
        pass

class Round1(Round):
    admin:ADMIN = None
    __questions:tuple = None
    num_q = 5 # number of questions asked to each participant

    def __init__(self, admin:ADMIN, questions:tuple) -> None:
        self.admin = admin
        # self.qPath = qPath
        self.__questions=questions
        # self.loadQ()
        pass

    def loadQ(self):
        """Load current round question from given and other settings"""
        # with open(self.qPath,"r") as f:
        # reader = csv.reader(f)
        allQuestions = list(self.__questions)
        required_q = self.num_q*self.admin.participants.count()

        if len(allQuestions) < required_q:
            raise Exception("NUMBER OF QUESTIONs in DB is less than participants")
        random.shuffle(allQuestions)
        self.__questions = tuple(allQuestions[0:required_q])

    def start(self):
        """Starting sending questions to clients and managing score"""
        self.loadQ()
        i=0
        ids = self.admin.participants.getClientIDs()
        pn = self.admin.participants.count()
        for question in self.__questions:
            self.askQ(ids[i], question)
            i = (i+1)%pn
            pass

    def askQ(self, clientID:Participant.clientID, question):
        """Send individual question to a participant"""
        self.admin.askQ(clientID, question)
        pass

    def onend(self):
        """Manage Score and Clean up"""
        pass
