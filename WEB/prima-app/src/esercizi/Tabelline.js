import React from 'react'

const Tabelline = (props) => {
  let numeri = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  return (
    <div>
      Tabelline
      {
      numeri.map((i) => {
        return <p>{i*props.numero}</p>
        })
      }
    </div>
  )
}

export default Tabelline
