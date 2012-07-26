'''
RPN Calculator
'''

from opus7.stackAsLinkedList import StackAsLinkedList

class Algorithms(object):

  @staticmethod
  def calculator(input, output):
    stack = StackAsLinkedList()
    for line in input.readlines():
      for word in line.split():
        if word == "+":
          print "it is +"
          arg2 = stack.pop()
          arg1 = stack.pop()
          stack.push(arg1 + arg2)
        elif word == "*":
          print "it is *"
          arg2 = stack.pop()
          arg1 = stack.pop()
          stack.push(arg1 * arg2)
        elif word == "-":
          print "it is -"
          arg2 = stack.pop()
          arg1 = stack.pop()
          stack.push(arg1 - arg2)
        elif word == "/":
          print "it is /"
          arg2 = stack.pop()
          arg1 = stack.pop()
          stack.push(arg1 / arg2)
        # exponential expression
        elif word == "^":
          print "it is ^"
          arg2 = stack.pop()
          arg1 = stack.pop()
          stack.push(arg1 ** arg2)
        elif word == "=":
          print "it is ="
          arg = stack.pop()
          output.write(str(arg) + "\n")
          print "ans is ", arg
        else:
          print "it is number"
          # make it double
          stack.push(float(word))


Algorithms.calculator(open("input.txt", 'r'), open("output.txt", 'w+'))
