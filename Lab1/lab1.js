const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
})

function function1() {
  readline.question("Enter an expression: ", expr => {
    let val = eval(expr)
    console.log(expr + " is " + val + " with type " + typeof(val))
  })
}

function function2() {
  console.log("  .   ")
  console.log(" / \\  ")
  console.log("/   \\ ")
  console.log("+---+ ")
  console.log("|   | ")
  console.log("+---+ ")
  console.log()
}

function function3() {
  readline.question("Enter the field length in yards: ", yards => {
    console.log("The field is " + (Number(yards) * 36) + " inches long.")
  })
}

// function1()
// function2()
// function3()
