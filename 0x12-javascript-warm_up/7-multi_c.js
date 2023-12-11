#!/usr/bin/node
const mVar = 'C is fun';
const mArgs = process.argv.splice(2);
const num = Number(mArgs[0]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  for (i = 0; i < num; i++) {
    console.log(mVar);
  }
}
