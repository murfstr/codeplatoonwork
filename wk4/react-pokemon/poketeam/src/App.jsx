import { useState } from 'react'
import axios from "axios"
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  const createImg = (url) => {
    let img = document.createElement("img")
    img.src = url
    img.style.height = "30vmin"
    img.style.width = "30vmin"
    img.style.border = "solid 1px black"
    document.getElementById('img-container').appendChild(img)
  }

  const getPokemonImg = async(poke) => {
    let resp = await axios.get(`https://pokeapi.co/api/v2/pokemon/${poke}`)
    let data = resp.data
    return data.sprites.front_default
  }

  const handleSubmit = (evt) => {
    evt.preventDefault()
    console.log("form submitted")
    let input = document.getElementById('user-input')
    let usrInput = input.value
    let imgUrl = getPokemonImg(usrInput)
    createImg(imgUrl)
  }

  return (
    <>
      <form onSubmit={(evt)=>handleSubmit(evt)}>
        <input id='user-input' type='text' placeholder='pokemon name'/>
        <input type='submit'/>
      </form>
      <div id='img-container'>
      </div>
    </>
  )
}

export default App
