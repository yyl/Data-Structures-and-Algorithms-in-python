'''
Devise a scheme using a stack to convert an infix expression to a postfix expression. Hint: In a postfix expression operators appear after their operands whereas in an infix expression they appear between their operands. Process the symbols in the prefix expression one-by-one. Output operands immediately, but save the operators in a stack until they are needed. Pay special attention to the precedence of the operators.

NOTE: only works without paranthesis
'''


from opus7.stackAsLinkedList import StackAsLinkedList

class Algorithms(object):

  def __init__(self):
    self.stack = StackAsLinkedList()

  def calculator(self, input, output):
    operators = ["+", "-"]
    priors = ["*", "/"]
    for line in input.readlines():
      flag = 0
      size = 0
      for word in line.split():
        '''
        match_left = re.search(r'\(', word)
        match_right = re.search(r'\)', word)
        if match_left:
          self.stack.push(word[1:])
          flag = 1
        if match_right:
          self.stack.push(word[:-1])
          '''
        if word in operators:
          print "it is an operator: ", word
          while size >= 3:
            arg2 = self.stack.pop()
            op = self.stack.pop()
            arg1 = self.stack.pop()
            size -= 3
            self.stack.push("%s %s %s" % (arg1, arg2, op))
            size += 1
            print "push ", arg1, arg2, op
          self.stack.push(word)
          print "pushing ", word
          size += 1
          flag = 0
        elif word in priors:
          print "it is a prior: ", word
          # indicating there are a pair of arg1 * arg2 in stack
          # waiting for poping out
          if flag == 1 and size >= 3:
            arg2 = self.stack.pop()
            op = self.stack.pop()
            arg1 = self.stack.pop()
            size -= 3
            self.stack.push("%s %s %s" % (arg1, arg2, op))
            size += 1
            print "push ", arg1, arg2, op
          # push the operator itself
          self.stack.push(word)
          print "pushing ", word
          size += 1
          flag = 1
        elif word == "=":
          print "it is ="
          while size >= 3:
            arg2 = self.stack.pop()
            op = self.stack.pop()
            arg1 = self.stack.pop()
            size -= 3
            self.stack.push("%s %s %s" % (arg1, arg2, op))
            size += 1
            print "push ", arg1, arg2, op
          output.write("%s %s %s = \n" % (arg1, arg2, op))
          print "writing into files", arg1, arg2, op
        else:
          print "it is number: ", word
          self.stack.push(word)
          print "pushing ", word
          size += 1



a = Algorithms()
a.calculator(open("infix_input.txt", 'r'), open("output.txt", 'w+'))


