from opus7.stackAsLinkedList import StackAsLinkedList

class Algorithms(object):
  def __init__(self):
    self.stack = StackAsLinkedList()

  def isBalanced(self, input, output):
    dic = {"]":"[", "}":"{", ")":"("}

    for line in input.readlines():
      for word in line:
        if word in dic.values():
          self.stack.push(word)
          result = False
        elif word in dic.keys():
          if self.stack.getTop() == dic[word]:
            self.stack.pop()
            result = True
          else:
            self.stack.push(word)
            result = False
      output.write(str(result) + "\n")


a = Algorithms()
a.isBalanced(open("balancing.txt", "r"), open("output.txt", "w+"))

