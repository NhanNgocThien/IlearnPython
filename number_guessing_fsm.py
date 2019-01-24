# Date created: 24/01/2019
# Number guessing game implemented with finite state machine

import os
import sys
from random import randrange

# Legend
s_exit  = -1
s_start =  0
s_guess =  1
s_show  =  2
s_wrong =  3
s_lose  =  4
s_win   =  5
s_again =  6

# Initialization
state = s_start

# Main
while state != s_exit:
    if state == s_start:
        if sys.platform[0] == 'l':      # If current OS is linux
            os.system("clear")
        elif sys.platform[0] == 'w':    # If current OS is window
            os.system("cls")
        num_of_trials = 0
        min_val = int(input("Input minimum value = "))
        max_val = int(input("Input maximum value = "))
        threshold = int(input("Input maximum numbers of trials = "))
        n = randrange(min_val, max_val, 1)
        state = s_guess


    elif state == s_guess:
        guess_val = int(input("Input your guess value: "))
        num_of_trials += 1
        state = s_win if guess_val == n else (s_show if guess_val == -1 else s_wrong) 


    elif state == s_show:
        num_of_trials -= 1
        print("n =", n)
        state = s_guess


    elif state == s_wrong:
        if (num_of_trials < threshold):
            print("Incorrect! You have",threshold - num_of_trials,"tries left")
        state = s_lose if num_of_trials >= threshold else s_guess 


    elif state == s_win:
        print("Congrats! You win!")
        state = s_again


    elif state == s_lose:
        print("Too bad, you lose")
        state = s_again


    elif state == s_again:
        cont = bool(int(input("Continue? 0/1 ")))
        state = s_exit if cont == 0 else s_start
