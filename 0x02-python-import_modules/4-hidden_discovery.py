#!/usr/bin/python3
import hidden_4


def main():
    file = dir(hidden_4)
    l1 = len(file)
    for i in range(0, l1):
        if file[i][0:2] != "__":
            print(file[i])


if __name__ == "__main__":
    main()
