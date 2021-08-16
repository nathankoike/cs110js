/*
PART A: Preliminaries
*/

function mystery(someArray) {
  let answer = 1;

  for (let i = 0; i < someArray.length; i++) {
    let item = someArray[i];
    item *= 2;
    answer += item;
  }

  return answer;
}

function testMystery() {
  let myArray = [1, 2, 3];
  console.log(mystery(myArray));
  console.log(myArray);
}

// Return the numvber of occurences of item in ary
function count(ary, item) {
  let ans = 0;

  for (let i = 0; i < ary.length; i++) if (ary[i] == item) ans++;

  return ans;
}

// Return an array of the indices i where ary[i] == item
function locations(ary, item) {
  let indices = [];

  for (let i = 0; i < ary.length; i++) if (ary[i] == item) indices.push(i);

  return indices;
}

/*
PART B: Deriving the definition of "split"
*/

function locationsOfLetter(letter, string) {
  let locations = [];

  for (let i = 0; i < string.length; i++)
    if (string[i] == letter) locations.push(i);

  return locations;
}

// Build a list of all the locations of substring in string
function locationsOfSubstr(substring, string) {
  let locations = [];

  for (let i = 0; i < string.length; i++)
    if (string.substr(i, substring.length) == substring) locations.push(i);

  return locations;
}

/*
Return a list of substrings of string, the first one beginning at position 0,
the rest beginning at indices given in positions
*/
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

/*
Using the functions above, write a function that splits a string according to a
sepatarator
*/

function split(string, separator) {
  let ans = divideString(string, locationsOfSubstr(separator, string));

  for (let i = 1; i < ans.length; i++)
    ans[i] = ans[i].substr(separator.length, ans[i].length - separator.length);

  return ans;
}

// -----------------------------------------------------------------------------

console.log(split("this is a test", "is"));
