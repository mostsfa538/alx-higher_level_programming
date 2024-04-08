#!/usr/bin/node

const { argv } = require('process');

console.log(argv.length === 2 ? 'undefined is undefined' : (argv.length === 3 ? argv[2] + ' is undefined' : argv[2] + ' is ' + argv[3]));
