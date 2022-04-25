const CACHE_HIT = 1;
const CACHE_MISS = 5;

function solution(cacheSize, cities) {
	if (!cacheSize) return cities.length * CACHE_MISS;

	const cache = {};
	const answer = cities.reduce((result, city, at) => {
		city = city.toLowerCase();

		const time = city in cache ? CACHE_HIT : CACHE_MISS;
		cache[city] = at;

		const entries = Object.entries(cache);
		if (entries.length > cacheSize) {
			const [target] = entries.reduce((min, cur) =>
				min[1] < cur[1] ? min : cur
			);
			delete cache[target];
		}

		return result + time;
	}, 0);

	return answer;
}
