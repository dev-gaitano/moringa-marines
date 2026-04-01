// Clean the data
// filter scores below 75
// sort in descending order
// Join hyphen-separated string

const rawScores = ["TEST_ENTRY", 45, 88, 92, 34, 76, 95, 81, 10, "SYSTEM_LOG"];

// Clean scores
rawScores.shift()
rawScores.pop()
const cleanedScores = rawScores;

// Filter scores
const filteredScores = cleanedScores.filter(n => n >= 75);

// Sort scores
const sortedScores = filteredScores.sort((a, b) => b - a);

// Join scores
const joinedScores = sortedScores.join(" - ")

console.log(joinedScores)
