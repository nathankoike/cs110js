/*
long comment
*/

const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout
});

function reverse(string) {
  let reversed = "";

  for (let i = string.length - 1; i >= 0; i--) {
    reversed += string[i];
  }

  return reversed;
}

function main() {
  readline.question(
    "Enter a number to serve as an upper bound for the summation of perfect squares: ",
    upper_int => {
      let sum = 0;
      for (let val = 1; val <= upper_int; val++) sum += Math.pow(val, 2);

      console.log(sum);
      console.log(reverse(sum.toString()));
    }
  );
}

main();
