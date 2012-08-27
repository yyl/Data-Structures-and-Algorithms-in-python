from opus7.tree import Tree

class treeCompare(Tree):

  def _compareTo(self, obj):
    assert isInstance(self, obj.__class__)
    if self.isEmpty:
      if obj.isEmpty:
        return 0
      else:
        return -1
    elif obj.isEmpty:
      return 1
    else:
      result = cmp(self._key, obj._key)
      i = 0
      while result == 0 and i < self.degree:
        result = cmp(self.getSubtree(i), obj.getSubtree(i))
        i += 1
      return result

