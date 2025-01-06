class employee:

    company = "ITC"
    name = "faiz"
    salary = 50000

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


# class programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")


#     def showlanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language}language")

class programmer(employee):
    company = "ITC Infotech"
    language = "python"
    
    def showlanguage(self):
        print(f"The name is {self.name} and he is good with {self.language}language")
        
        
a = employee()
b = programmer()
print(a.company, b.company)

a.show()
b.show()
b.showlanguage()