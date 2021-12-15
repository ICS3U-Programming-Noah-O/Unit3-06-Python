#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Dec. 14, 2021
# This program allows a user to guess a number between
# 0 and 9 when the initial number is randomly generated
# it also includes a try catch to prevent crashing

import colorama
import random
import time
from colorama import Fore, Back, Style


def main():
    # This function asks for the users number and
    # then compares it to the randomly generated number

    # Randomly generate the number
    rand_num = random.randint(0, 9)

    # Ask for user input
    print(Fore.WHITE + "I have picked a number between 0 and 9.")
    time.sleep(1)
    print(Fore.WHITE + "Guess my number!!!")
    print(Fore.BLUE + " ")
    user_num = (input("Enter your guess: "))

    try:
        # Mke sure user input is an integer
        user_num_int = int(user_num)

        if user_num_int == rand_num:
            print("You guessed it! Most impressive.")
        else:
            print("Sorry, that is incorrect. The number was: "
                  + "{}.".format(rand_num) + " Try again")
            print("")
            time.sleep(1)

    except Exception:
        # Prevent crash by displaying error messsage
        print("'{}' is not a number".format(user_num))


if __name__ == "__main__":
    main()
