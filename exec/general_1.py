#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def test(a):
    if a >= 0:
        positive()
    else:
        negative()

def positive():
    print("Положительное")

def negative():
    print("Отрицательное")

if __name__ == "__main__":
    test(int(input("Введите целочисленное значение: ")))
    