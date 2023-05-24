"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""


def strin(a, b):
    if type(a) is not str or type(b) is not str:
        return 0
    elif a == b:
        return 1
    elif a != b and len(a) > len(b):
        return 2
    elif a != b and b == "learn":
        return 3


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    a, b = 1234, 5467
    res = strin(a, b)
    print(res)         # 1
    a, b = "asfxz", 5467
    res = strin(a, b)
    print(res)         # 2
    a, b = "rod", "rod"
    res = strin(a, b)
    print(res)         # 3
    a, b = "teriss", "tir"
    res = strin(a, b)
    print(res)         # 4
    a, b = "dtop", "learn"
    res = strin(a, b)
    print(res)         # 5


if __name__ == "__main__":
    print(main())
