# Ex_12865 평범한 배낭 [골5]

# Model
class Item:
    def __init__(self, weight, value):
        self.value = value
        self.weight = weight

class Dp:
    def __init__(self) -> None:
        self.item_list = []
        self.total_value = 0
        self.total_weight = 0
        
    def can_insert_item(self, item, K) -> bool:
        return self.total_weight + item.weight <= K and item not in self.item_list
    
    def set_item(self, item):
        self.item_list.append(item)
        self.total_value += item.value
        self.total_weight += item.weight
        
    def update_dp(self, dp, item):
        self.item_list = dp.item_list[:]
        self.total_value = dp.total_value
        self.total_weight = dp.total_weight
        
        self.set_item(item)

# Controller    
def list_to_items(backpack):
    return [Item(item[0], item[1]) for item in backpack]

def create_dp(K, backpack):
    dp_list = [Dp() for _ in range(K + 1)]
    
    for item in backpack:
        if item.weight <= K and dp_list[item.weight].total_value < item.value:
            dp_list[item.weight].set_item(item)
                
    return dp_list

def start_dp(K, backpack, dp_list):
    for dp in dp_list:
        for item in backpack:
            if dp.can_insert_item(item, K):

                # value 비교
                if dp.total_value + item.value > dp_list[dp.total_weight + item.weight].total_value:
                    dp_list[dp.total_weight + item.weight].update_dp(dp, item)
        
    return dp_list

def solution(_, K, backpack) -> int:
    backpack = list_to_items(backpack)
    dp = create_dp(K, backpack)
    dp = start_dp(K, backpack, dp)
    
    return max(dp, key= lambda x: x.total_value).total_value

# View
if __name__ == "__main__":
    N, K = map(int, input().split())
    backpack = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, K, backpack))