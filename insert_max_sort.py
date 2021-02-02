#!/usr/bin/env python
# coding: utf-8

def selection_max_sort(array_acak):
    banyak_element = len(array_acak)

    for i in range(banyak_element):
        for j in range(i+1, banyak_element):
            if array_acak[j] < array_acak[i]:
                temp = array_acak[i]
                array_acak[i] = array_acak[j]
                array_acak[j] = temp

    print(array_acak)


array_acak = [27, 35, 6, 15, 51, 2, 64, 11, 93, 38, 80]
selection_max_sort(array_acak)
