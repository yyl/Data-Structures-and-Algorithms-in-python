import unittest
from doublyLinkedList import DoublyLinkedList
from opus7.exception import *
from copy import copy
from pro8 import Deque

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

  def test_extract(self):
    self.l.append(1)
    self.l.append(2)
    self.l.append(3)
    self.l.append(4)
    self.l.append(5)
    self.assertEqual(self.l.extract(1), 1)
    self.assertEqual(self.l.head.value, 2)
    self.assertEqual(self.l.extract(10), None)
    self.assertEqual(self.l.extract(5), 5)
    self.assertEqual(self.l.tail.value, 4)

  def test_copy(self):
    self.l.append(1)
    self.l.append(2)
    self.l.append(3)
    a = copy(self.l)
    self.assertEqual(a.head.value, 1)
    self.assertEqual(a.tail.value, 3)

  def test_empty(self):
    self.assertTrue(self.l.isEmpty)
    self.l.append(1)
    self.assertFalse(self.l.isEmpty)
    self.l.extract(1)
    self.assertTrue(self.l.isEmpty)

class DequeTest(unittest.TestCase):
  def setUp(self):
    self.d = Deque()

  def test_init(self):
    self.assertEqual(self.d.head, None)
    self.assertEqual(self.d.tail, None)

  def test_head(self):
    self.d.enqueueHead(1)
    self.assertEqual(self.d.head.value, 1)
    self.assertEqual(self.d.tail.value, 1)
    self.d.enqueueHead(2)
    self.d.enqueueHead(3)
    self.assertEqual(self.d.head.value, 3)
    self.assertEqual(self.d.tail.value, 1)
    self.assertEqual(self.d.dequeueHead() , 3)
    self.assertEqual(self.d.dequeueHead() , 2)
    self.assertEqual(self.d.dequeueHead() , 1)
    self.assertRaises(AssertionError, self.d.dequeueHead)

if __name__ == "__main__":
  unittest.main()
