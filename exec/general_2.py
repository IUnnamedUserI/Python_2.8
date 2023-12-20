#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def cylinder(r, h):
    """
    Вычисление площади цилиндра
    """

    side = 2 * math.pi * r * h
    answer = input("Хотите ли Вы получить полную площадь цилиндра? (y/n) ")
    if answer == 'y':
        def circle(r):
            square = math.pi * r**2
            return square
        
        return circle(r) + side * 2
    
    else:
        return side


if __name__ == "__main__":
    """
    Основная программа
    """
    
    print(cylinder(float(input("Введите радиус: ")),
             float(input("Введите высоту: "))))
