'''
RPN Calculator
'''

from opus7.stackAsLinkedList import StackAsLinkedList

class Algorithms(object):

  def __init__(self):
    self.stack = StackAsLinkedList()

  def calculator(self, input, output):
    for line in input.readlines():
      for word in line.split():
        if word == "+":
          print "it is +"
          arg2 = self.stack.pop()
          arg1 = self.stack.pop()
          self.stack.push(arg1 + arg2)
        elif word == "*":
          print "it is *"
          arg2 = self.stack.pop()
          arg1 = self.stack.pop()
          self.stack.push(arg1 * arg2)
        elif word == "-":
          print "it is -"
          arg2 = self.stack.pop()
          arg1 = self.stack.pop()
          self.stack.push(arg1 - arg2)
        elif word == "/":
          print "it is /"
          arg2 = self.stack.pop()
          arg1 = self.stack.pop()
          self.stack.push(arg1 / arg2)
        # exponential expression
        elif word == "^":
          print "it is ^"
          arg2 = self.stack.pop()
          arg1 = self.stack.pop()
          self.stack.push(arg1 ** arg2)
        elif word == "=":
          print "it is ="
          arg = self.stack.pop()
          output.write(str(arg) + "\n")
          print "ans is ", arg
        else:
          print "it is number"
          # make it double
          self.stack.push(float(word))

  # remove all by calling purge method of linked list
  def clear(self):
    self.stack.purge()

  # use the iterator of linked list to access every remaining element
  def printall(self):
    for ele in self.stack:
      print ele

a = Algorithms()
a.calculator(open("input.txt", 'r'), open("output.txt", 'w+'))
a.printall()
a.clear()
print "print all again"
a.printall()
