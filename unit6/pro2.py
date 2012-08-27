from opus7.tree import Tree

class treeCount(Tree):
  def getCount(self):
    if self.isEmpty:
      return 0
    return sum([self.getSubtree(i).count for i in xrange(self.degree)])
