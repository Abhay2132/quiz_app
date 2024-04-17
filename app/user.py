from .ui.user.main import App
from .lib.sockets import ClientSocket
from .settings import addr
from .lib.struct import USER
from .lib.util import createPayload, rand_str
import json
from .lib.qb import ClientQuestion
from ._globals import _GLOBALs
from .settings import addr, getWIFI, port

class User(USER):
    ui:App=None
    connecting=False

    def __init__(self) -> None:
        USER.me=self
        _GLOBALs['user']=self
        self.ui = App()
        USER.me = self

    def login(self):
        if self.connecting: return
        self.connecting = True
        print("doing Login")
        self.client = ClientSocket(addr)
        self.client = ClientSocket(addr=(getWIFI(), port))
        # self.client.on("handshake-done", self.onHandshakeDone)
        self.client.on("handshake-error", self.reconnect)
        self.client.on("disconnected", self.reconnect)
        self.client.on("data", self.handleDataEvent)
        # self.client.attach(print)
        self.client.connect()
        self.uid = rand_str()
        # self

    def submit_answer(self, qid, answer):
        self.client.send(createPayload("checkanswer", {"qid":qid, "answer":answer}))
        pass

    def handleDataEvent(self, args):

        payload = args[0]
        payload = json.loads(payload)

        print(f"PAYLOAD : {payload}")
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
        
    def reconnect(self, *args):
        print("reconnecting after 3 secs")
        self.connecting=False
        self.client.off_all()
        self.client.disconnect()
        self.ui.after(3000, self.login)

    def start(self):
        self.ui.show()

    def onHandshakeDone(self, args):
        self.connecting = False
        print("setting active Frame")
        self.ui.mainpanel.setActiveFrame(self.ui.mainpanel.f_screensaver)
        print("sending name")
        payload = createPayload("setdata", self.name)
        self.client.send(payload)

    def on_buzzer_pressed(self, qid):
        self.client.send(createPayload("buzzer-pressed", ))


def main():
    user = User()
    user.start()
    pass

if __name__ == "__main__":
    main()