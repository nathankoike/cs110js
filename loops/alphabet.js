const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
  crlfDelay: Infinity
});

function main() {
  let alphabet = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z"
  ];
  readline.question("Enter some text: ", text => {
    for (let i = 0; i < text.length; i++) {
      let upperText = text.toUpperCase();
      if (alphabet.includes(upperText[i]))
        alphabet.splice(alphabet.indexOf(upperText[i]), 1);
    }

    let absent = "";
    alphabet.map(x => (absent += x));

    console.log("Letters not in the text:", absent);
  });
}

main();
