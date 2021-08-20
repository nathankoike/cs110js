const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
  crlfDelay: Infinity
});

function getNewDia(normRad, normSlices, countSlices) {
  readline.question(
    "What is the diameter of the pies you will buy? ",
    bigDia => {
      let bigRad = parseInt(bigDia) / 2;

      normArea = Math.PI * Math.pow(parseInt(normRad), 2);
      totalArea = (normArea / parseInt(normSlices)) * parseInt(countSlices);

      bigArea = Math.PI * Math.pow(bigRad, 2);

      console.log(Math.pow(parseInt(normRad), 2), countSlices);

      console.log(
        "You will need to buy",
        String(Math.ceil(totalArea / bigArea)),
        bigDia + "-inch diameter pies."
      );
    }
  );
}

function getSliceCount(normRad, normSlices) {
  readline.question("How many standard slices do you want? ", ans =>
    getNewDia(normRad, normSlices, ans)
  );
}

function getNormSlices(normRad) {
  readline.question('How many slices are in a "standard" size pie? ', ans =>
    getSliceCount(normRad, ans)
  );
}

function main() {
  readline.question('What is the diameter of a "standard" size pie? ', ans =>
    getNormSlices(ans / 2)
  );
}

main();
