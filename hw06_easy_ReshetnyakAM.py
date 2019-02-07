'''
Задача-1: Написать класс, например, Worker, который должен содержать информацию
о работнике (ФИО, оклад, надбавка за напряженность).

Создать экземпляр класса и передать конкретные данные (примеры ФИО, должности,
оклад и надбавки). Оклад и надбавку передать в виде строки.

На основе строки создать атрибут income, который реализовать в виде словаря
и инкапуслировать. Словарь income должен содержать информацию об окладе и надбавке.

Применить к экземпляру
класса метод __dict__ и проверить какой будет результат применения этого метода.
А комментариях к заданию написать тип результата на русском языке.
'''
import ast

class Worker:
    def __init__(self, name = '', age = 0, post = '', salary_and_addition = "{'salary': 0.00, 'addition': 0.00}"):
        self.name = name
        self.age = age
        self.post = post
        self.__income = ast.literal_eval(salary_and_addition)
        self.salary = self.__income['salary']
        self.addition = self.__income['addition']

    def __str__(self):
        return 'ФИО: {0}, возраст: {1}'.format(self.name, self.age)

    def full_income(self):
        return self.__income['salary'] + self.__income['addition']


worker = Worker("Иванов Василий", 50, "Директор", "{'salary': 10000, 'addition': 100}")
print(worker.__dict__)

# После применения __dict__ класс "разбился" на словарь са значениями {'поле1': значение1, 'поле2': значение2}
# скрытое поле тоже присутсвует, но в его имя добавлен префикс с названием класса _Worker

'''
Задача-2: Продолжить работу над задачей 1. Создать на основе класса Worker класс
Position (реализовать наследование). Добавить классу уникальный атрибут -
% премии к зарплате (от суммы оклада).
Создать метод расчета зарплаты с учетом только премии.
Реализовать обращение к этому атриубуту, как к свойству.
Проверить работу всей структуры на реальных данных, вывести результаты.
'''

class Position(Worker):
    premium = 0.00
    def get_premium_salary(self):
        return self.salary * (1 + self.premium / 100)
    premium_salary = property(get_premium_salary)

    def full_income(self):
        return self.premium_salary + self.addition



position = Position("Петров Генадий", 65, "Бухгалтер", "{'salary': 8000, 'addition': 80}")
position.premium = 25
print(position.__dict__)
print(position.premium_salary)
   

'''
Задача-3: Продолжить работу над задачей 2.  Реализовать полиморфизм
использования знака + в методах 
1) вывода полного имени работника и возраста
2) вычисления общего дохода работника с учетом надбавки .
Проверить работу всей структуры на реальных данных, вывести результаты.
'''
print(worker)
print(position)

print(worker.full_income())
print(position.full_income())
