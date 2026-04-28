import './App.css'
import Greeting from './components/Greeting'

function App() {
  function handleClick() {
    alert("Clicked")
  }

  return (
    <>
      <Greeting studentName={"Gaitano"} />
      <button onClick={handleClick}>Click Me!</button>
    </>
  )
}

export default App
