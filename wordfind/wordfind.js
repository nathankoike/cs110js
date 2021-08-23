function printGrid(grid) {
  for (row of grid) {
    let line = " ";
    row.map(x => (line += x + " "));
    console.log(line);
  }
}

// Traverse the grid for, at most, word.length spaces in the given direction
// from the given starting coordinates, with the coordinates being in the form
// of [row, col] and the direction being in the form of [rStep, cStep]
function traverseDirection(grid, word, start, direction, fn) {
  const [dr, dc] = direction;
  let [r, c] = start;
  let i = 0;

  for (
    let iteratorFn = () => {
      r += dr;
      c += dc;
      i++;
    };
    r >= 0 &&
    r < grid.length &&
    c >= 0 &&
    c < grid[0].length &&
    i < word.length;
    iteratorFn()
  )
    fn(r, c);
}

// Find each word in the grid (case insensitive), and convert those words to
// uppercase, returning the total number of words found
function wordfind(grid, words) {
  let found = 0;

  for (word of words)
    for (let r = 0; r < grid.length; r++)
      for (let c = 0; c < grid[0].length; c++)
        for (let dr = -1; dr < 2; dr++)
          for (let dc = -1; dc < 2; dc++) {
            let built = ""; // We will build the found word in here

            traverseDirection(
              grid,
              word,
              [r, c],
              [dr, dc],
              (y, x) => (built += grid[y][x]) // Builds the found word
            );

            // Capitalize the word if found in the direction
            if (built.toUpperCase() == word.toUpperCase()) {
              traverseDirection(
                grid,
                word,
                [r, c],
                [dr, dc],
                (y, x) => (grid[y][x] = grid[y][x].toUpperCase())
              );

              found++;
            }
          }

  return found;
}

function main() {
  let myGrid = [
    ["j", "m", "w", "e"],
    ["e", "e", "p", "p"],
    ["q", "o", "x", "u"],
    ["w", "w", "e", "d"],
    ["w", "g", "j", "o"]
  ];
  let words = ["wed", "meow", "jexd", "wwxp"];
  printGrid(myGrid);
  console.log(wordfind(myGrid, words));
  printGrid(myGrid);
}

main();
