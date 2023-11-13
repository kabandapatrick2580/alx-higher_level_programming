#!/usr/bin/node
function display () {
  const firstNum = arguments[0];
  if (firstNum === undefined) {
    console.log('No argument');
  } else {
    console.log(firstNum);
  }
}
display(...process.argv.slice(2));
