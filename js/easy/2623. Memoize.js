/**
 * @param {Function} fn
 */

// Use an empty object
function memoizeObject(fn) {
  const cache = {};
  return function (...args) {
    if (!([...args] in cache)) {
      cache[[...args]] = fn(...args);
    }
    return cache[[...args]];
  };
}

// Use the Map object
function memoize(fn) {
  console.log("memoized!!!", memoize)
  const cache = new Map();
  return function (...args) {
    const sArgs = JSON.stringify([...args])
    if (!cache.has(sArgs)) {
      cache.set(sArgs, fn(...args));
    }
    return cache.get(sArgs);
  };
}
memoize.owner = "ABC"


let callCount = 0;
const memoizedFn = memoize(function (a, b) {
  callCount += 1;
  return a + b;
});
console.log(memoizedFn(2, 3)); // 5
memoizedFn(2, 3); // 5
console.log(callCount); // 1

/*
Given a function fn, return a memoized version of that function.

A memoized function is a function that will never be called twice with the same inputs. Instead it will return a cached value.

You can assume there are 3 possible input functions: sum, fib, and factorial.

sum accepts two integers a and b and returns a + b.
fib accepts a single integer n and returns 1 if n <= 1 or fib(n - 1) + fib(n - 2) otherwise.
factorial accepts a single integer n and returns 1 if n <= 1 or factorial(n - 1) * n otherwise.

 */
