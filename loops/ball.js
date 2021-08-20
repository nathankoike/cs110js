const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
  crlfDelay: Infinity
});

function getBounceCount(initHeight, firstBounce) {
  readline.question("Enter the number of bounces: ", ans => {
    let bounceCount = parseInt(ans);

    let ratio = firstBounce / initHeight;

    // We'll just modify the height and bounce height in place to save memory
    for (; bounceCount > 0; bounceCount--) {
      initHeight += firstBounce * 2;
      firstBounce *= ratio;
    }

    initHeight += firstBounce;

    console.log(
      "The total distance the ball traveled is",
      String(Math.round(initHeight * 100) / 100),
      "feet."
    );
  });
}

function getFirstBounce(initHeight) {
  readline.question("Enter height of first bounce: ", ans =>
    getBounceCount(initHeight, parseFloat(ans))
  );
}

function main() {
  readline.question("Enter initial height: ", ans =>
    getFirstBounce(parseFloat(ans))
  );
}

main();
