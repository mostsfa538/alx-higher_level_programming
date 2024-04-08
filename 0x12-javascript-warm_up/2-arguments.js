#!/usr/bin/node

const { argv } = require('process');

console.log(argv.length === 2 ? 'No argument' : (argv.length === 3 ? 'Argument found' : 'Arguments found'));
