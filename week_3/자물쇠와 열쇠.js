Array.prototype.rotate90 = function () {
	const copied = this.map((line) => [...line]);
	copied.forEach((line, y) => {
		line.forEach((_, x) => (this[y][x] = !!copied[this.length - 1 - x][y]));
	});
};

function derive_key(key, controlLock, env) {
	let { count } = env;
	const { m, n, bx, by } = env;
	const gap = m - 1;
	const sx = Math.max(bx, gap);
	const sy = Math.max(by, gap);
	const ex = Math.min(bx + m, gap + n);
	const ey = Math.min(by + m, gap + n);

	for (let y = sy; y < ey; y++) {
		for (let x = sx; x < ex; x++) {
			const key_v = key[y - by][x - bx];
			const lock_v = controlLock[y][x];
			count -= key_v && lock_v;
			if (key_v ^ lock_v) return false;
		}
	}

	return count === 0;
}

function solution(key, lock) {
	const [m, n] = [key.length, lock.length];
	const ext = n + 2 * (m - 1);

	let count = 0;
	const controlLock = lock.reduce(
		(controled, line, y) => {
			line.forEach((value, x) => {
				count += !value;
				controled[y + (m - 1)][x + (m - 1)] = !value;
			});
			return controled;
		},
		Array.from(Array(ext), () => Array(ext).fill(false))
	);

	const compL = n + (m - 1);
	for (let i = 0; i < 4; i++) {
		key.rotate90();
		for (let y = 0; y < compL; y++) {
			for (let x = 0; x < compL; x++) {
				const env = { m, n, bx: x, by: y, count };
				if (derive_key(key, controlLock, env)) return true;
			}
		}
	}

	return false;
}
