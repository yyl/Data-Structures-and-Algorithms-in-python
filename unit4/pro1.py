'''
Write a visitor to solve each of the following problems:
  1. Find the smallest element of a list.
  2. Find the largest element of a list.
  3. Compute the sum of all the elements of a list.
  4. Compute the product of all the elements of a list.
'''

from opus7.orderedListAsArray import OrderedListAsArray
from opus7.visitor import Visitor

def pro1():
  order_list = OrderedListAsArray(10)
  m_visitor = MinimumVisitor()
  order_list.insert(42)
  order_list.insert(21)
  order_list.insert(41)
  order_list.insert(13)
  order_list.insert(94)
  order_list.insert(34)
  order_list.accept(m_visitor)
  m_visitor.current()

class MinimumVisitor(Visitor):

  def __init__(self):
    self.minimum = 9999999999

  def visit(self, obj):
    if obj < self.minimum:
      self.minimum = obj

  def current(self):
    print "current minimum value is:", self.minimum


pro1()
