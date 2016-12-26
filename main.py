# coding=utf-8
import sys
from constant import  *
import platform
from commandHelp import *

# define the version number
version = 1.0
_ch = ""

# version function
def handleVerstionList():
    print "version :", version

# help function
def handleHelpList():
    print(COLOR_GREEN)
    print "------------------------------ help list -----------------------------------------------------------\n"
    print "--help, -h : print help list\n"
    print "--version, -v : print the version information\n"
    print "--all, -a : list all the commands\n"
    print "--list, -l : list all the sample commands\n"
    print "--group, -g : list all the command groups\n"
    print  "[keywords]: fuzzy search the [keywords] for command and description:\n"
    print "--search, -s [keywords]: precise search for the [keywords] with show all the information\n"
    print  "--hot, -o: list all the hot command \n"
    print "--edit, -e: edit or update the resource for the command"
    print "------------------------------ help list -----------------------------------------------------------\n"


# input command error function
def handleErrorCommand():
    print(COLOR_GREEN)
    print  "---------------------------------------------------------------------------\n"
    print "the input command is invalid. \n"
    print  "---------------------------------------------------------------------------\n"
    handleHelpList()

# print all the linux commands
def handleAllCommandsList():
    print(COLOR_GREEN)
    print  "---------------------------------------------------------------------------\n"
    print "all the linux commands: \n"
    print  "---------------------------------------------------------------------------\n"
    _ch.listAllCommands()

#print all the linux command groups
def handleAllCommandGroups():
    print(COLOR_GREEN)
    print  "---------------------------------------------------------------------------\n"
    print "all the linux command groups"
    print  "---------------------------------------------------------------------------\n"
    _ch.listAllGroups()

# fuzzy search for the linux command
def handleFuzzySearch(c):
    print(COLOR_GREEN)
    print  "---------------------------------------------------------------------------\n"
    print "search result for  ", c , ":\n"
    print  "---------------------------------------------------------------------------\n"
    _ch.listFuzzySearch(c)

# precise search for the linux command
def handlePreciseSearch(c):
    print(COLOR_GREEN)
    print  "---------------------------------------------------------------------------\n"
    print "search result for  ", c , ":\n"
    print  "---------------------------------------------------------------------------\n"
    _ch.listPreciseSearch(c)

# list all the linux hot command
def handleHotCommand():
    print(COLOR_GREEN)
    print  "---------------------------------------------------------------------------\n"
    print " hot linux commands: \n"
    print  "---------------------------------------------------------------------------\n"
    _ch.listHotCommand()

#list all the sample linux command
def handleListSampleCommand():
    print(COLOR_GREEN)
    print  "---------------------------------------------------------------------------\n"
    print " all sample linux commands: \n"
    print  "---------------------------------------------------------------------------\n"
    _ch.listSampleCommand()

def handleUpdateCommandResource(c):
    print(COLOR_GREEN)
    print  "---------------------------------------------------------------------------\n"
    print " update linux commands: \n"
    print  "---------------------------------------------------------------------------\n"
    _ch.updateCommandResource(c)

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
        elif option == "list":
            handleListSampleCommand()
        elif option == "edit":
            if len(sys.argv) >=3:
                cmd = command[2]
            else:
                cmd = ""
            handleUpdateCommandResource(cmd)
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
        elif option == "l":
            handleListSampleCommand()
        elif option == "e":
            if len(sys.argv) >=3:
                cmd = command[2]
            else:
                cmd = ""
            handleUpdateCommandResource(cmd)
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
    # get current python exe path
    path = sys.argv[0]
    lastSplash = path.rindex('/')
    path = path[0: lastSplash]

    ch = commandHelp(path+"/linux_command.csv", path+"/linux_command_detail.csv")
    if ch.importData() == -1:
        sys.exit(-1)
    if ch.importSampleData() == -1:
        sys.exit(-1)
    else:
        _ch = ch
    main(sys.argv)
    print COLOR_WHITE
