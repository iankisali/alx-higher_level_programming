#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const complete = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!complete[todo.userId]) {
        complete[todo.userId] = 1;
      } else {
        complete[todo.userId] += 1;
      }
    }
  });
  console.log(complete);
});
