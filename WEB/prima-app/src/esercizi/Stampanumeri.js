import React from 'react'

const Stampanumeri = () => {
  let numeri = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  return (
    <div>
      Stampanumeri
      {
      numeri.map((i) => {
        return <p>{i}</p>
        })
      }
    </div>
  )
}

export default Stampanumeri
