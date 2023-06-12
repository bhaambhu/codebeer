/**
 * @param {string} val
 * @return {Object}
 */

var expect = function (val) {
  return {
    toBe: (val2) => {
      if (val === val2) return true;
      else {
        throw "Not Equal";
      }
    },
    notToBe(val2) {
      if (val !== val2) return true;
      else {
        throw "Equal";
      }
    },
  };
};

try {
  console.log(expect('10').toBe(10))
  console.log(expect(5).toBe(5)); // true
  expect(5).notToBe(5); // throws "Equal"
} catch (e) {
  console.log(e);
}
