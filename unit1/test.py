import unittest
from copy import copy
from array import Array
from linkedlist import LinkedList
from linkedlist2 import LinkedList as Linked2

@unittest.skip("demonstrating skipping")
class TestArray(unittest.TestCase):

	def setUp(self):
		self.array = Array(10, 0)
		self.offarray = Array(5, 5)

	def test_init(self):
        # the length of the array should equal to the input
		self.assertEqual(len(self.array._data), 10)
		self.assertEqual(self.array._baseIndex, 0)
        # no negative length input is allowed
		self.assertRaises(AssertionError, Array, -10, 0)

	def test_copy(self):
		a = copy(self.array)
		self.assertEqual(len(a._data), 10)
		self.assertEqual(a._baseIndex, 0)
	
	def test_offset(self):
		self.assertEqual(self.array.getOffset(1), 1)
		# for array with the start index as 5
		self.assertEqual(self.offarray.getOffset(6), 1)
		self.assertRaises(IndexError, self.array.getOffset, -1)
		self.assertRaises(IndexError, self.array.getOffset, 11)
	
	def test_item(self):
		# test getitem
		for i in range(10):
			self.assertEqual(self.array[i], None)
		for i in range(10):
			self.array[i] = 10-i
		# test setitem
		for i in range(10):
			self.assertEqual(self.array[i], 10-i)

	def test_properties(self):
		self.assertEqual(self.array.data, self.array._data)
		self.assertEqual(self.array.baseIndex, self.array._baseIndex)
		self.array.baseIndex = 1
		self.assertEqual(1, self.array._baseIndex)
			
	def test_resizing(self):
		self.assertEqual(self.array.length, len(self.array._data))
		self.array.length = 5
		self.assertEqual(5, len(self.array._data))
		self.array.length = 15
		self.assertEqual(15, len(self.array._data))

@unittest.skip("demonstrating skipping")
class TestLinkedList(unittest.TestCase):

	def setUp(self):
		self.list = LinkedList()
	
	def test_element(self):
		e = LinkedList.Element(self.list, 10)
		self.assertEqual(e._list, self.list)
		self.assertEqual(e.value, 10)
		self.assertEqual(e.next, None)
		
	def test_init(self):
		self.assertEqual(self.list.head, None)
		self.assertEqual(self.list.tail, None)
		self.assertEqual(self.list.isEmpty, True)
		# self.assertRaises(RuntimeError, self.list.first)
		# self.assertRaises(RuntimeError, self.list.last)
		
	def test_pend(self):
		self.list.prepend(10)
		self.assertEqual(self.list.head.value, 10)
		self.list.prepend(11)
		self.assertEqual(self.list.head.value, 11)
		self.list.append(5)
		self.assertEqual(self.list.last, 5)
		self.assertEqual(self.list.isEmpty, False)
		self.list.purge()
		self.assertEqual(self.list.isEmpty, True)
	
	def test_extract(self):
		self.assertRaises(KeyError, self.list.extract, 10)
		self.list.prepend(10)
		self.list.prepend(5)				
		self.list.extract(10)
		self.assertRaises(KeyError, self.list.extract, 6)		
		self.list.extract(5)
		self.assertEqual(self.list.isEmpty, True)
		
	def test_copy(self):
		self.list.prepend(10)
		self.list.prepend(5)						
		a = copy(self.list)
		self.assertEqual(a.first, self.list.first)
		self.assertEqual(a.last, self.list.last)
								
class TestLinked2(unittest.TestCase):
  def setUp(self):
	  self.list = Linked2()

  def test_element(self):
    e = Linked2.Element(self.list, 10)
    self.assertEqual(e._list, self.list)
    self.assertEqual(e._value, 10)
    self.assertEqual(e._next, None)
    e2 = Linked2.Element(self.list, 5, e)
    self.assertEqual(e2._list, self.list)
    self.assertEqual(e2._value, 5)
    self.assertEqual(e2._next, e)
    self.assertEqual(e2.next, e)
    self.assertEqual(e2.value, e2._value)

  def test_init(self):
    self.assertEqual(self.list.head, None)
    self.assertTrue(self.list.isEmpty)

  def test_pend(self):
    self.list.prepend(10)
    self.assertFalse(self.list.isEmpty)
    self.assertEqual(self.list.head.value, 10)
    self.list.prepend(5)
    self.assertEqual(self.list.head.value, 5)
    self.assertEqual(self.list.head.next.value, 10)
    self.list.append(15)
    start = self.list.head
    while start.next != None:
      start = start.next
    self.assertEqual(start.value, 15)
    self.assertEqual(self.list.head.value, 5)

  def test_purge(self):
    self.list.append(10)
    self.list.append(5)
    self.assertFalse(self.list.isEmpty) 
    self.assertTrue(self.list.head) 
    self.list.purge()
    self.assertTrue(self.list.isEmpty) 
    self.assertFalse(self.list.head) 

  def test_getFirst(self):
    self.list.append(10)
    self.list.append(5)
    self.assertEqual(self.list.first.value, 10)
    self.assertEqual(self.list.last.value, 5)
    
  def test_copy(self):
    self.list.append(10)
    self.list.append(5)
    a = copy(self.list)
    self.assertEqual(self.list.first.value, a.first.value)
    self.assertEqual(self.list.last.value, a.last.value)
    self.assertFalse(a == self.list)

  def test_extract(self):
    self.list.append(10)
    self.list.append(5)
    res1 = self.list.extract(10)
    self.assertEqual(res1, 10)
    self.assertRaises(KeyError, self.list.extract, 10)
    self.assertRaises(KeyError, self.list.extract, 9)

  def test_insert(self):
    self.list.append(10)
    self.list.append(5)
    self.list.first.insertAfter(7)
    self.assertEqual(self.list.head.next.value, 7)
    self.list.last.insertAfter(12)
    self.assertEqual(self.list.last.value, 12)
    self.list.first.insertBefore(3)
    test1 = [3, 10, 7, 5, 12]
    i = iter(test1)
    start = self.list.head
    while start != None:
      self.assertEqual(start.value, i.next())
      start = start.next

    self.assertEqual(self.list.head.value, 3)
    self.list.last.insertBefore(11)
    self.assertEqual(self.list.last.value, 12)
    res = self.list.extract(11)
    self.assertEqual(res, 11)






if __name__ == '__main__':
    unittest.main()
