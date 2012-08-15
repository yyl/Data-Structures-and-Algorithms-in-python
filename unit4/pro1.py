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
  order_list.accept(m_visitor)
  m_visitor.current()
  order_list.accept(max_visitor)
  max_visitor.current()

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
    self.minimum = 9999999999

  def visit(self, obj):
    if obj < self.minimum:
      self.minimum = obj

  def current(self):
    print "current minimum value is:", self.minimum


# visitor to find minimum element
class MaxVisitor(Visitor):

  def __init__(self):
    self.maximum = -9999999999

  def visit(self, obj):
    if obj > self.maximum:
      self.maximum = obj

  def current(self):
    print "current maximum value is:", self.maximum

pro1()
