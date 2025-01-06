class employee:
    def __init__(self):
        print("constructor of employee")
    a = 1

class programmer(employee):
    def __init__(self):
        print("constructor of programmer")
    b = 2

class maneger(programmer):
    def __init__(self):
        super().__init__()
        print("constructor of maneger")
    c = 3

o = employee()
print(o.a)
#  print(o.b)

o = programmer()
print(o.a, o.b)

o = maneger()
print(o.a, o.b, o.c)