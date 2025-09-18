import random

def roll_dice():
    dice_total =random.randint(1,6)+random.randint(1,6)
    return dice_total

def main():
    player1 = input("Enter player 1's name \n")
    player2 = input("Enter player 2's name \n")

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(player1,' Rolled ',roll1)
    print(player2,' Rolled ',roll2)

    if roll1 > roll2:
        print('The winner is player',player1)

    elif roll1 < roll2:
        print('The winner is player',player2)
    else:
        print('Its a TIE')

main()