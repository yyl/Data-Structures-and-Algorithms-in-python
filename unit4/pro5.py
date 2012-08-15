'''
Devise and implement an algorithm to compute the   power of a polynomial, where k is a positive integer. What is the running time of your algorithm?
'''

from pro4 import MultiplyPolynomial

class PowerPolynomial(MultiplyPolynomial):
  def __mul__(self, poly):
    return MultiplyPolynomial.__mul__(self, poly)

  def expo(self, ex):
    result = self
    print type(result)
    print type(self)
    for i in range(ex-1):
      result = result * self

    return result

def powerPoly(poly, exp):
  if exp == 0:
    result = MultiplyPolynomial()
    result.addTerm(MultiplyPolynomial.Term(1,0))
    return result
  result = poly
  for i in range(exp-1):
    result *= poly

  return result

def pro5():
  print "===pro5==="
  m = MultiplyPolynomial()
  m.addTerm(MultiplyPolynomial.Term(1,0))
  m.addTerm(MultiplyPolynomial.Term(1,1))
  print powerPoly(m, 3)

pro5()
