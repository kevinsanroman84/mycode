import random
import os
clear = lambda: os.system('clear')
clear()

def main():
    choices = {"rock": "✊", "paper": "✋", "scissors": "✌️"}
    defeats = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

    opponets_defeated = 0

    health = 100
    attack = 10 
    defense = 10 

    while 0 < health:
        move = "invalid"
        ans = input("Choose your move: [Rock] [Paper] [Scissors] ").lower()
        print()

        # Validate choice for move
        while move == "invalid":
            if ans in choices:
                move = ans
                break
            print("Choice invalid...")
            ans = input("Choose your move: [Rock] [Paper] [Scissors] ").lower()
            print()

        # Choose random move for opponent
        opponet_move = random.choice(list(choices.keys()))
        print(opponet_move)

        # Create string for players choices
        choice_string = f"You choose: {choices[move]}".ljust(30) + f"Opponent choose: {choices[opponet_move]}".rjust(30) + "\n"

        # Check game state
        if move == opponet_move:
            health -= 10
            print(choice_string)
            print("You tied... You took 10 knockback damage!".center(60))
            print(f"You have {health} health remaining!".center(60))
        elif defeats[move] == opponet_move:
            opponets_defeated += 1
            print(choice_string)
            print("Opponent defeated! Here comes your next challenger!".center(60))
        else:
            health -= 30 
            print(choice_string)
            print("You lost... You took 30 damage!".center(60))
            print(f"You have {health} health remaining!".center(60))
        print()

        # Check game loss
        if 0 >= health:
            print("You are overwhelmed by your defeat!".center(60))
            print("Everything went black!!!".center(60))
            print(f"You defeated {opponets_defeated} opponents!".center(60))
            redo = input("Would you like to try again?... [yes][no] ").lower()
            if redo == "yes":
                health = 100
                opponets_defeated = 0
            else:
                print("Thanks for playing!!!".center(60))
                input()
                break

        # Clear screen and prompt for next round
        input("Hit enter to continue".center(60))
        clear()
        
main()