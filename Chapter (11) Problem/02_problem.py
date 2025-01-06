# Create a class 'pets' from a class 'Dog' from 'pets'. Add a method 'bark' to class 'dog'.
class animals:
    pass


class pets(animals):
    pass

class dog(pets):
    @staticmethod
    def bark():
        print("bow bow!")

d = dog()
d.bark()