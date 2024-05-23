#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const data = JSON.parse(body);

  const emp = {};
  for (const todo of data) {
    if (todo.completed) {
      if (emp[todo.userId]) {
        emp[todo.userId]++;
      } else {
        emp[todo.userId] = 1;
      }
    }
  }

  console.log(emp);
});
