import React from 'react'

const Componente1 = (props) => {
  const anni = 20;
  return (
    <div style={{ color: "white", fontWeight: "600", margin: "15px", border: "1px #000 solid", padding: " 15px", backgroundColor: "grey" }}>
      Componente1 {props.children} di anni {anni}
      <Anagrafica></Anagrafica>
      <Messaggio></Messaggio>
    </div>
  )
}

const Anagrafica = () => {
  return (
    <div>
      Anagrafica
    </div>
  )
}

const Messaggio = () => {
  return (
    <div>
      Messaggio
    </div>
  )
}

export default Componente1
