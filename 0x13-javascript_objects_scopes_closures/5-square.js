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
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Rectangle;
module.exports = Square;
