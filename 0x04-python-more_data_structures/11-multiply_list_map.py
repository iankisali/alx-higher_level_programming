#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    mul_by_num = list(map(lambda x: number * x, my_list))
    return mul_by_num
