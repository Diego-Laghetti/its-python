#esercizio3C-5
utente: dict= { "nome":str(input("Inserire il nome utente: ")), "ruolo" : str(input("Inserire il ruolo: ")), "età" : int(input("Inserite l'età: "))} 
match utente:
    case utente if utente["ruolo"] == "admin":
        print("Accesso completo a tutte le funzionalità")
    case utente if utente["ruolo"] == "moderatore":
        print("Può gestire i contenuti ma non modificare le impostazioni")
    case utente if utente["ruolo"] == "ospite":
        print("Accesso ristretto! Solo visualizzazione dei contenuti")
    case utente if utente["ruolo"] !=["admin", "moderatore","ospite"]:
        print ("Attenzione! Ruolo non riconsciuto! Accesso Negato!") 
    case utente if utente["età"] >= 18:
        print("Accesso standard a tutti i servizi") 
    case utente if utente["età"] < 18:
        print("Accesso limitato! Alcune funzionalità sono bloccate")






