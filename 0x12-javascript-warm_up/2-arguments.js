#!/usr/bin/node
let res;
if (process.argv.length === 3) {
  res = 'Argument found';
} else if (process.argv.length > 3) {
  res = 'Arguments found';
} else {
  res = 'No argument';
}
console.log(res);
