#!/usr/bin/node
const numbers = process.argv.slice(2).map(Number);
if (numbers.length <= 1) {
  console.log(0);
} else {
  const sortedNumbers = numbers.sort((a, b) => b - a);

  const secondBiggest = sortedNumbers[1];

  console.log(secondBiggest);
}
