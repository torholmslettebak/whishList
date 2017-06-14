import glob, os, sys, json
os.chdir(".")

class Whish(object):
    def __init__(self, name):
        self.name = name
        # self.number = number
        self.price = None

    def addPrice(self, price):
        self.price = price


class WhishList(object):
    def __init__(self, name):
        self.name = name
        self.whishlist = []

    def addWhish(self, object, number):
        print(object.price)
        self.whishlist.insert(int(number) -1,object)

def jsonDefault(object):
    return object.__dict__


def getWhishAndInsert(listObject):
    # This function asks user for input, and makes an object which is inserted into the WhishList-object
    print('Hello mate, what\'s your whish?')
    name = input('Insert the name of what you want: ')
    number = input('Insert the priority of your whish, 1-10: ')
    price_temp = input('The price of your thingy? --> ')
    try:
        int(price_temp)
        price = price_temp
    except ValueError:
        price = None

    whish = Whish(name)
    whish.addPrice(price)
    listObject.addWhish(whish, number)

def interpret(opt, listObject):
    switcher = {
        0: exitProgram,
        1: view,
        2: getWhishAndInsert
    }
    func = switcher.get(opt, lambda: "Nothing")
    return func(listObject)

def printOptions():
    print('To exit the program press 0: \n To view the whishList press 1: \n To add a whish to the whishList press 2: ')

def exitProgram(listobject):
    print('Goodbye!')
    test = json.dumps(listobject, default=jsonDefault)
    textFile = open('whishList.json','w')
    textFile.write(test)
    sys.exit()

def view(whishList):
    counter = 1
    for whish in whishList.whishlist:
        print('#', counter, ' ', whish.name)
        counter = counter + 1

def readJsonFromFile():
    # Reading data back
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data

def main():
    # Controls program flow
    whishList = WhishList('My whishList')
    running = True
    while running:
        printOptions()
        opt = input('--> ' )
        interpret(int(opt), whishList)

main()
