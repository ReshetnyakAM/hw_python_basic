'''
Задание_1. Создать класс. В конструктор передать два параметра - два числа.
Создать второй класс. В конструкторе первого предусмотреть создание
объекта второго класса. Кроме того, в первом классе предусмотреть три метода,
в которых делегировать получение остатка от деления, результата деления и целой
части от деления в методы второго класса (предусмотреть вычисление в соотв. методах
второго класса).
'''

class MyData:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

class MyWrapper:
    def __init__(self, value1, value2):
        self.data = MyData(value1, value2)
    
    def div_rest(self):
        return self.data.value1 % self.data.value2
    def div(self):
        return self.data.value1 / self.data.value2
    def div_int(self):
        return self.data.value1 // self.data.value2

obj = MyWrapper(5,2)
print(obj.div_rest())
print(obj.div())
print(obj.div_int())