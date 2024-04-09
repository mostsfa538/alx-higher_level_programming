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

  rotate () {
    for (let i = 0; i < this.width + this.width; i++) {
      let rectRotate = '';
      for (let i = 0; i < this.height + this.height; i++) {
        rectRotate += 'X';
      }
      console.log(rectRotate);
    }
  }

  double () {
    for (let i = 0; i < this.height * 2; i++) {
      let rectDouble = '';
      for (let i = 0; i < this.width * 2; i++) {
        rectDouble += 'X';
      }
      console.log(rectDouble);
    }
  }
}

module.exports = Rectangle;
