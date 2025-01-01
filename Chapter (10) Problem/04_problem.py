# Add a static method in problem 2 to greet the user with hello.
class calculator:
    def __init__(self, n):
        self.n = n
 
    def square(self):
        print(f"This is sruare{self.n * self.n}")
         
         
    def cube(self):
        print(f"This is cube{ self.n * self.n * self.n}")
    
    
    def squareroot(self):
        print(f"thi is sruareroot{self.n ** 0.5}")


    @staticmethod
    def hello():
        print("hello There!")


a = calculator(4)
a.square()
a.cube()
a.squareroot()
a.hello()