from .util import connect, cls, askMCQ, prompt
from ..lib.sockets import ClientSocket
from .settings import addr
import sys
import json

class Client():
    name=None

    def __init__(self) -> None:
        self.client = ClientSocket(addr)
        self.client.attach(print)

    def sendName(self):
        payload = {
            "action":"setname",
            "data":self.name,
        }
        self.client.send(bytes(json.dumps(payload), encoding="utf-8"))

    def quiz(self):
        ans = askMCQ(f"\tQUIZ APP ({self.name})\n\nWAITING FOR ADMIN TO START QUIZ", ["REFRESH", "EXIT"])
        if ans == 1:
            sys.exit()
        self.quiz()

    def start(self):
        ans = askMCQ(title="\tQUIZ APP", options=("Start QUIZ", "EXIT"))

        if ans == 0:
            cls()
            self.name = input("\tQUIZ APP\n\nNAME : ")
            self.client.connect()
            # self.client.on("handshake-done", self.quiz)
            while self.client.handshakeStage != 3:
                pass
            data = json.dumps({"action":"setname", "data":self.name})
            self.client.send(bytes(data, encoding="utf-8"))
            self.quiz()
            pass
        elif ans ==1:
            sys.exit(1)

def main():
    client = Client()
    client.start()

if __name__ == "__main__":
    main()