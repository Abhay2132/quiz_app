from .util import Participants
from .qb import QuestionBank, Question
from .sm import Scores
from ..ui.admin.structs import _App
from .sockets import ServerSocket,ClientSocket
import os

class ADMIN():
    participants=Participants()
    qBank=QuestionBank(qdir=os.path.join(os.getcwd(), "data", "questions"))
    scores:Scores=None
    ui:_App=None
    server:ServerSocket=None
    me=None

    def askQ(self,clientID, question:Question):
        pass

    def checkQ(self, question)->bool:
        pass

    def updateScore(self):
        pass

    def start(self):
        pass

class USER():
    client:ClientSocket=None
    me=None
    ui=None
    name:str=None

    def setName(self, name):
        self.name = name