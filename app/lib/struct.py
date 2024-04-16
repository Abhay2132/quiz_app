from .util import Participants, createPayload
from .qb import QuestionBank, Question, ClientQuestion
from .sm import Scores
from ..ui.admin.structs import _App
from .sockets import ServerSocket,ClientSocket
import os
import random
# from .rounds import 
from ..ui.admin.frames.live import PlayFrame

class Round():
    admin=None
    __questions:tuple=None
    num_q = 5
    currentParticipant:int=0
    currentQuestion:int=0
    isFinished=False
    curr_scores:Scores=None
    lastQuestionMarked=False
    mark=10
    minusMark=0
    id=None
    name=None
    roundEnded=False

    def __init__(self, admin, questions, mark, minusMark, id, name, num_q=5) -> None:
        self.admin:ADMIN = admin
        self.__questions = tuple(questions)
        self.mark=mark
        self.minusMark=minusMark
        self.id=id
        self.name=name
        self.num_q = num_q

    def check_answer(self, qid, answer):
        self.lastQuestionMarked=True
        rightAns = None
        for question in self.__questions:
            if str(qid) == str(question.qid):
                rightAns=question.answer
        isRight=int(rightAns)==int(answer)
        print(f"CHECKING ANSWER qid:{qid}, ans:{answer}, correct:{rightAns}")
        participantID = self.admin.participants.getClientIDs()[self.currentParticipant]
        if isRight:
            self.curr_scores.add(participantID, self.mark)
        else:
            self.curr_scores.add(participantID, self.minusMark)

        print(isRight)
        return rightAns
        
    def loadQ(self):
        allQuestions = list(self.__questions)
        required_q = self.num_q*self.admin.participants.count()
        if len(allQuestions) < required_q:
            raise Exception("NUMBER OF QUESTIONs in DB is less than participants")
        random.shuffle(allQuestions)
        self.__questions = tuple(allQuestions[0:required_q])

    def start(self):
        print(f"ROUND-{self.id} started")
        self.loadQ()
        self.admin.server.broadcast(createPayload("setround", self.id))
        self.askQ()
        self.curr_scores=Scores(self.admin.participants.getClientIDs())

    def askQ(self):
        participantID = self.admin.participants.getClientIDs()[self.currentParticipant]
        question:Question = self.__questions[self.currentQuestion]
        self.admin.askQ(participantID, question.forParticipant())
        pf:PlayFrame = PlayFrame.me
        name = self.admin.participants.getNames()[self.currentParticipant]
        pf.setInfo(name, f"Question : {self.currentQuestion+1}/{len(self.__questions)}")
        pass

    def askNextQ(self):
        if not self.lastQuestionMarked : return
        self.lastQuestionMarked = False
        self.currentParticipant = (self.currentParticipant+1)%self.admin.participants.count()
        self.currentQuestion += 1
        if self.currentQuestion >= len(self.__questions):
            self.onend()
            return
        self.askQ()

    def mark_right(self):
        if self.lastQuestionMarked or self.roundEnded:return
        self.lastQuestionMarked=True
        participantID = self.admin.participants.getClientIDs()[self.currentParticipant]
        self.curr_scores.add(participantID, self.mark)
        # print(self.curr_scores.toString())
        # print(self.admin.scores.toString())
        # print(self.curr_scores.scores is self.admin.scores.scores)

    def mark_wrong(self):
        if self.lastQuestionMarked or self.roundEnded:return
        self.lastQuestionMarked=True
        participantID = self.admin.participants.getClientIDs()[self.currentParticipant]
        self.curr_scores.add(participantID, self.minusMark)

    def onend(self):
        """Add scores to main and SHOW SCOREBOARD"""
        self.roundEnded=True
        self.admin.scores.addScore(self.curr_scores)
        self.curr_scores.reset()
        print(self.curr_scores.toString())
        print(self.admin.scores.toString())
        pf:PlayFrame=PlayFrame.me
        pf.f_scores.setData(self.name, self.admin.scores.scores, self.id < 4)
        pf.setActiveFrame(pf.f_scores)

class ADMIN():
    
    lastQuestionMarked=False
    participants=Participants()
    qBank:QuestionBank=None
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

    def askAll(self, question):
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