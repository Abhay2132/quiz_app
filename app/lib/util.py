import shutil
from .sockets import ClientSocket
import json
import os

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
        self.__participants[p.clientID] = p

    def remove(self, clientID:Participant.clientID):
        self.__participants.pop(clientID)
    
    def find(self, clientID:Participant.clientID)->bool:
        return clientID in self.__participants
    
    def get(self, clientID:Participant.clientID)->Participant:
        if self.find(clientID):
            return self.__participants[clientID]
    
    def at(self, index:int):
        return self.__participants.get(self.getClientIDs()[index])

    def count(self):
        return len(self.__participants.keys())
    
    def getClientIDs(self):
        return tuple(self.__participants.keys())
    
    def getNames(self):
        names = [self.__participants[i].name for i in self.__participants]
        return names

def createPayload(action:str, data:dict|str=None)->bytes:
    return bytes(json.dumps({"action":action, "data":data}), encoding="utf-8")


class Obj(dict):
    def set(self, **kwargs):
        for key in kwargs:
            # self.__data[key] = kwargs[key]
            super().__setitem__(key, kwargs[key])
        return self
    
    def copy(self):
        return Obj(**self)
    

class UI:
    parent=None
    def show(self):
        pass

def copy_file(source_path, destination_path, new_name):
  """Copies a file from source to destination with a new name.

  Args:
      source_path (str): The path to the original file.
      destination_path (str): The path to the destination directory.
      new_name (str): The desired name for the copied file.
  """

  try:
    # Construct the full destination path with the new name
    # full_destination_path = f"{destination_path}/{new_name}"
    full_destination_path = os.path.join(destination_path, new_name)

    # Use shutil.copy2 to preserve file metadata (e.g., creation time)
    shutil.copy2(source_path, full_destination_path)
    print(f"File copied successfully: {source_path} -> {full_destination_path}")

  except Exception as e:
    print(f"Error copying file: {e}")