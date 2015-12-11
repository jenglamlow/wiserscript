import sys
import re


def print_menu():
    print ("")
    print ("WISER GAME RECORDER")
    print ("===================")
    print ("1. New Game")
    print ("x. Exit")


def validate(action_string):
    pass
    if action_string == "y":
        return False
    else:
        return True


def process_game():
    sequence = 1
    while(True):
        action = input("[" + str(sequence) + "]: ")
        if (validate(action)):
            if (action == "x"):
                break
            sequence = sequence + 1
        else:
            print ('"' + action + '" is invalid action input')
            print ("Valid Format: bNbN or bf, b = r/g, N = 1 to 7")
            print ("For foul, rf = red foul, wf = white foul")
            print ("Example: r1g1, r1r2, r3w6, rf")
            print ("")


def new_game():
    print ("")
    print ("New Game")
    print ("========")

    while(True):
        game_name = input("Enter Game Name --> ")
        if (re.match('^[\w\-_]+$', game_name)):
            break
        else:
            print ('"' + game_name + '" is invalid filename format')

    print ("Game Name:", game_name)

    process_game()

    print ("Exit new game")


def errHandler():
    print("")
    print ("Invalid Input..")


action_map = {
    '1': new_game,
}


# Main Routine
def main(argv):
    while (True):
        print_menu()
        selection = input("-->")
        if selection != 'x':
            action_map.get(selection, errHandler)()
        else:
            break

    print ("")
    print ("Exit")

if __name__ == "__main__":
    main(sys.argv[1:])
