# Create a class 'employee' and add salary and increment properties to it. 
# Write a method 'salaryAtterincrement' method with a @ property decorator with a setter which changes the value of increment based on the salary.

class employee:
    salary = 234
    increment = 20
    @property
    def salaryAtterincrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryAtterincrement.setter
    def salaryAtterincrement(self, salary):
        self.increment = ((salary/self.salary) -1)*100
e = employee()    
# print(e.salaryAtterincrement)
e.salaryAtterincrement = 280.8
print(e.increment)