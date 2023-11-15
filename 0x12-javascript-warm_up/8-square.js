#!/usr/bin/node
const size = process.argv[2];
const convSize = parseInt(size);

if (isNaN(convSize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < convSize; i++) {
    console.log('X'.repeat(convSize));
  }
}
