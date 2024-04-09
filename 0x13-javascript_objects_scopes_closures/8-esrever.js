#!/usr/bin/node

exports.esrever = function (list) {
  const arr = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    arr[j] = list[i];
    j += 1;
  }
  return arr;
};
