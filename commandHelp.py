# coding=utf-8
import csv
import os
from command import *
from sampleCommand import *
from constant import *


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
                print COLOR_RED, "parsing command resource file failed\n"
                return -1
            else:
                return 0
        else:
            print COLOR_RED, "invalid linux command resource file path : ", self.commandFilePath, "\n"
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
                print COLOR_RED, "parsing sample command resource file failed\n"
                return -1
            else:
                return 0
        else:
            print COLOR_RED, "invalid linux sample command resource file path : ", self.sampleFilePath, "\n"
            return -1


    def listAllCommands(self):
        print(COLOR_WHITE)
        if len(self.commandArray) >0 :
            for line in self.commandArray:
                print line.getName(), " : ", line.getDescription(), "\t"

    def listAllGroups(self):
        print(COLOR_WHITE)
        groups = []
        if len(self.commandArray) > 0:
            for line in self.commandArray:
                if groups.__contains__(line.getGroup()):
                    continue
                else:
                    groups.append(line.getGroup())
                    print line.getGroup(), "\t"

# list the sample command for the search k
# and handle for quick using
    def listSampleSearch(self, k):
        # print the sample command usage for the command k
        if len(self.sampleCommandArray) > 0:
            index = 0
            sampleList = []
            for line in self.sampleCommandArray:
                if k == line.getKeyword():
                    index += 1
                    sampleList.append(line.getSample())
                    print COLOR_YELLOW, index, ":", COLOR_RED, line.getSample(), COLOR_YELLOW, line.getDescription(), "\t"
        while(1):
            print COLOR_WHITE
            inputStr = raw_input("please input the index to run the sample command:(q to quit)")
            if inputStr == 'q':
                break
            inputInt = int(inputStr)
            if inputInt <= index and inputInt >= 1:
                print COLOR_YELLOW, "run command:", COLOR_RED, sampleList[inputInt - 1], COLOR_WHITE
                print "\n============================================================================="
                os.system(sampleList[inputInt - 1])
                print "\n============================================================================="
            else:
                break



#precise search for the keyword in the commandArray
    def listPreciseSearch(self, k):
        print(COLOR_WHITE)
        # print the basic information for the command k
        if len(self.commandArray) >0 :
            for line in self.commandArray:
                if k == line.getName():
                    print COLOR_WHITE, "Name : ", COLOR_YELLOW, line.getName(), "\t"
                    print COLOR_WHITE, "Description : ", COLOR_YELLOW, line.getDescription(), "\t"
                    print  COLOR_WHITE, "Group : ", COLOR_YELLOW, line.getGroup(), "\t"
                    print COLOR_WHITE, "Keywords : ", COLOR_YELLOW, line.getKeyword(), "\t"
                    print  COLOR_WHITE, "Hot : ", COLOR_YELLOW, line.getIsHot(), "\t"
                    print COLOR_WHITE, "Usage : ", COLOR_YELLOW, line.getUsage(), "\t\n"
                    break
        # handle for the sample command search
        self.listSampleSearch(k)

# fuzzy search the keyword in the commandArray
    def listFuzzySearch(self, k):
        index = 0
        commandList = []
        if len(self.commandArray) >0 :
            for line in self.commandArray:
                if line.getName().find(k) >= 0:
                    index += 1
                    commandList.append(line.getName())
                    print COLOR_YELLOW, index, ":", COLOR_WHITE, line.getName(), " : ", COLOR_YELLOW, line.getDescription(), "\t"
                elif line.getDescription().find(k) >=  0:
                    index += 1
                    commandList.append(line.getName())
                    print COLOR_YELLOW, index, ":", COLOR_WHITE, line.getName(), " : ", COLOR_YELLOW, line.getDescription(), "\t"
            if index:
                while (1):
                    print COLOR_WHITE
                    inputStr = raw_input("please input the index to show the command detail information:(q to quit)")
                    if inputStr == 'q':
                        break
                    inputInt = int(inputStr)
                    if inputInt <= index and inputInt >= 1:
                        self.listPreciseSearch(commandList[inputInt-1])
                        break
                    else:
                        break
    def listHotCommand(self):
        print(COLOR_WHITE)
        if len(self.commandArray) >0 :
            for line in self.commandArray:
                if line.getIsHot():
                    print line.getName()