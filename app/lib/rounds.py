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
from ..ui.admin.frames.live import PlayFrame
from ..ui.rounds.round2 import Round2 as R2
import random

class Round1(Round):
    name="Straight Forward"
    def __init__(self,admin:ADMIN) -> None:
        super().__init__(admin, admin.qBank.round1, mark=10, minusMark=0,id=1, name=Round1.name)

class Round2(Round):
    name="Bujho Toh Jano"
    def __init__(self,admin:ADMIN) -> None:
        super().__init__(admin, admin.qBank.round2,mark=10, minusMark=-5, id=2, name=Round2.name)

    def check_answer(self, qid, answer):
        rightAns = super().check_answer(qid, answer)
        self.admin.show_right_answer(qid, rightAns, answer)
    
class Round3(Round):
    name="Roll the Dice"
    rolling_i=None # store the index of the participant who is rolling the dice
    target_i=None # the index of the participant came by rolling the dice

    def __init__(self,admin) -> None:
        super().__init__(admin, admin.qBank.round3,mark=10, minusMark=-5, id=3, name=Round3.name)

    def check_answer(self, qid, answer):
        rightAns = super().check_answer(qid, answer)
        # self.admin.show_right_answer(qid, rightAns, answer)
        if int(rightAns) != int(answer) and self.rolling_i is None:
            self.roll_the_dice()
            pass
    
    def roll_the_dice(self):
        """Show the roll the dice interface and then """
        pf:PlayFrame = PlayFrame.me
        pf.curr_round.dice.show()
        self.rolling_i=self.curr_participant_i
        pass

    def roll(self)->int:
        num:int = self.admin.participants.count()
        indices = list(range(0,num))
        indices.remove(int(self.rolling_i))
        result = random.choice(indices)
        self.target_i = result

        name = self.admin.participants.getNames()[result]
        return name
        pass

    def ask(self):
        pf:PlayFrame = PlayFrame.me
        pf.curr_round.dice.hide()
        self.curr_participant_i = self.target_i
        self.askQ()
    
    def mark_right(self):
        if self.lastQuestionMarked or self.roundEnded:return
        self.lastQuestionMarked=True
        participantID = self.admin.participants.getClientIDs()[self.curr_participant_i]
        self.curr_scores.add(participantID, self.mark)

    def mark_wrong(self):
        if self.lastQuestionMarked or self.roundEnded:return
        self.lastQuestionMarked=True
        participantID = self.admin.participants.getClientIDs()[self.curr_participant_i]
        self.curr_scores.add(participantID, self.minusMark)

    def askNextQ(self):
        if not self.lastQuestionMarked : return
        self.lastQuestionMarked = False

        if self.rolling_i is not None:
            self.curr_participant_i = self.rolling_i
            self.target_i = None
            self.rolling_i=None
            pass
        self.curr_participant_i = (self.curr_participant_i+1)%self.admin.participants.count()
        self.curr_question_i += 1
        if self.curr_question_i >= len(self.questions__):
            self.onend()
            return
        self.askQ()



class Round4(Round):
    name="Speedo Round"
    totalQ = 20
    isBuzzerPressed=False
    first_id = None

    def __init__(self,admin) -> None:
        super().__init__(admin, admin.qBank.round4,mark=10, minusMark=-5, id=4, name=Round4.name)

    
    def check_answer(self, qid, answer):
        self.lastQuestionMarked=True
        rightAns = None
        for question in self.questions__:
            if str(qid) == str(question.qid):
                rightAns=question.answer
        isRight=int(rightAns)==int(answer)
        print(f"CHECKING ANSWER qid:{qid}, ans:{answer}, correct:{rightAns}")
        participantID = self.admin.participants.getClientIDs()[self.curr_participant_i]
        if isRight:
            self.curr_scores.add(participantID, self.mark)
        else:
            self.curr_scores.add(participantID, self.minusMark)

        print(isRight)
        return rightAns
        
    def loadQ(self):
        allQuestions = list(self.admin.qBank.round4)
        
        if len(allQuestions) < self.totalQ:
            raise Exception(f"NUMBER OF QUESTIONs in DB is less than participants : {len(allQuestions)} < {self.totalQ}")
        random.shuffle(allQuestions)
        self.questions__ = tuple(allQuestions[0:self.totalQ])

    def start(self):
        print(f"ROUND-{self.id} started")
        self.loadQ()
        self.admin.server.broadcast(createPayload("setround", self.id))
        self.askQ()
        self.curr_scores=Scores(self.admin.participants.getClientIDs())

    def askQ(self):
        self.first_id=None
        self.isBuzzerPressed=False
        self.clear_users()
        # participantID = self.admin.participants.getClientIDs()[self.currentParticipant]
        question:Question = self.questions__[self.curr_question_i]
        # self.admin.askQ(participantID, question.forParticipant())
        question:ClientQuestion = question.forParticipant()
        # self.admin.ui.f_main.f_live.f_play.curr_round.setQ(question)
        self.admin.server.broadcast(
            createPayload("setquestion", question.jsons())
            )

        pf:PlayFrame = PlayFrame.me
        pf.curr_round.setQ(question)
        # name = self.admin.participants.getNames()[self.currentParticipant]
        pf.setInfo("", f"Question : {self.curr_question_i+1}/{len(self.questions__)}")
        pass

    def askNextQ(self):
        if not self.lastQuestionMarked : return
        self.lastQuestionMarked = False
        # self.currentParticipant = (self.currentParticipant+1)%self.admin.participants.count()
        self.curr_question_i += 1
        if self.curr_question_i >= len(self.questions__):
            self.onend()
            return
        self.askQ()

    def mark_right(self):
        if self.lastQuestionMarked or self.roundEnded :return
        self.lastQuestionMarked=True
        # participantID = self.admin.participants.getClientIDs()[self.currentParticipant]
        participantID = self.first_id
        if not participantID: return
        self.curr_scores.add(participantID, self.mark)

    def mark_wrong(self):
        if self.lastQuestionMarked or self.roundEnded:return
        self.lastQuestionMarked=True
        # participantID = self.admin.participants.getClientIDs()[self.currentParticipant]
        participantID = self.first_id
        if not participantID: return
        self.curr_scores.add(participantID, self.minusMark)

    def check_answer(self, qid, answer):
        rightAns = super().check_answer(qid, answer)
        self.admin.show_right_answer(qid, rightAns, answer)

    def clear_users(self):
        pf:PlayFrame = PlayFrame.me
        pf.curr_round.clearusers()
        pass

    def add_user(self,clientID):
        name = self.admin.participants.get(clientID).name
        pf:PlayFrame = PlayFrame.me
        pf.curr_round.adduser(name)
        pass

    def buzzer_pressed(self, clientID):
        # add client to list
        self.add_user(clientID)
        if self.isBuzzerPressed: return
        self.isBuzzerPressed=True
        self.first_id = clientID
        
        print("ADDING ")