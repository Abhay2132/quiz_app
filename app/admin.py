from .lib.sm import Scores
import json
from .lib.qb import QuestionBank
from app.lib.qb import ClientQuestion
from .lib.struct import ADMIN
from .lib.sockets import ClientSocket, ServerSocket, EventEmitter
from .ui.admin.main import App
from .settings import addr
from .lib.util import Participant, createPayload
from .lib.rounds import Round1, Round2, Round3, Round4
import os
from .ui.admin.frames.live import PlayFrame

class Admin(ADMIN):

    def __init__(self, ) -> None:
        super().__init__()
        ADMIN.me = self
        self.ui=App()
        self.qBank = QuestionBank(qdir=os.path.join(os.getcwd(), "data", "questions"))
        self.server = ServerSocket(addr=addr)
        self.server.on("new-connection", self.addParticipant)
        self.server.on("data", self.handleDataEvents)
        self.server.on("disconnected", self.onDisconnect)

        # self.rounds =(
        #     Round1(self), 
        #     Round2(self), 
        #     Round3(self), 
        #     Round4(self)
        # )
        self.currentRound=Round1(self)

    def onDisconnect(self, args):
        clientID=args[0]
        # print("DISCONNECTED : ", args)
        self.participants.remove(clientID)
        pass

    def handleDataEvents(self, args):
        payload = args[0]
        clientID = payload["clientID"]
        data = json.loads(payload["data"])
        action = data["action"]
        data = data["data"]

        if action == "setname":
            self.setName(clientID, data)
        
        if action == "checkanswer":
            self.currentRound.checkAnswer()

    def askQ(self, clientID, question: ClientQuestion):
        # return super().askQ(clientID, question)()
        self.ui.f_main.f_live.f_play.curr_round.setQ(question)
        self.server.sendTo(createPayload("setquestion", question.jsons()), clientID)

    def setName(self,clientID, name):
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
        
        self.quiz_started=True
        self.num_participants = self.participants.count()
        self.currentRound.start()
        self.scores = Scores(self.participants.getClientIDs())
    
        pf:PlayFrame = PlayFrame.me
        pf.setCurrRound(pf.roundUIs[0])
        pass

        # self.roundUIs = (Round1(self.ui.f_main.f_live.f_play.))

def main():
    admin = Admin()
    admin.start()
    pass

if __name__=="__main__":
    main()