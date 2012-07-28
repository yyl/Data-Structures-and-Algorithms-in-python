import unittest
from doublyLinkedList import DoublyLinkedList
from opus7.exception import *

class TestList(unittest.TestCase):
  def setUp(self):
    self.l = DoublyLinkedList()

  def test_init(self):
    self.assertEqual(self.l.head, None)
    self.assertEqual(self.l.tail, None)

  def test_append(self):
    self.l.append(1)
    self.assertEqual(self.l.head.value, 1)
    self.assertEqual(self.l.tail.value, 1)
    self.l.append(2)
    self.assertEqual(self.l.head.value, 1)
    self.assertEqual(self.l.tail.value, 2)
    self.assertEqual(self.l.first.value, 1)
    self.assertEqual(self.l.last.value, 2)

  def test_prepend(self):
    self.l.prepend(1)
    self.assertEqual(self.l.head.value, 1)
    self.assertEqual(self.l.tail.value, 1)
    self.l.prepend(2)
    self.assertEqual(self.l.head.value, 2)
    self.assertEqual(self.l.tail.value, 1)
    self.l.prepend(3)
    self.assertEqual(self.l.head.value, 3)
    self.assertEqual(self.l.tail.value, 1)

  def test_purge(self):
    self.l.append(1)
    self.l.append(2)
    self.l.append(3)
    self.assertEqual(self.l.head.value, 1)
    self.assertEqual(self.l.tail.value, 3)
    self.l.purge()
    self.assertEqual(self.l.head, None)
    self.assertEqual(self.l.tail, None)


if __name__ == "__main__":
  unittest.main()
