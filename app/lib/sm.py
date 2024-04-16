import json

class SCORE():
    scores=dict()

class Scores(SCORE):
    """Score Mangaer Class"""
    scores:dict= dict() # client ID -> SCORE

    def __init__(self, IDs, minScore=0) -> None:
        self.scores = dict()
        for id in IDs:
            self.scores[id] = 0
        self.minScore=minScore

    def get(self, id):
        return self.scores.get(id)
    
    def set(self, id, val):
        if val < self.minScore:
            val = self.minScore
        self.scores[id] = val
    
    def add(self, id, val):
        self.scores[id] += val
        if self.scores[id] < self.minScore:
            self.scores[id] = self.minScore
        # if 

    def addUser(self, id, score=0):
        self.scores[id] = score

    def getUserIDs(self):
        return tuple(self.scores.keys())
    
    def toString(self):
        return json.dumps(self.scores)
        pass

    def addScore(self, curr_score:SCORE):
        for clientID in curr_score.scores:
            self.add(clientID, curr_score.get(clientID))
        # for clientID 
        pass
    
    def reset(self):
        for id in self.scores:
            self.scores[id] = 0
    pass
