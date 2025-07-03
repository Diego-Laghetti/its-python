import React from 'react'

const Persona = () => {
    let nome = 'Diego';
    let cognome = 'Laghetti'; 
    let data_nascita = '08/6/2005';
    let luogo_nascita = "Roma";
    let dati_anagrafici = ['Nome: ' + nome, 'Cognome ' + cognome, 'Data Nascita ' + data_nascita, 'Luogo Nascita ' + luogo_nascita];
  return ( 
    <div>
      Persona
      {
        dati_anagrafici.map((d) => {
            return <p>{d}</p>
        })
      }
    </div>
  )
}

export default Persona
