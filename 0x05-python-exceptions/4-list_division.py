#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    list = []
    try:
        for i in ranger(list_length):
            list.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            list.append(0)
            print("division by 0")
        except TypeError:
            list.append(0)
            print("wrong type")
        except IndexError:
            list.append(0)
            print("out of range")
    finally:
        return list
