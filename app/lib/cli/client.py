from .util import connect, cls, askMCQ, prompt
from ..sockets import ClientSocket
from .settings import addr
import sys

class Client():
    def __init__(self) -> None:
        self.client = ClientSocket(addr)
        self.client.attach(print)

    def quiz(self):
        ans = askMCQ("\tQUIZ APP\n\nWAITING FOR ADMIN TO START QUIZ", ["REFRESH", "EXIT"])
        if ans == 1:
            sys.exit()
        self.quiz()

    def start(self):
        ans = askMCQ(title="\tQUIZ APP", options=("Start QUIZ", "EXIT"))

        if ans == 0:
            cls()
            name = input("\tQUIZ APP\n\nNAME : ")
            self.client.connect()
            self.quiz()
            pass
        elif ans ==1:
            sys.exit(1)

def main():
    client = Client()
    client.start()

if __name__ == "__main__":
    main()