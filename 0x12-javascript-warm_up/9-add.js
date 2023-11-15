#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const arg1 = process.argv[2];
const arg2 = process.argv[3];

const convArga = parseInt(arg1);
const convArgb = parseInt(arg2);

if (isNaN(convArga) || (isNaN(convArgb))) {
  console.log('NaN');
} else {
  const result = add(convArga, convArgb);
  console.log(result);
}
