import { useState } from 'react'
import './App.css'
import onImg from "../icons/on.svg"
import offImg from "../icons/off.svg"
// icons/on.svg
// mute_button/src/App.jsx
function App() {

  const [onOff, setOnOff] = useState(false)

  const handleClick = () => {
    if (onOff) {
      setOnOff(false) //turns off
    }
    else {
      setOnOff(true) //turns on
    }
  }
  let displayedImg = onImg
  let buttonText = "turn off"
  
  if (onOff) {
    displayedImg = offImg
    buttonText = "turn on"
  }
  
  return (
    <>
      <h1>ON/OFF Switch</h1>
      <img src={displayedImg}></img>
      <button onClick={handleClick}>{buttonText}</button>
    </>
  )
}

export default App
