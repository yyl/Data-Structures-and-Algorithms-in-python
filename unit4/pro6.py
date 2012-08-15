'''
For some calculations it is necessary to have very large integers, i.e., integers with an arbitrarily large number of digits. We can represent such integers using lists. Design and implement a class for representing arbitrarily large integers. Your implementation should include operations to add, subtract, and multiply such integers, and to compute the   power of such an integer, where k is a small positive integer. Hint: Base your design on the Polynomial class given in Program .
'''

from opus7.polynomialAsOrderedList import PolynomialAsOrderedList
from opus7.visitor import Visitor
from opus7.linkedList import LinkedList

class LargeInt(PolynomialAsOrderedList):

  def __add__(self, poly):
    result = LargeInt()
    p1 = iter(self._list)
    p2 = iter(poly._list)
    term1 = self.nextTerm(p1)
    term2 = self.nextTerm(p2)
    carry = 0
    while term1 is not None and term2 is not None:
      temp = term1 + term2 + carry
      carry = temp/10
      temp %= 10
      print "adding %d to %d, get %d and %d as carry" % (term1, term2, temp, carry)
      result.addTerm(temp)
      term1 = self.nextTerm(p1)
      term2 = self.nextTerm(p2)
    while term1 is not None:
      print "entering only term1"
      term1 += carry
      carry = term1/10
      term1 %= 10
      print "adding %d and %d as carry" % (term1, carry)
      result.addTerm(term1)
      term1 = self.nextTerm(p1)
    while term2 is not None:
      print "entering only term2"
      term2 += carry
      carry = term2/10
      term2 %= 10
      print "adding %d and %d as carry" % (term2, carry)
      result.addTerm(term2)
      term2 = self.nextTerm(p2)
    if carry != 0:
      print "adding extra carry", carry
      result.addTerm(carry)
    return result

  def nextTerm(self, iter):
    """
    (PolynomialAsSortedList, Iterator) -> Polynomial.Term
    Returns the next term or None if there are no more terms.
    """
    try:
      return iter.next()
    except StopIteration:
      return None

  def generateInt(self, *ints):
    for i in reversed(ints):
      self.addTerm(i)

  def __str__(self):
    r = self.ReverseVisitor()
    self.accept(r)
    return str(r.list)

  class ReverseVisitor(Visitor):
    def __init__(self):
      self._list = LinkedList()

    def visit(self, obj):
      self._list.prepend(obj)

    def getList(self):
      return self._list

    list = property(
        fget = lambda self: self.getList())

def pro6():
  p1 = LargeInt()
  p1.generateInt(1, 9, 9)
  p2 = LargeInt()
  p2.generateInt(9,9)
  result = p1 + p2
  print p1, " + ", p2, " = ", result

pro6()
