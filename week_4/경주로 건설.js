class Queue {
    constructor(arr) {
        this.front = null;
        this.rear = null;
        this.size = 0;

        if(Array.isArray(arr)) this.enqueue(...arr);
    }
    enqueue(...arr) {
        this.rear = arr.reduce((prev, data) => {
            const node = { data, next: null, prev };
            this.size++;
            if(!prev) this.front = node;
            else prev.next = node;
            return node;
        }, this.rear);
    }
    dequeue() {
        if(!this.size) return;
        this.size--;

        const target = this.rear;
        const { data, prev } = target;
        if(prev) {
            prev.next = null;
            this.rear = prev;
        }
        else {
            this.front = null;
            this.rear = null;
        }
        return data;
    }
}

const STRAIGHT_COST = 100;
const CORNER_COST = 500;
const DIRECTION = [[1, 0], [0, 1], [-1, 0], [0, -1]];

function solution(board) {
    const n = board.length;
    const dp = Array.from(Array(n),
        () => Array.from(Array(n),
            () => Array(4).fill(Infinity)
        )
    );
    
    dp[0][0] = [0, 0, 0, 0];
    const que = new Queue([{ x: 0, y: 0, dir: -1 }]);
    while(que.size) {
        const { x, y, dir } = que.dequeue();
        const cost = dp[y][x][dir] || 0;
        
        DIRECTION.forEach(([dx, dy], i) => {
            const tx = dx + x;
            const ty = dy + y;
            const has_corner = (i != dir) && (dir >= 0);
            const tcost = cost + STRAIGHT_COST + has_corner * CORNER_COST;
            
            const is_out = tx < 0 || ty < 0 || tx >= n || ty >= n;
            if(is_out || board[ty][tx] || dp[ty][tx][i] <= tcost) return;
            
            dp[ty][tx][i] = tcost;
            que.enqueue({ x: tx, y: ty, dir: i });
        });
    }
    return Math.min(...dp[n - 1][n - 1]);
}