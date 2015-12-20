import sys
import re
from game import Game


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
    print ("-----------------")
    game.print_info()


def action_validate(action):
    mode_regex = r"\b[hluq]{1}\b|\b[s][1-9][0-9]{0,2}\b"
    action_regex = r"\b[rw][1-7][rw][1-7]\b|\b[rw][1-7][f][o]{0,1}\b"

    if re.match(mode_regex, action):
        pass
    elif re.match(action_regex, action):
        if len(action) == 4:
            if action[:2] == action[2:]:
                raise ValueError("\"%s\" has same striker and target" %
                                 (action))
    else:
        raise ValueError("\"%s\" is invalid action input" % (action))


def print_match_help():
    print ("Usage: [STRIKER][TARGET]")
    print ("  or:  [BALL][FOUL]")
    print ("  or:  [OPTION]")
    print ("    [STRIKER][TARGET]     [rw][1-7][rw][1-7]")
    print ("    [BALL][FOUL][OUT]     [rw][1-7][f][o]")
    print ("Example: r1w1, w1r2, r3r6, r2f, r3fo")
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
        print ("")
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
        try:
            action_validate(action)

            if action == 'q':
                break
            if process_action_option(game, action):
                continue

            try:
                game.process(action)
                game.seq_num = game.seq_num + 1
            except ValueError as err:
                print (err)

        except ValueError as err:
            print (err)
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
