
from .lib.struct import ADMIN
from .lib.sockets import ClientSocket, ServerSocket, EventEmitter
from .ui.admin.main import App
from .settings import addr
from .lib.util import Participant

class Admin(ADMIN):

    def __init__(self, ) -> None:
        super().__init__()
        ADMIN.me = self
        self.ui=App()
        self.server = ServerSocket(addr=addr)
        self.server.on("new-connection", self.addParticipant)

    def addParticipant(self, args):
        clientID = args[0]
        client = self.server.clients[clientID]
        participant = Participant(client=client, clientID=clientID)
        self.participants.add(participant)
    
    def start(self):
        self.server.start()
        self.ui.show()


def main():
    admin = Admin()
    admin.start()
    pass

if __name__=="__main__":
    main()