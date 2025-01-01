# Create a class program for storing information of few programmers working at microsoft.

class programmer:
    company = "microsoft"

    def __init__(self , name , salary , pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode


programmer1 = programmer("faiz", 763394 , 846004)
print(programmer1.name, programmer1.salary, programmer1.pincode, programmer1.company)

programmer2 = programmer("faizan", 763395 , 846004)
print(programmer2.name, programmer2.salary, programmer2.pincode, programmer2.company)
