import { piatti } from './piatti';  

function MenuRistorante() {
  return (
    <div>
      <h2>Menu Ristorante</h2>
      <ul>
        {piatti.map(p => (
          <li key={p.id}>{p.nome} - €{p.prezzo}</li>
        ))}
      </ul>
    </div>
  );
}

export default MenuRistorante;  // default export

