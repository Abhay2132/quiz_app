from .util import Participants
from .qb import QuestionBank, Question

class ADMIN():
    participants:Participants=None
    qBank:QuestionBank=None

    def askQ(self,clientID, question:Question):
        pass