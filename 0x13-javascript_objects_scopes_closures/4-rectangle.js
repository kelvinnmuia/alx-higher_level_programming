#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // method that prints the rectangle
  print () {
    for (let i = 0; i < this.height; i++) console.log('X'.repeat(this.width));
  }

  // method for rotating the rectangle
  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  // method that doubles the rectangle height and width
  double () {
    this.height *= 2;
    this.width *= 2;
  }
};
