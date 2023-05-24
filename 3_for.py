"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [
        363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [
        317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [
        343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
products = [
    {'product': 'iPhone 12', 'items_sold': [
        363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [
        317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [
        343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]


def sum_sold():
    total_ip = 0
    for i in products[0]['items_sold']:
        total_ip += i

    total_xia = 0
    for i in products[1]['items_sold']:
        total_xia += i

    total_sams = 0
    for i in products[2]['items_sold']:
        total_sams += i
    return total_ip, total_xia, total_sams


def avg_sold():
    total_ip = 0
    for i in products[0]['items_sold']:
        total_ip += i

    total_xia = 0
    for i in products[1]['items_sold']:
        total_xia += i

    total_sams = 0
    for i in products[2]['items_sold']:
        total_sams += i
    return int(total_ip/len(products[0]['items_sold'])), int(total_xia/len(products[1]['items_sold'])), int(total_sams/len(products[2]['items_sold']))


def all_sold():
    global total
    total = 0
    for i in products[0]['items_sold']:
        total += i
    for j in products[1]['items_sold']:
        total += j
    for k in products[2]['items_sold']:
        total += k
    return total


def all_avg():
    summ = len(products[0]['items_sold']) + len(products[1]
                                                ['items_sold']) + len(products[2]['items_sold'])
    return int(total/summ)


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(sum_sold())
    print(avg_sold())
    print(all_sold())
    print(all_avg())


if __name__ == "__main__":
    main()
