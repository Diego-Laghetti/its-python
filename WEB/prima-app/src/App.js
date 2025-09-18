import { useState } from 'react';
import './App.css';
import { anagrafica } from './Data/Dati';
import Contatore from './Data/Contatore';
import EsempioUseEffect from './esercizi/EsempioUseEffect';
import CambiaNome from './CambiaNome';
import LoginForm from './LoginForm';
import Saluto from './esercizio1/Saluto';
import CardUtente from './esercizio2/CardUtente';
import MenuRistorante from './esercizio3/MenuRistorante';
import Termostato from './esercizio4/Termostato';

function App() {
  const [persone, setPersone] = useState(anagrafica);

  const elimina = (id) => {
    setPersone(persone.filter(p => p.id !== id));
  };

  const cliccami = (nome, cognome) => {
    alert("Ciao " + nome + " " + cognome);
  };

  return (
    <div className="App">
      <h2>Lista Utenti</h2>

      {/* Uso di CardUtente con props */}
      <CardUtente
        nome="Diego Laghetti"
        email="diego@example.com"
        imgUrl="https://static.sky.it/editorialimages/1aacc8af9f89be2032e23a0afca4b0e365f00313/skytg24/it/sport/approfondimenti/scudetto-lazio-2000/02_scudetto_lazio_getty.jpg?im=Resize,width=335"
      />

      <CardUtente
        nome="Maria Rossi"
        email="maria@example.com"
        imgUrl="https://static.sky.it/editorialimages/1aacc8af9f89be2032e23a0afca4b0e365f00313/skytg24/it/sport/approfondimenti/scudetto-lazio-2000/02_scudetto_lazio_getty.jpg?im=Resize,width=335"
      />

      <br />
      <Termostato /><br />
      <MenuRistorante /><br />
      <Saluto /><br />
      <LoginForm /><br />
      <EsempioUseEffect /><br />
      <Contatore /><br />
      <CambiaNome /><br />

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

