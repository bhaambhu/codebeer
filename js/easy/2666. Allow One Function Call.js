function once(fn) {
  let called = false;
  return function (...args) {
    if (!called) {
      called = true
      return fn(...args);
    } else {
      return undefined;
    }
  };
}
let onceFn = once(() => console.log("damn"));
onceFn();
onceFn();
onceFn();
