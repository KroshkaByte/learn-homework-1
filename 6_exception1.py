"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""


def hello_user():
    """
    Замените pass на ваш код
    """
    while True:
        try:
            n = 0
            while n < 1:
                m = input("Как дела? ")
                if m == "Хорошо":
                    n += 1
        except KeyboardInterrupt:
            print("Пока!")
            break


if __name__ == "__main__":
    hello_user()
