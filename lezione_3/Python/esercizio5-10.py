#esercizio5-10
current_users=["BomberTuca05","PlayDido", "Mugnifico", "SavaTeam"]
new_users= ["Ziro303","Poaseidone","Amogus","PlayDido","SkibidiToilette"]


for doppione in range (len(new_users)):
    if new_users[doppione] in current_users:
        print(f"ci dispiace ma il nome utente {new_users[doppione]} e' gia' stato utilizzato nella lista {current_users}")

current_users1=["BomberTuca05","PlayDido", "Mugnifico", "SavaTeam"]
new_users1= ["Ziro303","Poaseidone","Amogus","Capofatto","SkibidiToilette"]

for doppione in range (len(new_users1)):
    if new_users1[doppione] in current_users1:
        print(f"ci dispiace ma il nome utente {new_users1[doppione]} e' gia' stato utilizzato nella lista {current_users1}")
    else:
        print(f"{new_users1[doppione]} nome utente valido")