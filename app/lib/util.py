from .sockets import ClientSocket
import json

class Participant():
    name=None
    client=None
    clientID=None
    def __init__(self, client:ClientSocket, clientID, name:str="") -> None:
        self.client=client
        self.clientID=clientID
        self.name = name

class Participants():
    __participants = dict()

    def add(self, p:Participant):
        id = p.clientID
        self.__participants[p.clientID] = p

    def remove(self, clientID:Participant.clientID):
        self.__participants.pop(clientID)
    
    def find(self, clientID:Participant.clientID)->bool:
        return clientID in self.__participants
    
    def get(self, clientID:Participant.clientID)->Participant:
        if self.find(clientID):
            return self.__participants[clientID]
    
    def count(self):
        return len(self.__participants.keys())
    
    def getClientIDs(self):
        return tuple(self.__participants.keys())
    
    def getNames(self):
        names = [self.__participants[i].name for i in self.__participants]
        return names

def createPayload(action:str, data)->bytes:
    return bytes(json.dumps({"action":action, "data":data}), encoding="utf-8")