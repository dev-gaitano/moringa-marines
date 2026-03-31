// BLOCK SCOPE (LET & CONST)
// Variables are declared inside {}
// Only exist inside that Block

if (true) {
  let x = 10;
  const y = 20;
}

function multiply(a, b) {
  a * b; // No return
}

const result = multiply(7, 9);
//console.log(result); // logs undefined
//console.log(multiply(7, 9)) // logs undefined


// OPERATORS
// Comparison operators
// Assignment operators
// Arithmetic operators

const x = 9;
const y = "9";

strictEqualityOperator = x === y; // Checks if both the values and the data types are the same
looseEqualityOperator = x == y; // Compares only the values not the data type
looseInequalityOperator = x != y; // The `!` is the Inequality operator
strictInequalityOperator = x !== y; // The `===` equivalent of the Inequality operator

//console.log(strictEqualityOperator); // false
//console.log(looseEqualityOperator); // true
//console.log(looseInequalityOperator); // false
//console.log(strictInequalityOperator); // true

const poorOperatorUse = !x == y; // (!x) == y; -> false == "9"; -> false



// ASSIGNMENT: Player Stats Checker
// Each player has individual variables storing their scores
// Checks if player score is missing
// Determines if a player is "active" (0) or "inactive" (1)
// (Nested) Calculates player bonus based on score (score > 50 = score * 0.1)
// Returns player info

const validatePlayer = (score, activity) => {
  // Check if player has a valid score
  if (!score) {
    return false
  } else {
    // Check if player is active
    if (activity === 1) {
      return true
    } else if (activity === 0) {
      return false
    }
  }
}

// Calculate bonus function
const calculateBonus = (score) => {
  if (score >= 50) {
    return score * 0.1
  } else {
    return score * 0.05
  }
}

// Main application function
function main() {
  const playerData = ["Hugo Ekitike", 10, 1] // playerData = [name, score, activity]

  if (validatePlayer(playerData[1], playerData[2])) {
    // Log player info to console
    console.log(`Name: ${playerData[0]}`)
    console.log(`Score: ${playerData[1]}`)
    console.log(`Activity: ${playerData[2]}`)
    console.log(`Bonus: ${calculateBonus(playerData[1])}`)
    return calculateBonus(playerData[1])
  } else {
    console.log("Oops! Score invalid or player inactive")
    return 0
  }
}

main()
