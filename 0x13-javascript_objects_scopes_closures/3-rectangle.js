#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((isNaN(w) || isNaN(h)) || w <= 0 || h <= 0) {
      return 'Rectangle {}';
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let rect = '';
      for (let i = 0; i < this.width; i++) {
        rect += 'X';
      }
      console.log(rect);
    }
  }
}

module.exports = Rectangle;
