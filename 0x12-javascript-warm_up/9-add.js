#!/usr/bin/node

const { argv } = require('process');

if (argv.length < 4) {
  console.log('NaN');
} else {
  console.log(add(argv[2], argv[3]));
}

function add(a, b) {
  return (a + b);
}
