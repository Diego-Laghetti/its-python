#esercizio8-11
list = ["CIAO", "WHAT", "OMAIGOD"]
sent_messages = []

def send_messages():
    for i in list:
        print(i)
        sent_messages.append(i)
    list.clear()

send_messages()

print("Lista originale:", list)
print("Messaggi inviati: ", sent_messages)