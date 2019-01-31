# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

# с re
import re
line = 'mtMmEZUOmcq'
list_re = re.findall(r'[a-z]+', line)
print(list_re)

# без re
line = 'mtMmEZUOmcq'
res = []
tmp = ''
for val in line:
    if val.islower():
        tmp += val
    elif tmp != '':
        res.append(tmp)
        tmp = ''
if tmp != '':
    res.append(tmp)
print(res)


# Задание-2:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import random
with open('test.txt', 'w') as f:
    for i in range(2500):
        f.write(str(random.randint(0, 9)))

with open('test.txt', 'r') as f:
    s = list(f.read())

a, b = 0, 0
c = ''
for i in range(1, len(s)):
    if  s[i] == s[i-1]:
        a += 1
    else:
        if a > b:
            b = a
            c = s[i-1]
        a = 0
print('Длинная последовательность одинаковых цифр:', c * b)