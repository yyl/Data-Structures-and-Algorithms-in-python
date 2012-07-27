from opus7.stackAsLinkedList import StackAsLinkedList

class Algorithms(object):

  def __init__(self):
    self.stack = StackAsLinkedList()

  def calculator(self, input, output):
    operators = ["+", "-", "*", "/", "^"]
    for line in input.readlines():
      for word in line.split():
        if word in operators:
          print "it is operator ", word
          arg2 = self.stack.pop()
          arg1 = self.stack.pop()
          self.stack.push("(%s %s %s)" % (arg1, word, arg2))
        elif word == "=":
          print "it is ="
          arg = self.stack.pop()
          output.write(arg + " = " + "\n")
          print "ans is ", arg
        else:
          print "it is number, push it"
          # make it double
          self.stack.push(word)


a = Algorithms()
a.calculator(open("input.txt", 'r'), open("output.txt", 'w+'))

