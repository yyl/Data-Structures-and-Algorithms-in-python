
#2nd type of linkedlist
#only a head pointer, no tail pointer; the next of the last element points to null

class LinkedList(object):

  class Element(object):
    
    def __init__(self, list, value, next=None):
      self._list = list
      self._value = value
      self._next = next

    def getNext(self):
      return self._next

    next = property(
        fget = lambda self: self.getNext()
        )

    def getValue(self):
      return self._value

    value = property(
        fget = lambda self: self.getValue()
        )

    def insertAfter(self, value):
      e = LinkedList.Element(self._list, value, self._next)
      self._next = e

    def insertBefore(self, value):
      e = LinkedList.Element(self._list, value, self)
      if self is self._list._head:
        self._list._head = e
      else:
        start = self._list._head
        while start != None and start._next is not self:
            start = start._next
        start._next = e

  def __init__(self):
    self._head = None

  def getIsEmpty(self):
    return self._head == None

  isEmpty = property(
      fget = lambda self: self.getIsEmpty()
      )

  def getHead(self):
    return self._head

  head = property(
      fget = lambda self: self.getHead()
      )

  def prepend(self, value):
    e = self.Element(self, value, self._head)
    self._head = e

  def append(self, value):
    e = self.Element(self, value)
    if self._head == None:
      self._head = e
    else:
      start = self._head
      while start._next != None:
        start = start._next
      start._next = e

  def purge(self):
    self._head = None

  def getFirst(self):
    return self._head

  def getLast(self):
    if self._head == None:
      return None
    else:
      start = self._head
      while start._next != None:
        start = start._next
      return start

  first = property(
      fget = lambda self: self.getFirst()
      )

  last = property(
      fget = lambda self: self.getLast()
      )

  def __copy__(self):
    tmp = LinkedList()
    start = self._head
    while start != None:
      tmp.append(start._value)
      start = start._next
    return tmp
      
  def extract(self, value):
    start = self._head
    if start == None:
      raise KeyError
    else:
      prev = start
      if start._value == value:
        self._head = start._next
        return value
      else:
        start = start._next
        while start != None:
          if start._value == value:
            prev._next = start._next
            return value
          prev = start
          start = start._next
        else:
          raise KeyError
