#!/usr/bin/node

const request = require('request');
const baseUrl = process.argv[2];
const id = 18;
const characterUrl = `https://swapi-api.alx-tools.com/api/people/${id}/`;

request(baseUrl, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;

    films.forEach(film => {
      if (film.characters.includes(characterUrl)) {
        count++;
      }
    });
    console.log(count);
  }
});
