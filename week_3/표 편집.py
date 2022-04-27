class Node:
    def __init__(self, data = 0, prev = None):
        self.data = data
        self.prev = prev
        self.next = None

class KakaoList:
    def __init__(self, length = 8, point = 2):
        self.head = self.create_node_list(length)
        self.pointer = self.search(point)
        self.trash = []
    
    def create_node_list(self, length = 1):
        head = cur = Node('head')
        for i in range(0, length):
            cur.next = Node(i, cur)
            cur = cur.next
        return head
    
    def search(self, data):
        cur = self.head
        while cur.next:
            cur = cur.next
            if cur.data == data:
                return cur
        return None
    
    def up(self, amount):
        while amount > 0 and self.pointer.prev:
            amount -= 1
            self.pointer = self.pointer.prev
    
    def down(self, amount):
        while amount > 0 and self.pointer:
            amount -= 1
            self.pointer = self.pointer.next
    
    def delete(self):
        self.trash.append(self.pointer)
        nxt = self.pointer.next
        prv = self.pointer.prev
        prv.next = nxt
        self.pointer = prv
        if nxt:
            nxt.prev = prv
            self.pointer = nxt
    
    def restore(self):
        if not self.trash:
            return False
        
        target = self.trash.pop()
        target.prev.next = target
        if target.next:
            target.next.prev = target

def solution(n, k, cmd):
    program = KakaoList(n, k)
    
    for string in cmd:
        word = string.split()
        op = word[0]
        
        if op == 'U':
            program.up(int(word[1]))
        if op == 'D':
            program.down(int(word[1]))
        if op == 'C':
            program.delete()
        if op == 'Z':
            program.restore()
    
    answer = ['X'] * n
    cur = program.head
    while cur.next:
        cur = cur.next
        answer[cur.data] = 'O'
    
    return ''.join(answer)