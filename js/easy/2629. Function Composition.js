/**
 * @param {Function[]} functions
 * @return {Function}
 */

// Recursive approach
// var compose = function (functions) {
//   return function (x) {
//     if (functions.length === 0) return x;
//     let firstFunction = functions.shift();
//     return firstFunction(compose(functions)(x));
//   };
// };

// Loop approach
var compose = function (functions) {
  return function (x) {
    let accum = x;
    for (let i = functions.length - 1; i >= 0; i--) {
      accum = functions[i](accum);
    }
    return accum;
  };
};

const fn = compose([(x) => x + 1, (x) => 2 * x]);
console.log(fn(4)); // 9
