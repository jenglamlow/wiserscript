import sys
import re
from game import Game


ACTION_VALID = 0
ACTION_INVALID = 1
ACTION_CONFLICT_BALL = 2


def print_menu():
    print ("")
    print ("WISER GAME RECORDER")
    print ("===================")
    print ("1. New Game")
    print ("q. Exit")


def list_game_info(game):
    seq = 1
    for action in game.sequence:
        print ('[' + str(seq) + ']: ' + action)
        seq = seq + 1

    game.print_info()


def action_validate(action_string):
    if re.match('[hluq]|[s][\d]+', action_string):
            return ACTION_VALID

    if re.match('[rw][1-7][rw][1-7]|[rw][1-7][f]', action_string):
        if len(action_string) == 4:
            if action_string[:2] == action_string[2:]:
                return ACTION_CONFLICT_BALL
        return ACTION_VALID
    else:
        return ACTION_INVALID


def print_match_help():
    print ("Usage: [STRIKER][TARGET]")
    print ("  or:  [BALL][FOUL]")
    print ("  or:  [OPTION]")
    print ("    [STRIKER][TARGET]     [rw][1-7][rw][1-7]")
    print ("    [BALL][FOUL]          [rw][1-7][f]")
    print ("Example: r1w1, w1r2, r3r6, r2f")
    print ("[OPTION]:")
    print ("    h                     Help information")
    print ("    l                     List all match sequence and info")
    print ("    u                     Undo previous sequence")
    print ("    s[Number]             Start edit from sequence number")
    print ("    q                     Exit")
    print ("")


def process_action_option(game, action_string):
    if action_string == 'h':
        print_match_help()
    elif action_string == 'l':
        print ("=================")
        print ("List information")
        list_game_info(game)
        print ("=================")
    elif action_string == 'u':
        print ("Undo")
    elif action_string[0] == 's':
        print ("start from")
    else:
        return False

    return True


def process_game(game):
    while(True):
        action = input("[" + str(game.seq_num) + "]: ")
        action = action.lower()
        result = action_validate(action)
        if result == ACTION_VALID:
            if action == 'q':
                break
            if process_action_option(game, action):
                continue
            if game.process(action):
                game.seq_num = game.seq_num + 1
            else:
                # print ("Please enter a valid input")
                continue
        else:
            if result == ACTION_INVALID:
                print ("\"%s\" is invalid action input" % (action))
            else:
                print ("\"%s\" has same striker and target" % (action))
            print ('Try "h" to for more infomation.')
            print ("")


def new_game():
    print ("")
    print ("New Game")
    print ("========")

    while(True):
        game_name = input("Enter Game Name --> ")
        if re.match('^[\w\-_]+$', game_name):
            break
        else:
            print ("\"%s\" is invalid filename format" % (game_name))

    game = Game(game_name)
    process_game(game)

    print ("Exit new game")


def errHandler():
    print("")
    print ("Invalid Input..")


menu_map = {
    '1': new_game,
}


# Main Routine
def main(argv):
    while (True):
        print_menu()
        selection = input("-->")
        if selection.lower() != 'q':
            menu_map.get(selection, errHandler)()
        else:
            break

    print ("")
    print ("Exit")

if __name__ == "__main__":
    main(sys.argv[1:])
