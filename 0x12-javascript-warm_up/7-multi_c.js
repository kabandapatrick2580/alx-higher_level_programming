#!/usr/bin/node
const arg1 = process.argv[2];
const convNum = parseInt(arg1);

if (isNaN(convNum)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < convNum; i++) {
    console.log('C is fun');
  }
}
