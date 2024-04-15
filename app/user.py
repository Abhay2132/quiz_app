from .ui.user.main import App
from .lib.sockets import ClientSocket
from .settings import addr
from .lib.struct import USER
from .lib.util import createPayload
import json
from .lib.qb import ClientQuestion
from ._globals import _GLOBALs
from .settings import addr, getWIFI, port


class User(USER):
    ui:App=None
    def __init__(self) -> None:
        USER.me=self
        _GLOBALs['user']=self
        self.ui = App()
        # self.client = ClientSocket(addr)
        self.client = ClientSocket(addr=(getWIFI(), port))
        self.client.on("handshake-done", self.onHandshakeDone)
        # self.client.on("disconnected", self.reconnect)
        self.client.on("data", self.handleDataEvent)
        # self.client.attach(print)
        USER.me = self

    def submit_answer(self, qid, answer):
        self.client.send(createPayload("checkanswer", {"qid":qid, "answer":answer}))
        pass

    def handleDataEvent(self, args):
        payload = args[0]
        payload = json.loads(payload)

        action = payload["action"]
        data = payload["data"]

        if action == "setround":
            if int(data) == 1:
                self.ui.mainpanel.setActiveFrame(self.ui.mainpanel.f_round1)
            if int(data) == 2:
                self.ui.mainpanel.setActiveFrame(self.ui.mainpanel.f_round2)
            if int(data) == 3:
                self.ui.mainpanel.setActiveFrame(self.ui.mainpanel.f_round3)
            if int(data) == 4:
                self.ui.mainpanel.setActiveFrame(self.ui.mainpanel.f_round4)
            pass
        if action == "setquestion":
            d = json.loads(data)
            q=ClientQuestion(qid=d["qid"], text=d["text"], options=d["options"], imgPath=d["imgPath"])
            self.ui.mainpanel.activeframe.setQ(q)
            pass
        pass
    def reconnect(self, *args):
        print("reconnecting after 3 secs")
        self.ui.after(3000, lambda *args : self.client.connect())

    def start(self):
        self.ui.show()

    def onHandshakeDone(self, args):
        print("setting active Frame")
        self.ui.mainpanel.setActiveFrame(self.ui.mainpanel.f_screensaver)
        print("sending name")
        payload = createPayload("setname", self.name)
        self.client.send(payload)

def main():
    user = User()
    user.start()
    pass

if __name__ == "__main__":
    main()