#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for c in range(len(r)):
            print("{:d}".format(r[c]),
                  end=' ' if c < len(r) - 1 else '')
        print()
