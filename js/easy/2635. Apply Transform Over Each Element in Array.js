var map = function (arr, fn) {
  const newArr = [];
  for (let i = 0; i < arr.length; i++) {
    newArr.push(fn(arr[i], i));
  }
  return newArr;
};

console.log(map([1, 2, 3], (x) => x + 10));
