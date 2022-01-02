class Node:
    def __init__(self, key) -> None:
        self.key = [key]
        self.is_leaf = False
        self.prev = None
        self.next = None

    def add_key(self, key) -> None:
        if type(key) is list:
            self.key += key
        else:
            self.key.append(key)