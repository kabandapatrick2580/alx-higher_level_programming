#!/usr/bin/node

// Importing the 'request' module for making HTTP requests
const request = require('request');

// Constructing the URL using a base URL and the movie ID from the command line arguments
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

// Making a GET request to the specified URL
request(url, function (error, response, body) {
  // Checking if there's no error during the HTTP request
  if (!error) {
    // Parsing the JSON response body to extract character URLs
    const characters = JSON.parse(body).characters;

    // Calling the printCharacters function to print the names of characters
    printCharacters(characters, 0);
  }
});

// Function to print the names of characters recursively
function printCharacters(characters, index) {
  // Making a GET request to the character URL at the given index
  request(characters[index], function (error, response, body) {
    // Checking if there's no error during the HTTP request
    if (!error) {
      // Parsing the JSON response body to extract the character name
      console.log(JSON.parse(body).name);

      // Checking if there are more characters in the array
      if (index + 1 < characters.length) {
        // Recursively calling the function for the next character
        printCharacters(characters, index + 1);
      }
    }
  });
}
