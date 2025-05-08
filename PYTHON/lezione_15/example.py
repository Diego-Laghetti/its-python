PATH: str = "PYTHON/lezione_15/example.txt"
mode: str = "w"
encoding: str = "utf-8"

file = open(PATH, mode)

print(file)
#input_text: str = input("Enter text to write to the file: ")
message: str = 'forza lazio'
output: str = file.write(message)
print(message)
print(output)
file.close()