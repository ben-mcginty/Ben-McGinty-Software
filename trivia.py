import linecache
validModeInput = False

def blankLine():
    print("")
    return

def mathQuiz(score):
    return

#generated math quiz
def generatedQuestions(score):
    return

#trivia quiz
def triviaQuiz(score):
    lineAccessNumber = 1
    setNumber = input("What set would you like to do? 1 or 2? ")
    lineAccessNumber = lineAccessNumber * 10 + 1
    for x in range(0, 5):
        questionResponse = str(input(linecache.getline('triviaQuestions.txt',lineAccessNumber)))
        lineAccessNumber += 1
        questionQueryAnswer = str(linecache.getline('triviaQuestions.txt',lineAccessNumber))
        if questionQueryAnswer != questionResponse:
            print("Congratulations! Correct")
            lineAccessNumber += 1
            score += 1
            blankLine()
        else:
            print("Oh no! That is not the correct answer")
            lineAccessNumber += 1
            blankLine()
    print("You scored a score of ", score, " out of 5.")
    return

#generates numbers between user enterd numbers
def numberGeneration(minNum, maxNum):
    return

#selects mode
print("Hello! Welcome to trivia and math quiz! What would you like to do?")
print("1, Trivia")
print("2, Set math questions")
print("3, Generated math questions")
blankLine()

mode = input("")
if mode == str(1):
    validModeInput = True
    blankLine()
    triviaQuiz(score = 0)
elif mode == str(2):
    validModeInput = True
    blankLine()
    mathQuiz(score = 0)
elif mode == str(3):
    blankLine()
    validModeInput = True
    generatedQuestions(score = 0)
else:
    print("We apologise, that dosn't seem to be a valid input.")
    blankLine()
