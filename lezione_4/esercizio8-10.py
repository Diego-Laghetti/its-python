#esercizio8-10
list = ["CIAO", "WHAT", "OMAIGOD"]
sent_messages = []

def send_messages():
    while list:
        message= list.pop(0)
        print(message)
        sent_messages.append(message)

send_messages()

print("Lista originale:", list)
print("Messaggi inviati: ", sent_messages)