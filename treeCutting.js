const readline = require("readline");

class TreeCutting {
  constructor() {
    this.N = 0; // 1 <= N <= 1,000,000
    this.M = 0; // 1 <= M <= 2,000,000,000

    this.treeList = [];

    this.lineNumber = 1;
  }

  getInput(line) {
    const lineArray = line.split(" ");

    if (this.lineNumber === 1) {
      this.N = Number(lineArray[0]);
      this.M = Number(lineArray[1]);
    } else if (this.lineNumber === 2) {
      this.treeList = lineArray.map((val) => Number(val));
    } else {
      throw new Error("Input Error");
    }

    this.lineNumber += 1;
  }

  cutTree(tree, cutline) {
    return tree - cutline > 0 ? tree - cutline : 0;
  }

  // while 반복문을 통한 이진 탐색
  solution() {
    const { M, treeList, cutTree } = this;

    let low = 1;
    let high = Math.max(...treeList);

    while (low <= high) {
      let mid = Math.floor((low + high) / 2);

      let treeUsage = treeList.reduce((pre, cur) => pre + cutTree(cur, mid), 0);
      treeUsage >= M ? (low = mid + 1) : (high = mid - 1);
    }

    return high;
  }

  // 재귀를 통한 이진 탐색
  binarySearch(low, high) {
    const { M, treeList } = this;

    if (low > high) return high;

    let mid = Math.floor((low + high) / 2);

    let treeUsage = treeList.reduce(
      (pre, cur) => pre + this.cutTree(cur, mid),
      0
    );

    return treeUsage >= M
      ? this.binarySearch(mid + 1, high)
      : this.binarySearch(low, mid - 1);
  }

  // 재귀를 통한 이진탐색 풀이
  solution2() {
    return this.binarySearch(1, Math.max(...this.treeList));
  }
}

function main() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  const tc = new TreeCutting();

  rl.on("line", function (line) {
    tc.getInput(line);
  }).on("close", function () {
    // console.log(tc.solution());
    console.log(tc.solution2());
    process.exit();
  });
}

main();
