"use strict";
require("babel-core/register");
require("babel-polyfill");

var asyncFun = function () {
  var _ref = _asyncToGenerator(/*#__PURE__*/regeneratorRuntime.mark(function _callee() {
    var value;
    return regeneratorRuntime.wrap(function _callee$(_context) {
      while (1) {
        switch (_context.prev = _context.next) {
          case 0:
            _context.next = 2;
            return Promise.resolve(1).then(function (x) {
              return x * 3;
            }).then(function (x) {
              return x + 5;
            }).then(function (x) {
              return x / 2;
            });

          case 2:
            value = _context.sent;
            return _context.abrupt("return", value);

          case 4:
          case "end":
            return _context.stop();
        }
      }
    }, _callee, this);
  }));

  return function asyncFun() {
    return _ref.apply(this, arguments);
  };
}();

function _asyncToGenerator(fn) {
  return function () {
    var gen = fn.apply(this, arguments);
    return new Promise(function (resolve, reject) {
      function step(key, arg) {
        try {
          var info = gen[key](arg);
          var value = info.value;
        } catch (error) {
          reject(error);
          return;
        }
        if (info.done) {
          resolve(value);
        } else {
          return Promise.resolve(value).then(function (value) {
            step("next", value);
          }, function (err) {
            step("throw", err);
          });
        }
      }

      return step("next");
    });
  };
}

asyncFun().then(function (x) {
  return console.log("x: " + x);
});
