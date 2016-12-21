# coding=utf-8
import sys
import os
from commandHelp import *

# define the version number
version = 1.0
_ch = ""

# version function
def handleVerstionList():
    print "version :", version

# help function
def handleHelpList():
    print('\033[1;32;40m')
    print "------------------------------ help list -----------------------------------------------------------\n"
    print "--help, -h : print help list\n"
    print "--version, -v : print the version information\n"
    print "--all, -a : list all the commands\n"
    print "--group, -g : list all the command groups\n"
    print  "[keywords]: fuzzy search the [keywords] for command and description:\n"
    print "--search, -s [keywords]: precise search for the [keywords] with show all the information\n"
    print  "--hot, -o: list all the hot command \n"
    print "------------------------------ help list -----------------------------------------------------------\n"

# input command error function
def handleErrorCommand():
    print('\033[1;32;40m')
    print  "---------------------------------------------------------------------------\n"
    print "the input command is invalid. \n"
    print  "---------------------------------------------------------------------------\n"
    handleHelpList()

# print all the linux commands
def handleAllCommandsList():
    print('\033[1;32;40m')
    print  "---------------------------------------------------------------------------\n"
    print "all the linux commands: \n"
    print  "---------------------------------------------------------------------------\n"
    _ch.listAllCommands()

#print all the linux command groups
def handleAllCommandGroups():
    print('\033[1;32;40m')
    print  "---------------------------------------------------------------------------\n"
    print "all the linux command groups"
    print  "---------------------------------------------------------------------------\n"
    _ch.listAllGroups()

# fuzzy search for the linux command
def handleFuzzySearch(c):
    print('\033[1;32;40m')
    print  "---------------------------------------------------------------------------\n"
    print "search result for  ", c , ":\n"
    print  "---------------------------------------------------------------------------\n"
    _ch.listFuzzySearch(c)

# precise search for the linux command
def handlePreciseSearch(c):
    print('\033[1;32;40m')
    print  "---------------------------------------------------------------------------\n"
    print "search result for  ", c , ":\n"
    print  "---------------------------------------------------------------------------\n"
    _ch.listPreciseSearch(c)

# list all the linux hot command
def handleHotCommand():
    print('\033[1;32;40m')
    print  "---------------------------------------------------------------------------\n"
    print " hot linux commands: \n"
    print  "---------------------------------------------------------------------------\n"
    _ch.listHotCommand()

# parsing command function
def parseCommand(commad):
    if commad[1].startswith('--'):
        option = commad[1][2:]
        if option == 'version':
            handleVerstionList()
        elif option == 'help':
            handleHelpList()
        elif option == 'all':
            handleAllCommandsList()
        elif option == "group":
            handleAllCommandGroups()
        elif option == "hot":
            handleHotCommand()
        elif option == "search":
            handlePreciseSearch(commad[2])
        else:
            handleErrorCommand()
    elif commad[1].startswith('-'):
        option = commad[1][1:]
        if option == 'v':
            handleVerstionList()
        elif option == 'h':
            handleHelpList()
        elif option ==  'a':
            handleAllCommandsList()
        elif option == "g":
            handleAllCommandGroups()
        elif option == "o":
            handleHotCommand()
        elif option == "s":
            handlePreciseSearch(commad[2])
        else:
            handleErrorCommand()
    else:
        # do the search
        handleFuzzySearch(commad[1])


def main(argv):
    if len(argv) <= 1:
        handleHelpList()
    else:
        parseCommand(argv)

if __name__=='__main__':
    print "\nwelcome to linux command helper, more at:( http://man.linuxde.net/)"
    ch = commandHelp("./linux_command.csv", "./linux_command_detail.csv")
    if ch.importData() == -1:
        sys.exit(-1)
    if ch.importSampleData() == -1:
        sys.exit(-1)
    else:
        _ch = ch
    main(sys.argv)
