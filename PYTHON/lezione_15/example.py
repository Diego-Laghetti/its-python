PATH: str = "ITS/PYTHON/lezione_15/example.txt"
mode: str = "w"
encoding: str = "utf-8"

file = open(PATH, mode)

print(file)
#input_text: str = input("Enter text to write to the file: ")
output: str = file.write("forza lazio")
print(output)
file.close()