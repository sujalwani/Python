class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programeer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2

class Manager(Programeer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 3

o = Employee()
print(o.a)

x = Programeer()
print(x.a,x.b)

y = Manager()
print(y.a, y.b, y.c)