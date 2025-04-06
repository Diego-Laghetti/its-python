#esercizio8-10
list = ["CIAO", "WHAT", "OMAIGOD"]
sent_messages = []

def send_messages():
    for i in list:
        print(i)
        sent_messages.append(i)

send_messages()

print("Lista originale:", list)
print("Messaggi inviati: ", sent_messages)