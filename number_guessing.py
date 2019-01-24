# Date created: 24/01/2019
# Number guessing game

from random import randrange

# Initialization
cont = True

# Main
while cont:
    number_of_trials = 0
    win = False
    min_range = int(input("Input minimum value: "))
    max_range = int(input("Input maximum value: "))
    threshold = int(input("Input threshold: "))
    n = randrange(min_range, max_range, 1)
    print("Random number is created")
    while number_of_trials < threshold:
        number_of_trials += 1
        guess_value = int(input("Input your guess value: "))
        if guess_value == n:
            win = True
            print("Conrats! You win the game")
            break
        elif guess_value == -1:
            number_of_trials -= 1
            print("n =", n)
        else:
            print("Try again, you have %d tries left" % (threshold - number_of_trials))
    
    if not win:
        print("You lose! Game over")

    cont = bool(int(input("Play again? 0/1 ")))

