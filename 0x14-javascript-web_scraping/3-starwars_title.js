#!/usr/bin/node

// Importing the 'request' module for making HTTP requests
const request = require('request');

// Fetching the movie ID and constructing the API URL
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Making a GET request to the specified URL
request.get(url, (error, response, body) => {
  // Checking if there's an error during the HTTP request
  if (error) {
    console.log(error); // Logging the error to the console
  } else {
    // Parsing the JSON response body
    const data = JSON.parse(body);
    
    // Logging the title of the movie from the parsed JSON data
    console.log(data.title);
  }
});
