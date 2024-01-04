#!/usr/bin/node

// Importing the 'fs' (file system) module
const fs = require('fs');

// Fetching the filename and content from the command line arguments
const filename = process.argv[2];
const content = process.argv[3];

// Writing the content to the file asynchronously
fs.writeFile(filename, content, 'utf-8', err => {
  // Checking if there's an error while writing to the file
  if (err) {
    console.error(err); // Logging the error to the console
  }
});
