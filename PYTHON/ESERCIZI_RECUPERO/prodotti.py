def prodDict():
    d = {}
    for x in range(0, 101):  
        for y in range(2, 89, 2): 
            d[(x, y)] = x * y
    return d

if __name__ == "__main__":
    d = prodDict()
    print(f"(13, 88): {d[(13, 88)]}")
    print(f"(83, 56): {d[(83, 56)]}")
    print(f"(71, 44): {d[(71, 44)]}")
