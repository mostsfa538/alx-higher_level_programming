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

  const films = JSON.parse(body).results;
  const count = films.filter(film =>
    film.characters.includes(characterUrl));
  console.log(count.length);
});
