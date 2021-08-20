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
  readline.question(
    "What time does your upside-down watch read (hours:minutes)? ",
    time => {
      let [timeHrs, timeMin] = split(time, ":").map(x => parseInt(x));

      // 390: 6 hours + 30 mins
      let fixedMins = timeHrs * 60 + timeMin + 390;

      let fixedHours = Math.floor(fixedMins / 60);
      fixedMins -= fixedHours * 60;

      if (fixedHours > 12) fixedHours -= 12;

      console.log(
        "The right-side-up time is:",
        (fixedHours.length < 2 ? "0" + fixedHours : fixedHours) +
          ":" +
          (fixedMins.length < 2 ? "0" + fixedMins : fixedMins)
      );
    }
  );
}

main();
