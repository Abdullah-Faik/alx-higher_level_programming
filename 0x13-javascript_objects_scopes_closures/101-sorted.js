#!/usr/bin/node
const dict = require('./101-data.js').dict;
const sorted = {};

for (const item in dict) {
  if (typeof sorted[dict[item]] === 'undefined') {
    sorted[dict[item]] = [item];
  } else {
    sorted[dict[item]].push(item);
  }
}

console.log(sorted);
