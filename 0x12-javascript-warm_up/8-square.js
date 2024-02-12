#!/usr/bin/node
if (isNaN(process.argv[2]) === true) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Number(process.argv[2]); i++) {
    console.log('X'.repeat(Number(process.argv[2])));
  }
}
