from .util import Participants
from .qb import QuestionBank, Question, ClientQuestion
from .sm import Scores
from ..ui.admin.structs import _App
from .sockets import ServerSocket,ClientSocket
import os
import random
# from .rounds import 

class Round():
    admin=None
    __questions = tuple()
    num_q = 5
    currentParticipant:int=0
    currentQuestion:int=0
    isFinished=False
    curr_scores:Scores=None

    def loadQ(self):
       pass

    def start():
        pass
    
    def askQ():
        """
        Send `start` signal to participants
        
        """
        pass

    def askNextQ(self):
        pass

    def onend():
        pass

class ADMIN():
    participants=Participants()
    qBank=None
    scores:Scores=None
    ui:_App=None
    server:ServerSocket=None
    me=None
    quiz_started=False
    currentRound:Round=None
    num_participants:int=0 # number of participant in quiz when it started
    scores:Scores=None

    def askQ(self,clientID, question:ClientQuestion):
        pass

    def checkQ(self, question)->bool:
        pass

    def updateScore(self):
        pass

    def start(self):
        pass

    def setName(clientID, name):
        pass

class USER():
    client:ClientSocket=None
    me=None
    ui=None
    name:str=None

    def setName(self, name):
        self.name = name