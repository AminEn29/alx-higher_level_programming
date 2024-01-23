#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number = len(sys.argv) - 1
    if (number == 0):
        print("0")
    if (number == 1):
        print("{}".format(sys.argv[1]))
    else:
        sum = 0
        for i in range(len(sys.argv) -1):
            sum += int(sys.argv[i + 1])
        print(sum)
