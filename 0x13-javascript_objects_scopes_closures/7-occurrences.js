#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nb = 0;

  list.forEach(element => {
    if (element === searchElement) {
      nb++;
    }
  });

  return nb;
};
