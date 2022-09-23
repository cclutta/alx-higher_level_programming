#!/usr/bin/python3
""" Module peak """


def find_peak(list_of_integers):
    """ Finds the peak in a list of unsorteed integers

    Arguments:
        list_of_integers: list used to fund the peak
    """
    if list_of_integers == []:
        return None

    l_len = len(list_of_integers)
    if l_len == 1:
        return list_of_integers[0]
    if l_len == 2:
        return max(list_of_integers)

    mid = int(l_len / 2)
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak > list_of_integers[mid + 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
