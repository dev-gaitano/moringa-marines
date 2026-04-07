// LOOPS
// for loop - For when you aalready know how many times you want to iterate
for (let i = 0; i < 10; i++) {
  console.log(i)
}

let z = ["banana", "kiwi"]

// Allows you to iterate the for loop over an array
for (i of z) {
  console.log(i)
}

let nums = [1, 2, 3]

for (i of nums) {
  i = i * 2
  console.log(i)
}

// Returns the index positions of the items in the array
for (i in z) {
  console.log(i)
}
