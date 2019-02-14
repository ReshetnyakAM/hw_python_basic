'''
Задание 1. Реализовать класс-строитель. В его конструктор передать два списка.
Класс должен возвратить python-объект словарь. Проверить, что объект
создается корректно - создать экземпляр класса и обратиться к значению
элемента словаря, как к атрибуту класса.
'''
class MyBuilder:
    def __init__(self, listKey, listValue):
        if len(listKey) != len(listValue):
            raise Exception('Длина списков должна быть одинакова')
        for i in range(len(listKey)):
            setattr(self, listKey[i], listValue[i])

obj = MyBuilder(['Person1','Person2'],['Иванов Василий','Петров Владимир'])
print(obj.Person1)

'''
Задание 2.
Создать класс-обертку для списка. Список передвайте в конструктор класса.
Реализуйте удаление всех элементов из списка через функцию clear.
Но функция должна применяться не к списку, а к экземпляру класса.
Внутри класса должно быть предусмотрено делегирование этой функции методу (clear)
списка.
'''

class MyWrapper:
    def __init__(self, object):
        self.wrapped = object
    def clear(self):
        self.wrapped.clear()
    def __str__(self):
        return str(self.wrapped)

obj = MyWrapper([1,2,3,4,5,6])
print(obj)
obj.clear()
print(obj)
