from functools import reduce


class CustomList:
    def __init__(self, elements = []) -> None:
        # 생성자에 깊은복사가 필요하다니
        self.elements = elements[:]
    
    def __add__(self, other):
        return CustomList(self.elements + (other - self).elements)

    def __sub__(self, other):
        sorted_max_list, sorted_min_list = self.__sort_self_and_other(other)
        result = []

        element_in_max = sorted_max_list.pop()
        element_in_min = sorted_min_list.pop()
        while sorted_min_list:
            if element_in_max != element_in_min:
                result.append(element_in_max)
            else:
                element_in_min = sorted_min_list.pop()
                
            element_in_max = sorted_max_list.pop()
        
        print(self.elements, other.elements, result + sorted_max_list)

        return CustomList(result + sorted_max_list)
    
    def __sort_self_and_other(self, other):
        key= lambda a: len(a) 
        sorted_list = [sorted(self.elements), sorted(other.elements)]

        return max(sorted_list, key= key), min(sorted_list, key= key)
    
    def __lt__(self, other):
        return len(self.elements) < len(other.elements)
    
    def __str__(self):
        return self.elements.__str__()
    
    def append(self, char):
        self.elements.append(char)

def solution(s):
    # sum -> TypeError: unsupported operand type(s) for +: 'int' and 'CustomList'
    return reduce(lambda acc, cur : acc + cur, sorted(parse(s))).elements

def parse(str):
    splited_list = str[2:-2].split("},{")
    
    stack = []
    for splited in splited_list:
        stack.append(CustomList(list(map(int, splited.split(",")))))
    return stack