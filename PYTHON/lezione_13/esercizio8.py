#esercizio8
def vowelsCounter(s: str) -> int:
    if not s: 
        return 0
    if s[0].lower() in ["a", "e", "i", "o", "u"]:
        return 1 + vowelsCounter(s[1:])
    else:
        return vowelsCounter(s[1:])  

print(f"La stringa \"CIAO\" contiene: {vowelsCounter('CIAO')} vocali")