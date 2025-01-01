class employee:
    language = "python" # This is a class attribute
    salary = 120000


faiz = employee()
faiz.language = "java" # This is an instance attribute
print(faiz.language, faiz.salary)