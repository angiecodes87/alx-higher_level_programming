#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boolist = [False] * len(my_list)
    for count, num in enumerate(my_list):
        if num % 2 == 0:
            boolist[count] = True
    return (boolist)
