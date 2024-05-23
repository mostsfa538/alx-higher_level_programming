#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(url, (err, reponse, body) => {
  if (err) {
    console.log(err);
  }

  const movData = JSON.parse(body);
  const chars = movData.characters;

  for (const charLink of chars) {
    request(charLink, (err, response, body) => {
      if (err) {
        console.log(err);
        return;
      }
      const charName = JSON.parse(body).name;

      console.log(charName);
    });
  }
});
