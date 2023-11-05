#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

# вариант - 11

if __name__ == "__main__":
    sample = ['surname', 'name', 'phone', 'date']
    lst = []

    # ввод данных
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о работнике.
            surname = input('Фамилия: ')
            name = input("Имя: ")
            phone = input("Номер телефона: ")
            date = input('Дата рождения (число:месяц:год): ').split(':')

            # Создать словарь.
            dct = {'surname': surname,
                   'name': name,
                   'phone': phone,
                   'date': date}
            lst.append(dct)

            # Сортировка списка словарей
            lst.sort(key=lambda x:
            datetime.strptime('-'.join(x['date']), '%d-%m-%Y'))
            print(lst)

        elif command == 'phone':
            numbers_phone = input()
            fl = True
            for i in lst:
                if i['phone'] == numbers_phone:
                    print(f"Фамилия: {i['surname']}\n"
                          f"Имя: {i['name']}\n"
                          f"Номер телефона: {i['phone']}\n"
                          f"Дата рождения: {':'.join(i['date'])}")
                    fl = False
                    break
            if fl:
                print("Человека с таким номером телефона нет в списке.")
