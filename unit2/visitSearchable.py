#################
# unit2 project 2:
# Using visitors, devise an implementation for the __contains__ method and 
# the find method of the SearchableContainer class
#################

from opus7.searchableContainer import SearchableContainer
from opus7.visitor import Visitor
from opus7.iterator import Iterator

class VisitSearchable(SearchableContainer):

  ##########################
  # inherited from SeachableContainer class
  def __init__(self):
    self._list = []
    super(VisitSearchable, self).__init__()

  def insert(self, obj):
    assert obj not in self._list
    self._list.append(obj)

  def withdraw(self, obj):
    assert obj in self._list
    self._list.remove(obj)

  def __contains__(self, obj):
    if self.accept(self.myVisitor(obj)) == None:
      return False
    else:
      return True

  def find(self, obj):
    return self.accept(self.myVisitor(obj))

  def _compareTo(self, obj):
    pass

  def __copy__(self):
    tmp = VisitSearchable()
    tmp = self.accept(copyVisitor())
    self.purge()
    return tmp

  ###########################
  # inherited from Container class
  def accept(self, visitor):
    assert isinstance(visitor, Visitor)
    for obj in self._list:
      if visitor.isDone():
	    return
      visitor.visit(obj)
    else:
	  return None


  def purge(self):
    self._list = []

  def __iter__(self):
    return self
  
  ##########################
  # subclass of Visitor
  # use to implement __contains__ and find functions
  class myVisitor(Visitor):
    def __init__(self, target):
      self._target = target
      self._found = None

    def visit(self, obj):
      if obj == self._target:
        self._found = obj

    def isDone(self):
      return self._found != None
