#!/usr/bin/node
function to_integer () {
  const argum = process.argv[2];
  const convertedNum = Number(argum);
  if (!isNaN(convertedNum)) {
    console.log(`My number : ${convertedNum}`);
  } else {
    console.log('Not a number');
  }
}
to_integer();