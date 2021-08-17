function getDimensions(grid) {
  return [grid.length, grid[0].length];
}

function twice(ary) {
  let newAry = [];

  for (let i = 0; i < ary.length; i++) newAry.push(ary[i], ary[i]);

  return newAry;
}

function minGrid(grid) {
  let smallest = grid[0][0];

  for (let r = 0; r < grid.length; r++)
    for (let c = 0; c < grid[r].length; c++)
      if (grid[r][c] < smallest) smallest = grid[r][c];

  return smallest;
}

function hasMost(grid, target) {
  if (grid == [[]]) return -1;

  if (grid.length < 2) {
    let count = 0;

    for (let c = 0; c < grid[0].length; c++) if (grid[0][c] == target) count++;

    return count == 0 ? -1 : count;
  }

  let count = -1;
  let most = -1;

  for (let i = 0; i < grid.length; i++) {
    let row = hasMost([grid[i]], target);

    if (row > count) {
      count = row;
      most = i;
    }
  }

  return most;
}

let g = [
  [1, 3, 3],
  [4, 3, 3],
  [7, 8, 9]
];

console.log(hasMost(g, 3));
