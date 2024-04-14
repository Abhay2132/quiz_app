from .util import Participants
from .qb import QuestionBank, Question
from .sm import Scores
from ..ui.admin.structs import _App
from .sockets import ServerSocket

class ADMIN():
    participants:Participants=None
    qBank:QuestionBank=None
    scores:Scores=None
    ui:_App=None
    server:ServerSocket=None

    def askQ(self,clientID, question:Question):
        pass

    def checkQ(self, question)->bool:
        pass

    def updateScore(self):
        pass

    def start(self):
        pass