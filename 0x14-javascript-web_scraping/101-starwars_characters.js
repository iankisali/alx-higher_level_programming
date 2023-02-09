#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi.dev/api/films/${id}/`;
let chars = [];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const data = JSON.parse(body);
  chars = data.characters;
  getCharacters(0);
});
const getCharacters = (index) => {
  if (index === chars.length) {
    return;
  }
  request(chars[index], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    const charData = JSON.parse(body);
    console.log(charData.name);
    getCharacters(index + 1);
  });
};
