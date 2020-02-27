#Author: Simon Parris
import disassembler

class Rational:
    #No self parameter used for gcd function
    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)
    
    #Variables n and d stand for numerator and denominator
    def __init__(self, n, d):
        self.n = n//gcd(n, d)
        self.d = d//gcd(n, d)
    
    def __add__(self, other):
        return Rational((self.getNumerator()* other.getDenominator() + other.getNumerator()* self.getDenominator()), (self.getDenominator()* other.getDenominator()))
    
    def getNumerator(self):
        return self.numerator
    
    def getDenominator(self):
        return self.denominator

    def __mul__(self, other):
        return Rational(self.getNumerator()*other.getNumerator(), self.getDenominator()*other.getDenominator())
    
    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)    
        
def main():
    x = Rational(1,2)
    y = Rational(2,3)
    print(x+y)
    print(x*y)
disassembler.disassemble(Rational)
disassembler.disassemble(main)