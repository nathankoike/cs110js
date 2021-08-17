function mystery(n) {
  let result = [];

  for (let i = 0; i < n; i++) {
    result.push([]);

    for (let j = 0; j < n; j++) result[result.length - 1].push([i, j]);
  }

  return result;
}

// lastNum should be an integer
function printsSomething(lastNum) {
  for (let i = 1; i <= lastNum; i++) {
    let x = String(i);

    for (let j = 0; j < String(lastNum).length; j++)
      if (x.length < String(lastNum).length) x = " " + x;

    if (parseInt(x) % 10 == 0) console.log(x);
    else console.log(x, "ree");
  }
}

function printLists(lists) {
  for (let i = 0; i < lists.length; i++) console.log(lists[i]);
}

// Copy a list into a new list
function copyList(list) {
  let newList = [];

  for (let i = 0; i < list.length; i++) newList.push(list[i]);

  return newList;
}

function worksWithLists() {
  let tenThings = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
  let lists = [];

  for (let i = 0; i < 8; i++) lists.push(copyList(tenThings));

  printLists(lists);

  console.log("------------------------------");
  lists[5][5] = 100;
  printLists(lists);
}

// -----------------------------------------------------------------------------

console.log(worksWithLists());
