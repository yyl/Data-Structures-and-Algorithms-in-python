import unittest
from mytype import Bool
from mySearchable import mySearchable
from visitSearchable import VisitSearchable

    
class TestBool(unittest.TestCase):
  def setUp(self):
    self.b0 = Bool()
    self.b1 = Bool(False)
    self.b2 = Bool(True)
    self.b3 = Bool(True)

  def test_truth(self):
    self.assertRaises(AssertionError, Bool, 10)
    self.assertEqual(self.b0.val, False)
    self.assertEqual(self.b1.val, False)
    self.assertEqual(self.b2.val, True)
    self.assertEqual(self.b3.val, True)

class TestSeachable(unittest.TestCase):
  def setUp(self):
    self.s = mySearchable()
    self.s.insert(1)
    self.s.insert(2)

  def test_insert(self):
    self.assertRaises(AssertionError, self.s.insert, 2)

  def test_iter(self):
    i = iter(self.s)
    self.assertEqual(i.next(), 1)
    self.assertEqual(i.next(), 2)
    self.assertRaises(StopIteration, i.next)

  def test_contains(self):
    self.assertTrue(1 in self.s)
    self.assertFalse(10 in self.s)

  def test_withdraw(self):
    self.s.withdraw(1)
    self.assertFalse(1 in self.s)
    self.assertRaises(AssertionError, self.s.withdraw, 20)

  def test_purge(self):
    self.s.purge()
    self.assertFalse(1 in self.s)
    self.assertFalse(2 in self.s)

  def test_find(self):
    self.assertEqual(self.s.find(1), 1)
    self.assertTrue(1 in self.s)
    self.assertEqual(self.s.find(10), None)

class TestVisitSearchable(unittest.TestCase):
  def setUp(self):
    self.s = VisitSearchable()
    self.s.insert(1)
    self.s.insert(2)

  def test_contains(self):
    self.assertTrue(1 in self.s)
    self.assertFalse(10 in self.s)

  # def test_transfer(self):
  #   s2 = VisitSearchable()
  #   self.assertTrue(1 in self.s)
  #   self.assertFalse(1 in s2)
  #   s2.copy(self.s)
  #   self.assertTrue(1 in s2)
  #   self.assertTrue(2 in s2)
  #   self.assertFalse(1 in self.s)
  #   self.assertFalse(2 in self.s)

if __name__ == '__main__':
    unittest.main()
