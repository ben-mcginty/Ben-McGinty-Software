import random
numStr = random.randint(1,100)
num = int(numStr)

timesGuessed = int(0)
correct = False

while ( correct == False ):
    requestStr = input("What is your number guess? ")
    requestInt = int(requestStr)

    if ( requestInt == num ):
        print("Your number is correct! You guessed the number in ", timesGuessed, " attempts!")
        correct = True
        break
    elif ( requestInt > num ):
        print ("Your number is Too High.")
        timesGuessed += 1
    elif ( requestInt < num ):
        print ("Your number is Too Low.")
        timesGuessed += 1
