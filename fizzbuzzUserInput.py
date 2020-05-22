i = input("What is the number? ")
num = int(i)
if num % 15 == 0:
    print ("FizzBuzz")
elif num % 3 == 0:
    print ("Fizz")
elif num % 5 == 0:
    print ("Buzz")
else:
    print ("Bad luck, no prize today")
