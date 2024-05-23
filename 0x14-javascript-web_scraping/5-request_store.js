#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const path = process.argv[3];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  fs.writeFile(path, body, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
