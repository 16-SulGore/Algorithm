function solution(gems) {
	const types = new Set(gems);
	const n = gems.length;
	const k = types.size;

	const counter = [...types].reduce(
		(obj, key) => {
			obj[key] = 0;
			return obj;
		},
		{ __has: 0 }
	);
	let ep = -1;

	return gems.reduce(
		(answer, start, sp) => {
			while (ep < n - 1 && counter.__has != k) {
				const end = gems[++ep];
				if (!counter[end]++) counter.__has++;
			}

			if (ep - sp < answer[1] - answer[0] && counter.__has == k)
				answer = [sp + 1, ep + 1];

			if (!--counter[start]) counter.__has--;

			return answer;
		},
		[1, n]
	);
}
