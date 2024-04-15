import csv
import json
import random
import os

class QuestionBank():
    qdir=None
    round1:tuple=tuple()
    round2:tuple=tuple()
    round3:tuple=tuple()
    round4:tuple=tuple()

    def __init__(self, qdir:str) -> None:
        self.qdir = qdir
        if not os.path.exists(self.qdir):
            os.makedirs(self.qdir, exist_ok=True)
        self.load()
        pass

    def loadQfromCSV(self, csvPath):
        with open(csvPath,"r") as f:
            reader = csv.reader(f)
            allQuestions = list() # list of class Quetion

            for i,row in enumerate(reader):
                if i ==0 : continue # skip header row
                allQuestions.append(Question(*row))
                pass
            # random.shuffle(allQuestions)
            return tuple(allQuestions)

    def load(self):
        if not os.path.exists(self.qdir):
            raise OSError(f"question directory {self.qdir} does not exists")
        
        # files = filter(lambda _ : _[-4:]==".csv", os.listdir(self.qdir))
        files = tuple(map(lambda _ : os.path.join(self.qdir, _), ("r1.csv", "r2.csv", "r3.csv", "r4.csv")))

        if os.path.exists(files[0]):
            self.round1 = self.loadQfromCSV(files[0])
        if os.path.exists(files[1]):
            self.round2 = self.loadQfromCSV(files[1])
        if os.path.exists(files[2]):
            self.round3 = self.loadQfromCSV(files[2])
        if os.path.exists(files[3]):
            self.round4 = self.loadQfromCSV(files[3])

        print("round1:",len(self.round1))
        print("round2:",len(self.round2))
        print("round3:",len(self.round3))
        print("round4:",len(self.round4))

class Question():
    """Data class for Question"""
    qid:str=None
    imgPath:str=None
    text:str=None
    options:str = None
    answer:int=None

    def __init__(self, qid, text, options, answer, imgPath, *args) -> None:
        self.qid = qid
        self.text = text
        self.options = options
        self.answer = answer
        self.imgPth = imgPath
    
    def forParticipant(self):
        # data = {
        #     "qid":self.qid,
        #     "text":self.text,
        #     "options":self.options,
        #     "imgPath":self.imgPath
        # }

        return ClientQuestion(self.qid, self.text, self.options, self.imgPath)
    
class ClientQuestion():
    def __init__(self, qid, text, options, imgPath) -> None:
        self.qid = qid
        self.text = text
        self.options = options
        self.imgPath = imgPath

    def jsons(self):
        return json.dumps({
            "qid":self.qid,
            "text":self.text,
            "options":self.options,
            "imgPath":self.imgPath
        })
    
    def loads(self, s):
        data = json.loads(s)
        self.qid=data.get("qid")
        self.text=data.get("text")
        self.options=str(data.get("qid")or"").split(",")
        self.imgPath=data.get("imgPath")
        return self