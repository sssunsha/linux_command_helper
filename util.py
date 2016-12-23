# coding=utf-8
from constant import *

def inputValidationCheck(index, inputInt):
    if inputInt <= index and inputInt >= 1:
        return 1
    else:
        return 0

def checkQuit(inputStr):
    if inputStr == 'q':
        return 1
    else:
        return 0

def updateCommandNameInput():
    commandStr = raw_input("(return to skip) Name: ")
    return commandStr
def updateCommandDescriptionInput():
    desStr = raw_input("(return to skip) Description: ")
    return desStr
def updateCommandGroupInput():
    groupStr = raw_input("(return to skip) Group: ")
    return groupStr
def updateCommandKeywordsInput():
    keyStr = raw_input("(return to skip) Keywords: ")
    return keyStr
def updateCommandHotInput():
    isHotStr = raw_input("(return to skip) isHot: ")
    return isHotStr
def updateCommandUsageInput():
    usageStr = raw_input("(return to skip) Usage: ")
    return usageStr

def confirmChange4Command(n, d, g, k, h, u):
    print COLOR_GREEN
    print "Updated command:"
    print COLOR_WHITE, "Name : ", COLOR_YELLOW, n
    print COLOR_WHITE, "Description : ", COLOR_YELLOW, d
    print COLOR_WHITE, "Group : ", COLOR_YELLOW, g
    print COLOR_WHITE, "keywords : ", COLOR_YELLOW, k
    print COLOR_WHITE, "Hot : ", COLOR_YELLOW, h
    print COLOR_WHITE, "Usage : ", COLOR_YELLOW, u
    print COLOR_WHITE
    result = raw_input("confirm the change? y=yes, n=no, q=quit:  ")
    if result == 'y':
        return 1
    elif result == 'n':
        return 0
    else:
        return -1