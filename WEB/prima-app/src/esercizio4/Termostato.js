import React, { useState } from 'react';

function Termostato() {
  const [temperatura, setTemperatura] = useState(20); 
  return (
    <div>
      <h1>Temperatura: {temperatura}°C</h1>
      <button onClick={() => setTemperatura(temperatura + 1)}>+ PIU'</button>
      <button onClick={() => setTemperatura(temperatura - 1)}>- MENO</button>
    </div>
  );
}

export default Termostato;

