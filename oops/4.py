# Add a static method in problem 2, to greet the user with hello.

class Calculator:
    def __init__(self,side):
        self.side = side
    
    def square(self):
        print(self.side * self.side)

    def cube(self):
        print(self.side*self.side*self.side)
        
    def sqrt(self):
        print(self.side**(0.5))

    @staticmethod
    def greet():
        print("hi have a good day!!!")
    
num = Calculator(5)
num.square()
num.cube()
num.sqrt()
num.greet()