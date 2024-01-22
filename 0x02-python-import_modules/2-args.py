#!/usr/bin/python3
if __name__ == "__main__":
    import sys

nmber = len(sys.argv) - 1
if nmber == 0:
    print("{} arguments.".format(nmber))
elif nmber == 1:
    print("{} argument:".format(nmber))
    print("{}: {}".format(nmber, sys.argv[1]))
elif nmber > 1:
    print("{} arguments:".format(nmber))
    for i in range(1, nmber + 1):
        print("{}: {}".format(i, sys.argv[i]))
