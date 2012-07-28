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

  def __iter__(self):
    pass

  def _compareTo(self, obj):
    pass

  def purge(self):
    pass
