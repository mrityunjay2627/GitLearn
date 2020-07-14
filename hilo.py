low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start") # Remember

guesses = 1
while low != high:
    # print("\tGuessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h or l, or c if my guess was correct "
                     .format(guess)).casefold()

    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess.
        low = guess + 1
    elif high_low == "l":
        # G
        # uess lower. The high end of the range becomes one less than the guess.
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l or c")

    # guesses = guesses + 1
    # An augmented assignment is used to replace a statement where an operator takes a
    # variable as one of its arguments and then assigns the result back to same variable.
    # A simple example is x += 1 which is expanded to x = x + (1).
    # Similar constructions are often available for various binary operators.
    guesses += 1
else:  # else for while loop. See the indentation. Will run when low = high.
    #  When a loop terminates normally, the else block is executed.
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))
