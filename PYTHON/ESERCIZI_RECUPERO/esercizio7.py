class ContactManager:
    def __init__(self) -> None:
        # Dizionario {nome: [numeri]}
        self.contacts: dict[str, list[str]] = {}

    def create_contact(self, nome: str, numeri: list[str]) -> dict:
        """Crea un nuovo contatto; se esiste solleva errore."""
        if nome in self.contacts:
            raise ValueError(f"Il contatto '{nome}' esiste già.")
        self.contacts[nome] = numeri
        return self.contacts

    def add_phone_number(self, nome: str, numero: str) -> dict:
        """Aggiunge un numero a un contatto esistente; se non esiste solleva errore."""
        if nome not in self.contacts:
            raise KeyError(f"Il contatto '{nome}' non esiste.")
        if numero in self.contacts[nome]:
            raise ValueError(f"Il numero {numero} è già presente per '{nome}'.")
        self.contacts[nome].append(numero)
        return self.contacts

    def remove_phone_number(self, contact_name: str, phone_number: str) -> dict:
        """Rimuove un numero a un contatto esistente; se non esiste solleva errore"""
        if contact_name not in self.contacts:
            raise KeyError(f"Il contatto '{contact_name}' non esiste.")
        if phone_number not in self.contacts[contact_name]:
            raise KeyError(f"Il numero di telefono {phone_number} non è presente")
        self.contacts[contact_name].remove(phone_number)
        return self.contacts
    
    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str) -> dict:
        """Sostituisce un numero di telefono con un altro nel contatto specificato"""
        if contact_name not in self.contacts:
            raise KeyError(f"Il contatto '{contact_name}' non esiste.")
        if old_phone_number not in self.contacts[contact_name]:
            raise KeyError(f"Il numero di telefono {old_phone_number} non è presente")
        if new_phone_number in self.contacts[contact_name]:
            raise KeyError(f"Il numero di telefono {new_phone_number} esiste già")
        # Trova l'indice del vecchio numero e lo sostituisce
        index = self.contacts[contact_name].index(old_phone_number)
        self.contacts[contact_name][index] = new_phone_number
        # Restituisce solo il contatto aggiornato
        return self.contacts
    
    def list_contacts(self) -> list:
        return list(self.contacts.keys())
    
    def list_phone_numbers(self, contact_name: str) -> list:
        if contact_name not in self.contacts:
            raise KeyError(f"Il contatto '{contact_name}' non esiste.")
        list_numbers: list[str] = []
        for number in self.contacts[contact_name]:
            list_numbers.append(number)
        return list_numbers

        
    def search_contact_by_phone_number(self, phone_number: str) -> list:
        list_contacts_number: list[str] = []
        for n, l in self.contacts.items():
            if phone_number in l:
                list_contacts_number.append(n)
            else:
                continue
        return list_contacts_number

# Creo l’istanza
cm = ContactManager()

# Creo un contatto
print(cm.create_contact("Alice", ["1234567890"]))

# Aggiungo un numero a Alice
print(cm.add_phone_number("Alice", "0987654321"))

# Provo a rimuovere un numero
print(cm.remove_phone_number("Alice", "1234567890"))

# Aggiorno un numero di Alice
print(cm.update_phone_number("Alice", "0987654321", "1112223333"))

# Stampo la lista di contatti
print(cm.list_contacts())

# Stampo i numeri di Alice
print(cm.list_phone_numbers("Alice"))

# Cerco il contatto che ha il numero "1112223333"
print(cm.search_contact_by_phone_number("1112223333"))


    



                        



