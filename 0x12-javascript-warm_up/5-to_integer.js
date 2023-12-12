#!/usr/bin/node

const q = parseInt(process.argv[2]);
if (isNaN(q)) {
  console.log('Not a number');
} else {
  console.log('My number:', q);
}
