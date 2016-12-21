# coding=utf-8
import csv
from command import *
from sampleCommand import *


class commandHelp:

    # linux command resource csv file path
    commandFilePath = ""
    # linux command sample resource json file path
    sampleFilePath = ""
    # linux command array
    commandArray = []
    # linux sample command json object
    sampleCommandArray = []

    # init method
    def __init__(self, commandFilePath, sampleFilePath):
        self.commandFilePath = commandFilePath
        self.sampleFilePath = sampleFilePath

    def setCommandArray(self, array):
        self.commandArray = array

    def setSampleCommandArray(self, array):
        self.sampleCommandArray = array

    # import csv command resource file
    def importData(self):
        if self.commandFilePath != "":
            csvReader = csv.reader(file(self.commandFilePath, 'r'))
            index = 0
            ca = []
            for line in csvReader:
                if index > 0:
                    c = command(line[0], line[1], line[2], line[3], line[4], line[5])
                    ca.append(c)
                index+=1
            self.setCommandArray(ca)
            if len(self.commandArray) == 0:
                print "parsing command resource file failed\n"
                return -1
            else:
                return 0
        else:
            print "invalid linux command resource file path : ", self.commandFilePath, "\n"
            return -1

    def importSampleData(self):
        if self.sampleFilePath != "":
            csvReader = csv.reader(file(self.sampleFilePath, 'r'))
            index = 0
            ca = []
            for line in csvReader:
                if index > 0:
                    c = sampleCommand(line[0], line[1], line[2])
                    ca.append(c)
                index += 1
            self.setSampleCommandArray(ca)
            if len(self.sampleCommandArray) == 0:
                print "parsing sample command resource file failed\n"
                return -1
            else:
                return 0
        else:
            print "invalid linux sample command resource file path : ", self.sampleFilePath, "\n"
            return -1


    def listAllCommands(self):
        if len(self.commandArray) >0 :
            for line in self.commandArray:
                print line.getName(), " : ", line.getDescription(), "\t"

    def listAllGroups(self):
        groups = []
        if len(self.commandArray) > 0:
            for line in self.commandArray:
                if groups.__contains__(line.getGroup()):
                    continue
                else:
                    groups.append(line.getGroup())
                    print line.getGroup(), "\t"

#precise search for the keyword in the commandArray
    def listPreciseSearch(self, k):
        # print the basic information for the command k
        if len(self.commandArray) >0 :
            for line in self.commandArray:
                if k == line.getName():
                    print "Name : ", line.getName(), "\t"
                    print "Description : ", line.getDescription(), "\t"
                    print  "Group : ", line.getGroup(), "\t"
                    print "Keywords : ", line.getKeyword(), "\t"
                    print  "Hot : ", line.getIsHot(), "\t"
                    print "Usage : ", line.getUsage(), "\t"
                    break

# fuzzy search the keyword in the commandArray
    def listFuzzySearch(self, k):
        if len(self.commandArray) >0 :
            for line in self.commandArray:
                if line.getName().find(k) >= 0:
                    print line.getName(), " : ", line.getDescription(), "\t"
                elif line.getDescription().find(k) >=  0:
                    print line.getName(), " : ", line.getDescription(), "\t"

    def listHotCommand(self):
        if len(self.commandArray) >0 :
            for line in self.commandArray:
                if line.getIsHot():
                    print line.getName()