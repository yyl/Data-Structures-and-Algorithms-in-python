'''
Write a program to convert a postfix expression into an infix expression using a stack. One way to do this is to modify the RPN calculator program given in Program to use a stack of infix expressions. A binary operator should pop two strings from the stack and then push a string which is formed by concatenating the operator and its operands in the correct order. For example, suppose the operator is ``*'' and the two strings popped from the stack are "(b+c)" and "a". Then the result that gets pushed onto the stack is the string "a*(b+c)".
'''

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

