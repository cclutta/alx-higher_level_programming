#!/usr/bin/node

exports.esrever = function (list) {
  const reversed = [];
  let revlength = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    reversed[revlength] = list[i];
    revlength++;
  }
  return reversed;
};
