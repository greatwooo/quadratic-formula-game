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
            if complex(pos_answer).real + complex(pos_answer).imag == self.get_pos().real + self.get_pos().imag and complex(neg_answer).real + complex(neg_answer).imag == self.get_neg().real + self.get_neg().imag:
                global correct
                correct += 1
                return correct
            else:
                global wrong
                wrong += 1
                return wrong

            
#problems
problem1 = Quadratic_Formula(1,2,3)
problem2 = Quadratic_Formula(3,2,1)
#problem3 = Quadratic_Formula()
print(problem1.get_pos())
print(problem1.get_neg())




answer1_pos = input('What is the + x int of problem 1:')
answer1_neg = input('What is the - x int of problem 1:')
problem1.answer_check(answer1_pos, answer1_neg)


print('Correct', correct, ':', 'Wrong', wrong)

#problem 2
print(problem2.get_pos())
print(problem2.get_neg())




answer2_pos = input('What is the + x int of problem 1:')
answer2_neg = input('What is the - x int of problem 1:')
problem2.answer_check(answer2_pos, answer2_neg)


print('Correct', correct, ':', 'Wrong', wrong)








