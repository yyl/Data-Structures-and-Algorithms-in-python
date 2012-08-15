'''
Write a visitor to solve each of the following problems:
  1. Find the smallest element of a list.
  2. Find the largest element of a list.
  3. Compute the sum of all the elements of a list.
  4. Compute the product of all the elements of a list.
'''

from opus7.orderedListAsArray import OrderedListAsArray
from opus7.visitor import Visitor
from random import random

def pro1():
  order_list = RandomList(10)
  order_list.generate()
  print order_list
  m_visitor = MinimumVisitor()
  max_visitor = MaxVisitor()
  sum_visitor = SumVisitor()
  product_visitor = ProductVisitor()
  order_list.accept(m_visitor)
  order_list.accept(max_visitor)
  order_list.accept(sum_visitor)
  order_list.accept(product_visitor)
  print "smallest one:", m_visitor.minimum
  print "biggest one:", max_visitor.maximum
  print "sum of the list:", sum_visitor.sum
  print "product of the list:", product_visitor.product

# subclass of OrderedListAsArray, has the method to randomly generate elements
class RandomList(OrderedListAsArray):

  # based on the length of array, randomly generate, <100
  def generate(self):
    self.purge()
    size = len(self._array)
    for i in range(size):
      value = int(random() * 100)
      self.insert(value)

# visitor to find minimum element
class MinimumVisitor(Visitor):

  def __init__(self):
    self._minimum = 9999999999

  def visit(self, obj):
    if obj < self._minimum:
      self._minimum = obj

  def getMin(self):
    return self._minimum

  minimum = property(
      fget = lambda self: self.getMin())


# visitor to find minimum element
class MaxVisitor(Visitor):

  def __init__(self):
    self._maximum = -9999999999

  def visit(self, obj):
    if obj > self._maximum:
      self._maximum = obj

  def getMax(self):
    return self._maximum

  maximum = property(
      fget = lambda self: self.getMax())

class SumVisitor(Visitor):

  def __init__(self):
    self._sum = 0

  def visit(self, obj):
    self._sum += obj

  def getSum(self):
    return self._sum

  sum = property(
      fget = lambda self: self.getSum())

class ProductVisitor(Visitor):

  def __init__(self):
    self._product = 1

  def visit(self, obj):
    self._product *= obj

  def getProduct(self):
    return self._product

  product = property(
      fget = lambda self: self.getProduct())

pro1()
