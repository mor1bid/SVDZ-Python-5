import os

# 1. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов путь, имя файла, расширение файла.

def pathrec(path):
    absolute = os.path.abspath(path).split("\\")
    file = path
    path = ''
    for l in absolute:
        if l not in file:
            path += l + '\\'
    file = file.split('.')
    record = ({"Путь:", path}, {"Имя файла:", file[0]}, {"Расширение файла:", file[-1]})
    return record

path = input("1. Здравствуйте. Введите имя желаемого файла, вместе с его расширением\n: ")
print(f'Результат\n: {pathrec(path)}')

# 2. Напишите однострочный генератор словаря, который принимает на вход три списка 
# одинаковой длины: имена str, ставка int, премия str с указанием процентов 
# вида 10.25%». В результате получаем словарь с именем в качестве ключа и суммой 
# премии в качестве значения. Сумма рассчитывается 
# как ставка умноженная на процент премии

names = ["Agent Dennis", "Killing Spree", "Hearr Icks", "Puppet Master", "Jake El"]
payday = [500, 1000, 200, 360, 800]
levelup = ["10.17%", "17.03%", "100.0%", "6.66%", "13.07%"]
l = [l.replace('%', '') for l in levelup]
fin = dict(i1 * i2 / i for i, (i1, i2) in zip(payday, map(float, l)))
# res = list(fin)
print(f'Результат\n: {fin}')

# 3. Создайте функцию генератор чисел Фибоначчи

def fibgen(n, fibn = 0):
    for fib in range(n):
        if fib >= 2:
            fib = (fib - 1) + (fib - 2)
            yield fib
        elif fib < 0:
            fib = (fib + 2) - (fib + 1)
            yield fib
        else:
            # if fib == 1:
            #     fibn = 1
            # else:
            #     fibn = 0
            yield fib

number = int(input("\n3. Введите число\n: "))
for f in fibgen(number):
    print(f)