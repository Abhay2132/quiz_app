from .lib.sm import Scores
import json
from .lib.qb import QuestionBank
from app.lib.qb import ClientQuestion
from .lib.struct import ADMIN
from .lib.sockets import ClientSocket, ServerSocket, EventEmitter
from .ui.admin.main import App
from .settings import addr, getHOTSPOT, port
from .lib.util import Participant, createPayload
from .lib.rounds import Round1, Round2, Round3, Round4
import os
from .ui.admin.frames.live import PlayFrame, LiveFrame
from ._globals import _GLOBALs

class Admin(ADMIN):
    curr_round_i=0
    min_participants=1
    currentRound = None
    rounds=tuple()
    
    def __init__(self, ) -> None:
        super().__init__()
        _GLOBALs["admin"] = self
        ADMIN.me = self
        self.ui=App()
        self.qBank = QuestionBank(qdir=os.path.join(os.getcwd(), "data", "questions"))
        self.server = ServerSocket(addr=addr)
        # self.server = ServerSocket(addr=(getHOTSPOT(), port))
        self.server.on("new-connection", self.addParticipant)
        self.server.on("data", self.handleDataEvents)
        self.server.on("disconnected", self.onDisconnect)

        self.rounds =(
            Round1(self), 
            Round2(self), 
            Round3(self), 
            Round4(self)
        )
        # self.curr_round_i=0
        # self.curr_round_i=1
        # self.curr_round_i=2
        self.currentRound=self.rounds[self.curr_round_i]

    def onDisconnect(self, args):
        clientID=args[0]
        # print("DISCONNECTED : ", args)
        if self.participants.get(clientID).isPlaying:
            return
        self.participants.remove(clientID)
        pass

    def handleDataEvents(self, args):
        payload = args[0]
        clientID = payload["clientID"]
        data = json.loads(payload["data"])
        action = data["action"]
        data = data["data"]

        if action == "setdata":
            self.setUserData(clientID, data)
        
        if action == "checkanswer":
            qid=data["qid"]
            answer=data["answer"]
            self.currentRound.check_answer(qid, answer)
            self.ui.f_main.f_live.f_play.curr_round.stop_timer()

        if action == "buzzer-pressed" and self.curr_round_i == 3:
            self.currentRound.buzzer_pressed(clientID)
            self.ui.f_main.f_live.f_play.curr_round.stop_timer()

    def askQ(self, clientID, question: ClientQuestion):
        # return super().askQ(clientID, question)()
        self.ui.f_main.f_live.f_play.curr_round.setQ(question)
        self.server.sendTo(createPayload("setquestion", question.jsons()), clientID)

    def setUserData(self,clientID, name, id=None):
        # check if user already exists 
        participant:Participant =  self.participants.get(clientID)
        participant.name = name

    def addParticipant(self, args):
        clientID = args[0]
        client = self.server.clients[clientID]
        participant = Participant(client=client, clientID=clientID)
        self.participants.add(participant)
    
    def start(self):
        self.server.start()
        self.ui.show()

    def askAll(self, question:ClientQuestion):
        pass
        # return super().askAll(question)()

    def start_quiz(self):
        if self.participants.count() < self.min_participants:
            return
        print(f"Participants : {self.participants.count()}")
        self.quiz_started=True
        self.num_participants = self.participants.count()
        self.scores = Scores(self.participants.getClientIDs())

        
        lf:LiveFrame = LiveFrame.me
        lf.setActiveFrame(lf.f_play)
        self.start_curr_round()
        # self.currentRound.start()
        # self.scores = Scores(self.participants.getClientIDs())
    
        # pf:PlayFrame = PlayFrame.me
        # pf.setCurrRound(pf.roundUIs[0])
        pass

    def start_curr_round(self):
        """udpate Frame and send signal"""
        pf:PlayFrame = PlayFrame.me
        pf.setCurrRound(pf.roundUIs[self.curr_round_i])
        self.currentRound.start()
        pass

    def start_next_round(self):
        self.curr_round_i+=1
        self.currentRound = self.rounds[self.curr_round_i]
        # self.currentRound.start()
        self.start_curr_round()
        pass
        # self.roundUIs = (Round1(self.ui.f_main.f_live.f_play.))

    def show_right_answer(self, qid, rightAns, answer):
        pf:PlayFrame = PlayFrame.me
        if pf.curr_round.hasOptions: pf.curr_round.show_answer(rightAns, answer)
        # show_answer(self, correct_i, selected_i):
        pass

def main():
    admin = Admin()
    admin.start()
    pass

if __name__=="__main__":
    main()