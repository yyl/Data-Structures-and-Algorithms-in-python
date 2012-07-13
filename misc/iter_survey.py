class IterTest(object):
  def __init__(self, data):
    self._data = data
    self._count = 0

  def __iter__(self):
    return self

  def next(self):
    if self._count == len(self._data):
      raise StopIteration
    else:
      output = self._data[self._count]
      self._count += 1
      return output

class GenTest(object):
  def __init__(self, data):
    self._data = data

  def gen(self):
    count = 0
    while count < len(self._data):
      count += 1
      yield self._data[count - 1]

class IterableTest(object):
  def __init__(self, data):
    self._data = data

  def __iter__(self):
    return self.iterall()

  def iterall(self):
    count = 0
    while count < len(self._data):
      count += 1
      yield self._data[count - 1]



if __name__ == '__main__':
  L = [1,2,3,4,5]
  i = iter(L)
  print i
  D = {'a':1, 'b':2, 'c':3}
  print D.iteritems()
  print D.iterkeys()
  print D.itervalues()
  for li in i:
    print li
  d = GenTest([1,2,3,4,5])
  g = d.gen()
  print g
  print g.next()
  for dat in g:
    print dat
  g2 = d.gen()
  print g2.next()
  d2 = IterTest("abcd")
  I = iter(d2)
  print I
  for char in I:
    print char
  d3 = IterableTest([4,3,2,1])
  I2 = iter(d3)
  print I2
  for dat in I2:
    print dat
  print d3
  for dat in d3:
    print dat
  for dat in d3:
    print dat
