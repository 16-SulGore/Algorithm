import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def postorder(arr):
    if len(arr) <= 1:
        return arr

    for i in range(1, len(arr)):
        if arr[i] > arr[0]:
            return postorder(arr[1:i]) + postorder(arr[i:]) + [arr[0]]
            
    return postorder(arr[1:]) + [arr[0]]

preorder = []

while True:
    try:
        preorder.append(int(input()))
    except:
        break

for node in postorder(preorder):
    print(node)