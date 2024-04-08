#!/usr/bin/node

const factorial = (number) => {
  if (number === 1) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
};

const { argv } = require('process');

const inputNumber = parseInt(argv[2]);
if (isNaN(inputNumber)) {
  console.log('1');
} else {
  console.log(factorial(inputNumber));
}
