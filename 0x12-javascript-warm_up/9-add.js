#!/usr/bin/node
function add (a, b) {
  if (process.argv[2] !== undefined || process.argv[3] !== undefined) {
    console.log(Number(process.argv[2]) + Number(process.argv[3]));
  } else {
    console.log('NaN');
  }
}
add(process.argv[2], process.argv[3]);
