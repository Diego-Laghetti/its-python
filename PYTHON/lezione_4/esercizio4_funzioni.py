def check_each(numbers):
    for number in numbers:
        print(number)
        if number > 5:
            print(f"il numero è maggiore di 5")
        elif number < 5:
            print(f"il numero è minore di 5")
        else:
            print(f"il numero è 5")
            
check_each([7, 2, 6, 4, 5])
        
