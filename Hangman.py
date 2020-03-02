''' Initialize global variables'''
word = ""
letter = ""
updatedSpaces = []

def intialize():
    ''' List = ["Dog","Cat","Tree"]
    random.choice(
    '''
    print("print word")
    

def getLetter():
    '''Out letter from user'''
    global letter
    
def checkLetter():
    '''tests if letter in secret, 
    if True updates undatedSpaces displays 
        updatedSoaces, calls checkIfWon
    if False displays updatedSpaces, updates lives, calls 
        getLetter
    '''
    global updatedSpaces
    
def checkIfWon():
    '''outputs a message if won or 
        calls getLetter if not'''
    print()

def main():
    '''Starts the program'''
    intialize()
    getLetter()
    checkLetter()

main()

def checkLetter():
    global updatedSpaces
    if letter in word:
        checkifWon()
        updatedSpaces = updatedSpaces -1
    
    else:
        lives = lives -1
        getLetter()
