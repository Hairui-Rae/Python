# Practice1: guess_random_number

import random
num = random.randint(1,100)

print("I'm thinking of a number between 1 and 100, let's guess it")
guess_number = int(input("Please input your guess:"))

if guess_number == num:
    print("Congrats! You guessed the right number at the first time!")

else:
    if guess_number < num:
        print(" The number you guessed is lower than my number.")

    elif guess_number > num:
        print(" The number you guessed is higher than my number.")

    guess_number = int(input("Please input your guess again:"))

    if guess_number == num:
        print("Congrats! You guessed the right number at the second time!")

    else:
        if guess_number < num:
            print("The number you guessed is lower than my number.")
        elif guess_number > num:
            print("The number you guessed is higher than my number.")

    guess_number = int(input("Please input your guess at the last time:"))

    if guess_number == num:
        print("Congrats! You guessed the right number at the last time!")

    else:
        print("Sorry, you guessed the wrong number at the last time.")



