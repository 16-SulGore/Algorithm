class Node:
    def __init__(self) -> None:
        self.keys = []
        self.values = []
        self.is_leaf = False
        self.prev = None
        self.next = None
        self.MAX_ORDER = 2

    # https://gist.github.com/savarin/69acd246302567395f65ad6b97ee503d
    def add(self, key, value):
        # insert last
        if not self.keys or key > max(self.keys):
            self.keys.append(key)
            self.values.append([value])
            return
        
        # new key
        for i, old_key in enumerate(self.keys):
            # existed key
            if key == old_key:
                self.values[i].append(value)
                break
            
            # small key
            # insert left
            elif key < old_key:
                self.keys = self.keys[:i] + [key] + self.keys[i:]
                self.values = self.values[:i] + [[value]] + self.values[i:]
                break 

    def __eq__(self, __o: object) -> bool:
        if type(__o) is Node:
            return self.keys == __o.keys
        else:
            return False
    
    def __hash__(self) -> int:
        return sum(int(self.keys))