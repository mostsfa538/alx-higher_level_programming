#!/usr/bin/node

const { argv } = require('process');

if (isNaN(argv[2]) || argv.length === 3) {
  console.log(0);
} else {
  const numbers = argv.slice(2).map(Number);
  const sortedNumbers = numbers.sort((a, b) => a - b);
  const secondBiggest = sortedNumbers[sortedNumbers.length - 2];
  console.log(secondBiggest);
}
