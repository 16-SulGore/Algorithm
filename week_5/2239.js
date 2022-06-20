class Sudoku {
    constructor(input) {
        this.graph = input;
        this.N = this.graph?.length || 0;
    }
    toString() {
        return this.graph
            .map((line) => line.map(char => char.toString()).join(''))
            .join('\n')
            .trim();
    }
    isUnique(x, y, target) {
        const { graph, N } = this;
        for(let i = 0; i < N; i++) {
            if(graph[y][i] === target || graph[i][x] === target) return false;
        }
        const squaredX = parseInt(x / 3) * 3;
        const squaredY = parseInt(y / 3) * 3;
        for(let a = squaredX; a < squaredX + 3; a++) {
            for(let b = squaredY; b < squaredY + 3; b++) {
                if(graph[b][a] === target) return false;   
            }
        }
        return true;
    }
    backtrack(num) {
        const { graph, N } = this;
        if(num === N * N) {
            console.log(this.toString());
            process.exit(0);
        }

        const x = num % N;
        const y = parseInt(num / N);
        if(graph[y][x] != 0) return this.backtrack(num + 1);

        for(let i = 1; i <= N; i++){
            if(this.isUnique(x, y, i)) {
                graph[y][x] = i;
                this.backtrack(num + 1)
                graph[y][x] = 0;
            }
        }
    }
    solve() { this.backtrack(0); }
}

(function solution() {
    const readline = require('readline'); 
    const ioInterface = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    })
    const input = [];
    ioInterface
        .on("line", (line) => {
            input.push(line.trim().split('').map((char) => parseInt(char)));
        })
        .on("close", () => {
            const problem = new Sudoku(input);
            problem.solve();
            process.exit();
        });
})();

// (function solution() {
//     const fs = require('fs');
//     let input = fs.readFileSync('./dev/stdin').toString().split('\n');
//     input = input.map((line) => line.trim().split('').map((char) => parseInt(char)));
//     const problem = new Sudoku(input);
//     problem.solve();
// })();
