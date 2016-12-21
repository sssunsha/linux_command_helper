# coding=utf-8

class sampleCommand:
    name = ""
    description = ""
    keyword = ""

    def __init__(self, k, n, d):
        self.name = n
        self.description = d
        self.keyword = k

    def getName(self):
        return self.name
    def setName(self, n):
        self.name = n
    def getDescription(self):
        return self.description
    def setDescription(self, d):
        self.description = d
    def getKeyword(self):
        return self.keyword
    def setKeyword(self, k):
        self.keyword = k
