#esercizio8_16
import import_nomi

print(import_nomi.saluto("diego"))

from import_nomi import saluto
print(saluto("alessio"))

from import_nomi import saluto as fn
print(fn("claudio"))

import import_nomi as mn
print(mn.saluto("luca"))

from import_nomi import *
print(saluto("claudia"))