class Employee:
    a = 1

class Programeer(Employee):
    b = 2

class Manager(Programeer):
    c = 3

o = Employee()
print(o.a)

x = Programeer()
print(x.a,x.b)

y = Manager()
print(y.a, y.b, y.c)