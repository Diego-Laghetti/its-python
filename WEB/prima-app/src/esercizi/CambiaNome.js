import React, { useState } from 'react';

const CambiaNome = () => {
  const nomeOriginale = "Diego Laghetti";
  const nuovoNome = "PlayDido";
  const [nome1, setNome1] = useState(nomeOriginale);

  const nome = () => {
    if (nome1 === nomeOriginale) {
      setNome1(nuovoNome);
    } else {
      setNome1(nomeOriginale);
    }
  };

  return (
    <div>
      <p>{nome1}</p>
      <button onClick={nome} className="btn btn-primary">
        Cambia / Ripristina
      </button>
    </div>
  );
};

export default CambiaNome;

