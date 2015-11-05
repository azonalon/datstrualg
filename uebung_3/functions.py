#!/bin/python

def permute(data, permutation):
    n = len(data)
    cycle_begin = 0
    not_in_cycle = 1
    for _ in range(n):

        current_index = cycle_begin
        erased = 0
        while current_index != cycle_begin:
            next_index = permutation[current_index]
            erased = data[next_index]
            data[next_index] = data[current_index]
            current_index = next_index
        data[cycle_begin] = erased

        not_in_cycle = cycle_begin + 1
        cycle_begin = not_in_cycle
