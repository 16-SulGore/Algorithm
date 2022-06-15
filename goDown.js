const readline = require("readline");

class goDown {
  constructor() {
    this.N = 0;
    this.lineNum = 0;

    this.maxDp = [];
    this.minDp = [];
  }

  getInput(line) {
    if (this.lineNum === 0) {
      this.N = Number(line);
    } else if (this.lineNum <= this.N) {
      const inputLine = line.split(" ");
      this.maxDp.push(inputLine.map((val) => Number(val)));
      this.minDp.push(inputLine.map((val) => Number(val)));
    } else {
      throw new Error("Input Error");
    }

    this.lineNum += 1;
  }

  getMaxDp() {
    for (let i = 0; i < this.N; i++) {
      for (let j = 0; j < 3; j++) {
        let before = [];

        if (i > 0) {
          if (this.maxDp[i - 1][j - 1]) before.push(this.maxDp[i - 1][j - 1]);
          if (this.maxDp[i - 1][j]) before.push(this.maxDp[i - 1][j]);
          if (this.maxDp[i - 1][j + 1]) before.push(this.maxDp[i - 1][j + 1]);

          this.maxDp[i][j] += Math.max(...before);
        }
      }
    }
    return Math.max(...this.maxDp[this.N - 1]);
  }

  getMinDp() {
    for (let i = 0; i < this.N; i++) {
      for (let j = 0; j < 3; j++) {
        let before = [];

        if (i > 0) {
          if (this.minDp[i - 1][j - 1]) before.push(this.minDp[i - 1][j - 1]);
          if (this.minDp[i - 1][j]) before.push(this.minDp[i - 1][j]);
          if (this.minDp[i - 1][j + 1]) before.push(this.minDp[i - 1][j + 1]);
          this.minDp[i][j] += Math.min(...before);
        }
      }
    }

    return Math.min(...this.minDp[this.N - 1]);
  }

  solution() {
    let result = [];

    result.push(this.getMaxDp());
    result.push(this.getMinDp());

    return result.join(" ");
  }
}

function main() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  const gd = new goDown();

  rl.on("line", function (line) {
    gd.getInput(line);
  }).on("close", function () {
    console.log(gd.solution());
    process.exit();
  });
}

main();
