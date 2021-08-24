class LazyList {
  constructor(start) {
    this.head = start;
  }

  next() {
    return this.head++;
  }
}

class Seive extends LazyList {
  constructor(start) {
    super(start);

    this.found = [];

    this.filter = x => {
      for (let prime of this.found) if (x % prime == 0) return false;
      return true;
    };
  }

  nextPrime() {
    while (!this.filter(this.head)) {
      // console.log(this.head);
      this.next();
    }

    this.found.push(this.head);

    return this.next();
  }
}

let GlobalSieve = new Seive(2);

function sumDigits(num) {
  let sum = 0;

  for (const digit of String(num)) sum += parseInt(digit);

  return sum;
}

function prime(num) {
  while (GlobalSieve.nextPrime() < num);

  return GlobalSieve.found.includes(num);
}

function additivePrime(num) {
  if (num < 10) {
    return prime(num);
  }

  if (prime(num)) return additivePrime(sumDigits(num));

  return false;
}

// Returns an array of all the additive prime numbers on the interval [1, n]
function additivePrimesList(n) {
  return Array.from(Array(n + 2).keys())
    .splice(2)
    .filter(additivePrime);
}

function main() {
  console.log(additivePrimesList(10000));
}

main();
