#esercizio8-12
def make_sandwich(*items):
    print("Fammi un panino con i seguenti ingredienti:")
    for i in items:
        print(f"-{i}")
    print("Il tuo panino è pronto!")

make_sandwich("prosciutto", "formaggio", "mozzarella")
make_sandwich("uovo", "avocado")
make_sandwich("nutella", "noccioline")