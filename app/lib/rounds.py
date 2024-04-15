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
from .struct import ADMIN
from .qb import QuestionBank
from .util import Participants,Participant
from .struct import Round
from .qb import ClientQuestion, Question
from .sm import Scores
from .util import createPayload

class Round1(Round):
    name="Straight Forward"
    mark=10
    minusMark=0

    def __init__(self,admin) -> None:

        self.admin:ADMIN = admin
        self.__questions = tuple(self.admin.qBank.round1)

        print(len(self.__questions))

    def loadQ(self):
        return super().loadQ()

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
        self.admin.server.broadcast(createPayload("setround", 1))
        self.askQ()
        self.curr_scores=Scores(self.admin.participants.getClientIDs())

    def askQ(self):
        participantID = self.admin.participants.getClientIDs()[self.currentParticipant]
        question:Question = self.__questions[self.currentQuestion]
        self.admin.askQ(participantID, question.forParticipant())

    def askNextQ(self):
        self.currentParticipant = (self.currentParticipant+1)%self.admin.participants.count()
        self.currentQuestion += 1
        if self.currentQuestion >= len(self.__questions):
            self.onend()
            return
        self.askQ()

    def onend(self):
        """Manage Score and Clean up"""
        
        pass

class Round2(Round):

    name="Bujho Toh Jano"
    def __init__(self,admin) -> None:
        self.admin:ADMIN = admin
        self.__questions = tuple(self.admin.qBank.round2)


    def loadQ(self):
        return super().loadQ()

class Round3(Round):
    name="Roll the Dice"
    def __init__(self,admin) -> None:
        self.admin:ADMIN = admin
        self.__questions = tuple(self.admin.qBank.round3)

    def loadQ(self):
        return super().loadQ()

class Round4(Round):

    name="Straight Forward"
    def __init__(self,admin) -> None:
        self.admin:ADMIN = admin
        self.__questions = tuple(self.admin.qBank.round4)

    def loadQ(self):
        return super().loadQ()

