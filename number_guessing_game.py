import random
import time

print("""
-----------------------------
WELCOME TO THE GAME!
You have 5 guesses.
Enter 'q' or 'Q' for EXİST
-----------------------------

""")

guess_right=5

while True:
    if guess_right == 0:
        break
    num_range=input("Which number from 0 would you like to predict?: ")

    if num_range== 'q' or num_range=='Q':
        print("The Game is Ending...")
        time.sleep(1)
        break

    try:
        num_range =int(num_range)
    except ValueError:
        print("Please enter only one number.")
        continue

    num=random.randint(0,num_range)

    while True:
        if guess_right==0:
            print(f"Your rights are over\nThe Game is Ending...\nThe number was: {num}")
            time.sleep(1)
            break

        user_guess=input("What is your guess?:")
        try:
            user_guess=int(user_guess)
        except ValueError:
            print("Please enter only one number.")
            continue

        if user_guess == 'q' or user_guess== 'Q':
            print("The Game is Ending...")
            time.sleep(1)
            break
        elif num == user_guess:
            print(f"Congratulations on your correct guess\nThe number was:{num} ")
            guess_right-=1
            print("New round\nPress 'q' or 'Q' to exit.")
            break
        elif num > user_guess:
             print("Increase your number!")
             guess_right-=1
             continue
        elif num < user_guess:
            print("Reduce your number!")
            guess_right-=1
            continue
        else:
            print("Wrong command...")
            guess_right -=1
            continue