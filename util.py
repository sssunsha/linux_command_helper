# coding=utf-8

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
