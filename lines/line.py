import sys

def main():
    open_file()

def open_file():
        if len(sys.argv)<2:
            sys.exit("Empty argument")
        elif len(sys.argv) > 2:
            sys.exit("Too many argument")
        elif not or_csv(sys.argv[1]):
            sys.exit("Not csv format")
        else:
            formating(sys.argv[1])

def or_csv(str):
    names = str.split('.')
    try:
        if names[1] == "csv":
            return True
        else:
            return False
    except IndexError:
        return False

def formating(file_name):
    try:
        with open(file_name, "r") as file:
            row = []
            for line in file:
                name, smaller_price, bigger_price = line.rstrip().split(',')
                row.append((name, smaller_price, bigger_price))
            border1 = "+------------------+---------+---------+"
            border2 = "+==================+=========+=========+"
            print(border1)
            i = 0
            for name, smaller_price, bigger_price in row:
                print(f"|{name:<18}|{smaller_price:<9}|{bigger_price:<9}|")
                i += 1
                if i == 1:
                    print(border2)
                else:
                    print(border1)
    except FileNotFoundError:
            sys.exit("File not exist")

if __name__ == "__main__":
    main()
