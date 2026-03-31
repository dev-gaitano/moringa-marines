// CALLBACK FUNCTIONS
// - A function passed as an argument to another function

function sayHello() {
  console.log("Hello World!");
}

function process(callback) {
  callback(); // Run callback function
}

process(sayHello)


// ARRAYS
// - A list of items stored in a variable

const fruits = ["apple", "banana", "mango"]
// The index starts at 0

console.log(fruits[0])
console.log(fruits[1])

const numbers = [10, 20, 30]
console.log(numbers)
numbers[3] = 40 // Add to a specific index
console.log(numbers)
numbers.push(50) // Add to end of array
console.log(numbers)
numbers.push(60, 70) // Push can push multiple items
console.log(numbers)
numbers.pop() // delete from the end
console.log(numbers)
numbers.unshift(80) // Add to start of array
console.log(numbers)
numbers.shift() // Remove from start of array
console.log(numbers)
numbers.splice(1, 2, 77, 99) // Allows to delete and replace multiple items in array
console.log(numbers)
