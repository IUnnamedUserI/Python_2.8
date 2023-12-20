#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_input():
    """
    Функция запрашивает ввод с клавиатуры и возвращает
    полученную строку
    """

    string = input("Введите строку: ")
    return string


def test_input(string):
    """
    Функция проверяет, возможно ли преобразовать полученную строку
    в целочисленное значение. Если можно, то возвращает логическое True,
    если нельзя - логическое False
    """
    
    if string.isdigit():
        return True
    else:
        return False
    

def str_to_int(string):
    """
    Функция преобразует полученную строку в целочисленное значение
    и возвращает его
    """
    
    integer = int(string)
    return integer


def print_int(integer):
    """
    Функция выводит полученное целочисленное значение на экран
    """
    
    print(f"Полученное число: {integer}")


if __name__ == "__main__":
    string = get_input()
    if test_input(string) == True:
        print_int(str_to_int(string))
    else:
        print("Введённое число не удалось конвертировать. Завершение работы")
