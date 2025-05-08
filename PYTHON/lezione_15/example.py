PATH: str = "ITS/PYTHON/lezione_15/example.txt"
mode: str = "r"
encoding: str = "utf-8"

file = open(PATH, mode)

print(file)
#input_text: str = input("Enter text to write to the file: ")
output: str = file.read()
print(output)
file.close()