const readline = require("readline");

class OnlineCutting {
  constructor() {
    this.K = null;
    this.N = null;

    this.onlineList = [];
  }

  doInput(line) {
    const inputLine = line.split(" ");
    if (inputLine.length === 2) {
      this.K = Number(inputLine[0]);
      this.N = Number(inputLine[1]);
    } else if (inputLine.length == 1) {
      const [online] = inputLine;

      this.onlineList.push(Number(online));
    } else {
      throw new Error("Input Error");
    }
  }

  solution() {
    const { onlineList, N } = this;

    let low = 0;
    let high = Math.max(...onlineList);

    while (low <= high) {
      let mid = Math.floor((low + high) / 2);

      let onlines = onlineList.reduce(
        (pre, cur) => pre + Math.floor(cur / mid),
        0
      );

      onlines >= N ? (low = mid + 1) : (high = mid - 1);
    }

    return high;
  }
}

function main() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  const oc = new OnlineCutting();

  rl.on("line", function (line) {
    oc.doInput(line);
  }).on("close", function () {
    console.log(oc.solution());
    process.exit();
  });
}

main();
