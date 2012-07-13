#################
# unit2 project 2:
# Using an iterator, devise an implementation for the __contains__ method and 
# the find method of the SearchableContainer class
#################


from opus7.searchableContainer import SearchableContainer
from opus7.visitor import Visitor
from opus7.iterator import Iterator

class mySearchable(SearchableContainer):

  ##########################
  # inherited from SeachableContainer class
  def __init__(self):
    self._list = []
    super(mySearchable, self).__init__()

  def insert(self, obj):
    assert obj not in self._list
    self._list.append(obj)

  def withdraw(self, obj):
    assert obj in self._list
    self._list.remove(obj)

  def __contains__(self, obj):
    i = iter(self)
    while True:
      try:
        d = i.next()
        if d == obj:
          return True
      except:
        break
    else:
      return False

  def find(self, obj):
    for elt in self:
      if elt == obj:
        return elt
    else:
      return None

  def _compareTo(self, obj):
	pass
	
  ###########################
  # inherited from Container class
  def purge(self):
    self._list = []

  def __iter__(self):
    return self.myIterator(self)

  ############################
  # subclass of Iterator
# # use to implement __iter__ function
  class myIterator(Iterator):
    def __init__(self, container):
      super(Iterator, self).__init__()
      self._count = 0
      self._container = container

    def __iter__(self):
      return self

    def next(self):
      if self._count >= len(self._container._list):
        raise StopIteration
      else:
        self._count += 1
        return self._container._list[self._count - 1]
