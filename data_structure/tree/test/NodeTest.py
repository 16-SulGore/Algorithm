import unittest

from ..model.Node import Node

class NodeTest(unittest.TestCase):

    def testAddKey_whenAddKey_thenAppend(self):
        # Given node and key
        old = 1
        node = Node(old)
        new = 2

        # When add solo key
        node.add_key(new)

        # Then [old, new]
        self.assertEqual([old, new], node.key)

    def testAddKey_whenAddKeyList_thenPlus(self):
        # Given node and key
        old = 1
        node = Node(old)
        new = [2, 3]
        expect = [1, 2, 3]

        # When add solo key
        node.add_key(new)

        # Then [old, new]
        self.assertEqual(expect, node.key)
