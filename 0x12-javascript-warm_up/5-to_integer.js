#!/usr/bin/node
function to_integer () {
  const argum = process.argv[2];
  const convertedNum = parseInt(argum);
  if (isNaN(convertedNum)) {
    console.log('Not a number');
  } else {
    console.log(`My number : ${convertedNum}`);
  }
}
to_integer();