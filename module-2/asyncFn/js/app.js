// Store DOM elements in variables
const form = document.querySelector("form")
const email = document.getElementById("exampleInputEmail1").value
const password = document.getElementById("exampleInputPassword1").value
const submitBtn = document.getElementById("submitBtn")

// Listen for form submission
form.addEventListener("submit", async function(e) {
  e.preventDefault()

  try {
    // Get users
    let users = await fetch("https://jsonplaceholder.typicode.com/users")
    users = await users.json()

    // Find user by email
    let user = users.find((user) => user.email === email)

    // Check if user exists
    if (user) {
      console.log(email)
      console.log(user)
    } else {
      console.log(email)
      console.log("Not a user")
    }
  } catch (error) {
    console.log(error)
  }
})

