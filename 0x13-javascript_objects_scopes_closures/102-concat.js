#!/usr/bin/node

const fuse = require('fs');

function concatFiles (srceFile1, srceFile2, destinationFile) {
  try {
    const data1 = fuse.readFileSync(srceFile1, 'utf8');
    const data2 = fuse.readFileSync(srceFile2, 'utf8');
    const concatenatedData = data1 + data2;

    fuse.writeFileSync(destinationFile, concatenatedData);

    console.log(`Concatenated ${srceFile1} and ${srceFile2} to ${destinationFile}`);
  } catch (error) {
    console.error('An error occurred:', error.message);
  }
}

const srceFile1 = process.argv[2];
const srceFile2 = process.argv[3];
const destinationFile = process.argv[4];

if (!srceFile1 || !srceFile2 || !destinationFile) {
  console.log('Usage: node concat.js <srceFile1> <srceFile2> <destinationFile>');
} else {
  concatFiles(srceFile1, srceFile2, destinationFile);
}
