#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi.dev/api/films/${id}/`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const data = JSON.parse(body);
  const chars = data.characters;
  for (const character of chars) {
    request(character, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      const charData = JSON.parse(body);
      console.log(charData.name);
    });
  }
});
