import math

class Quadratic_Formula:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def Formula(self, a, b, c):
        plus = (-b+(b**2-(4*a*c))**.5)/(2*a)
        minus = (-b-(b**2-(4*a*c))**.5)/(2*a)
        return plus, minus
test = Quadratic_Formula(1,2,3)
print(-1**.5)





