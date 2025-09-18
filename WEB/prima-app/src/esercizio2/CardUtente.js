import React from 'react';

const CardUtente = (props) => {
  return (
    <div classname="card" style={{width: "18rem"}}>
        <img src={props.imgUrl} className="card-img-top" alt="..." />
        <div className="card-body">
            <h5 className="card-title">{props.nome}</h5>
            <p className="card-text">
              {props.email}
              </p>
        </div>
      
    </div>
  );
};

export default CardUtente;

