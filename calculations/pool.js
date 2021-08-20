const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
  crlfDelay: Infinity
});

function getFlow(length, width, depth) {
  readline.question("Water fill rate (gal/min): ", ans => {
    let flow = parseFloat(ans);

    let volume = length * width * depth * 7.48051948;
    let timeSec = (volume / flow) * 60;

    timeHrs = String(Math.floor(timeSec / 3600));
    timeSec -= parseInt(timeHrs) * 3600;

    timeMin = String(Math.floor(timeSec / 60));
    timeSec = Math.round(parseInt(timeSec) - timeMin * 60);

    console.log(
      "Time: " +
        (timeHrs.length < 2 ? "0" + timeHrs : timeHrs) +
        ":" +
        (timeMin.length < 2 ? "0" + timeMin : timeMin) +
        ":" +
        (timeSec.length < 2 ? "0" + timeSec : timeSec)
    );
  });
}

function getDepth(length, width) {
  readline.question("Additional depth desired (inches): ", ans =>
    getFlow(length, width, parseFloat(ans) / 12)
  );
}

function getWidth(length) {
  readline.question("Pool width (feet): ", ans =>
    getDepth(length, parseFloat(ans))
  );
}

function main() {
  readline.question("Pool length (feet): ", ans => getWidth(parseFloat(ans)));
}

main();
