import sys

length = int(len(sys.argv))

def Hello(name):
        print("Hello " + name + "!")

if length <=1:
    Hello(name="World")
else:
    Hello(name=sys.argv[1])
