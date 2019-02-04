# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# скрипт создающий директории

import os

path = 'C:\Temp\catalogs'
folders = ['dir_1', 'dir_2', 'dir_3', 'dir_4', 'dir_5', 'dir_6', 'dir_7',
'dir_8', 'dir_9']

def createFolders(path):
    if not os.path.exists(path):
        os.mkdir(path)

fullPhath = os.path.join(path)
createFolders(fullPhath)

for f in folders:
    folder = os.path.join(fullPhath, f)
    createFolders(folder)
    print(f'Директория {folder} создана')
    

# скрипт удаляющий папки

import os

def delete_dirs():
    a = 1
    while a < 10:
        dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(a))
        try:
            os.rmdir(dir_path)
        except FileExistsError:
            print('Такая директория уже не существует')
        a = a + 1
    return

delete_dirs()

# вариант каскадного удаления директории

import os
import shutil

path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'catalogs')
shutil.rmtree(path)
print('Директория catalogs удалена')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
#ТОЛЬКО ПАПКИ, А НЕ ФАЙЛЫ!

import os

def print_dirs():
    for item in os.listdir():
        if os.path.isdir(item):
            print(item)
print_dirs()


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
# ИСПОЛЬЗОВАТЬ ТОЛЬКО МОДУЛЬ OS

import os

def copy_file(source, dest):
    with open(source, 'r') as src, open(dest, 'w') as dst: dst.write(src.read())

copy_file(os.path.basename(__file__), os.path.basename(__file__) + '.copy')
print('У скопированного файла расширение .copy в директории:', os.getcwd())

