# coding=utf-8

class sampleCommand:
    sample = ""
    description = ""
    keyword = ""

    def __init__(self, k="", s="", d=""):
        self.sample = s
        self.description = d
        self.keyword = k

    def getSample(self):
        return self.sample

    def setSample(self, s):
        if s != "":
            self.sample = s
        return self.getSample()

    def getDescription(self):
        return self.description

    def setDescription(self, d):
        if d != "":
            self.description = d
        return self.getDescription()

    def getKeyword(self):
        return self.keyword

    def setKeyword(self, k):
        if k != "":
            self.keyword = k
        return self.getKeyword()