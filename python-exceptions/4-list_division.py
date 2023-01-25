#!/usr/bin/python3


def list_division(list_1, list_2, lenght):
    new_list = []
    for i in range(lenght):
        try:
            new_list.append(list_1[i] / list_2[i])
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        except TypeError:
            new_list.append(0)
            print("wrong type")
        except IndexError:
            new_list.append(0)
            print("out of range")
        finally:
            continue
    return new_list
