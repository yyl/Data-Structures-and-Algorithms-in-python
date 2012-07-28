'''
Design and implement a class called DequeAsDoublyLinkedList that implements the Deque interface using a doubly-linked list. Select one of the approaches shown in Figure .
'''

from doublyLinkedList import DoublyLinkedList
from opus7.container import Container

class Deque(Container):
  def __init__(self):
    self._list = DoublyLinkedList()

  def getHead(self):
    return self._list.head
  def getTail(self):
    return self._list.tail

  head = property(
      fget = lambda self: self.getHead())
  tail = property(
      fget = lambda self: self.getTail())

  def enqueueHead(self, obj):
    self._list.prepend(obj)

  def dequeueHead(self):
    assert not self._list.isEmpty
    return self._list.extract(self._list.head.value)

  def enqueueTail(self, obj):
    self._list.append(obj)

  def dequeueTail(self):
    assert not self._list.isEmpty
    return self._list.extract(self._list.tail.value)

  def __iter__(self):
    pass

  def _compareTo(self, obj):
    pass

  def purge(self):
    self._list.purge()

  #override
  def getIsEmpty(self):
    return self._list.isEmpty
