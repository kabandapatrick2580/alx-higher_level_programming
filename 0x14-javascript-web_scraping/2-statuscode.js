#!/usr/bin/node

// Importing the 'request' module for making HTTP requests
const request = require('request');

// Fetching the URL from the command line arguments
const url = process.argv[2];

// Making a GET request to the specified URL
request.get(url, (error, response) => {
  // Checking if there's an error during the HTTP request
  if (error) {
    console.log(error); // Logging the error to the console
  } else {
    // Logging the HTTP status code from the response
    console.log(`code: ${response.statusCode}`);
  }
});
