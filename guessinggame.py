# To add in git branch br1.
# Changes will remain in br1 branch only. Not master branch.
import random

highest = 1000
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing
# TODOs are a great way to keep track of things so that you don't forget
# about changes you intended to make. Note that this is a feature of IntelliJ
# It's not a Python feature.
guess = 0 # initialise to any number that doesn't equal the answer
print("Please guess number between 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input()) # To make sure user enters an integer.

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:   # guess must be greater than answer
            print("Please guess lower")
        # guess = int(input())
        # if guess == answer:
        #     print("Well done, you guessed it")
        # else:
        #     print("Sorry, you have not guessed correctly")
