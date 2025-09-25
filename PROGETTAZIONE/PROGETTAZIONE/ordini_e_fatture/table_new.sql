create table statoordine (
	id serial primary key
	nome stringa not null,
	unique(nome)
);

create table nazione (
	nome stringa primary key
);

create table regione (
	nome stringa not null,
	nazione stringa not null,
	primary key (nome, nazione),
	
	foreign key (nazione)
		references nazione(nome)
);

create table città(
	id serial primary key,
	nome stringa not null,
	regione stringa not null,
	nazione stringa not null,
	unique (nome, regione, nazione)
)

create table direttore (
	cf codicefiscale primary key,
	nome stringa not null,
	cognome stringa not null,
	anni_servizio intgez not null,
	data_nascita date not null,
	cit_nasc intger not null,
	foreign key (cit_nasc)
		references citta(id)
);

create table dipartimento (
	nome stringa primary key,
	indirizzo indirizzo,
	dip_dir codicefiscale not null,
	
	 





