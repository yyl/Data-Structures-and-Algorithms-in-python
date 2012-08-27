from opus7.tree import Tree

class treeHeight(Tree):

  def getHeight(self):
    if self.isEmpty:
      return -1
    degree = self.degree
    return 1 + max([self.getSubtree(i).height for i in xrange(degree) if self.getSubtree(i)])
