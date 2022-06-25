class Sudoku {
  constructor() {
    this.graph = [];
  }

  print() {
    let answer = "";
    for (let i = 0; i < 9; i++) {
      for (let j = 0; j < 9; j++) {
        answer += this.graph[i][j];
      }
      answer += "\n";
    }
    console.log(answer);
  }

  checkRow(row, target) {
    for (let i = 0; i < 9; i++) {
      if (this.graph[row][i] === target) {
        return false;
      }
    }
    return true;
  }

  checkCol(col, target) {
    for (let i = 0; i < 9; i++) {
      if (this.graph[i][col] === target) {
        return false;
      }
    }
    return true;
  }

  checkBox(row, col, target) {
    row = parseInt(row / 3);
    col = parseInt(col / 3);

    for (let i = 0; i < 3; i++) {
      for (let j = 0; j < 3; j++) {
        let rowIdx = row * 3 + i;
        let colIdx = col * 3 + j;

        if (this.graph[rowIdx][colIdx] === target) {
          return false;
        }
      }
    }

    return true;
  }

  getInput(line) {
    this.graph.push(line.split("").map((val) => Number(val)));
  }

  backtracking(depth) {
    if (depth === 81) {
      this.print();
      process.exit(); // 1만 출력하고 종료
    }

    const row = parseInt(depth / 9);
    const col = depth % 9;

    if (this.graph[row][col] === 0) {
      for (let i = 1; i < 10; i++) {
        if (
          this.checkBox(row, col, i) &&
          this.checkRow(row, i) &&
          this.checkCol(col, i)
        ) {
          this.graph[row][col] = i;
          this.backtracking(depth + 1);
          this.graph[row][col] = 0;
        }
      }
    } else {
      this.backtracking(depth + 1);
    }
  }
}

(function solution() {
  const readline = require("readline");
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  const sdk = new Sudoku();

  rl.on("line", function (line) {
    sdk.getInput(line);
  }).on("close", function () {
    sdk.backtracking(0);
  });
})();
