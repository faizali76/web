class employee:
    language = "python" # This is a class attribute
    salary = 120000
    def __init__(self,name, salary,language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print(" I am creating an object ")



    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    @staticmethod  
    def greet():
        print("good morning")





faiz = employee("faiz",130000,"js")

# faiz.name = "faiz"
print(faiz.name, faiz.salary, faiz.language)





