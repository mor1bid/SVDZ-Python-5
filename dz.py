import os

# 1
# path = input("1. Здравствуйте. Введите путь к желаемому файлу: ")
path = os.path.abspath("dz.py").split()
print(path)