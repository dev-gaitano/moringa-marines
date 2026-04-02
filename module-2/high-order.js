let strArray = ["gaitano", "Qoli", "mohammad", "sara", "mohammad", "lina", "Quinta", "sara", "mohammad", "lina"];


// Filter
function filteringCriteria(name) {
  if (name[0] !== "Q") {
    console.log(true)
    return true
  } else {
    console.log(false)
    return false
  }
}

//strArray = strArray.filter(name => name[0] !== "Q")
strArray = strArray.filter(filteringCriteria)
//console.log(strArray)

// Map
function double(n) {
  return n * 2
}

let nums = [1, 2, 3, 4, 5, 6]

//nums = nums.map(n => n * 2)
//console.log(nums)


// Sort
nums = nums.sort((a, b) => b - a)
//console.log(nums)

// Reduce
//function sum(prevValue, currentValue) {
//return prevValue + currentValue;
//}

nums = nums.reduce((a, b) => a + b)
console.log(nums)
