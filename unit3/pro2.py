'''
RPN Calculator
Modify Program  so that it accepts expressions written in prefix (Polish) notation
'''

from opus7.stackAsLinkedList import StackAsLinkedList

class Algorithms(object):

  def __init__(self):
    self.stack = StackAsLinkedList()

  def calculator(self, input, output):
    for line in input.readlines():
      # prefix is acrtually the reversed version of postfix
      line = line.split()
      operation = line[:-1]
      operation.reverse()
      operation.append(line[-1])
      for word in operation:
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
	'''
    def operating(a2, a1, word):
        print "operating: ", a2, a1, word
        if word == "+":
          print "it is +"
          return a2 + a1
        elif word == "*":
          print "it is *"
          return a2 * a1
        elif word == "-":
          print "it is -"
          return a2 - a1
        elif word == "/":
          print "it is /"
          return a2 / a1
        # exponential expression
        elif word == "^":
          print "it is ^"
          return a2 ** a1
        else:
          print "unrecognizable"
          # make it double
    operators = ["+", "-", "*", "/", "^"]
    for line in input.readlines():
      for word in line.split():
        if word in operators:
          print "push operator " + word
          self.stack.push(word)
        elif word == "=":
          arg = self.stack.pop()
          output.write(str(arg) + "\n")
          print "ans = ", arg
        else:
          print "push number " + word
          flag = 0
          if self.stack.getTop() not in operators:
            flag = 1
          self.stack.push(float(word))
          if flag == 1:
            arg2 = self.stack.pop()
            arg1 = self.stack.pop()
            oper = self.stack.pop()
            self.stack.push(operating(arg2, arg1, oper))
            print "push answer"
			'''
		
a = Algorithms()
a.calculator(open("input2.txt", 'r'), open("output.txt", 'w+'))

