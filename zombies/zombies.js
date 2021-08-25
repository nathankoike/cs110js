const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
  crlfDelay: Infinity
});

const util = require("util");
const question = util.promisify(readline.question).bind(readline);

class Die {
  constructor(sides, team, location, value = 0) {
    this.sides = sides;
    this.team = team;
    this.location = location;
    this.value = value;
  }

  roll() {
    this.value = getRandInt(this.sides);
  }

  changeTeam() {
    this.team = this.team == "vampire" ? "zombie" : "vampire";
  }
}

class Game {
  constructor(numDice) {
    this.turn = 0;

    this.dice = [];

    let sides = [4, 6, 8, 10];
    let teams = ["vampire", "Zombie"];

    for (let i = 0; i < numDice; i++)
      this.dice.push(
        new Die(
          sides[getRandInt(sides.length)],
          teams[getRandInt(teams.length)],
          i
        )
      );
  }

  toString() {
    let result = "";

    for (let die of this.dice)
      result +=
        "Die " +
        die.location +
        ": " +
        die.sides +
        "(" +
        die.team +
        ")" +
        " rolled " +
        die.value +
        "\n";

    return result;
  }

  rollAll() {
    for (let die of this.dice) die.roll();
  }

  isGameOver() {
    let firstTeam = this.dice[0].team;

    for (let die of this.dice) if (die.team != firstTeam) return false;

    return true;
  }

  checkBattles() {
    let needsToSwitch = [];

    for (let i = 0; i < this.dice.length - 1; i++) {
      // Should this die change its team?
      if (
        this.dice[i].value < this.dice[i + 1].value &&
        this.dice[i].team != this.dice[i + 1].team
      )
        needsToSwitch.push(this.dice[i]);

      // Should the next die change its team?
      if (
        this.dice[i].value > this.dice[i + 1].value &&
        this.dice[i].team != this.dice[i + 1].team
      )
        needsToSwitch.push(this.dice[i + 1]);
    }

    return needsToSwitch;
  }

  updateTeams() {
    let needsToSwitch = this.checkBattles();

    for (let die of needsToSwitch) {
      die.changeTeam();
    }
  }

  nextTurn() {
    this.rollAll();
    this.updateTeams();
    this.turn++;
  }
}

function getRandInt(max) {
  return Math.floor(Math.random() * max);
}

function main() {
  let w = new Game(10);
  while (!w.isGameOver()) {
    console.log("Turn", w.turn);
    console.log(w.toString());
    w.nextTurn();
  }

  console.log(`\nFinal status after ${String(w.turn)} turns:`);
  console.log(w.toString());
}

main();
