#!/usr/bin/node

// Importing the 'request' module for making HTTP requests
const request = require('request');

// Making a GET request to the specified URL with JSON response expected
request.get(process.argv[2], { json: true }, (error, response, body) => {
  // Checking if there's an error during the HTTP request
  if (error) {
    console.log(error); // Logging the error to the console
    return; // Exiting the function early if there's an error
  }

  // Initializing an object to store the count of completed tasks per user
  const tasksCompleted = {};

  // Iterating through each todo item in the response body
  body.forEach((todo) => {
    // Checking if the task is completed
    if (todo.completed) {
      // Updating the count of completed tasks for each user
      if (!tasksCompleted[todo.userId]) {
        tasksCompleted[todo.userId] = 1;
      } else {
        tasksCompleted[todo.userId] += 1;
      }
    }
  });

  // Logging the final count of completed tasks per user to the console
  console.log(tasksCompleted);
});
