const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
  crlfDelay: Infinity
});

function calc(temp, speed) {
  let chill =
    0.6215 * temp +
    35.74 -
    35.75 * Math.pow(speed, 0.16) +
    0.4275 * temp * Math.pow(speed, 0.16);

  console.log(
    "At " + temp + " degrees, with a wind speed of " + speed,
    "miles per hour,\nthe windchill is:",
    chill + " degrees"
  );
}

function getSpeed(temp) {
  readline.question("Enter the wind speed: ", ans => {
    calc(temp, parseInt(ans));
  });
}

function main() {
  console.log("Welcome to the windchill calculator!");

  readline.question("Enter the temperature: ", ans => {
    getSpeed(parseInt(ans));
  });
}

main();
