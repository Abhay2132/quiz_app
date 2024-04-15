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
        self.admin.show_right_answer(qid, answer, rightAns)
    
class Round3(Round):
    name="Roll the Dice"
    def __init__(self,admin) -> None:
        super().__init__(admin, admin.qBank.round3,mark=10, minusMark=-5, id=3, name=Round3.name)

class Round4(Round):
    name="Speedo Round"
    def __init__(self,admin) -> None:
        super().__init__(admin, admin.qBank.round4,mark=10, minusMark=-5, id=4, name=Round4.name)

