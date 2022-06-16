const readline = require("readline");

class solutionWater {
  constructor() {
    this.lineNum = 0;
    this.N = 0;
    this.waterList = []; // input
  }

  getInput(line) {
    if (this.lineNum === 0) this.N = 0;
    else if (this.lineNum === 1) {
      this.waterList = line.split(" ").map((val) => Number(val));
    } else {
      throw new Error("Input Error");
    }

    this.lineNum++;
  }

  solution() {
    let { waterList } = this;
    const map = new Map();

    waterList = waterList.sort((x, y) => x - y);

    let left = 0;
    let right = waterList.length - 1;

    while (left < right) {
      let waterSum = waterList[left] + waterList[right];
      let waterKey = Math.abs(waterSum);

      map.set(
        waterKey,
        map.get(waterKey)
          ? [...map.get(waterKey), [left, right]]
          : [[left, right]]
      );

      if (waterSum > 0) right -= 1;
      else if (waterSum < 0) left += 1;
      else break;
    }

    return [...map]
      .sort((x, y) => x[0] - y[0])[0][1][0]
      .map((IdxVal) => waterList[IdxVal])
      .join(" ");
  }
}

function main() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  const sw = new solutionWater();

  rl.on("line", function (line) {
    sw.getInput(line);
  }).on("close", function () {
    console.log(sw.solution());
    process.exit();
  });
}

main();
