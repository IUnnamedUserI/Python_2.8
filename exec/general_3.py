#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def multiply():
    """
    Функция перемножения двух чисел
    """

    a = int(input("Введите первое число: "))
    if a != 0:
        b = int(input("Введите второе число: "))
        if b != 0:
            print(f"{a} * {b} = {a * b}")
            multiply()
    else:
        print("Завершение работы программы...")

if __name__ == "__main__":
    """
    Основная программа
    """
    
    multiply()
    