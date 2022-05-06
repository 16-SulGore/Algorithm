import sys
sys.setrecursionlimit(10 ** 6)

class Node:
    def __init__(self, value, x):
        self.value = value
        self.x = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, node):
        if not self.root:
            self.root = node

        current_node = self.root
        while current_node:
            if node.x < current_node.x:
                if current_node.left:
                    current_node = current_node.left
                    continue
                else:
                    current_node.left = node
            if node.x > current_node.x:
                if current_node.right:
                    current_node = current_node.right
                    continue
                else:
                    current_node.right = node
            break
    
    def order(self, pre_order, post_order, node):
        pre_order.append(node.value)
        if node.left:
            self.order(pre_order, post_order, node.left)
        if node.right:
            self.order(pre_order, post_order, node.right)
        post_order.append(node.value)

def solution(nodeinfo):
    nodes = sorted([(i + 1, x, y) for i, (x, y) in enumerate(nodeinfo)], key=lambda node: (-node[2], node[1]))
    
    tree = Tree()
    for value, x, _ in nodes:
        node = Node(value, x)
        tree.insert(node)

    pre_order, post_order = [], []
    tree.order(pre_order, post_order, tree.root)
    return [pre_order, post_order]