function sum(a, b) {
  return a + b
}

console.log(sum(1, 2))

function weatherForecast(temp) {
  if (temp >= 30) {
    console.log("Hot")
  } else {
    console.log("cold")
  }
}

weatherForecast(30)

let result = 0;
function add(num) {
  let result = num + 5;
  return result;
}
add(10);
console.log(result);


(function() {
  var a = b = 5;
})();

console.log(b);
