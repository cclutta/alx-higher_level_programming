#!/usr/bin/node

const req = require('request');

req.get(process.argv[2], (err, res, body) => {
  if (err) console.log(err);
  else {
    let i = 0;
    const movies = JSON.parse(body).results;
    movies.forEach(movie => {
      movie.characters.forEach(character => {
        if (character.includes('people/18/')) i++;
      });
    });
    console.log(i);
  }
});
