'''
Consider the Polynomial class given in Program . Implement a method that computes the value of a polynomial, say p(x), for a given value of x. Hint: Use a visitor that visits all the terms in the polynomial and accumulates the result.
'''

from opus7.polynomialAsOrderedList import PolynomialAsOrderedList
from opus7.visitor import Visitor

class MyPoly(PolynomialAsOrderedList):

  def poly(self, x):
    poly_visitor = PolyVisitor(x)
    self.accept(poly_visitor)
    return poly_visitor.sum

  
class PolyVisitor(Visitor):

  def __init__(self, x):
    self._x = x 
    self._sum = 0

  def visit(self, obj):
    self._sum += obj.coefficient * self._x ** obj.exponent

  def getSum(self):
    return self._sum

  sum = property(
      fget = lambda self: self.getSum())

my_poly = MyPoly()
# test polynomial 1 + 2x + x^2
term1 = MyPoly.Term(1, 0)
term2 = MyPoly.Term(2, 1)
term3 = MyPoly.Term(1, 2)
my_poly.addTerm(term1)
my_poly.addTerm(term2)
my_poly.addTerm(term3)
print my_poly.poly(6)
