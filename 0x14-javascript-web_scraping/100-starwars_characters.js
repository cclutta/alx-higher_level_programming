#!/usr/bin/node

const req = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

req.get(url, (err, res, body) => {
  if (err) console.log(err);
  else {
    JSON.parse(body).characters.forEach(character => {
      req.get(character, (err, res, body) => {
        if (err) console.log(err);
        else console.log(JSON.parse(body).name);
      });
    });
  }
});
