#flowchart2
nord_sud=int(input("leggi nord sud: ")) 
est_ovest=int(input("leggi est ovest: ")) 
soglia = 70
if nord_sud > soglia and est_ovest > soglia:
    time_ns = 50
    time_eo = 50
elif nord_sud>soglia:
    time_ns=60
    time_eo=40
elif est_ovest>soglia:
    time_ns=40
    time_eo=60
else:
    time_ns = (nord_sud/ (nord_sud + est_ovest)* 100)
    time_eo = (est_ovest/(nord_sud + est_ovest)* 100)

print("Il tempo assegnato alla dierzione Nord_sud è: ", time_ns)
print("Il tempo assegnato alla dierzione Est-oves è: ", time_eo)