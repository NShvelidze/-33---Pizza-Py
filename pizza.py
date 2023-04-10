import sys
import csv
from tabulate import tabulate

def main():
    command_line_argument_check()
    list = []
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                list.append(row)
            print(tabulate(list[1:], headers = list[0], tablefmt = "grid"))
    except(FileNotFoundError):
        sys.exit("File does not exist")

def command_line_argument_check():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()
