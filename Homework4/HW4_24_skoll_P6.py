"""
Homework 4
>Problem 6

Author: Derrick Unger
Date: 2/07/20
CSC232 Winter 2020
"""

# Recommend using getpass() to hide user input, however QtConsole in Spyder
# does not support this funciton, for full credit I will not include.
# EX:
# import getpass as gp
# p1Turn = gp.getpass(p1Name + "'s turn: ")  # P1 Turn Indicator

print("\n")
print("="*50)
print("Rock, Paper, Scissors")
print("="*21)
print("Rules: Follow prompts, when its your turn, enter Rock, Paper or"
      " Scissors")
code = 0  # Play again?
p1Wins, p2Wins = 0, 0  # Win Counters
rnd = 0  # Round Counter
namer = 0  # Toggle Name Prompt
tie = 0  # Number of ties counter

while code == 0:
    try:
        if namer == 0:  # Name Input Prompt
            p1Name = input("Enter name of 1st player: ")
            p2Name = input("Enter name of 2nd player: ")
            namer += 1

        while rnd < 3:
            while code == 0:  # Keep on turn until correct input entered
                p1Turn = input("\n"+p1Name+"'s turn: ")  # P1 Turn Indicator
                p1Turn = p1Turn.upper()
                if (p1Turn != "ROCK" and p1Turn != "SCISSORS" and p1Turn != "PAPER"):
                    print("Error, wrong choice! Try again.")
                    code = 0
                else:
                    code = 1

            while code == 1:  # Keep on turn until correct input entered
                p2Turn = input(p2Name + "'s turn: ")  # P2 Turn Indicator
                p2Turn = p2Turn.upper()
                if (p2Turn != "ROCK" and p2Turn != "SCISSORS" and p2Turn != "PAPER"):
                    print("Error, wrong choice! Try again.")
                    code = 1
                else:
                    code = 0  # Return code to original state

            # Win and Tie Conditions
            if(p1Turn == "ROCK" and p2Turn == "SCISSORS" or
               p1Turn == "PAPER" and p2Turn == "ROCK" or
               p1Turn == "SCISSORS" and p2Turn == "PAPER"):

                p1Wins += 1
                print("\n")
                print(p1Name, "won that round!")

            elif(p2Turn == "ROCK" and p1Turn == "SCISSORS" or
                 p2Turn == "PAPER" and p1Turn == "ROCK" or
                 p2Turn == "SCISSORS" and p1Turn == "PAPER"):

                p2Wins += 1
                print("\n")
                print(p2Name, "won that round!")

            elif p1Turn == p2Turn:

                tie += 1
                print("\nThat round was a Tie!")

            else:  # Should never occur if program is error tight beforehand
                err = 1/0

            rnd += 1  # Next Round

        # Win Announcement
        if p1Wins > p2Wins and tie != rnd:
            print("\n!!!!!!!!!!!!!!")  # A more robust program would center
            print(p1Name, "wins!")     # player names based on size within
            print("!!!!!!!!!!!!!!\n")  # the ! box created, like with "Tie"
        elif p2Wins > p1Wins and tie != rnd:
            print("\n!!!!!!!!!!!!!!")
            print(p2Name, "wins!")
            print("!!!!!!!!!!!!!!\n")
        else:
            print("\n!!!!!!!!!!!!!!")
            print("!  Tie game  !")
            print("!!!!!!!!!!!!!!\n")

        print("Statistics:")
        print(p1Name, "won", p1Wins, "rounds.")
        print(p2Name, "won", p2Wins, "rounds.")
        print(p1Name, "and", p2Name, "tied", tie, "rounds.")

        # Play Again?
        playIn = input("\nPlay again? Y/N: ")
        if playIn.upper() == "Y":

            # New Names?
            newNames = input("\nNew Players? Y/N: ")
            if newNames.upper() == "Y":
                namer = 0
                tie, rnd, p1Wins, p2Wins = 0, 0, 0, 0  # Reset values
            elif newNames.upper() == "N":
                namer = 1
                tie, rnd, p1Wins, p2Wins = 0, 0, 0, 0  # Reset values
            else:
                print("That wasn't a valid option enter Y or N.")

        elif playIn.upper() == "N":
            code = 1
        else:
            print("That wasn't a valid option enter Y or N.")

    except:
        print("\nError: Invalid input, retry\n")
print("="*50)
