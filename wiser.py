import sys
from openpyxl import Workbook
from openpyxl import load_workbook


def process_excel(name):
    wb = load_workbook(name, data_only=True)
    sheet = wb['Match Info']

    red_scorer = wb.get_named_range("RedScorer").destinations[0]
    white_scorer = wb.get_named_range("WhiteScorer").destinations[0]

    red_scorer = red_scorer[1].replace('$', '')
    white_scorer = white_scorer[1].replace('$', '')

    val = sheet[c2].value
    print(val)


# Main Routine
def main(argv):
    if len(sys.argv) != 2:
        print ("Invalid number of argument (1)")
        return

    name = sys.argv[1]
    print(name)

    process_excel(name)


if __name__ == "__main__":
    main(sys.argv[1:])
