import sys
import re


def print_menu():
    print ("")
    print ("WISER GAME RECORDER")
    print ("===================")
    print ("1. New Game")
    print ("x. Exit")


ACTION_VALID = 0
ACTION_INVALID = 1
ACTION_CONFLICT_BALL = 2


def validate(action_string):
    if (action_string == 'x'):
            return ACTION_VALID

    if (re.match('[rw][1-7][rw][1-7]|[rw][f]', action_string)):
        if (len(action_string) == 4):
            if(action_string[:2] == action_string[2:]):
                return ACTION_CONFLICT_BALL
        return ACTION_VALID
    else:
        return ACTION_INVALID


def process_game():
    sequence = 1
    while(True):
        action = input("[" + str(sequence) + "]: ")
        result = validate(action.lower())
        if (result == ACTION_VALID):
            if (action.lower() == "x"):
                break
            sequence = sequence + 1
        else:
            if (result == ACTION_INVALID):
                print ('"' + action + '" is invalid action input')
            else:
                print ('"' + action + '" is has same striker and target')
            print ("Usage: [STRIKER][TARGET]")
            print ("  or:  [BALL][FOUL]")
            print ("  [STRIKER][TARGET]     [rRwW][1-7][rRwW][1-7]")
            print ("  [BALL][FOUL]          [rRwW][fF]")
            print ("Example: r1w1, w1r2, r3r6, rf")
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
        if (selection.lower() != 'x'):
            action_map.get(selection, errHandler)()
        else:
            break

    print ("")
    print ("Exit")

if __name__ == "__main__":
    main(sys.argv[1:])
