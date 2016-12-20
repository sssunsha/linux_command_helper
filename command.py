# coding=utf-8

class command:
    name = ""
    description = ""
    group = ""
    keyword = ""
    isHot = 0
    usage = ""

    def __init__(self, n, d, g, k, h, u):
        self.name = n
        self.description = d
        self.group = g
        self.keyword = k
        self.isHot = h
        self.usage = u
    def getName(self):
        return self.name
    def setName(self, n):
        self.name = n
    def getDescription(self):
        return self.description
    def setDescription(self, d):
        self.description = d
    def getGroup(self):
        return self.group
    def setGroup(self, g):
        self.group = g
    def getKeyword(self):
        return self.keyword
    def setKeyword(self, k):
        self.keyword = k
    def getIsHot(self):
        return self.isHot
    def setIsHot(self, h):
        self.isHot = h
    def getUsage(self):
        return self.usage
    def setUsage(self, u):
        self.usage = u
