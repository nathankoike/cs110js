class Elevator {
  constructor(number, floor, direction, moving, target, buttons) {
    this.number = number;
    this.floor = floor; // true for up, false for down
    this.direction = direction;
    this.moving = moving;
    this.target = target;
    this.buttons = buttons;
  }

  getNumber() {
    return this.number;
  }

  getFloor() {
    return this.floor;
  }

  getDirection() {
    return this.direction ? "up" : "down";
  }

  getTarget() {
    return this.target;
  }

  getMoving() {
    return this.moving;
  }

  getButtons() {
    return this.buttons;
  }

  toggleElev() {
    this.moving = !this.moving;
  }

  setTarget(goal) {
    this.target = goal;
  }
}

class Building {
  constructor(numElevators = 1, topFloor = 1) {
    this.topFloor = topFloor;

    this.elevs = [];

    for (let i = 0; i < numElevators; i++)
      this.elevs.push(new Elevator(i, 1, true, false, 0, []));
  }

  toString() {
    let fullReport = "";

    for (let i = 0; i < this.elevs.length; i++) {
      let report = "";

      report += "\n +++ Elevator " + this.elevs[i].getNumber() + " +++\n";
      report += " On floor:           " + this.elevs[i].getFloor() + "\n";
      report += " Aimed in direction: " + this.elevs[i].getDirection() + "\n";
      report += " Currently moving:   " + this.elevs[i].getMoving() + "\n";
      report += " Target floor:       " + this.elevs[i].getTarget() + "\n";
      report += " Buttons pushed:     " + this.elevs[i].getButtons() + "\n";

      fullReport += report;
    }
    return fullReport;
  }

  move(elevNum, goal) {
    let elev = this.elevs[elevNum];

    elev.setTarget = goal;
    elev.moving = true;

    if (elev.getFloor() < goal) elev.direction = false;
    else if (elev.getFloor > goal) elef.direction = true;
  }
}

let b = new Building();

console.log(b.toString());
