def check_lenght (parola):
    if len(parola) > 10:
        print(f"la parola ha piu di 10 caratteri")
    elif len(parola) < 10:
         print(f"la parola ha meno di 10 caratteri") 
    else:
        print(f"la parola ha 10 caratteri")
        
x = str(input())
check_lenght(x)