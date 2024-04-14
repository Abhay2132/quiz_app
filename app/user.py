from .ui.user.main import App
from .lib.sockets import ClientSocket
from .settings import addr

class User():
    app:App = None
    client:ClientSocket = None

    def __init__(self) -> None:
        self.app = App()
        self.client = ClientSocket(addr=addr)

    def start(self):
        self.app.show()

def main():
    user = User()
    user.start()
    pass

if __name__ == "__main__":
    main()