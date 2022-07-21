class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return self.count+other.count

    def __sub__(self, other):
        return self.count - other.count

    def __mul__(self, other):
        return self.count * other.count

    def __truediv__(self, other):
        return self.count // other.count

    def make_order(self, param):
        s = ''
        for i in range(1,self.count+1):
            s+="*"
            if i%param==0:
                s+='\\n'
        return s

cell = Cell(24)
cell2 = Cell(16)
print(cell+cell2)
print(cell-cell2)
print(cell*cell2)
print(cell/cell2)
print(cell.make_order(6))
print(cell2.make_order(6))