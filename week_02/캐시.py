from collections import deque
from itertools import chain, islice

CACHE_HIT = 1
CACHE_MISS = 5

def get_new_cache(cache, cache_size, target_index):
    indexs = [(0, target_index), (target_index + 1, cache_size), (target_index, target_index + 1)]
    return deque(chain(*map(lambda index: islice(cache, index[0], index[1]), indexs)))

def solution(cache_size, cities):
    if not cache_size:
        return len(cities) * CACHE_MISS
    
    cache = deque()
    answer = 0
    for city in map(lambda city: city.upper(), cities):
        if city in cache:
            target_index = cache.index(city)
            cache = get_new_cache(cache, cache_size, target_index)
            answer += CACHE_HIT
        else:
            if len(cache) == cache_size:
                cache.popleft()
            cache.append(city)
            answer += CACHE_MISS
    return answer