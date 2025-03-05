#esercizio8-4
def make_shirt(size: str, text: str):
    size: str= (input("Taglia: "))
    text="I love python"
    match(size):
        case size if size == "L" and text == "I love python":
            print(f"The size is {size} and the text on the shirt is {text}")
        case size if size == "M" and text == "I love python":
            print(f"The size is {size} and the text on the shirt is {text}")
        case _:
            print(f"The size is {size} and the text on the shirt is Forza Lazio")

make_shirt("text", "size")

