import sys


def print_menu():
    print ("")
    print ("WISER GAME RECORDER")
    print ("===================")
    print ("1. New Game")
    print ("x. Exit")


def new_game():
    print ("New Game")


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
