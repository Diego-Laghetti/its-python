create domain Stringa as varchar (100);

create domain Cap as char(5)
        check (value ~'^\d{5}$');

create domain CodiceFiscale as char (16)
        check (value ~ '^[A-Z0-9]{16}');

create domain PartitaIVA as char(11)
        check (value ~ '^[0-9]{11}$');

create type Indirizzo as (
        via varchar(50),
        numero_civico varchar(10),
        cap Cap
);

create domain Telefono as varchar (15);

create domain Email as varchar (255)
        check (value like '%@%%');

create type StatoOrdine as enum ('In preparazione', 'Inviato', 'Da saldare', 'Saldato');

create domain IntGEZ as Integer
        check (value>=0);

create domain RealGez as real
        check (value>0);

create domain Real0_1 as real
        check (value>=0 and value<=1);

create table nazione (
        nome stringa primary key
);

create table regione (
        nome stringa not null,
        nazione stringa not null,
        primary key (nome, nazione),
        foreign key (nazione) references nazione (nome)
);

create table citta (


)