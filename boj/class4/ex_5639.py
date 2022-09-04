# Ex_5639 이진 검색 트리 [실1]
# 재귀함수로 후위 순회할 시 재귀가 많아 런타임 에러가 발생한다.

import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(100000)

class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None

def insert(root, node):
    cur = root
    
    while True:
        if cur.key > node.key:
            if cur.left == None:
                cur.left = node
                return
            
            cur = cur.left
        
        else:
            if cur.right == None:
                cur.right = node
                return
            
            cur = cur.right

def postorder(root) -> list:
    if root == None:
        return []
    
    return postorder(root.left) + postorder(root.right) + [root.key]

def solution(node_list) -> list:
    root = Node(node_list[0])
    
    for i in node_list[1:]:
        insert(root, Node(i))
        
    return postorder(root)

if __name__ == "__main__":
    node_list = []
    
    while True:
        try:
            node_list.append(int(input()))
        except:
            break
        
    print(*solution(node_list))