import sys
from opus7.container import Container
from opus7.exception import *


class DoublyLinkedList(object):
  def __init__(self):
    self._head = None
    self._tail = None

  class Element(object):
    def __init__(self, prev, value, next, thelist):
      self._prev = prev
      self._next = next
      self._value = value
      self._thelist = thelist

    def getPrev(self):
      return self._prev

    def getNext(self):
      return self._next

    def getValue(self):
      return self._value

    prev = property(
        fget = lambda self: self.getPrev())
    next = property(
        fget = lambda self: self.getNext())
    value = property(
        fget = lambda self: self.getValue())

    def insertAfter(self, obj):
      pass

    def insertBefore(self, obj):
      pass

  def getHead(self):
    return self._head

  def getTail(self):
    return self._tail

  head = property(
      fget = lambda self: self.getHead())

  tail = property(
      fget = lambda self: self.getTail())

  def getFirst(self):
    if self._head == None:
      raise ContainerEmpty
    return self._head

  def getLast(self):
    if self._tail == None:
      raise ContainerEmpty
    return self._tail

  first = property(
      fget = lambda self: self.getFirst())

  last = property(
      fget = lambda self: self.getLast())

  def append(self, obj):
    tmp = self.Element(self._tail, obj, None, self)
    if self._head == None or self._tail == None:
      self._head = tmp
      self._tail = tmp
    else:
      self._tail._next = tmp
      self._tail = tmp

  def prepend(self, obj):
    tmp = self.Element(None, obj, self._head, self)
    if self._head == None:
      self._head = tmp
      self._tail = tmp
    else:
      self._head._prev = tmp
      self._head = tmp

  def purge(self):
    self._head = None
    self._tail = None

  def extract(self, obj):
    tmp = self._head
    prev = tmp
    while tmp != None:
      if tmp._value == obj:
        if tmp == self._head:
          tmp._next._prev = None
          self._head = tmp._next
        elif tmp == self._tail:
          tmp._prev = None
          prev._next = None
          self._tail = prev
        else:
          prev._next = tmp._next
          tmp._prev = None
          tmp._next._prev = prev
          tmp._next = None
        return obj
      prev = tmp
      tmp = tmp._next
    return None

  def __copy__(self):
    tmp = DoublyLinkedList()
    current = self._head
    while current != None:
      tmp.append(current.value)
      current = current._next
    return tmp
