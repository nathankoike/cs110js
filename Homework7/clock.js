const S = String;

class Clock {
  constructor(hrs, min, sec) {
    this.hrs = hrs;
    this.min = min;
    this.sec = sec;

    this.display24Hour = false;
  }

  toString() {
    let hours = this.display24Hour ? this.hrs : this.hrs % 12;

    let result =
      (S(hours).length < 2 ? "0" + S(hours) : S(hours)) +
      ":" +
      (S(this.min).length < 2 ? "0" + S(this.min) : S(this.min)) +
      ":" +
      (S(this.sec).length < 2 ? "0" + S(this.sec) : S(this.sec));

    if (!this.display24Hour) result += this.hrs > 12 ? " PM" : " AM";

    return result;
  }

  tick() {
    this.sec++;

    if (this.sec > 59) {
      this.sec = 0;
      this.min++;

      if (this.min > 59) {
        this.min = 0;
        this.hrs++;

        if (this.hrs > 23) this.hrs = 0;
      }
    }
  }

  toggle24HourFormat() {
    this.display24Hour = !this.display24Hour;
  }
}

function main() {
  let myClock = new Clock(23, 58, 58);
  console.log(myClock.toString());
  myClock.toggle24HourFormat();

  console.log(myClock.toString());

  for (let _ = 0; _ < 63; _++) {
    myClock.tick();
    console.log(myClock.toString());
  }
}

main();
