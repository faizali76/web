class employee():
    a = 1
    @classmethod
    def show(cls):
        print(f"The class value is a attribut:{cls.a}")
    
    @property 
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = employee()
e.a = 45

e.name = "faiz ali"
print(e.fname,e.lname)
e.show()