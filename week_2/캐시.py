CACHE_HIT = 1
CACHE_MISS = 5

def solution(cacheSize, cities):
    if not cacheSize:
        return len(cities) * CACHE_MISS
    
    result = 0
    cache = dict()
    for at, city in enumerate(cities):
        city = city.lower()
        
        result += CACHE_HIT if city in cache else CACHE_MISS
        cache[city] = at
        
        if len(cache) > cacheSize:
            target = min(cache.items(), key = lambda x: x[1])[0]
            cache.pop(target)
    
    return result
