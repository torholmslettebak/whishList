import glob, os, sys
os.chdir(".")


def initWhishList(textFile):
    print('Welcome to your whish list')
    # Check if there exist a txt for storing the whish list.
    print('The length of the list of files containing .txt ', len(glob.glob("*.txt")))
    if len(glob.glob("*.txt")) > 0:
        list = glob.glob("*.txt")
        fileName=list[0]
        print('The folder has a whishList: ', list[0])
        textFile = open(fileName, 'r+')
        whishList = readFileToList(textFile)
    else:
        # Make a txt file
        fileName = 'whishList.txt'
        textFile = open(fileName, 'w')
        print('Created whish list text file')
        whishList = []

    return textFile, whishList

def insertTextInRow(fileHandle, whishList):
    # Inserts a text string into desired row/position in text file
    print('The current whishList holds the following: ')
    view(fileHandle, whishList)
    correctInput = False
    while correctInput==False:
        lineNumber = input('Insert line number: ')
        if stringIsNumber(lineNumber):
            lineNumber = int(lineNumber)
            correctInput = True
        else:
            print('Input is not a number')

    whish = input('Whish: ')
    whishList.insert(int(lineNumber)-1, whish+'\n')
    print(whishList)
    return whishList

def stringIsNumber(text):
    try:
        int(text)
        return True
    except ValueError:
        return False

def readFileToList(textFile):
    whishList = textFile.readlines()
    print((whishList))
    print(type(whishList) is list)
    input('wait')
    # you may also want to remove whitespace characters like `\n` at the end of each line
    # whishList = [x.strip('\n') for x in whishList]
    return whishList

def writeListToFile(whishList, fileHandle):
    fileHandle.writelines(whishList)

def deleteRow(position, file):
    # Deletes and reorganizes rows.
    pass
def reorganize(file):
    # If this isn't automatically done by the text file.
    pass
# def view(file):
#     # Build a reasonable data structure for showing the whish list
#     pass

def printOptions():
    options = ['0: To exit the program press Q/q or 0', '1: To view the whish list press: 1', '2: To Add a whish press 2', '3: To delete all text in file, press: 3']
    print(options)

def exitProgram(fileHandle, whishList):
    print('Goodbye!')
    fileHandle.truncate(0) # Truncates file size as far as possible towards 0
    writeListToFile(whishList, fileHandle)
    fileHandle.close()
    sys.exit()

def view(fileHandle, whishList):
    # Print the whishList, method reads a python list of whishes and prints them in wanted
    # for whish in whishList:
    #     print(whish)
    count = 1
    print(whishList)
    for whish in whishList:
        print('#' + str(count) + ' ' + whish)
        count = count + 1

def clearTextFile(fileHandle, whishList):
    fileHandle.truncate(0)

def interpret(opt, fileHandle, whishList):
    switcher = {
        0: exitProgram,
        1: view,
        2: insertTextInRow,
        3: clearTextFile
    }
    print('option = ', opt)
    func = switcher.get(opt, lambda: "Nothing")
    return func(fileHandle, whishList)

def main():
    # Controls program flow
    fileHandle = None
    whishList = None
    fileHandle, whishList = initWhishList(fileHandle)
    # print('Filehandle is: ', fileHandle)
    running = True
    while running:
        printOptions()
        opt = input('--> ' )
        interpret(int(opt), fileHandle, whishList)




main()
