#!/usr/bin/node

const oldSquare = require('./5-square');

class Square extends oldSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let rect = '';
      for (let j = 0; j < this.width; j++) {
        rect += c;
      }
      console.log(rect);
    }
  }
}

module.exports = Square;
