#!/usr/bin/node

// Importing the 'request' module for making HTTP requests
const request = require('request');
// Importing the 'fs' (file system) module
const fs = require('fs');

// Fetching the URL and file path from the command line arguments
const url = process.argv[2];
const filepath = process.argv[3];

// Making a GET request to the specified URL
request(url, (error, response, body) => {
  // Checking if there's an error during the HTTP request
  if (error) {
    console.error(error); // Logging the error to the console
  } else {
    // Writing the body of the HTTP response to a file asynchronously
    fs.writeFile(filepath, body, 'utf-8', (error) => {
      // Checking if there's an error while writing to the file
      if (error) {
        console.log(error); // Logging the error to the console
      }
    });
  }
});
