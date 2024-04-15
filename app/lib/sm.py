

class Scores():
    """Score Mangaer Class"""
    
    __scores= dict()

    def __init__(self, IDs) -> None:
        for id in IDs:
            self.__scores[id] = 0
        pass

    def get(self, id):
        return self.__scores.get(id)
    
    def set(self, id, val):
        self.__scores[id] = val
    
    def add(self, id, val):
        self.__scores[id] += val

    def addUser(self, id, score=0):
        self.__scores[id] = score

    def getUserIDs(self):
        return tuple(self.__scores.keys())
    pass
