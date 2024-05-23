#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const charId = 18;

request(url, (error, respnose, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const filmData = JSON.parse(body);
  const countChar = filmData.results.filter(film =>
    film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${charId}/`));

  console.log(countChar.length);
});
