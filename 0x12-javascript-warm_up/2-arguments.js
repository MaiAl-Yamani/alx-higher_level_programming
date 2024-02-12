#!/usr/bin/node
const { argv } = require('node:process');
let res;
if (argv.length === 3) {
  res = 'Argument found';
} else if (argv.length > 3) {
  res = 'Arguments found';
} else {
  res = 'No argument';
}
console.log(res);
