#!/usr/bin/node
function printArgs (arg1, arg2) {
  console.log(`${arg1} in ${arg2}`);
}

const [arg1, arg2] = process.argv.slice(2);
printArgs(arg1, arg2);
