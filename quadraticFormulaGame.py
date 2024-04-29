import math
import cmath
correct = 0
wrong = 0
class Quadratic_Formula:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def get_pos(self):
        return (-self.b+cmath.sqrt(self.b**2-(4*self.a*self.c)))/(2*self.a)

    def get_neg(self):
        return (-self.b-cmath.sqrt(self.b**2-(4*self.a*self.c)))/(2*self.a)
    
    def answer_check(self,pos_answer, neg_answer):
        if pos_answer == self.get_pos() + .99 or self.get_pos() - .99:
            correct += 1
            return correct
        else:
            wrong -= 1
            return wrong

#problems
problem1 = Quadratic_Formula(1,2,3)
#problem2 = Quadratic_Formula()
#problem3 = Quadratic_Formula()
print(problem1.get_pos())
print(problem1.get_neg())

answer1_pos = input('What is the + x int of problem 1:')
answer1_neg = input('What is the - x int of problem 1:')

print(correct, wrong)








