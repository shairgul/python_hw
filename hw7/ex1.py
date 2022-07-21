class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        data = self.data
        s = ""
        for i in data:
            for j in i:
                s += str(j)
                s += " "
            s += '\n'
        return s

    def __add__(self, other):
        data = self.data
        s = ""
        for i in range(0, len(data)):
            for j in range(0, len(data[i])):
                a = data[i][j] + other.data[i][j]
                s += str(a)
                s += " "
            s += '\n'
        return s


matrix = Matrix([[3, 2], [2, 4], [1, 3]])
matrix2 = Matrix([[4, 1], [2, 3], [3, 4]])
print(matrix.__str__())
print(matrix2.__str__())
print(matrix.__add__(matrix2))
