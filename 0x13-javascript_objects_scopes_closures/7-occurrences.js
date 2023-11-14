#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let a = 0;

  for (const element of list) {
    if (element === searchElement) {
      a++;
    }
  }
  return a;
};
