function quickSort(values) {
  if (!Array.isArray(values)) {
    throw new TypeError('quickSort expects an array');
  }

  if (values.length <= 1) {
    return values.slice();
  }

  const [pivot, ...rest] = values;
  const left = [];
  const right = [];

  for (const value of rest) {
    if (value < pivot) {
      left.push(value);
    } else {
      right.push(value);
    }
  }

  return [...quickSort(left), pivot, ...quickSort(right)];
}

const demoValues = [8, 3, 5, 1, 9, 2, 7, 4, 6];
console.log('before:', demoValues);
console.log('after: ', quickSort(demoValues));

module.exports = { quickSort };
