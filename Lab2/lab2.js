const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
})

function main() {
  readline.question("Write a sentence: ", sentence => {
    console.log(sentence.slice(0, sentence.indexOf(' ')))
    console.log(sentence.slice(sentence.indexOf(' ') + 1))
  })
}

main()
