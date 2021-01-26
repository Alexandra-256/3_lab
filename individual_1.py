#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 9. Вводится число экзаменов N ≤ 20.
# Напечатать фразу Мы успешно сдали N экзаменов, согласовав слово "экзамен" с числом N.


if __name__ == '__main__':
    N = input("Введите N число: ")
    ending = ""
    if N.isnumeric():
        for x in ['0', '5', '6', '7', '8', '9']:
            if N.endswith(x):
                ending = "ов"
        for x in ['2', '3', '4']:
            if N.endswith(x):
                ending = "a"
    print(f"Мы успешно сдали {N} экзамен{ending}")