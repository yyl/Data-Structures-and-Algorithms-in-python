from opus7.object import Object

class Bool(Object):
  def __init__(self, val=False):
    assert val in [True, False]
    self._val = val

  def _compareTo(self, obj):
    return self._val == obj._val

  def getVal(self):
    return self._val

  val = property(
      fget = lambda self: self.getVal()
      )

