const readline = require("readline");

class TermProject {
  constructor() {
    this.T = 0;
    this.n = 0;
    this.input = [];

    this.circleResult = [];

    this.visited = [];
    this.circle = [];

    this.result = [];

    this.lineNum = 1;
  }

  dfs(start) {
    const next = this.input[start];

    this.visited[start] = true;
    this.circle.push(start);

    if (this.visited[next]) {
      if (this.circle.includes(next)) {
        const idx = this.circle.indexOf(next);
        this.circleResult.push(...this.circle.slice(idx));
      }
      return;
    } else {
      this.dfs(next);
    }

    return;
  }

  getInput(line) {
    if (this.lineNum === 1) this.T = line;
    else if (this.lineNum % 2 === 0) this.n = line;
    else {
      this.input = line.split(" ").map((val) => Number(val));
      this.input.unshift(0);

      const inputLen = this.input.length;
      this.visited = new Array(inputLen).fill(false);

      this.circle = [];
      this.circleResult = [];

      for (let i = 1; i < inputLen; i++) {
        this.circle = [];
        this.dfs(i);
      }

      this.result.push(this.n - new Set([...this.circleResult]).size);
    }

    this.lineNum++;
  }

  solution() {
    const { result } = this;
    for (let i = 0; i < result.length; i++) {
      console.log(result[i]);
    }
  }
}

function main() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  const tp = new TermProject();

  rl.on("line", function (line) {
    tp.getInput(line);
  }).on("close", function () {
    tp.solution();
    process.exit();
  });
}

main();
