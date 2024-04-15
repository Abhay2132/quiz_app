class P():

    a=1

    def __init__(self, a) -> None:
        self.a=a
    
    def ca(self):
        self.a = 22

class C(P):
    
    def __init__(self, a) -> None:
        super().__init__(a)

c=C(1)
c.ca()

print(c.a)