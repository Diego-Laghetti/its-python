#esercizio1
import math
def safe_sqrt(number=-1):
    if number < 0:
        raise ValueError(f"Il numero è negativo")
    ris = math.sqrt(number)
    print(ris)

try:
    safe_sqrt()
except Exception as e:
    print(e)