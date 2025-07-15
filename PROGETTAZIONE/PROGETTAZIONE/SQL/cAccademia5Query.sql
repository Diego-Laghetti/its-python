--1 
select distinct WP.nome, WP.inizio, WP.fine
from WP, Progetto
where Progetto.nome = 'Pegasus' and Progetto.id = WP.progetto;

--2
select distinct p.nome, p.cognome, p.posizione
from AttivitaProgetto as a, Persona as p, Progetto as pr
where a.persona = p.id and a.progetto = pr.id and pr.nome = 'Pegasus'
order by cognome desc;

--3
select
from
where

--4
select distinct p.nome, p.cognome
from Persona as p, Assenza as a
where p.posizione = 'Professore Ordinario' and p.id = a.persona and a.tipo = 'Malattia';

--5
select
from
where

--6
select distinct p.nome, p.cognome
from Persona as p,LavoroNonProgettuale as l
where p.posizione = 'Ricercatore' and p.id = l.persona and l.tipo = 'Didattica';


