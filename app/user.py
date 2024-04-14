from .ui.user.main import App
from .lib.sockets import ClientSocket
from .settings import addr
from .lib.struct import USER

class User(USER):

    def __init__(self) -> None:
        self.ui = App()
        self.client = ClientSocket(addr=addr)
        self.client.on("handshake-done", lambda args: self.ui.mainpanel.setActiveFrame(self.ui.mainpanel.f_screensaver))
        USER.me = self

    def start(self):
        self.ui.show()

    def onHandshakeDone(self, args):
        print("setting active Frame")
        self.ui.mainpanel.setActiveFrame(self.ui.mainpanel.f_screensaver)


def main():
    user = User()
    user.start()
    pass

if __name__ == "__main__":
    main()