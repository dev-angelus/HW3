class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self):
        print(f'Sum : {x.__add__(y)}')
    def __sub__(self):
        print(f'Subtraction :  {x.__sub__(y)}')
    def __mul__(self):
        print(f'Multiplication : {x.__mul__(y)}')
    def __truediv__(self):
        print(f'Division :  {x.__truediv__(y)}')

x = int(input("Enter first number : "))
y = int(input("Enter second number : "))
number = Calculator(x, y)

number.__add__()
number.__sub__()
number.__mul__()
number.__truediv__()