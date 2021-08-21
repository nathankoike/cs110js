const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
  crlfDelay: Infinity
});

// Extra space at the beginning for indexing purposes
const Alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ";

function solve(indices, key) {
  let deciphered = [];

  // Build a list of the indices of the deciphered characters
  for (let i = 0; i < indices.length; i++)
    deciphered.push(indices[i] - Alphabet.indexOf(key[i % key.length]));

  return deciphered.map(x => Alphabet[x]).join("");
}

function decrypt(text, keyword) {
  let capturedIndices = [];

  // Build an array of the alphabetical indices of each character in the text
  for (char of text) capturedIndices.push(Alphabet.indexOf(char));

  // Make sure we can solve the Caesar cipher with subtraction
  for (let i = 0; i < capturedIndices.length; i++)
    if (
      capturedIndices[i] <
      Alphabet[Alphabet.indexOf(keyword[i % keyword.length])]
    )
      capturedIndices[i] += 26;

  return solve(capturedIndices, keyword);
}

function getClues(capturedText, keyword) {
  readline.question("Enter the clues separated by one space: ", ans => {
    let clues = ans.split();

    let message = decrypt(capturedText.split().join(""), keyword);

    for (clue of clues)
      if (message.includes(clue))
        console.log("Clue", clue, "discovered in", message);
  });
}

function getKeyword(capturedText) {
  readline.question("Enter a keyword: ", ans => getClues(capturedText, ans));
}

function main() {
  readline.question("Enter the captured text: ", ans =>
    getKeyword(ans.toUpperCase())
  );
}

main();
