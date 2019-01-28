# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def Fibonacci(n, m):
    result = [1, 1]
    for i in range(2, m):
        result.append(result[i-1] + result[i-2])
    return result[n-1:m]
print(Fibonacci(1,10))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sortMax(originList):
    newList = list(originList)
    sortList = []
    for i in originList:
        a = min(newList)
        sortList.append(a)
        newList.remove(a)
    return sortList
print(sortMax([-1, 39, 4, 7, 10, 25, 38, 100]))


#Задача-3:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.