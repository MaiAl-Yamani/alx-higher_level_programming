#!/usr/bin/node
function secondbiggest (arr) {
  if (arr.length < 4) {
    return 0;
  }
  arr.splice(arr[0], 2);
  const max = Math.max.apply(null, arr);
  arr.splice(arr.indexOf(max), 1);
  return Math.max.apply(null, arr);
}
console.log(secondbiggest(process.argv));
