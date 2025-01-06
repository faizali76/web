class employee():
    a = 1
    @classmethod
    def show(cls):
        print(f"The class value is a attribut:{cls.a}")

e = employee()
e.a = 45
e.show()