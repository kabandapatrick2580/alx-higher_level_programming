#!/usr/bin/node

const argum = process.argv[2];
const convertedNum = parseInt(argum);
if (isNaN(convertedNum)) {
  console.log('Not a number');
} else {
  console.log(`My number : ${convertedNum}`);
}
