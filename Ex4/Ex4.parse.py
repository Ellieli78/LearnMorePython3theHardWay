import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help = "display a square of a given number")
parser.add_argument("-i", "--increase",
                    help = "increase input number")
parser.add_argument("-d", "--decrease",
                   help = "decrease input number")
parser.add_argument("-dd", "--double",
                   help = "double input number")
args = parser.parse_args()
answer = args.square**2
if args.increase:
    print("the square of {} equals {}. Increase your input number.".format(args.square, answer))
elif args.decrease:
    print("the square of {} equals {}. Decrease your input number".format(args.square, answer))
elif args.double:
    print("the square of {} equals {}. Double your input number.".format(args.square, answer))
else:
    print(answer)
