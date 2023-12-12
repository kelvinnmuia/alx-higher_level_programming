#!/usr/bin/node
const dict = require('./101-data.js').dict;
const nwDict = {};
for (const key in dict) {
  if (nwDict[dict[key]] === undefined) {
    nwDict[dict[key]] = [key];
  } else {
    nwDict[dict[key]].push(key);
  }
}
console.log(nwDict);
