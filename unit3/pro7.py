'''
Design and implement a MultipleStack class which provides   stacks in a single container.
'''

from opus7.stackAsLinkedList import StackAsLinkedList
from opus7.container import Container

class MultipleStack(Container):
  def __init__(self, numOfStack):
    self.stacks = [StackAsLinkedList() for i in range(numOfStack)]

  # for Container class
  def purge(self):
    for stack in self.stacks:
      stack.purge()

  def __iter__(self):
    return iter(self.stacks)

  # which indicates the stack, from 1 to len(stacks)
  def push(self, obj, which):
    assert which > 0 and which <= len(self.stacks)
    self.stacks[which - 1].push(obj)

  def pop(self, which):
    assert which > 0 and which <= len(self.stacks)
    return self.stacks[which - 1].pop()

  def getTop(self, which):
    assert which > 0 and which <= len(self.stacks)
    return self.stacks[which - 1].getTop()

  def _compareTo(self, obj):
    assert isinstance(self, obj.__class__)
    return len(self.stacks) > len(obj.stacks)

ms = MultipleStack(5)
for i in range(1, 6):
  ms.push(i, i)
  ms.push(i+1, i)
  ms.push(i+2, i)

i = iter(ms)
while True:
  print i.next()

for i in range(1, 6):
  print ms.pop(i)
  print ms.pop(i)
  print ms.pop(i)

