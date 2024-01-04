#!/usr/bin/node

// Importing the 'request' module for making HTTP requests
const request = require('request');

// Fetching the movie ID and constructing the API URL
const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

// Making a GET request to the specified movie URL
request.get(url, (error, response, body) => {
  // Checking if there's an error during the HTTP request
  if (error) {
    console.log(error); // Logging the error to the console
    return; // Exiting the function early if there's an error
  }

  // Parsing the JSON response body for movie details
  const data = JSON.parse(body);

  // Extracting the array of character URLs from the movie data
  const characters = data.characters;

  // Iterating through each character URL
  for (const character of characters) {
    // Making a GET request to each character URL
    request(character, (error, response, body) => {
      // Checking if there's an error during the HTTP request
      if (error) {
        console.log(error); // Logging the error to the console
        return; // Exiting the function early if there's an error
      }

      // Parsing the JSON response body for character details
      const characterData = JSON.parse(body);

      // Logging the name of each character to the console
      console.log(characterData.name);
    });
  }
});
