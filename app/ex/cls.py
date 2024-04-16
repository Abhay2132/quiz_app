class P():
    def a(self):
        print(self.b)

class C(P):
    def __init__(self) -> None:
        super().__init__()
        self.b=12

    def c(self):
        self.a()
    pass

c=C()

c.c()