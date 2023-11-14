#!/usr/bin/node
const { dict } = require('./101-data');

const invrtDict = {};

for (const [userId, occurrences] of Object.entries(dict)) {
  if (!invrtDict[occurrences]) {
    invrtDict[occurrences] = [];
  }
  invrtDict[occurrences].push(userId);
}

console.log(invrtDict);
