class Node {
    constructor(value) {
        this.next = null;
        this.value = value;
    }
}

class Queue {
    constructor() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    enqueue(value) {
        let node = new Node(value);
        if (this.size == 0) {
            this.head = node;
        } else {
            this.tail.next = node;
        }
        this.tail = node;
        this.size++;
    }

    dequeue() {
        if (this.size == 0) {
            return null;
        }
        let value = this.head.value;
        this.head = this.head.next
        this.size--;
        if (this.size == 0) {
            this.tail = null
        }
        return value
    }
    
    isEmpty() {
        return this.size == 0;
    }
}

let min = (array) => array.reduce((prev, cur) => prev < cur ? prev : cur);

function solution(board) {
    const n = board.length;
    const direction = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    let dp = Array.from({ length: n }, (_, i) => Array.from({ length: n }, (_, j) => Array(4).fill(!i && !j ? 0 : Infinity)));

    let q = new Queue();
    q.enqueue([0, 0, -1])
    while (!q.isEmpty()) {
        [i, j, d] = q.dequeue();
        direction.forEach(([di, dj], nd) => {
            ni = i + di;
            nj = j + dj;
            if (0 <= ni && ni < n && 0 <= nj && nj < n && !board[ni][nj]) {
                const nextCost = dp[i][j][d == -1 ? 0 : d] + (d == nd || d == -1 ? 100 : 600); 
                if (nextCost < dp[ni][nj][nd]) {
                    dp[ni][nj][nd] = nextCost;
                    q.enqueue([ni, nj, nd]);
                }
            }
        })
    };
    return min(dp[n - 1][n - 1]);
}