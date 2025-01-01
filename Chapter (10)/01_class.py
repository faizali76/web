class employee:
    language = "Py" # This is a class attribute
    salary = 120000


faiz = employee()
faiz.name = "faiz" # This is an instance attribute
print(faiz.name, faiz.language, faiz.salary)

faizan = employee()
faizan.name = "faizan"
print(faizan.name, faizan.language, faizan.salary)

# Here name is instance attribute and salary and language attributes as they directly belong to the class
