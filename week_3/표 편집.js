class Node {
	constructor(data = 0, prev = null) {
		this.data = data;
		this.prev = prev;
		this.next = null;
	}
}

function Program(length = 8, point = 2) {
	let head = new Node("head");
	let pointer = null;
	const trash = [];

	Array(length)
		.fill(0)
		.reduce((prev, _, i) => {
			const cur = new Node(i, prev);
			prev.next = cur;
			if (i === point) pointer = cur;
			return cur;
		}, head);

	const move = (way) => (amount) => {
		let count = Number(amount);
		while (count > 0 && pointer) {
			count--;
			pointer = pointer[way];
		}
	};

	const clear = () => {
		trash.push(pointer);
		const { prev, next } = pointer;
		prev.next = next;
		pointer = prev;
		if (next) {
			next.prev = prev;
			pointer = next;
		}
	};

	const undo = () => {
		if (!trash) return;

		const target = trash.pop();
		target.prev.next = target;
		if (target.next) target.next.prev = target;
	};

	return {
		head,
		up: move("prev"),
		down: move("next"),
		clear,
		undo,
	};
}

function solution(n, k, cmd) {
	const thread = Program(n, k);
	const work = {
		U: "up",
		D: "down",
		C: "clear",
		Z: "undo",
	};

	cmd.forEach((string) => {
		const [op, ...args] = string.split(" ");
		thread[work[op]](...args);
	});

	const answer = Array(n).fill("X");
	let cur = thread.head;
	while (cur.next) {
		cur = cur.next;
		answer[cur.data] = "O";
	}
	return answer.join("");
}
