#!/usr/bin/python3
import sys


def main():
    argc = len(sys.argv)
    c = 0
    for i in range(1, argc):
        c += int(sys.argv[i])
    print(c)


if __name__ == "__main__":
    main()
