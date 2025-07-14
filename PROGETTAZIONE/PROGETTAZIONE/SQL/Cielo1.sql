BEGIN TRANSACTION;
SET CONSTRAINTS ALL DEFERRED;


CREATE DOMAIN postinteger AS INTEGER
    CHECK (VALUE >= 0);

CREATE DOMAIN stringam AS VARCHAR(100);

CREATE DOMAIN codIATA AS CHAR(3);

CREATE TABLE compagnia (
    nome stringam PRIMARY KEY,
    annofondaz postinteger
);

CREATE TABLE volo (
    codice postinteger NOT NULL,
    comp stringam NOT NULL,
    durataMinuti postinteger NOT NULL,
    PRIMARY KEY (codice, comp),
    FOREIGN KEY (comp) REFERENCES compagnia(nome)
);

CREATE TABLE aeroporto (
    codice codIATA PRIMARY KEY,
    nome stringam NOT NULL
);

CREATE TABLE luogoaeroporto (
    aeroporto codIATA PRIMARY KEY,
    citta stringam NOT NULL,
    nazione stringam NOT NULL,
    FOREIGN KEY (aeroporto) REFERENCES aeroporto(codice)
);

CREATE TABLE arrpart (
    codice postinteger NOT NULL,
    comp stringam NOT NULL,
    partenza codIATA NOT NULL,
    arrivo codIATA NOT NULL,
    PRIMARY KEY (codice, comp),
    FOREIGN KEY (codice, comp) REFERENCES volo(codice, comp),
    FOREIGN KEY (partenza) REFERENCES aeroporto(codice),
    FOREIGN KEY (arrivo) REFERENCES aeroporto(codice)
);

INSERT INTO aeroporto (codice, nome)
VALUES 
    ('FCO', 'Aeroporto Leonardo Da Vinci'),
    ('MXP', 'Aeroporto di Milano Malpensa');

INSERT INTO luogoaeroporto (aeroporto, citta, nazione)
VALUES 
    ('FCO', 'Fiumicino', 'Italia'),
    ('MXP', 'Milano', 'Italia');

INSERT INTO compagnia (nome, annofondaz)
VALUES 
    ('WizardAir', 2006);

INSERT INTO volo (codice, comp, durataMinuti)
VALUES 
    (101, 'WizardAir', 55),
    (103, 'WizardAir', 50);

INSERT INTO arrpart (codice, comp, partenza, arrivo)
VALUES 
    (101, 'WizardAir', 'FCO', 'MXP'),
    (103, 'WizardAir', 'FCO', 'MXP');

COMMIT;


