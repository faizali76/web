# class father:
#     a = 1

# class mother(father):
#     b = 2

# class child(mother):
#     c = 3

# o = father()
# print(o.a)
# #  print(o.b)

# o = mother()
# print(o.a, o.b)

# o = child()
# print(o.a, o.b, o.c)

class father:
    def __init__(self, father_name):# Father ka naam lene wala function
        self.father_name = father_name

    def show_father(self): # Father ka naam dikhane wala function
        print(f"Father's Name: {self.father_name}")


# Parent class (Beech wali class)
class mother(father):# Mother class Father se inherit kar rahi hai
    def __init__(self, father_name, mother_name):
        super().__init__(father_name)  # (super()ka kaaam refer karna constructor ko call karna hota hai) Father ka constructor call kiya
        self.mother_name = mother_name

    def show_mother(self):
        print(f"Mother's Name: {self.mother_name}")

# Child class (Sabse chhoti class)
 
class child(mother):  # Child class Mother se inherit kar rahi hai
    def __init__(self, father_name, mother_name, child_name):
        super().__init__(father_name, mother_name) # Father ka __init__ call kiya
        self.child_name = child_name

    def show_child(self):# Child ka naam dikhane wala function
        print(f"Child's Name: {self.child_name}")

        
# Ab ek Child object banate hain
child = child("Ramesh", "sita", "Rahul")


# Sab ke naam dikhate hain
child.show_father()  # Father ka naam dikhaya
child.show_mother()  # Mother ka naam dikhaya
child.show_child()   # Child ka naam dikhaya