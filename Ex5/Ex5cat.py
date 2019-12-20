import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", metavar = 'E',type = str,nargs = '+',
                    help = "display a square of a given number")
parser.add_argument("-n", '--numbers', action='store_true',
        help = 'Print line numbers')

args = parser.parse_args()
print(">>>", args)

i = 1
for in_square_name in args.square: # read the file name from Terminal input
    in_file = open(in_square_name)
    if args.numbers:
        for line in in_file.readlines():
            print(f"{i} {line}", end='')
            i += 1
    else:
        print(in_file.read())
