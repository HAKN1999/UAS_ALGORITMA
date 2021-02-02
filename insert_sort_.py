#!/usr/bin/env python
# coding: utf-8

def insert_sort(array_acak):
    for index in range(1, len(array_acak)):
        target_index = index
        nilai_insert = array_acak[index]

        while target_index > 0 and array_acak[target_index-1] > nilai_insert:
            array_acak[target_index] = array_acak[target_index-1]
            target_index -= 1

        array_acak[target_index] = nilai_insert

    print(array_acak)


array_acak = [27, 35, 6, 15, 51, 2, 64, 11, 93, 38, 80]
insert_sort(array_acak)
