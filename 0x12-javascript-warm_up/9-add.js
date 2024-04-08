#!/usr/bin/node

const add = (a, b) => {
  return a + b;
};

const { argv } = require('process');

if (argv.length < 4) {
  console.log('NaN');
} else {
  console.log(add(parseInt(argv[2]), parseInt(argv[3])));
}
