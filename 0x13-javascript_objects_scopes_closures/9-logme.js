#!/usr/bin/node
let argumentCnt = 0;

exports.logMe = function (item) {
  console.log(`${argumentCnt}: ${item}`);
  argumentCnt++;
};
