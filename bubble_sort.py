#!/usr/bin/env python
# coding: utf-8

def buble_sort(daftar_tidak_urut):
    panjang_daftar_tidak_urut = len(daftar_tidak_urut) - 1

    for i in range(panjang_daftar_tidak_urut):
        for j in range(panjang_daftar_tidak_urut):
            if daftar_tidak_urut[j] > daftar_tidak_urut[j + 1]:
                temp = daftar_tidak_urut[j]
                daftar_tidak_urut[j] = daftar_tidak_urut[j + 1]
                daftar_tidak_urut[j + 1] = temp

    print(daftar_tidak_urut)


daftar_tidak_urut = [27, 35, 6, 15, 51, 2, 64, 11, 93, 38, 80]
buble_sort(daftar_tidak_urut)
