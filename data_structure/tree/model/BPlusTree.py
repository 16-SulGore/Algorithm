from ..model.Node import Node

class BPlusTree:

    def __init__(self):
        self.__root = Node()

    def insert_node(self, key, value):
        parent = None
        child: Node = self.__root

        # 삽입할 노드 위치 탐색
        while not child.is_leaf:
            parent = child
            child, index = self.__find_direction(child, key)

        child.add(key, value)

    def __find_direction(self, node, key) -> Node:
        # TODO: binary search if big order
        i = 0
        for i, item in enumerate(node.keys):
            if key < item:
                return node.values[i], i

        # key 보다 큰 item이 없을 때
        return node.values[i + 1], i + 1

    def __merge_node(self, parent, child, index):
        parent.value.pop(index)
        pivot = child.keys[0]

        for i, item in enumerate(parent.keys):
            if pivot < item:
                parent.keys = parent.keys[:i] + [pivot] + parent.keys[i:]
                parent.values = parent.values[:i] + child.values + parent.values[i:]
                break

            elif i + 1 == len(parent.keys):
                parent.keys += [pivot]
                parent.values += child.values
                break

    def __split_node(self, node):
        pass

    def search_linear(self):
        # find first leaf
        node = self.__get_first_leaf()
        result = []

        # search
        while node.next:
            result.append(node.key)
            node = node.next

        return result

    def __get_first_leaf(self):
        child = self.__root

        while not child.is_leaf:
            child = child.keys[0]

        return child

    # ---------TODO------------
    def search_node(self, node):
        pass

    def delete_node(self, node):
        pass

    def search_preorder(self):
        pass
