from opus7.tree import Tree

class treeLeafCount(Tree):

  def getLeafCount(self):
    if self.isEmpty:
      return 0
    result = 0
    for i in xrange(self.degree):
      if self.getSubtree(i).isLeaf:
        result += 1
      else:
        result += self.getSubtree(i).leafCount
    return result
