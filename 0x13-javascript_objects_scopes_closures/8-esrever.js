#!/usr/bin/node
exports.esrever = function (list) {
  const reversd = [];

  for (let i = list.length - 1; i >= 0; i--) {
    reversd.push(list[i]);
  }

  return reversd;
};
