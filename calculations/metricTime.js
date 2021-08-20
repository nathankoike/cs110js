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
    "Enter the time of day in 24-hour time (HH:MM:SS): ",
    earthTime => {
      let [earthHrs, earthMin, earthSec] = split(earthTime, ":").map(x =>
        parseInt(x)
      );

      // The ratio between seconds and "metric units"
      let ratio = 100000 / 86400;

      let metricSec = (earthHrs * 3600 + earthMin * 60 + earthSec) * ratio;

      metricHrs = String(Math.floor(metricSec / 1000));
      metricSec -= parseInt(metricHrs) * 1000;

      metricMin = String(Math.floor(metricSec / 100));
      metricSec -= parseInt(metricMin) * 100;

      let [secInt, secDec] = split(
        String(Math.round(metricSec * 100) / 100),
        "."
      );

      console.log('The "metric" time is:');
      console.log(
        (metricHrs.length < 2 ? "0" + metricHrs : metricHrs) +
          ":" +
          (metricMin.length < 2 ? "0" + metricMin : metricMin) +
          ":" +
          (secInt.length < 2 ? "0" + secInt : secInt) +
          "." +
          (secDec.length < 2 ? secDec + "0" : secDec)
      );
    }
  );
}

main();
