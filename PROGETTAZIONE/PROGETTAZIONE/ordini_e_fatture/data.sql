insert into statoordine (nome)
values
('In preparazione'),
('Inviato');

insert into statoordine(id, nome)
values
(3, 'Da saldare'),
(4, 'Saldato');

insert into nazione(nome)
values
('A'),
('B');

insert into regione (nome, nazione)
values
('Nord', 'A'),
('Est', 'B'),
('Sud', 'A'),
('Sud', 'B');

insert into citta(nome, regione, nazione)
values
('X', 'Nord, 'A'),
('Y', 'Est', 'B'),
('Z', 'Sud', 'A'),
('W', 'Sud', 'B');

insert into direttore (cf, nome, cognome, anni_servizio, data_nascita, cit_nasc)
values
('AAABBB67D19H501U', 'Franco', 'Cascio', 4, current_date - interval '32 year', 3);
