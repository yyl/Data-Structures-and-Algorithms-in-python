from opus7.polynomialAsSortedList import PolynomialAsSortedList

class MultiplyPolynomial(PolynomialAsSortedList):

  def __mul__(self, poly):
    result = MultiplyPolynomial()
    p1 = iter(self._list)
    term1 = self.nextTerm(p1)
    while term1 is not None: 
      p2 = iter(poly._list)
      term2 = self.nextTerm(p2)
      temp_poly = MultiplyPolynomial()
      while term2 is not None:
        exponent = term1.exponent + term2.exponent
        coefficient = term1.coefficient * term2.coefficient
        tmp = self.Term(coefficient, exponent)
        temp_poly.addTerm(tmp)
        term2 = self.nextTerm(p2)
      result += temp_poly
      term1 = self.nextTerm(p1)

    return result

# test (1+2x+x^2)*(1+x)
m1 = MultiplyPolynomial()
m1.addTerm(MultiplyPolynomial.Term(1,0))
m1.addTerm(MultiplyPolynomial.Term(2,1))
m1.addTerm(MultiplyPolynomial.Term(1,2))
m2 = MultiplyPolynomial()
m2.addTerm(MultiplyPolynomial.Term(1,0))
m2.addTerm(MultiplyPolynomial.Term(1,1))

print m1*m2
