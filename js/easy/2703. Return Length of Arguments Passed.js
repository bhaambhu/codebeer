/**
 * @return {number}
 */
var argumentsLength = function(...args) {
  console.log(typeof arguments)
  return args.length
};
let x = [1,2,3]
console.log(typeof x)
console.log(typeof [1,2,3])
console.log(argumentsLength(1, 2, 3)); // 3
