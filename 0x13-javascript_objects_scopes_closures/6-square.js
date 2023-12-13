#!/usr/bin/node
const OldSquare = require('./5-square');

class Square extends OldSquare {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      console.log((c || 'X').repeat(this.width));
    }
  }
}

module.exports = Square;
