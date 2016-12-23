# coding=utf-8

class command:
    name = ""
    description = ""
    group = ""
    keyword = ""
    isHot = ""
    usage = ""

    def __init__(self, n="", d="", g="", k="", h="", u=""):
        self.name = n
        self.description = d
        self.group = g
        self.keyword = k
        self.isHot = h
        self.usage = u
    def getName(self):
        return self.name

    def setName(self, n):
        if n != "":
            self.name = n
        return self.getName()

    def getDescription(self):
        return self.description

    def setDescription(self, d):
        if d != "":
            self.description = d
        return self.getDescription()

    def getGroup(self):
        return self.group

    def setGroup(self, g):
        if g != "":
            self.group = g
        return self.getGroup()

    def getKeyword(self):
        return self.keyword

    def setKeyword(self, k):
        if k != "":
            self.keyword = k
        return self.getKeyword()

    def getIsHot(self):
        return self.isHot

    def setIsHot(self, h):
        if h != "":
            self.isHot = h
        return self.getIsHot()

    def getUsage(self):
        return self.usage

    def setUsage(self, u):
        if u != "":
            self.usage = u
        return self.getUsage()