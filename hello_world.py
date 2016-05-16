import sys

length = int(len(sys.argv))

if length <= 1:
    print("Hello World!")
else:
    name = sys.argv[1]
    print("Hello " + name + "!")
