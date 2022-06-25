class goDown {
  constructor() {
    this.N = 0;
    this.lineNum = 0;

    this.MAX = [0, 0, 0];
    this.MIN = [0, 0, 0];
  }

  getInput(line) {
    if (this.lineNum === 0) {
      this.N = Number(line);
      this.lineNum += 1;
    } else if (this.lineNum <= this.N) {
      const inputLine = line.split(" ");

      const x = Number(inputLine[0]);
      const y = Number(inputLine[1]);
      const z = Number(inputLine[2]);

      let p = Math.max(...this.MAX.slice(0, 2));
      let q = Math.max(...this.MAX.slice(1));

      this.MAX[0] = x + p;
      this.MAX[1] = y + Math.max(p, q);
      this.MAX[2] = z + q;

      p = Math.min(...this.MIN.slice(0, 2));
      q = Math.min(...this.MIN.slice(1));

      this.MIN[0] = x + p;
      this.MIN[1] = y + Math.min(p, q);
      this.MIN[2] = z + q;
    } else {
      throw new Error("Input Error");
    }
  }

  solution() {
    return `${Math.max(...this.MAX)} ${Math.min(...this.MIN)}`;
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
