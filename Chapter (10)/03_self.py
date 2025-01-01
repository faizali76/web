class employee:
    language = "python" # This is a class attribute
    salary = 120000

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    # @staticmethod  # @staticmethod lekh deya hun as a function jo ki self nahi lega ki es ke ander object ka koi bhi property kuch bhi nahi chaiye    
    def greet(slef):
        print("good morning")

faiz = employee()
faiz.language = "java" # This is an instance attribute
faiz.getinfo()
faiz.greet()
# employee.getinfo(faiz)