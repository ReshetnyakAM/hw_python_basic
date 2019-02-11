'''
Задача-1: Создать класс Матрица. В конструктор класса передавать переменную
содержащую матрицу в виде списка списков. В конструкторе класса преобразовать
список списков в привычный матричный вид. Переопределить стандартное поведение
методов __add__ и __str__ класса. Создать два экземпляра класса Матрица с данными.
Метод __add__ должен реализовывать сложение матриц, а __str__ - вывод итоговой
матрицы.
'''

class Matrix:
    def __init__(self, lst):
        self.__list = lst
        self.height = len(lst) 
        self.width = len(lst[0]) 

    def __str__(self):
        res = "Matrix: {} x {}".format(self.height, self.width) + '\n'
        for row in self.__list:
            for item in row:
                res = res + ' ' + str(item)
            res = res + '\n'
        return res
    
    def __getitem__(self, key):
        return self.__list[key[0]][key[1]]
    
    def __setitem__(self, key, value):
        self.__list[key[0]][key[1]] = value

    def __add__(self, other):
        res = Matrix(self.__list)
        for i in range(self.height):
            for j in range(self.width):
                res[i,j] = res[i,j] + other[i,j]
        return res

matrix1 = Matrix([[1,0,0], 
                  [0,1,0], 
                  [0,0,1]])

matrix2 = Matrix([[2,0,0], 
                  [0,2,0], 
                  [0,0,2]])

print(matrix1[1,1])
print(matrix1 + matrix2)