# Write a class “Calculator” capable of finding square, cube and square root of a number. 

class Calculator:
    def __init__(self,side):
        self.side = side
    
    def square(self):
        print(self.side * self.side)

    def cube(self):
        print(self.side*self.side*self.side)
        
    def sqrt(self):
        print(self.side**(0.5))
    
num = Calculator(5)
num.square()
num.cube()
num.sqrt()
    