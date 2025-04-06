def find_disappeared_numbers(nums: list[int]) -> list[int]:
    cont=1
    list = []
    
    for i in nums:
        if cont != i and cont not in nums:
            list.append(cont)
        cont += 1
        
    return list

print(find_disappeared_numbers([4,3,2,7,8,2,3,1]))