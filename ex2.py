#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    dct = {1: 'hello',
           2: 'goodbye',
           3: 'good night',
           4: 'kitty',
           5: 'cat',
           6: 'dog'}

    new_dct = {value: key for key, value in dct.items()}
    print(new_dct)
