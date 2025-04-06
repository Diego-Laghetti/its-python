def even_odd_pattern(numbers:list[int]) -> list[int]:
    list = []
    cont = 0
    for n in numbers:
        if n%2==1:
            list.append(n)
        else:
            list.insert(cont,n)
            cont += 1
            
    return list

print(even_odd_pattern([3, 6, 1, 8, 4, 7]))