#!/usr/bin/node

const [,, argument] = process.argv;
const number = parseInt(argument);

if (!isNaN(number)) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
