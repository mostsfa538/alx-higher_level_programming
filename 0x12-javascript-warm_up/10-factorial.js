#!/usr/bin/node

const factorial = (number) => {
  if (isNaN(number) || number === 0) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
};

const { argv } = require('process');

const n = parseInt(argv[2]);

console.log(factorial(n));
