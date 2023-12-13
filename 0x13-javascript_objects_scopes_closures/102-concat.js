#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], function (error1, data1) {
  if (error1) {
    throw error1;
  }

  fs.readFile(process.argv[3], function (error2, data2) {
    if (error2) {
      throw error2;
    }

    fs.writeFile(process.argv[4], data1 + data2, function (error3) {
      if (error3) {
        throw error3;
      }
    });
  });
});
