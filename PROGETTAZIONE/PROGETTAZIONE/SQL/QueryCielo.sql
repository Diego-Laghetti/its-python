--1
select * from volo 
where durataMinuti >= 180;

--2
select distinct volo.comp from volo where durataMinuti > 180;

--3
select codice, comp from ArrPart where partenza = 'CIA';

--4
select comp from ArrPart where arrivo = 'FCO';

--5
select codice, comp from ArrPart where partenza = 'FCO' and arrivo = 'JFK';

--6
select comp from ArrPart where partenza = 'FCO' and arrivo = 'JFK';

--7 
select distinct ap.comp
from Arrpart as ap, LuogoAeroporto as l1, LuogoAeroporto as l2
where ap.partenza = l1.aeroporto
    and ap.arrivo = l2.aeroporto
    and l1.citta = 'Roma'
    and l2.citta = 'New York';

--8
select distinct aeroporto.codice, aeroporto.nome, LuogoAeroporto.citta 
from aeroporto, LuogoAeroporto, ArrPart where ArrPart.comp = 'MagicFly';

--9
select distinct v.codice, v.comp, ap.partenza, ap.arrivo
from ArrPart as ap, LuogoAeroporto as l1, LuogoAeroporto as l2, volo as v, Aeroporto as a1, Aeroporto as a2
where l1.citta = 'Roma' and l2.citta = 'New York' and ap.partenza = a1.codice and ap.arrivo = a2.codice and a1.codice = l1.aeroporto and a2.codice = l2.aeroporto and v.codice = ap.codice and v.comp = ap.comp;

--10
select 
from 
where 

--11
select 
from 
where 