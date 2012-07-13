from exceptions import RuntimeError

class LinkedList(object):

  class Element(object):

    def __init__(self, list, value, next=None):
      self._list = list
      self._value = value
      self._next = next

    def getValue(self):
      return self._value

    value = property(
        fget = lambda self: self.getValue()
        )

    def getNext(self):
      return self._next

    next = property(
        fget = lambda self: self.getNext()
        )

    def insertAfter(self, item):
      elt = LinkedList.Element(self._list, item, self._next)
      self._next = elt
      if self == self._list._tail:
        self._list._tail = elt

    def insertBefore(self, item):
      elt = LinkedList.Element(self._list, item, self)
      if self._list._head == self:
        self._list._head = elt
      else:
        prev = self._list._head
        while prev._next != None and prev._next != self:
          prev = prev._next
        prev._next = elt

  # Linked list methods
  def __init__(self):
    self._head = None
    self._tail = None 

  def purge(self):
    self._head = None
    self._tail = None 

  def getHead(self):
    return self._head

  head = property(
      fget = lambda self: self.getHead()
      )

  def getTail(self):
    return self._tail

  tail = property(
      fget = lambda self: self.getTail()
      )

  def getIsEmpty(self):
    return self._head == None

  isEmpty = property(
      fget = lambda self: self.getIsEmpty()
      )

  # accessors for 1st and last list element
  def getFirst(self):
    if self._head == None:
      raise RuntimeError
    return self._head._value

  first = property(
      fget = lambda self: self.getFirst()
      )

  def getLast(self):
    if self._tail == None:
      raise RuntimeError
    return self._tail._value

  last = property(
      fget = lambda self: self.getLast()
      )

  def prepend(self, item):
    elt = self.Element(self, item, self._head)
    self._head = elt
    if self._tail == None:
      self._tail = elt

  def append(self, item):
    elt = self.Element(self, item, self._tail)
    if self._head != None:
      self._tail._next = elt
    else:
      self._head = elt
    self._tail = elt

  def __copy__(self):
    tmp = LinkedList()
    ptr = self._head
    while ptr != None:
        tmp.append(ptr._value)
        ptr = ptr._next
    return tmp

  def extract(self, value):
	ptr = self._head
	prev = None
	while ptr != None and ptr._value != value:
		prev = ptr
		ptr = ptr._next
	if ptr == None:
		raise KeyError
	if ptr == self._head:
		self._head = None
	else:
		prev._next = ptr._next
	if ptr == self._tail:
		self._tail = prev
