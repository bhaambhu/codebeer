/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */

function createCounter(init) {
  let count = init;
  return {
    increment() {
      return ++count;
    },
    decrement() {
      return --count;
    },
    reset() {
      return (count = init);
    },
  };
}

const counter = createCounter(5);
console.log(counter.increment()); // 6
console.log(counter.reset()); // 5
console.log(counter.decrement()); // 4
