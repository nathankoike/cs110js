const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
  crlfDelay: Infinity
});

function locationsOfLetter(letter, string) {
  let locations = [];

  for (let i = 0; i < string.length; i++)
    if (string[i] == letter) locations.push(i);

  return locations;
}

function locationsOfSubstr(substring, string) {
  let locations = [];

  for (let i = 0; i < string.length; i++)
    if (string.substr(i, substring.length) == substring) locations.push(i);

  return locations;
}

function divideString(string, positions) {
  let subs = [];
  let substring = "";

  for (let i = 0; i < string.length; i++) {
    if (i == positions[0]) {
      positions.shift();
      subs.push(substring);
      substring = "";
    }
    substring += string[i];
  }

  subs.push(substring);

  return subs;
}

function split(string, separator) {
  let ans = divideString(string, locationsOfSubstr(separator, string));

  for (let i = 1; i < ans.length; i++)
    ans[i] = ans[i].substr(separator.length, ans[i].length - separator.length);

  return ans;
}

function main() {
  readline.question("Enter the digits as input to the microwave: ", input => {
    if (input.includes(":")) {
      let [min, sec] = split(input, ":").map(x => parseInt(x));

      for (; min >= 0; min--) {
        for (; sec >= 0; sec--)
          console.log(
            (min > 9 ? String(min) : "0" + String(min)) +
              ":" +
              (sec > 9 ? String(sec) : "0" + String(sec))
          );

        sec += 60;
      }

      console.log("00:00");
    }
  });
}

main();
