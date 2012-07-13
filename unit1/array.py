from exceptions import IndexError
# fixed-size array
class Array(object):

  # baseIndex is for the lower bound of the array
  def __init__(self, length = 0, baseIndex = 0):
    assert length >= 0
    self._data = [None for i in xrange(length)]
    self._baseIndex = baseIndex

  def __copy__(self):
    tmp = Array(len(self._data))
    for i, datum in enumerate(self._data):
      tmp._data[i] = datum
    tmp._baseIndex = self._baseIndex
    return tmp

  # get the correct offset from the index input
  # return IndexError if the index is out of range
  def getOffset(self, index):
    offset = index - self._baseIndex
    if offset >= 0 and offset < len(self._data):
      return offset
    else:
      raise IndexError

  def __getitem__(self, index):
    return self._data[self.getOffset(index)]

  def __setitem__(self, index, value):
    self._data[self.getOffset(index)] = value

  def getData(self):
    return self._data

  data = property(
      fget = lambda self: self.getData()
      )

  def getBaseIndex(self):
    return self._baseIndex

  def setBaseIndex(self, baseIndex):
    self._baseIndex = baseIndex

  baseIndex = property(
      fget = lambda self: self.getBaseIndex(),
      fset = lambda self, value: self.setBaseIndex(value)
      )

  def __len__(self):
    return len(self._data)

  def setLength(self, value):
    if value > len(self._data):
      for i in xrange(value - len(self._data)):
        self._data.append(None)
    else:
      tmp = [None for i in xrange(value)]
      self._data = tmp
        
  length = property(
      fget = lambda self: self.__len__(),
      fset = lambda self, value: self.setLength(value)
      )
