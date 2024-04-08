#!/usr/bin/node

const factorial = (number) => {
  if (number === 1) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
};

const { argv } = require('process');

if (argv.length < 3) {
  console.log(1);
} else {
  console.log(parseInt(factorial(argv[2])));
}
