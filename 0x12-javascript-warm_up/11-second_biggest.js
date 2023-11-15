#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  let firstLargest = parseInt(args[0]);
  let secondLargest = parseInt(args[1]);

  if (secondLargest > firstLargest) {
    [firstLargest, secondLargest] = [secondLargest, firstLargest];
  }
  for (let i = 2; i < args.length; i++) {
    const currentNumber = parseInt(args[i]);

    if (currentNumber > firstLargest) {
      secondLargest = firstLargest;
      firstLargest = currentNumber;
    } else if (currentNumber > secondLargest && currentNumber < firstLargest) {
      secondLargest = currentNumber;
    }
  }
  console.log(firstLargest);
}
