import { useState } from 'react';
import logo from './logo.svg';
import './App.css';
import { anagrafica } from './Data/Dati';
import Contatore from './Data/Contatore';
import EsempioUseEffect from './esercizi/EsempioUseEffect';

function App() {
  const [nome1, setNome1] = useState("Diego Laghetti");
  const [persone, setPersone] = useState(anagrafica);

  const elimina = (id) => {
    const newAnag = persone.filter(p => p.id !== id);
    setPersone(newAnag);
  };

  const cliccami = (nome, cognome) => {
    alert("Ciao " + nome + " " + cognome);
  };

  const cambiaNome = () => {
    setNome1("PlayDido");
  };
  const [persona,setPersona]=useState({
    id:"i",
    nome: "Diego Prime Moment",
    cognome: "Goat",
    eta: 20
  })
  const compleanno=()=>{
    let anni=persona.eta+1;

    setPersona({
      ...persona,
      eta:anni
    })
  }

  return (
    <div className="App">
      <EsempioUseEffect></EsempioUseEffect>
      <Contatore></Contatore>
      <h1>{nome1}</h1>
      <br></br>
      <button onClick={cambiaNome} className="btn btn-primary">
        Cambia Nome
      </button>
<br></br>
<br></br>   
<div>{persona.nome}</div>
<div>{persona.cognome}</div>
<div>{persona.eta}</div>
<br></br>
      <button onClick={compleanno} className="btn btn-primary">
        Compleanno
      </button>
      <br></br>
      <br></br>

      {persone.map((p) => (
        <div key={p.id}>
          <span>{p.nome} {p.cognome}</span>
          &nbsp;&nbsp;
          <button onClick={() => elimina(p.id)}>Elimina</button>
          &nbsp;
          <button onClick={() => cliccami(p.nome, p.cognome)}>Saluta</button>
        </div>
      ))}
    </div>
  );
}

export default App;

