#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # dct = {input("Класс: "): int(input("Кол-во учеников в классе: "))
    #        for i in range(int(input('Введите кол-во классов: ')))}
    dct = {'1а': 28,
           '1б': 30,
           '2б': 25,
           '2а': 29,
           '2в': 35,
           '3а': 20,
           '4а': 50,
           '4б': 15}

    # а
    dct['4а'] = 40

    # b
    dct.setdefault('2ж', 23)

    # с
    dct.pop('4б')

    print(dct)
    print(sum(dct.values()))