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
        self.sample = s
    def getDescription(self):
        return self.description
    def setDescription(self, d):
        self.description = d
    def getKeyword(self):
        return self.keyword
    def setKeyword(self, k):
        self.keyword = k
