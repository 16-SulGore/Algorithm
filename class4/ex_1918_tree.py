# Ex_1918 후위 표기식 [골3]
# Tree 방식

class Node:
    def __init__(self, str = ""):
        self.key = str
        self.left = None
        self.right = None

class Tree:
    def __init__(self, notation):
        self.__create_tree(notation)

    # __는 python에서 private 접근 제한자를 뜻함.
    def __create_tree(self, notation) -> None:
        self.root = ""
        
        # TODO: 수식을 순회하며 트리 생성하기
        for c in notation:
            True

    def get_postfix_recur(self, root) -> str:
        if root == None:
            return ""
        
        return self.get_postfix_recur(root.left) + self.get_postfix_recur(root.right) + root.key

def solution(notation):
    tree = Tree(notation)
    return tree.get_postfix_recur(tree.root)

if __name__ == "__main__":
    print(solution(input()))