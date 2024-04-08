#!/usr/bin/node

function callMeMoby (x, theFunction) {
  while (x--) {
    theFunction();
  }
}

module.exports.callMeMoby = callMeMoby;
