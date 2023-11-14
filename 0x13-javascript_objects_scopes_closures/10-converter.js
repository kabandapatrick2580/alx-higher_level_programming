#!/usr/bin/node
exports.converter = function (base) {
  function myConverter (c) {
    return c.toString(base);
  }
  return myConverter;
};
