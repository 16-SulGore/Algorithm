import unittest

from ..model.Node import Node

class NodeTest(unittest.TestCase):

    def testAddKey_whenAddSameKey_shouldAppendSameValueIndex(self):
        # Given old node
        old_node = Node()
        old_node.add(1, "old")
        
        # When add new data
        old_node.add(1, "new")
        
        # Then added same value index
        self.assertEqual(2, len(old_node.values[0]))

    def testAddKey_whenAddDiffKey_sholudNewValueIndex(self):
        # Given old node
        old_node = Node()
        old_node.add(1, "old")
        
        # When add new data
        old_node.add(2, "new")

        # Then added diff value index
        self.assertEqual(2, len(old_node.values))
        self.assertEqual(1, len(old_node.values[0]))
