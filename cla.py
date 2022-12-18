import sys

""" for num in sys.stdin.read():
    print(num) """

numstrings = sys.argv[1:]
for n in numstrings:
    if not n.isdigit():
        print("Numbers only")
        sys.exit(1)
args = [int(k) for k in numstrings]
total = sum(args)
length = len(args)
message = "The average is: " + str(total / length)
print(message, file=sys.stdout)