#!/usr/bin/node
const request = require('request')


const movieId = process.argv[2];
const endpoint = `https://swapi-api.hbtn.io/api`;

request(url, async (err, respons, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const charactersArray = JSON.parse(respons.body).characters;
  for (const character of charactersArray) {
    await new promise((resolve, reject) => {
      request(character, (err, respons, body) => {
        if (err) {
          console.log(err);
          reject();
       }

       console.log(JSON.parse(body).name);
       resolve();
     });
   });
  }
});
