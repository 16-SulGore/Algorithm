import unittest
from ..model.BPlusTree import BPlusTree
from ..model.Node import Node

class BPlusTreeTest(unittest.TestCase):

    def setUp(self) -> None:
        # Given B+Tree & sample keys
        self.tree = BPlusTree()
        self.keys = [1, 3, 5, 10, 12, 13, 16, 17, 18]
        self.sample_keys = [5, 13, 16, 17]
        # And sample nodes
        for key in self.sample_keys:
            self.tree.insert_node(key= key, value= key)

        return super().setUp()

    def testInsertNode_whenInsertNew_thenLinearIsSorted(self):
        # Given node 15
        self.tree.insert_node(key= 1, value= "new")

        # When linear search
        linear = self.tree.search_linear()

        # Then 15 between 13 & 16
        # [5, 13, 16, 17] -> [5, 13, 15, 16, 17]
        expect = sorted(self.sample_keys + new_node.keys)
        self.assertEqual(expect, linear)
