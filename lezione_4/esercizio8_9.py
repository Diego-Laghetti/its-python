#esercizio8-9
list = ("CIAO", "WHAT", "OMAIGOD")
def show_messages():
    i=0
    for x in list:
        if i < len(list):
            print(list[0+i])
            i += 1
        else:
            break

show_messages()

'''def show_messages(*args):
    for message in args:
        print(message)

show_messages("CIAO", "WHAT", "OMAIGOD")'''