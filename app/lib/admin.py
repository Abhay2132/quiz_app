from .util import Participants
from .qb import QuestionBank, Question
from .sm import Scores

class ADMIN():
    participants:Participants=None
    qBank:QuestionBank=None
    scores:Scores=None

    def askQ(self,clientID, question:Question):
        pass

    def checkQ(self, question)->bool:
        pass

    def updateScore(self):
        pass