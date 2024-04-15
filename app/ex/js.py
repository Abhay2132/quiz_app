import json

class Q():
    def __init__(self) -> None:
        self.a = 1

q = Q()

print(json.dumps(q))