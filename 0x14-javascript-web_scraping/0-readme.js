#!/usr/bin/node

// Importing the 'fs' (file system) module
const fs = require('fs');

// Fetching the filename from the command line arguments
const filename = process.argv[2];

// Reading the contents of the file asynchronously
fs.readFile(filename, 'utf-8', (err, data) => {
  // Checking if there's an error while reading the file
  if (err) {
    console.log(err); // Logging the error to the console
  } else {
    console.log(data); // Logging the content of the file to the console
  }
});
