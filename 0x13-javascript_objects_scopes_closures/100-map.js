#!/usr/bin/node
const list = require('./100-data.js').list;

const anotherList = list.map((val, id) => val * id);
console.log(list);
console.log(anotherList);
