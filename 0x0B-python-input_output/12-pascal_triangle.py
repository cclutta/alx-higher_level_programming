#!/usr/bin/python3
"""Pascal triangle module
contains one function, pascal_triangle()
"""


def pascal_triangle(n):
    """Returns Pascal's triangle with list of integers. """
    if n <= 0:
        return []

    tr = [[1]]
    while len(tr) is not n:
        temp = [1]
        for i in range(len(tr[-1]) - 1):
            temp.append(tr[-1][i] + tr[-1][i + 1])
        temp.append(1)
        tr.append(temp)
    return tr
